__version__ = '1.1.1'
_puzh = None


def it(*objects, token=None, silent=False, sep=' '):
    global _puzh

    if _puzh is None:
        from puzh.puzh import Puzh
        _puzh = Puzh(None)

    _puzh.it(*objects, token=token, silent=silent, sep=sep)
