# -*- coding: utf-8 -*-
"""TcEx Framework"""
__author__ = 'ThreatConnect (support@threatconnect.com)'
__version__ = '1.0.0'
__license__ = 'Apache License, Version 2'
name = 'tcex'

try:
    from .tcex import TcEx  # noqa: F401
except ImportError as e:
    print('Error: {}'.format(e))
    print('Try running tc_lib')

from .tcex_argparser import TcExArgParser  # noqa: F401; pylint: disable=C0413
