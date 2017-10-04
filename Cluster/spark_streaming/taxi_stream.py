from __future__ import print_function

from collections import defaultdict
from multiprocessing.connection import Client
from threading import Thread

import os
import sys

import pandas as pd

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

from pyproj import Proj, transform

def mock_input_stream():
    '''puts data into HDFS on an regular interval'''

    # load nyc taxi data
    path = './data/nyc_taxi.csv'
    pickup_date_field = 'tpep_pickup_datetime'
    dropoff_date_field = 'tpep_dropoff_datetime'
    date_fields = [pickup_date_field, dropoff_date_field]
    cols = ['pickup_longitude', 'pickup_latitude',
            'dropoff_longitude', 'dropoff_latitude', 'total_amount',
            pickup_date_field, dropoff_date_field]

    # stack pickups and dropoffs and ground into time periods
    df = pd.read_csv(path, usecols=cols, parse_dates=date_fields).dropna(axis=0)

    xs = df['pickup_longitude'].append(df['dropoff_longitude'])
    xs.reset_index(drop=True, inplace=True)

    ys = df['pickup_latitude'].append(df['dropoff_latitude'])
    ys.reset_index(drop=True, inplace=True)

    dates = df[pickup_date_field].append(df[dropoff_date_field])
    dates.reset_index(drop=True, inplace=True)

    fares = pd.Series(len(df) * [None]).append(df['total_amount'])
    fares.reset_index(drop=True, inplace=True)

    del df

    df2 = pd.DataFrame()
    df2['x'] = xs
    df2['y'] = ys
    df2['date'] = dates
    df2['fare'] = fares
    grouped = df2.set_index('date').groupby(pd.TimeGrouper('5T'))
    grouped_keys = sorted(grouped.groups.keys())

    # iterate over groups and write into hdfs
    for i, g in enumerate(grouped_keys):
        group = grouped.get_group(g)

        group_fname = 'temp{}.txt'.format(i)
        group.to_csv(group_fname, header=False)

        temp_hdfs = '/taxitemp/{}'.format(group_fname)
        os.system('hdfs dfs -put {} {}'.format(group_fname, temp_hdfs))

        output_hdfs = '/taxidata/{}'.format(group_fname)
        os.system('hdfs dfs -mv {} {}'.format(temp_hdfs, output_hdfs))

bokeh_proc = None
def to_bokeh(time, rdd, num=1000):
    global bokeh_proc

    result = dict(pickups=defaultdict(list), dropoffs=defaultdict(list))
    taken = rdd.take(num + 1)

    for record in taken[:num]:
        if not record[3]:
            result['pickups']['date'].append(record[0])
            result['pickups']['x'].append(record[1])
            result['pickups']['y'].append(record[2])
            result['pickups']['fare'].append(record[3])
        else:
            result['dropoffs']['date'].append(record[0])
            result['dropoffs']['x'].append(record[1])
            result['dropoffs']['y'].append(record[2])
            result['dropoffs']['fare'].append(record[3])

    if not bokeh_proc:
        bokeh_proc = Client(('localhost', 6000), authkey=b'secret password')

    if result['pickups'] or result['dropoffs']:
        bokeh_proc.send(result)

def process_record(r):
    s = r.split(',')
    date = s[0]
    x, y = transform(Proj("+init=EPSG:4326"),
                     Proj("+init=EPSG:3857"),
                     float(s[1]),
                     float(s[2]))
    fare = float(s[3]) if s[3] else ''

    return (date, x, y, fare)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python taxi_stream.py ./taxidata",
              file=sys.stderr)

        sys.exit(-1)

    # start mock input on background thread
    t = Thread(target=mock_input_stream)
    t.daemon = True
    t.start()

    # start spark streaming process on foreground thread
    sc = SparkContext(appName="BokehStreamingExample")
    ssc = StreamingContext(sc, 1)
    lines = ssc.textFileStream(sys.argv[1])
    lines.map(process_record).foreachRDD(to_bokeh)
    ssc.start()
    ssc.awaitTermination()
