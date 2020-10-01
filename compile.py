from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("main",  ["main.py"]),
    Extension("src.__init__",  ["src/__init__.py"]),
    Extension("src.math_func",  ["src/math_func.py"]),
    Extension("src.text_func",  ["src/text_func.py"]),
    ]

setup(
    name = 'Sample Program',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
        )
