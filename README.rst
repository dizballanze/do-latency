Digital Ocean latency checker
=============================

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
