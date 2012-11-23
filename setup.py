# -*- coding: utf-8 -*-
"""
ERequests allows you to use Requests with Eventlet to make asyncronous HTTP
Requests easily.

Usage
-----

Usage is simple::

    import erequests

    urls = [
        'http://www.heroku.com',
        'http://tablib.org',
        'http://httpbin.org',
        'http://python-requests.org',
        'http://kennethreitz.com'
    ]

Create a set of unsent Requests::

    >>> rs = (erequests.get(u) for u in urls)

Send them all at the same time::

    >>> erequests.map(rs)
    [<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>]

"""

from setuptools import setup

setup(
    name='erequests',
    version='0.1.0',
    url='https://github.com/jmg/erequests',
    license='BSD',
    author='Juan Manuel García',
    author_email='jmg.utn@gmail.com ',
    description='Requests + Eventlet',
    long_description=__doc__,
    install_requires=[
        'eventlet',
        'requests'
    ],
    py_modules=['erequests'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
