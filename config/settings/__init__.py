"""
Settings used by django auth service project.
This consists of the general produciton settings, with an optional import of any local
settings.
"""
from config.settings.production import *

try:
    from config.settings.local import *
except ImportError:
    pass
