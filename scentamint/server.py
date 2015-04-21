#!/usr/bin/python
"""
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
"""
import scentamint.config
import simplebayes
import simplejson
import getopt
import sys
from flask import Flask, request


SCENTAMINT_SERVER = Flask(__name__)
CONFIG = scentamint.config.get()
CLASSIFIER = simplebayes.SimpleBayes()


def set_headers(action):
    data, status = action()
    return data, status, {}


@SCENTAMINT_SERVER.route("/train/<string:category>/", methods=['POST'])
def train_action(category):
    pass


@SCENTAMINT_SERVER.route("/untrain/<string:category>/", methods=['POST'])
def untrain_action(category):
    pass


@SCENTAMINT_SERVER.route("/classify/", methods=['POST'])
def classify_action():
    if len(request.data.strip()) == 0:
        return encode({"data":"Missing Payload"}), 412,
    return "", 204
    pass


@SCENTAMINT_SERVER.route("/score/", methods=['POST'])
def score_action():
    pass


def encode(data):
    """
    Encodes the data as json.

    :return: the encoded data
    :rtype: str
    """
    return simplejson.dumps(
        data,
        ensure_ascii=False,
        encoding='utf8',
        indent=4
    )


def usage():
    """
    Cahoots Help
    """
    print("")
    print("Scentamint Server Help:")
    print("")
    print("\t-h, --help")
    print("\t\tShow this help")
    print("")
    print("\t-p [port], --port [port]")
    print("\t\tSet the port the server should listen on")
    print("")
    print("\t-d, --debug")
    print("\t\tRun the server in debug mode (errors displayed, debug output)")
    print("")


def launch_server():
    """
    Executes the scentamint server
    """
    try:
        opts, _ = getopt.getopt(
            sys.argv[1:],
            "hp:d",
            ["help", "port=", "debug"]
        )
    except getopt.GetoptError as gerror:
        print('\nError: ' + gerror.msg)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-d", "--debug"):
            CONFIG['debug'] = True
        elif opt in ("-p", "--port"):
            try:
                CONFIG['listen_port'] = int(arg)
                if CONFIG['listen_port'] > 65535:
                    raise ValueError
            except ValueError:
                print('\nError: Invalid port')
                usage()
                sys.exit()

    SCENTAMINT_SERVER.run(
        host="0.0.0.0",
        port=int(CONFIG['listen_port']),
        debug=CONFIG['debug']
    )


if __name__ == "__main__":
    launch_server()
