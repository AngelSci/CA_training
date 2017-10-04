mkdir data
cd data
wget https://storage.googleapis.com/tlc-trip-data/2015/yellow_tripdata_2015-01.csv 
head -n 1000000 yellow_tripdata_2015-01.csv > nyc_taxi.csv
hdfs dfs -mkdir /taxidata
hdfs dfs -mkdir /taxitemp
cd ..
