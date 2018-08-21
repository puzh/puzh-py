import requests
import threading


class Puzh:

    def __init__(self, token):
        if type(token) is not str and token is not None:
            raise TypeError('token must be a string, not %r' % token.__class__.__name__)
        self._token = token

    def it(self, *objects, token=None, silent=False, sep=' '):
        if self._token is None and (type(token) is not str or token is None):
            raise TypeError('token must be a string, not %r' % token.__class__.__name__)
        if type(silent) is not bool:
            raise TypeError('silent must be None or a bool, not %r' % silent.__class__.__name__)
        if type(sep) is not str:
            raise TypeError('sep must be None or a string, not %r' % sep.__class__.__name__)

        payload = dict(
            token=self._token if token is None else token,
            text=sep.join(objects),
            silent=str(silent).lower(),
        )
        thread = threading.Thread(target=requests.post,
                                  # args=('https://api.puzh.it',),
                                  args=(
                                    'https://us-central1-api-puzh-it.cloudfunctions.net/push',
                                  ),
                                  kwargs=dict(json=payload, timeout=60))
        thread.start()
