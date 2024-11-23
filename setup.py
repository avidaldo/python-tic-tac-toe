from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

# Define the minimax module extension
extension = Extension(
    'minimax',
    sources=['minimax.pyx'],
    include_dirs=[numpy.get_include()]  # NumPy is needed because of type hints
)

setup(
    ext_modules=cythonize([extension])
)
