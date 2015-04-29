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
import simplejson
import getopt
import sys
from flask import Flask, request
from functools import wraps
from scentamint.service import SimpleBayesService


SERVER = Flask(__name__)
CONFIG = scentamint.config.get()
SERVICE = SimpleBayesService(CONFIG)


def validate_and_set_headers(action):
    """
    Generates a decorator to validate data
    and automatically add json headers

    :param action: the function we're decorating
    :type action: function
    :return: decorator function
    :rtype: function
    """
    @wraps(action)
    def decorator(*args, **kwargs):
        """
        Decorates a route match function

        :return: the results of this route action
        :rtype: tuple
        """
        headers = {
            'Content-Type': 'application/json'
        }

        # Just skipping the function call if
        if len(request.data.strip()) == 0:
            return encode({"data": "Missing Payload"}), 412, headers

        data, status = action(*args, **kwargs)
        return encode(data), status, headers

    return decorator


@SERVER.route("/train/<string:category>/", methods=['POST'])
@validate_and_set_headers
def train_action(category):
    """
    Trains a category

    :param category: the category we're training
    :type category: string
    :return: status code
    :rtype: tuple
    """
    SERVICE.train(category, request.data)
    return "", 204


@SERVER.route("/untrain/<string:category>/", methods=['POST'])
@validate_and_set_headers
def untrain_action(category):
    """
    Untrains a category

    :param category: the category we're untraining
    :type category: string
    :return: status code
    :rtype: tuple
    """
    SERVICE.untrain(category, request.data)
    return "", 204


@SERVER.route("/classify/", methods=['POST'])
@validate_and_set_headers
def classify_action():
    """
    Classifies a set of text

    :return: the winning category and status code
    :rtype: tuple
    """
    result = SERVICE.classify(request.data)
    return {'result': result}, 200


@SERVER.route("/score/", methods=['POST'])
@validate_and_set_headers
def score_action():
    """
    Scores a sample of text and returns per-category scores

    :return: scores and status code
    :rtype: tuple
    """
    results = SERVICE.score(request.data)
    return {'scores': results}, 200


@SERVER.route("/flush/", methods=['POST'])
@validate_and_set_headers
def flush_action():
    """
    Untrains all data in the classifier

    :return: status code
    :rtype: tuple
    """
    SERVICE.flush()
    return "", 204


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
    Scentamint Help
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

    SERVER.run(
        host="0.0.0.0",
        port=int(CONFIG['listen_port']),
        debug=CONFIG['debug']
    )


if __name__ == "__main__":
    launch_server()
