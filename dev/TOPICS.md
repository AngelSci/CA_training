# Course Topics

## Topic Summary

Status:

* [Original topic outline with details](https://drive.google.com/a/continuum.io/file/d/0B3MLKrmM7TwvRU1jbURMM041dk0/view)
* Hunt will prioritize the items on the list in terms of client expectations

Outline:

* [Conda](#conda)
* [Anaconda Accelerate](#anaconda-accelerate)
* [IOPro](#iopro)
* [Anaconda Enterprise Notebooks](#anaconda-enterprise-notebooks)
* [Anaconda Repository](#anaconda-repository)
* [Bokeh](#bokeh)
* [DataShader](#datashader)
* [Anaconda Cluster](#anaconda-cluster)

Below, for each of the topics, try to provide the following meta-data:

* **Status** = what's being worked on, what's blocked, who's the current owner
* **Timing** = how much time to spend on this during training presentation
* **Outline** = what sub-topics must be covered, would be nice to cover
* **Raw Resources** = existing material that we can use NOW.
* **Material Ready** = material tested, lives in repo, and is ready to present without breaking.

## Conda

Status:

* Raw anaconda video training content was pulled in

Timing: 2 hours

* initial doc says 0.5 hours; that's WAY too little
* could easily do 2+ hours, especially if you have students do anything
* if covering conda recipes and conda build, add an hour

Sub-Topic Outline:

* Introduction
    * conda and Anaconda
    * what problem does conda solve
* Creating a Python Environment (P1) 
* Managing Environments (P1)
    * updating environments
    * exporting, sharing environment files
* Building a Conda Package (P2)
    * conda recipes
    * PyPI
    * Sharing on anaconda.org

Raw Resources:

* [Continuum Training Material on Conda](https://github.com/ContinuumIO/Training/blob/master/Introduction/Basic/00_CondaAndInterpreter.ipynb)
* [Continuum Anaconda Training Video scripts](https://github.com/ContinuumIO/anaconda_training_videos/tree/master/Conda)

Materials Ready:

* No
* Criteria for ready?

## Anaconda Accelerate

Anaconda Accelerate, formerly NumbaPro

Status:

* accelerate notebooks from Siu have been pulled in
* need to review notebooks

Timing:

* 4 hours

Sub-Topic Outline:

* Strategies for profiling and improving Python and NumPy code performance (P1)
* Speeding up array math for multicore CPUs and GPUs (P2)
* Accelerated signal processing and linear algebra using multicore CPUs and GPUs (P2)
* GPU programming basics with Python (P2)
* Natural language processing:
    * Topic clustering of documents (uses LDA) (P2)
    * Preparing text for analysis (uses D-L algorithm to fix mispellings and possibly word2vec for certain kinds of applications) (P2)
* Feature detection in images (P2)
* Using Accelerate with Dask and Spark (P2)


Raw Resources:

* [Siu has notebooks on NumbaPro](https://github.com/ContinuumIO/accelerate-iqt-course)
* [Accelerate Docs at continuum.io](https://docs.continuum.io/accelerate/index)
* [Numba Docs at pydata.org](http://numba.pydata.org/numba-doc/latest/index.html)
* [Number Examples at pydata.org](http://numba.pydata.org/numba-doc/dev/user/examples.html)
* [Numba and Spark tutorial by Stan, PDF](https://drive.google.com/drive/folders/0B3MLKrmM7TwvenR3N0RHV1dXUVU)
* [Numba and Spark tutorial by Stan, Keynote](https://drive.google.com/a/continuum.io/file/d/0B3MLKrmM7TwvQ3JJVHF2amtMcms/view)

Materials Ready:

* No
* Criteria for ready?

## IOPro

Status:

* pulled from ContinuumIO/docs repo, raw ReST converted to mark-down

Timing:

* 2 hours

Sub-Topic Outline:

* Basic IOPro interface
    * ...common to text, mongo, postgres, and accumulo adapters
    * Create adaptor (P1)
    * Using slicing to retrieve records (P1)
* Text Adaptor Basic Usage
    * Supported text formats (delimited text and CSVs, fixed width, json, and fields defined by regex) (P1)
    * Set field types using field_types property (P1)
    * Additional adapter properties (field_count, field_filter, field_names) (P1)
    * Set missing/fill values (P1)
    * Parsing gzipped files and creating separate index file for random access (P1)
    * Using regex to define fields (P1)
    * Using Converter Functions (P1)
    * Reading from S3 (P1)
* Mongo, Accumulo, and Postgres based adapter basic usage
    * Connecting to the database (P2)
    * Set field types using field_types property (P4)
    * Field_names property (P4)
    * Additional adapter properties (start_key, stop_key,Start/stop_key_inclusive) (P4)
    * Handling Missing Values (P4)
    * Using sql queries with the adaptor (P2)
    * Retrieving GIS data as Well Known Text (WKT) for use with GIS modules like Shapely (P2)


Raw Resources:

* [IOPro docs at Continuum.io](https://docs.continuum.io/iopro/index)
* Other?

Materials Ready:

* No
* Criteria for ready?

## Anaconda Enterprise Notebooks

Status:

* Starting with Continuum repo docs, converting from ReST to markdown

Timing:

* 4 hours

Sub-Topic Outline:

* Landing Page - [Introduction Notebook](https://github.com/ContinuumIO/training-products/blob/master/Enterprise_Notebooks/00_introduction.md)
    * Sections of Landing Page (P1)
    * How to always get back to Landing Page (P1)
* Projects - [Projects Notebook](https://github.com/ContinuumIO/training-products/blob/master/Enterprise_Notebooks/01_projects.md)
    * Reference link: http://docs.wakari.io/we/user/deploy/projects.html#new 
    * Create a project (P1)
    * Load a Project Page (P1)
    * Sections of a Project Page (P1)
    * Admin Page (P1)
    * Change Project default (py2.7) environment (P3)
    * Start and Stop a Project (P1)
    * Project Access Controls
        * How to make Private/Public (P1)
        * What does private/public mean (P1)
    * Navigate back to Project Page (P1)
* Manage Projects - [Projects Notebook](https://github.com/ContinuumIO/training-products/blob/master/Enterprise_Notebooks/01_projects.md)
    * Add team members to Project (P1)
    * They get full access (P1)
    * Appear in team list (P1)
* Default Project Environment (conda)
    * create new environment (P2)
    * exporting environment, sending to others (P2)
    * running notebook in different environments (P2)
* Jupyter inside AEN, special features (P2) - [Notebooks](https://github.com/ContinuumIO/training-products/blob/master/Enterprise_Notebooks/02_notebooks.md)
* Working with a team (P2) - [Teams](https://github.com/ContinuumIO/training-products/blob/master/Enterprise_Notebooks/03_team.md)
* Tagging and Search (P2) - [Search and Recommendations](https://github.com/ContinuumIO/training-products/blob/master/Enterprise_Notebooks/03b_search_recommend.md)
* Security and Access Control (P2) - [limiting_access](https://github.com/ContinuumIO/training-products/blob/master/Enterprise_Notebooks/04_limit_access.md)
* Publishing (P2) - [Sharing](https://github.com/ContinuumIO/training-products/blob/master/Enterprise_Notebooks/05_sharing.md) *Note: Possibly cover in Security add Access Control section since that notebook has sections on sharing*
* Advanced Project Management (Trouble Shooting) (P4)
  * Possible: Running different environents
  * Possible: Running pure Python or R code


Raw Resources:

* [Continuum Docs on Anaconda Enterprise Notebooks](http://docs.wakari.io/we/user/deploy/index.html)
* AEN Trial, https://docs.continuum.io/aetrial/index, talk to Ian on this one.
* Look for notebooks in the demo
* [AE Trial](https://github.com/Anaconda-Platform/aetrial)
* https://github.com/ContinuumIO/wakari/tree/master/examples
* [Online Demo Server](http://test.demo.wakari.io/)
    * create new log-in account
    * sand-box for playing with AEN 

Materials Ready:

* No
* Criteria for ready?

## Anaconda Repository


Status:

* Raw files from ContinuumIO/docs, converted from ReST to markdown
* Need to organize, review, try to convert into presentation material
* Need more demos, examples

Timing:

* 2 hours

Sub-Topic Outline:

* Navigating the interface (P1)
* Creating and using Packages (P1)
* Sharing notebooks, packages, environments, and files (P1)
* Private Packages and using Tokens (P2)
* Organizations (P2)
* Using Labels (P2)

Raw Resources:

* [Continuum Docs on Anaconda Repository](https://docs.continuum.io/anaconda-repository/index)
* pull in the RST files from the actual repo, see Makefile
* Ask Ian Stokes-Rees

Materials Ready:

* No
* Criteria for ready?

## Bokeh
[Starting notebook](./Bokeh/Bokeh.ipynb)

Status:

* Material taken from training deep dive course on data visualization

Timing:

* 6 hours (excluding lunch and other breaks)

Sub-Topic Outline:

* Introduction to Bokeh Plotting API (10 mins)
* Using the High-level Charts API (60 mins)
    * Histograms
    * Time series
    * Box plots
    * Bar charts
    * Exercises
* Introduction to Bokeh Plotting API (60 mins)
    * Creating figures
    * Setting axes
    * Adding glyphs
    * Customizing appearance
    * Exercise
* Plot layouts (40 mins)
    * Gridplot
    * Linking ranges
    * Linking sources
    * Exercise
* Plotting with customized tools (60 mins)
    * Preparing a ColumnDataSource
    * Creating a HoverTool
    * Exercise
* Bokeh for geospatial applications
    * Consuming vector formats (shapefiles, geojson)  (P2)
    * Adding tile layers to figures  (P1)
    * Adding WMS services  (P1)
    * Basic map projections  (P1)
    * Performing basic analysis using geopandas + geojson data source  (P3)
    * Visualizing large data with datashader (P3)
* Bokeh Server (60 mins)
    * Launching Bokeh plots from Anaconda prompt
    * Creating an interactive dashboard with widgets
    * Exercise

Raw Resources:

* [Continuum Training Material on Bokeh](https://github.com/ContinuumIO/Training/tree/master/Visualization/Bokeh)
* [Continuum Deep Dive Material on Bokeh](https://github.com/ContinuumIO/training-deepdive-visualization)
* [Bokeh Tutorial at jupyter.org/github](http://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/tutorial/00%20-%20intro.ipynb)
* [Bokeh Server Examples at github/bokeh](https://github.com/bokeh/bokeh/tree/master/examples/app)
* [Bokeh Server Examples at bokeh.pydata.org](http://bokeh.pydata.org/en/latest/docs/user_guide/server.html)
* [Bokeh CLI Examples at bokeh.pydata.org](http://bokeh.pydata.org/en/latest/docs/user_guide/cli.html)
* [Bryan EuroScipy 2015](https://www.euroscipy.org/2015/speaker/profile/24/)
* Links from Brendan
    * [github.com/bokeh/datashader examples](https://github.com/bokeh/datashader/tree/master/examples)
    * [ContinuumIO/bokeh-geo examples](https://github.com/ContinuumIO/bokeh-geo/tree/master/examples)
    * [bokeh/bokeh-notebooks examples](https://github.com/bokeh/bokeh-notebooks/tree/master/)
* Links from Bryan
    * [Bokeh Tutorial @github](https://github.com/bokeh/bokeh-notebooks/tree/master/tutorial)
        * these notebooks have been used for many conferences
        * updated by Bryan and Sarah
        * takes about 4-6 hours if you don't rush
        * [Bokeh Tutorial @nbviewer](http://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/tree/master/tutorial/) - rendered, with cell output
    * [Bokeh App Notebooks on GitHub](https://github.com/bokeh/bokeh/tree/master/examples/app) - demonstrate some Bokeh server apps.

Materials Ready:

* The tutorial looks to be in good shape
* Criteria for ready?

## DataShader

Status:

* JBednar notebooks from anaconda.org have been pulled in
* Feedback from Bednar
    * Need to delete uber.ipynb for reasons.
    * The order the notebooks should be run in is given in teh slide deck
    * To see problems that arise when you DONT use datashader see "plotting_pitfalls" which is based on holoviews (albert has a matplotlib version in the deepdive-visualization)
    * https://github.com/bokeh/datashader
    * https://github.com/bokeh/datashader/tree/master/examples
        * there's a dashboard to install  
    * https://anaconda.org/jbednar/notebooks/nyc_taxi/notebook
        * theres a class "InteractiveImage" that is not part of Datashader
        * allows you to have an interactive image, for Bokeh
    * Order the notebooks should be presented:
        * plotting_pitfalls:  Common plotting problems solved by datashader
        * pipeline: Using each step of the datashader pipeline
        * nyc_taxi , nyc_taxi-nongeo: NYC Taxi data
        * census: US census data on race and population density
        * tseries: Time-series data
        * trajectory: Tracing connected points

Timing:

* 4 hours

Sub-Topic Outline:

* Overview (P1)
    * [Teach yourself: Over-view slides for DataSharer PDF](https://fd-files-production.s3.amazonaws.com/123981/yjzFZsbmAb5AXxBeYyXo5w?X-Amz-Expires=300&X-Amz-Date=20160603T183822Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIA2QBI5WP5HA3ZEA/20160603/us-east-1/s3/aws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=64f0d3edbd3da12c04511c5f2311a91b744bf894570949a7fb4bbedc6be2fc53)
    * When to use: when you care about distibution, not points (e.g. 10^10 pts)
    * Complements MPL, Boekh
    * Works with Bokeh
    * Sub-select e.g. columns from data container to assign to (x,y)
    * isolate data from image/display
    * allows you to do operations on the buffer prior to display
    * scatter plots, time series, rasters
    * histogram equalization = equal number of pixels per color bin

* Projecting data into screen space
    * Choosing axes (P1)
    * Choosing aggregation(s) (P1)
* Color-mapping
    * Mapping from data space to color space (P1)
    * Choosing color maps (P1)
    * Spreading: adjusting point size (P1)
* Integrating plot with Bokeh (P1)
    * Interactive exploration in Jupyter notebook and Bokeh apps (P1)
    * Overlaying with geographical data (P1)
    * Legends and hover tools (P1)
* Supported data types
    * Points (scatter-plot/heat-map) (P1)
    * Time series (P2)
    * Trajectories (P3)
    * Rasters  (P3)
* Customizing datashader
    * Highlighting anomalies and goodness of fit (P2)
    * Comparing across aggregates (P3)
    * Manipulating aggregate arrays (P3)
* Get data into datashader
    * Local machine (P1)
    * Working out of core (P2)
    * Distributed  (P3)
    * Using Spark and Dask (P3)


Raw Resources:

* Contrast with HoloView to motivate why you'd use Datashader.
* [Datashader Overview Slide-deck](https://drive.google.com/a/continuum.io/file/d/0B3MLKrmM7TwvbUktc05zWDRJUGM/view)
* [Jbednar Datashader Notebooks on anaconda.org](https://anaconda.org/jbednar/notebooks)
* [Teach yourself: Over-view slides for DataSharer PDF](https://fd-files-production.s3.amazonaws.com/123981/yjzFZsbmAb5AXxBeYyXo5w?X-Amz-Expires=300&X-Amz-Date=20160603T183822Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIA2QBI5WP5HA3ZEA/20160603/us-east-1/s3/aws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=64f0d3edbd3da12c04511c5f2311a91b744bf894570949a7fb4bbedc6be2fc53)

Materials Ready:

* No
* Criteria for ready?

## Anaconda Cluster

Status:

* Pulled in ContinuumIO/docs, converted raw ReST to markdown

Timing:

* 8 hours
* Current docs support maybe 1-2 hours, at most.

Sub-Topic Outline:

* Defining and provisioning clusters (P1)
* Basic commands to interact with clusters (P1)
* Overview of PySpark (P1)
* Overview of Dask (P1)
* Working with conda packages and environments on a cluster (P1)
* Working with data on a cluster (file formats and storage systems) (P3)
* Run jobs on specified machines and instances (P3)
* Working interactively in a notebook on a cluster  (P2)
* Using Bokeh and Anaconda Cluster together exercise  (P4)
* Working with some examples (examples to possibly use)
    * Running PySpark (or Dask) jobs with conda packages (Python, R, etc.) (P1)
    * Working with tabular data in distributed dataframes on a cluster (pandas and Dask)
    * Distributed text and natural language processing (PySpark or Dask)  (P3)
    * Parallelizing and wrapping existing code for custom workflows (Dask)  (P2)
    * Interactive queries and visualizations with distributed databases (PySpark or Dask) (P4)
    * Distributed image processing and GPU computations (PySpark or Dask)  (P4)

Raw Resources:

* [See cluster section of material tracker for links on the examples outlined below](https://docs.google.com/document/d/1_22RUbLgYd8pu4QvteNNYVKY803n56Croy5FLBG76g0/edit)

* Example Workflows Using Anaconda with PySpark:
    * Overview of Spark, YARN and HDFS
    * How to Run with the YARN resource manager
    * How to perform a word count on text data in HDFS
    * How to do Natural Language Processing
    * How to do Image Processing with GPUs
* Example Workflows Using Anaconda with Dask.Distributed:
    * Distributed arrays on a cluster with global temperature data
    * Distributed dataframes on a Hadoop cluster with HDFS
    * Distributed language processing on a Hadoop cluster with HDFS

* [Spark and Dask: internal lunch and learn](https://drive.google.com/drive/u/0/folders/0B4LRrCKZqSrMNmNwbjNnWDliWEk)
* [Spark and Dask scaling notebook](https://drive.google.com/open?id=0B3MLKrmM7TwvUlRlQ0dVUDFPVzQ)
* [Anaconda Cluster Mgmt Docs at continuum.io](https://docs.continuum.io/anaconda-cluster/index)

Materials Ready:

* No
* Criteria for ready?
