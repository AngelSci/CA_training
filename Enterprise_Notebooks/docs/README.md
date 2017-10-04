This is a sample project to practice using Anaconda Enterprise Notebooks

1. Create a new account
  * URL: http://ec2-54-236-245-201.compute-1.amazonaws.com/
1. Create a new private project
  * It can be named `flights`
1. Launch a terminal to create conda env
  * run `conda create -n flights python=3.5 pandas bokeh`
1. Upload the notebook and data files
  * must be at the same directory level
1. Start the notebook
  * launch the `Flight_delays.ipynb` notebook
  * change the kernel to `flights`
  * Decide on year and month while running the cells
  * save the notebook
1. Revision control
  * commit the notebook
  * change the year and month
  * save the notebook
  * revert to earlier commit
