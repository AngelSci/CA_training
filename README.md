# Introductory Python Programming using Anaconda

## Course Material

This course has been created using [Jupyter Notebooks](http://jupyter.org/)

## Requirements

We will be using Anaconda throughout the course. Please download, sign up, and install those free tools before class begins.

This course material has been designed to run in Python 3, specifically, Python 3.5. *PLEASE MAKE SURE TO DOWNLOAD A PYTHON 3 INSTALLER.*

[Download Anaconda](https://www.continuum.io/downloads)

## Setup and run the Jupyter Notebook

We highly recommend that a new Python 3.5 [conda](http://conda.pydata.org/docs/) environment be setup for this course.

1. Open your terminal
    + On Mac OS X: Open Applications/Terminal.app
    + On Windows: Select from the Start Menu Anaconda3 -> Anaconda Prompt

2. Create a new conda environment

    + Navigate to the location of this course directory using `cd` in Linux, Mac OSX and Windows

```
conda env create -f environment.yml
```

3. Activate the environment in your terminal
    + On Linux and Mac OSX run:

```
source activate anaconda_training
```

    + On Windows  run:

```
activate anaconda_training
```

4. Navigate to the location of this course directory
    + Using `cd` in Linux, Mac OSX and Windows

5. Launch `Python.ipynb` notebook from the terminal

```
jupyter notebook Python.ipynb
```
