"""
INEX Library
============

A comprehensive Python library for AI integration, web development, encryption,
database management, file operations, and more.

Package Name: inex-library
Contact Information:
------------------
- Phone/WhatsApp: +20109673019
- Email: pbstzidr@ywp.freewebhostmost.com
- GitHub: https://github.com/AmmarBasha2011/inex_library
- PyPI: https://pypi.org/project/inex-library

Version: 1.0.0
Last Updated: 2025-01-20
"""

__version__ = '1.0.0'
__author__ = 'INEX Team'
__email__ = 'pbstzidr@ywp.freewebhostmost.com'
__url__ = 'https://github.com/AmmarBasha2011/inex_library'
__description__ = 'A comprehensive Python library for AI integration, web development, and more.'
__copyright__ = '2025 INEX Team'
__license__ = 'MIT'

from . import AI
from . import Crypto
from . import Database
from . import EnDeCrypt
from . import FastAPIServer
from . import Files
from . import Libraries
from . import PrintStyle
from . import Security
from . import Server
from . import System
from . import Translate
from . import VideosCreator
from . import Websites

__all__ = [
    'AI',
    'Crypto',
    'Database',
    'Files',
    'Libraries',
    'System',
    'Translate',
    'VideosCreator',
    'Websites',
    'EnDeCrypt',
    'FastAPIServer',
    'PrintStyle',
    'Security',
    'Server'
]
