# -*- coding: utf-8 -*-
"""
Generic logging functions
"""

import sys
import logging


def create_logger(name, formatter=None, handler=None, level=None):
    """
    Returns a new logger for the specified name.
    """
    logger = logging.getLogger(__name__)

    #: use a standard out handler
    if handler is None:
        handler = logging.StreamHandler(sys.stdout)

    #: set the formatter when a formatter is given
    if formatter is not None:
        handler.setFormatter(formatter)

    #: set DEBUG level if no level is specified
    if level is None:
        level = logging.DEBUG

    handler.setLevel(level)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
