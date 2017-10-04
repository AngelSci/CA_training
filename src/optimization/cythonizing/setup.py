from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "sum2d library",
    ext_modules = cythonize("sum2d.pyx")
    )
