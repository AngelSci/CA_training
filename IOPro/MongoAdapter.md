MongoAdapter
============

The MongoAdapter module reads data from a Mongo database collection and
produces a NumPy array containing the loaded. The following features are
currently implemented:

-   The MongoAdapter engine is written in C to ensure data is loaded
    fast with minimal memory usage.
-   Python slicing notation can be used to specify the subset of records
    to be read from the data source.
-   The MongoAdapter engine has automatic type inference so the user
    does not have to specify dtypes of the output array.

Methods
-------

The MongoAdapter module contains the follwowing constructor for creating
MongoAdapter objects:

**MongoAdapter** (host, port, database, collection)
:   MongoAdapter contructor

    host - Host name where Mongo database is running.\
    port - Port number where Mongo database is running.\
    database - Mongo database to connect to\
    collection - Mongo database collection

**set\_field\_names** (names)
:   Set field names to read when creating output NumPy array.

**get\_field\_names** ()
:   Returns names of fields that will be read when reading data from
    Mongo database.

**set\_field\_types** (types=None)
:   Set NumPy dtypes for each field, specified as a dict of field
    names/indices and associated dtype. (Example: {0:'u4', 1:'f8',
    2:'S10'})

**get\_field\_types** ()
:   Returns dict of field names/indices and associated NumPy dtype.

The MongoAdapter object contains the following properties:

**size** (readonly)
:   Number of documents in the Mongo database + collection specified in
    constructor.

Basic Usage
-----------

1.  Create MongoAdapter object for data source

    > \>\>\> import iopro \>\>\> adapter =
    > iopro.MongoAdapter('localhost', 27017, 'database\_name',
    > 'collection\_name')

2.  Load Mongo collection documents into NumPy array using slicing
    notation

    > \>\>\> \# read all records for 'field0' field \>\>\> array =
    > adapter['field0'][:]
    >
    > \>\>\> \# read first ten records for 'field0' and 'field1' fields
    > \>\>\> array = adapter[['field0', 'field1']][0:10]
    >
    > \>\>\> \# read last record \>\>\> array = adapter['field0'][-1]
    >
    > \>\>\> \# read every other record \>\>\> array =
    > adapter['field0'][::2]


