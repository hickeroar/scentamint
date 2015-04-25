Scentamint
==========
A web api providing naïve bayesian text classification and training using simplebayes.
--------------------------------------------------------------------------------------

Build Status
------------
.. image:: https://travis-ci.org/hickeroar/scentamint.svg?branch=master
.. image:: https://img.shields.io/badge/pylint-10.00/10-brightgreen.svg?style=flat
.. image:: https://img.shields.io/badge/flake8-passing-brightgreen.svg?style=flat

Basic Server Usage
------------------
.. code-block:: bash

    $ sudo scentamint --help

    Scentamint Server Help:

        -h, --help
            Show this help

        -p [port], --port [port]
            Set the port the server should listen on

        -d, --debug
            Run the server in debug mode (errors displayed, debug output)

    $ sudo scentamint --port 80 --debug
     * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
     * Restarting with reloader
    # CTRL+C pressed

    $ sudo scentamint --port 80
     * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)

Config
------
Config file is /etc/scentamint.ini::

    [scentamint]

    ; set the location that we want to store the bayes training cache
    persist_location = /var/lib/scentamint/

    ; the default port this server will runon
    listen_port = 80

License
-------
::

    The MIT License (MIT)

    Copyright (c) 2015 Ryan Vennell

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
