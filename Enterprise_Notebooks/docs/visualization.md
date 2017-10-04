# Visualization

Anaconda Enterprise Notebooks Visualization

### Plotting

Anaconda Enterprise Notebooks's Workbench Application supports two methods of plotting. One is plotting with IPython or the IPython Notebook using matplotlib. The second is Bokeh,
our custom interactive plotting library.

### Matplotlib

 <a href="http://matplotlib.org/" target="_blank">Matplotlib</a> is a Python 2D plotting library that produces publication-quality figures in a variety of hardcopy
formats and interactive environments across platforms.

To use matplotlib in Anaconda Enterprise Notebooks, you have two options.  You can either open a new terminal tab with *IPython w/ Matplotlib*
selected...


or open a New Notebook.


Anaconda Enterprise Notebooks's IPython Notebook comes with matplotlib already installed, so you don't need to worry about installing it
yourself or starting up IPython Notebook with the --pylab option.

In fact, the following example should execute and create a plot with either of the Anaconda Enterprise Notebooks options for using Matplotlib.

	x = linspace(0, 3*pi, 500)
	plot(x, sin(x**2))
	title(A simple chirp);



You can find a <a href="http://matplotlib.org/gallery.html" target="_blank">gallery</a>, <a href="http://matplotlib.org/examples/index.html" target="_blank">examples</a>, <a href="http://matplotlib.org/contents.html" target="_blank">documentation</a>, and a <a href="http://matplotlib.org/api/pyplot_summary.html" target="_blank">list of plotting commands</a> on the <a href="http://matplotlib.org/" target="_blank">matplotlib website</a>.

### Bokeh

In your *Examples* folder in the file browser, you'll find a file, webplot.py, which has been generated for you using your Anaconda Enterprise Notebooks
plotting API keys. Current functionality is limited to line plots and scatter plots. The interface is similar to
matplotlib.


	from webplot import p
This line will import the plotting client which can plot to your web browser. p.plot is the main function for plotting
data; it resembles the matplotlib.plot command:

	p.plot(y)             # plots y as a lineplot
	p.plot(x, y)          # plots y as a line plot with respect ot x
	p.plot(x, y, 'green) # using a green line
Similar to matplotlib, *y* can be a 2D array, in which case each column is plotted.
We default to having subsequent plotting commands render to the last completed plot. You can create a new plot by
calling p.figure. We also support matplotlib conventions for toggling the hold mode.

	p.figure()          # subsequent commands plot to a new plot
	p.hold(on)        # default to plotting to the current plot
	p.hold(off)       # default to plotting to new plot
	p.hold(True)        # default to plotting to the current plot
	p.hold(False)       # default to plotting to new plot
A key feature of plotting in Anaconda Enterprise Notebooks is interactivity. Clicking on the *Pan* and *Select* tools will allow you to pan and
select the plot using the mouse. The mouse wheel will also allow you to zoom in and out. For advanced users, shift +
mouse will pan and ctrl + mouse will select.

In Anaconda Enterprise Notebooks's plotting library, we introduce the notion of a data source. A data source is a collection of columns which
are joined into records. Interactivity is much more powerful when you link plots to data sources. Selecting on a data
source will render that selection in each plot or table which is viewing it.

![wakariui](img/visualization_bokeh1.png)
![wakariui](img/visualization_bokeh2.png)

	"""
	Create a data source, and then 2 line plots which point at that data source.
	Selections will propagate across plots. Finally, create a table which views
	the data source
	"""
	source = p.make_source(x=x, y=y, z=z)
	p.plot(x', 'y', data_source=source)
	p.figure()
	p.plot(x', 'z', data_source=source)
	p.table(source, ['x', 'y', 'z'])

#### Other interesting options

	p.plot(x, y, width=300, height=300)
You can pass width or height into each plot specified in pixels.
	p.scatter(x, y)
p.scatter has the same syntax as p.plot, however, it will generate a scatter plot (which is basically the same thing, except without connecting the dots).
	p.plot_dates(x, y)
p.plot_dates will treat the x-axis as a date axis. We currently expect dates to be milliseconds since the epoch.

#### Examples

Your Anaconda Enterprise Notebooks account comes preloaded with a number of examples included in the ~scripts/examples directory.

### Plots
