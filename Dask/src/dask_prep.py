""" dask prepare sample data """

import os
import numpy as np
import pandas as pd
from glob import glob
import json
import gzip
import h5py
from scipy.misc import imresize

names = ['Alice', 'Bob', 'Charlie', 'Dan', 'Edith', 'Frank', 'George',
'Hannah', 'Ingrid', 'Jerry', 'Kevin', 'Laura', 'Michael', 'Norbert', 'Oliver',
'Patricia', 'Quinn', 'Ray', 'Sarah', 'Tim', 'Ursula', 'Victor', 'Wendy',
'Xavier', 'Yvonne', 'Zelda']

k = 100

def account_params(k):
    ids = np.arange(k, dtype=int)
    names2 = np.random.choice(names, size=k, replace=True)
    wealth_mag = np.random.exponential(100, size=k)
    wealth_trend = np.random.normal(10, 10, size=k)
    freq = np.random.exponential(size=k)
    freq /= freq.sum()

    return ids, names2, wealth_mag, wealth_trend, freq

def account_entries(n, ids, names, wealth_mag, wealth_trend, freq):
    indices = np.random.choice(ids, size=n, replace=True, p=freq)
    amounts = ((np.random.normal(size=n) + wealth_trend[indices])
                                         * wealth_mag[indices])

    return pd.DataFrame({'id': indices,
                         'names': names[indices],
                         'amount': amounts.astype('i4')},
                         columns=['id', 'names', 'amount'])


def accounts(n, k):
    ids, names, wealth_mag, wealth_trend, freq = account_params(k)
    df = account_entries(n, ids, names, wealth_mag, wealth_trend, freq)
    return df


def json_entries(n, *args):
    df = account_entries(n, *args)
    g = df.groupby(df.id).groups

    data = []
    for k in g:
        sub = df.iloc[g[k]]
        d = dict(id=int(k), name=sub['names'].iloc[0],
                transactions=[{'transaction-id': int(i), 'amount': int(a)}
                              for i, a in list(zip(sub.index, sub.amount))])
        data.append(d)

    return data

def accounts_json(n, k):
    args = account_params(k)
    return json_entries(n, *args)

def random_array():
    if os.path.exists(os.path.join('tmp', 'random.hdf5')):
        return

    print("Create random data for array exercise")

    with h5py.File(os.path.join('tmp', 'random.hdf5')) as f:
        dset = f.create_dataset('/x', shape=(100000000,), dtype='f4')
        for i in range(0, 100000000, 1000000):
            dset[i: i + 1000000] = np.random.exponential(size=1000000)


def accounts_csvs(num_files, n, k):
    fn = os.path.join('tmp', 'accounts.%d.csv' % (num_files - 1))

    if os.path.exists(fn):
        return

    print("Create CSV accounts for dataframe exercise")

    args = account_params(k)

    for i in range(num_files):
        df = account_entries(n, *args)
        df.to_csv(os.path.join('tmp', 'accounts.%d.csv' % i),
                  index=False)


def accounts_json(num_files, n, k):
    fn = os.path.join('tmp', 'accounts.%02d.json.gz' % (num_files - 1))
    if os.path.exists(fn):
        return

    print("Create JSON accounts for bag exercise")

    args = account_params(k)

    for i in range(num_files):
        seq = json_entries(n, *args)
        fn = os.path.join('tmp', 'accounts.%02d.json.gz' % i)
        with gzip.open(fn, 'wb') as f:
            f.write(os.linesep.join(map(json.dumps, seq)).encode())


def create_weather(growth=3200):
    filenames = sorted(glob(os.path.join('data', 'weather-small', '*.hdf5')))

    if not os.path.exists(os.path.join('tmp', 'weather-big')):
        os.mkdir(os.path.join('tmp', 'weather-big'))

    if all(os.path.exists(fn.replace('small', 'big')) for fn in filenames):
        return

    print("Expand weather data for array exercise")

    for fn in filenames:
        with h5py.File(fn) as f:
            x = f['/t2m'][:]

        y = imresize(x, growth)

        out_fn = os.path.join('tmp', 'weather-big', os.path.split(fn)[-1])

        with h5py.File(out_fn) as f:
            f.create_dataset('/t2m', data=y, chunks=(500, 500))


if __name__ == '__main__':
    random_array()
    create_weather()
    accounts_csvs(3, 1000000, 500)
    accounts_json(50, 100000, 500)
