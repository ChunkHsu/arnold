# 进入到 utils目录，/isaac-sim/python.sh setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(name="compute_points", ext_modules=cythonize('compute_points.pyx'),)