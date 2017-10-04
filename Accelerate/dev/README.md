# README

## What's needed?

* CUDA GPU and drivers
* `import accelerate` (use 30 day trial or get a license)

## Lesson Plan

See [PLAN.md](PLAN.md)

## Content summary

1. Strategies for profiling and improving Python and NumPy code performance
    * `02_Optimization_and_Profiling.ipynb`
    * `03_Accelerate_Profiler.ipynb`
2. Speeding up array math for multicore CPUs and GPUs
    * `04_Accelerate_Numba.ipynb`
3. Accelerated signal processing and linear algebra using multicore CPUs and GPUs
    * Stand-alone example src/fftconvolve.py (show built-in and Guernica.jpg)
    * `05_Accelerate_Signal_Processing.ipynb`
    * `11_Accelerate_Dask_FFT_Convolution.ipynb`
    * `12_Accelerate_PySpark_FFT_Convolution.ipynb`
4. GPU programming basics with Python
    * `06_Accelerate_GPU_Programming.ipynb`
5. Natural language processing
    * Topic clustering of documents (uses LDA)
    * *BROKEN: Word2Vec unsupervised learning.*
    * Preparing text for analysis (uses D-L algorithm to fix mispellings and possibly word2vec for certain kinds of applications)
    * `07_Accelerate_NLP_LDA.ipynb`
    * `08_Accelerate_NLP_Word2Vec.ipynb`
    * `09_Accelerate_NLP_DL_Distance.ipynb`
6. Feature detection in images
    * `10_Accelerate_Feature_Detection.ipynb`
7. Using Accelerate with Dask (*SKIP: Spark equivalent*)
    * `11_Accelerate_Dask_FFT_Convolution.ipynb`
    * `12_Accelerate_PySpark_FFT_Convolution.ipynb`
