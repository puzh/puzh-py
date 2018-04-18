import threading


__version__ = '1.0.4'


def it(*objects, token='', silent=False, sep=' '):
    import requests

    if type(token) is not str or token is None:
        raise TypeError('token must be a string, not %r' % token.__class__.__name__)
    if type(silent) is not bool:
        raise TypeError('silent must be None or a bool, not %r' % silent.__class__.__name__)
    if type(sep) is not str:
        raise TypeError('sep must be None or a string, not %r' % sep.__class__.__name__)

    payload = {
        'token': token,
        'text': sep.join(objects),
        'silent': str(silent).lower(),
    }
    thread = threading.Thread(target=requests.post,
                              args=('https://api.puzh.it',),
                              kwargs=dict(json=payload, timeout=60))
    thread.start()
