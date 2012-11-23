# -*- coding: utf-8 -*-

"""
erequests
~~~~~~~~~

This module contains an asynchronous replica of ``requests.api``, powered
by eventlet. All API methods return a ``Request`` instance (as opposed to
``Response``). A list of requests can be sent with ``map()``.
"""


import eventlet
from eventlet import monkey_patch
from eventlet import GreenPool as Pool

# Monkey-patch.
monkey_patch(all=True, thread=False, select=False)

from requests import api


__all__ = (
    'map', 'imap',
    'get', 'options', 'head', 'post', 'put', 'patch', 'delete', 'request'
)


def patched(f):
    """Patches a given API function to not send."""

    def wrapped(*args, **kwargs):

        kwargs['return_response'] = False
        kwargs['prefetch'] = True

        config = kwargs.get('config', {})
        config.update(safe_mode=True)

        kwargs['config'] = config

        return f(*args, **kwargs)

    return wrapped


def send(r, pool=None, prefetch=False):
    """Sends the request object using the specified pool. Pools are useful because you can specify size
    and can hence limit concurrency."""

    pool.spawn_n(r.send, prefetch=prefetch)


# Patched requests.api functions.
get = patched(api.get)
options = patched(api.options)
head = patched(api.head)
post = patched(api.post)
put = patched(api.put)
patch = patched(api.patch)
delete = patched(api.delete)
request = patched(api.request)


def map(requests, prefetch=True, size=None):
    """Concurrently converts a list of Requests to Responses.

    :param requests: a collection of Request objects.
    :param prefetch: If False, the content will not be downloaded immediately.
    :param size: Specifies the number of requests to make at a time. 
    """

    requests = list(requests)

    pool = Pool(size) if size is not None else Pool()

    for r in requests:
        send(r, pool, prefetch=prefetch)

    pool.waitall()

    return [r.response for r in requests]


def imap(requests, prefetch=True, size=2):
    """Concurrently converts a generator object of Requests to
    a generator of Responses.

    :param requests: a generator of Request objects.
    :param prefetch: If False, the content will not be downloaded immediately.
    :param size: Specifies the number of requests to make at a time. default is 2
    """

    pool = Pool(size)

    def send(r):
        r.send(prefetch)
        return r.response

    for r in pool.imap(send, requests):
        yield r

    pool.waitall()