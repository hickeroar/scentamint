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
import simplebayes
from os.path import exists
from os import makedirs


class SimpleBayesService(object):
    """
    Interfaces with the simplebayes module
    """

    def __init__(self, config):
        """
        :param config: scentamint config
        :type config: dict
        """
        self.config = config

        if not exists(config['persist_location']):
            makedirs(config['persist_location'])

        self.classifier = \
            simplebayes.SimpleBayes(cache_path=config['persist_location'])

        # If there's a cache, load it
        self.classifier.cache_train()

    def train(self, category, text):
        """
        Trains a category with a sample of text and persists the cache

        :param category: the name of the category we want to train
        :type category: str
        :param text: the text we want to train the category with
        :type text: str
        """
        self.classifier.train(category, text)
        self.classifier.cache_persist()

    def untrain(self, category, text):
        """
        Untrains a category with a sample of text and persists the cache

        :param category: the name of the category we want to train
        :type category: str
        :param text: the text we want to untrain the category with
        :type text: str
        """
        self.classifier.untrain(category, text)
        self.classifier.cache_persist()

    def classify(self, text):
        """
        Chooses the highest scoring category for a sample of text

        :param text: sample text to classify
        :type text: str
        :return: the "winning" category
        :rtype: str
        """
        return self.classifier.classify(text)

    def score(self, text):
        """
        Scores a sample of text

        :param text: sample text to score
        :type text: str
        :return: dict of scores per category
        :rtype: dict
        """
        return self.classifier.score(text)

    def flush(self):
        """
        Deletes all tokens & categories
        """
        self.classifier.flush()
        self.classifier.cache_persist()
