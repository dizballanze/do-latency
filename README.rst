Digital Ocean latency checker
=============================

.. image:: http://badge.kloud51.com/pypi/v/do-latency.svg
    :target: https://pypi.python.org/pypi/do-latency
    :alt: PyPI Version

.. image:: http://badge.kloud51.com/pypi/w/do-latency.svg
    :target: https://pypi.python.org/pypi/do-latency
    :alt: PyPI Wheel

.. image:: http://badge.kloud51.com/pypi/s/do-latency.svg
    :target: https://pypi.python.org/pypi/do-latency
    :alt: PyPI Status

.. image:: http://badge.kloud51.com/pypi/l/do-latency.svg
    :target: https://pypi.python.org/pypi/do-latency
    :alt: PyPI License

.. image:: http://badge.kloud51.com/pypi/f/do-latency.svg
    :target: https://pypi.python.org/pypi/do-latency
    :alt: PyPI Format

.. image:: http://badge.kloud51.com/pypi/p/do-latency.svg
    :target: https://pypi.python.org/pypi/do-latency
    :alt: PyPI Py_versions

.. image:: http://badge.kloud51.com/pypi/d/do-latency.svg
    :target: https://pypi.python.org/pypi/do-latency
    :alt: PyPI Downloads

.. image:: http://badge.kloud51.com/pypi/i/do-latency.svg
    :target: https://pypi.python.org/pypi/do-latency
    :alt: PyPI Implementation

.. image:: http://badge.kloud51.com/pypi/e/do-latency.svg
    :target: https://pypi.python.org/pypi/do-latency
    :alt: PyPI Egg

Digital Ocean latency checker helps to find fastest DO region from your location.

INSTALLATION
------------

::

    pip install do-latency

USAGE
-----

.. image:: https://raw.githubusercontent.com/dizballanze/do-latency/master/usage.gif

-  **-h, --help** - show help
-  **--ping-count** - count of ICMP requests for latency check (default: 10)
-  **--file-size {10mb, 100mb}** - size of downloaded file (default: 10mb). 
-  **--udp** - use UDP not ICMP.

**In some linux systems UDP testing does not work, so you should use true ICMP and run `do-latency` from root:**

::

    sudo do-latency


TODO
----

[x]  latency check with ICMP

[x]  download speed measurement

[x]  python 3 support

LICENSE
-------

MIT
