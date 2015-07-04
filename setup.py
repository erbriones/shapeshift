from setuptools import setup
from shapeshift import __version__

setup(
    name='shapeshift',
    version=__version__,
    author='erbriones',
    author_email='evan@evanbriones.com',
    description=("A collection of python logging formats and helpers for "
                 "transforming logs."),
    long_description=open("README.md").read(),
    license="MIT License",
    url="https://github.com/erbriones/shapeshift",
    packages=['shapeshift'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Logging"
    ])
