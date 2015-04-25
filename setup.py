# coding: utf-8
from setuptools import setup

setup (
    name = 'scentamint',
    version = '1.0.0',
    url = 'https://github.com/hickeroar/scentamint',
    author = 'Ryan Vennell',
    author_email = 'ryan.vennell@gmail.com',
    description = 'A self-contained web api providing naïve bayesian text classification and training using simplebayes.',
    long_description = open('README.rst', 'r').read(),
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
    install_requires = [
        'simplejson',
        'simplebayes',
        'flask',
    ],
    packages = [
        'scentamint',
        'scentamint.service',
    ],
    entry_points={
        'console_scripts': [
            'scentamint = scentamint.server:launch_server',
        ],
    },
)
