# -*- coding: utf-8 -*-
"""
Transforming python logs
"""
from __future__ import absolute_import
from collections import namedtuple

from .formatters import JSONFormatter, KeyValueFormatter, MessagePackFormatter
from .generic import create_logger

version_info = namedtuple("version_info", ["major", "minor", "patch"])
VERSION = version_info(0, 3, 3)

__title__ = "shapeshift"
__author__ = "Evan Briones"
__copyright__ = "Copyright 2015, Evan Briones"
__license__ = "MIT LICENSE"
__version__ = "{0.major}.{0.minor}.{0.patch}".format(VERSION)

__all__ = ["create_logger",
           "JSONFormatter", "KeyValueFormatter", "MessagePackFormatter"]
