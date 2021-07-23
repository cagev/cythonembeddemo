
import sys 
import multiprocessing
from setuptools import setup
from Cython.Build import cythonize
from Cython.Distutils.extension import Extension

NB_COMPILE_JOBS = 4

#[   "engine.pyx", "market.pyx" ,"network.pyx", "bench.pyx" ], 
#include_path = ["mods", "../libs/buscli/include", "../libs/utils", "../opt/asio-1.18.1/include" ]

EXTENSIONS = [
        Extension("embedded",  ["embedded.pyx"],  include_path = ["mods", "../libs/buscli/include", "../libs/utils", "../opt/asio-1.18.2/include" ]),
        Extension("market",  ["market.pyx"],  include_path = ["mods", "../libs/buscli/include", "../libs/utils", "../opt/asio-1.18.2/include" ]),
        Extension("network",  ["network.py"],  include_path = ["mods", "../libs/buscli/include", "../libs/utils", "../opt/asio-1.18.2/include" ]),
              ]

def setup_given_extensions(extensions):
    setup( name = "embedded" , 
          ext_modules=cythonize(extensions),
         )

def setup_extensions_in_sequential():
    setup_given_extensions(EXTENSIONS)

def setup_extensions_in_parallel():
    cythonize(EXTENSIONS, nthreads=NB_COMPILE_JOBS)
    pool = multiprocessing.Pool(processes=NB_COMPILE_JOBS)
    pool.map(setup_given_extensions, EXTENSIONS)
    pool.close()
    pool.join()

if "build_ext" in sys.argv:
    setup_extensions_in_parallel()
else:
    setup_extensions_in_sequential()

