"Convenience function for starting Python programs"
from __future__ import absolute_import, division, print_function
from begin.context import context
from begin.convert import convert
from begin.main import start
from begin.subcommands import subcommand
from begin.version import __version__

from begin.extensions import tracebacks
from begin.extensions import logger_old as logging
from begin.extensions import logger

import begin.formatters
import begin.utils

__all__ = ['start']
