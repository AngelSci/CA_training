sudo yum install gcc make gcc-c++ libtool libxml2-devel libpng libtiff
# Change to home directory to download source
cd ~/
# Download GEOS and install
wget http://download.osgeo.org/geos/geos-3.4.2.tar.bz2
tar xjf geos-3.4.2.tar.bz2
cd geos-3.4.2
./configure
make
make install
# Download Proj.4 and install
￼￼￼￼￼￼￼￼￼￼￼￼￼￼
http://overtronic.com/2013/12/how-to-install-postgresql-with-postgis-on-amazon-ec2-linux/ Page 2 of 4
￼￼￼￼￼￼How to Install PostgreSQL with PostGIS on Amazon EC2 Linux - Overtronic 1/20/16, 5:02 PM
l
You should now have a PostgreSQL database server with PostGIS running on Amazon EC2 Linux
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
cd ~/
wget http://download.osgeo.org/proj/proj-4.8.0.tar.gz
tar xzf proj-4.8.0.tar.gz
cd proj-4.8.0
./configure
make
make install
# Download and install GDAL
cd ~/
wget http://download.osgeo.org/gdal/1.10.1/gdal-1.10.1.tar.gz
tar -xvzf gdal-1.10.1.tar.gz
cd gdal-1.10.1
./configure
make
make install
# Download and install JSON-C library
cd ~/
wget https://s3.amazonaws.com/json-c_releases/releases/json-c-0.11.tar.gz
tar -xvzf json-c-0.11.tar.gz
cd json-c-0.11
./configure
make
make install
# Download and install PostGIS
cd ~/
wget http://download.osgeo.org/postgis/source/postgis-2.1.2.tar.gz
tar -xvzf postgis-2.1.2.tar.gz
cd postgis-2.1.2
./configure --with-pgconfig=/usr/pgsql-9.3/bin/pg_config --with-geosconfig=/usr/loca
make
make install
# update your libraries
echo /usr/local/lib >> /etc/ld.so.conf
ldconfig
