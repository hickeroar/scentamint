Scentamint
==========
A web api providing naïve bayesian text classification and training using simplebayes.
--------------------------------------------------------------------------------------

Build Status
------------
.. image:: https://travis-ci.org/hickeroar/scentamint.svg?branch=master
.. image:: https://img.shields.io/badge/pylint-10.00/10-brightgreen.svg?style=flat
.. image:: https://img.shields.io/badge/flake8-passing-brightgreen.svg?style=flat

Why?
----
::

    Bayesian text classification is often used for things like
    spam detection, sentiment determination, or general categorization.

    Essentially you collect samples of text that you know are of a certain
    "type" or "category," then you use it to train a bayesian classifier.
    Once you have trained the classifier with many samples of various
    categories, you can begin to classify and/or score text samples to see
    which category they fit best in.

    You could, for instance, set up classification of sentiment by finding
    samples of text that are happy, sad, angry, sarcastic, and so on, then
    train a classifier using those samples. Once your classifier is trained,
    you can begin to classify other text into one of those categories.

    What a classifier does is look at text and tell you how much that text
    "looks like" other categories of text that it has been trained for.

Installation
------------
::

    sudo pip install scentamint

Config
------
Config file location is /etc/scentamint.ini::

    [scentamint]

    ; set the location that we want to store the bayes training cache
    persist_location = /var/lib/scentamint/

    ; the default port this server will run on
    listen_port = 80

Server Usage
------------
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
    # CTRL+C pressed

    # A simple, no fuss, server execution command.
    $ sudo nohup scentamint >> /var/log/scentamint.log 2>&1 &

API Usage
---------

All endpoints accept POST commands and return predictable results depending on what is posted.

Training the Classifier
-----------------------
Endpoint::

    /train/<string:category>/ (ex: /train/spam/)

Result Status::

    204 No Content

- The POST payload should contain the raw text that will train the classifier.
- You can train a category as many times as you want.

Untraining the Classifier
-------------------------
Endpoint::

    /untrain/<string:category>/ (ex: /train/ham/)

Result Status::

    204 No Content

- The POST payload should contain the raw text that will train the classifier.
- You can untrain a category as many times as you want, but a token's value will not go below zero.
- This action carries out the inverse operation of training so unintentional trains can be reversed.

Classifying Text
----------------
Endpoint::

    /classify/

Result Status::

    200 OK

Result JSON Example::

    {
        "result": "ham"
    }

- The POST payload should contain the raw text that you want to classify.

Scoring Text
------------
Endpoint::

    /score/

Result Status::

    200 OK

Result JSON Example::

    {
        "scores": {
            "ham": 268.4685238156538,
            "spam": 44.531476184346225
        }
    }

- The POST payload should contain the raw text that you want to score.

Emptying All Classifier Training Data
-------------------------------------
Endpoint::

    /flush/

Result Status::

    204 No Content

- This is a purely destructive, non-reversable action.

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
