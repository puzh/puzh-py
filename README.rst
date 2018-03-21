puzh
====

|Build Status| |PyPI version|

**puzh** is a simple wrapper package for the `puzh.it <https://puzh.it>`__ api. It supports
**python 3.x**.

You can easily push messages to the telegram `@puzhbot <https://t.me/puzhbot>`__.


Install
-------

::

    $ pip install puzh


Usage
-----

.. code:: py

    import puzh

    puzh.it('*Hi* ✌', token='secret_token')


API
---

puzh.\ ``it(*objects, token='secret', silent=False, sep=' ')``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Push a message to the telegram `@puzhbot <https://t.me/puzhbot>`__. Using ``silent=True`` will send
the message silently. Users will receive a notification without sound.

Messages can be formatted using `Markdown <https://core.telegram.org/bots/api#markdown-style>`__.
Multiple arguments will be separated by ``sep``, a space by default.

The method is executed asynchronously, if it fails, it will swallow any exception silently.


.. |Build Status| image:: https://travis-ci.org/puzh/puzh.py.svg?branch=master
    :target: https://travis-ci.org/puzh/puzh.py
.. |PyPI version| image:: https://img.shields.io/pypi/v/puzh.py.svg
    :target: https://pypi.org/project/puzh
