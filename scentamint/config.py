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
import configparser
from os.path import isfile, realpath
from shutil import copyfile


CONFIG_FILE_LOCATION = '/etc/scentamint.ini'


def get():
    """
    Imports the input ini file containing the config

    :return: scentamint config
    :rtype: dict
    """
    # Making sure our config file exists
    ensure_config_file_exists()

    # Importing config ini
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_LOCATION)

    # Some config values are internal only
    config_data = {
        "debug": False
    }

    for key in config['scentamint']:
        config_data[key] = config['scentamint'][key]

    return config_data


def ensure_config_file_exists():
    """
    Make sure the config file exists or create it if not
    """
    if not isfile(CONFIG_FILE_LOCATION):
        copyfile(
            realpath(__file__ + '/../data/scentamint.ini'),
            CONFIG_FILE_LOCATION
        )
