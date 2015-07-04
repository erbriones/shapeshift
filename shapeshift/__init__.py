# -*- coding: utf-8 -*-
"""
Transforming python logs
"""
from collections import namedtuple

from formatters import JSONFormatter

version_info = namedtuple("version_info", ["major", "minor", "patch"])
VERSION = version_info(0, 1, 2)
__version__ = "{0.major}.{0.minor}.{0.patch}".format(VERSION)

__all__ = ["JSONFormatter"]
