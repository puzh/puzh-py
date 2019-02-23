import os
import pkg_resources

from puzh.puzh import Puzh

try:
    __version__ = pkg_resources.get_distribution('puzh').version
except Exception:
    __version__ = 'unknown'

_puzh = None


def it(*objects, token=None, silent=False, sep=' '):
    global _puzh

    if _puzh is None:
        _puzh = Puzh(None)

    _puzh.it(*objects, token=token, silent=silent, sep=sep)
