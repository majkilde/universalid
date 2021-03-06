UniversalID
===========

Generates unique id's based on the current date/time

Features
--------

* Unid includes a datetime stamp - your can extract the creation time from a Unid
* You can assign a custom prefix to your id, e.g. a country code
* Unid is case-insentitive 
* Base 36 encoded (digits + letters from A-Z) 
* Uses the _secrets_ library to generate cryptographically strong pseudo-random numbers
* Fully documented: https://universalid.readthedocs.io/en/latest/
* 100% coverage


Installation
------------

Install the latest release from `PyPI <https://pypi.org/project/universalid/>`_:

.. code-block:: sh

    pip install universalid

Usage
---------------

The Unid class is available directly off the :code:`universalid` package::

    >>> from universalid import Unid
    >>> Unid.create(prefix='DK')
    'DKDQ2D6JCJXI2Q82J06X0PK16P34XDO0'

    >>> unid = Unid.create()
    >>> Unid.get_time( unid )
    datetime.datetime(2018, 12, 20, 11, 36, 27, 756356)

Links
-----

Useful links

* Nano Id collision `calculator <https://zelark.github.io/nano-id-cc/>`_
* `Universal ID <https://www-01.ibm.com/support/docview.wss?uid=swg21112556>`_ in Lotus Notes

Contribute
----------

- Issue Tracker: github.com/$project/$project/issues
- Source Code: https://github.com/majkilde/universalid.git


License
-------

The project is licensed under the MIT license.