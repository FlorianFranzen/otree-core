#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =============================================================================
# CONSTANTS and confs
# =============================================================================

VERSION = ('0', '3', '14')

__version__ = ".".join(VERSION)

default_app_config = 'otree.apps.OtreeConfig'


# =============================================================================
# FUNCTIONS
# =============================================================================

def get_version():
    return __version__
