# coding: utf-8
import sys
from setuptools import setup


requirements =  [
    'simplejson',
    'simplebayes',
    'flask',
]


# python2 requires us to install this.
if sys.version_info < (3,):
    requirements.append('configparser')


setup (
    name = 'scentamint',
    version = '1.1.2',
    url = 'https://github.com/hickeroar/scentamint',
    author = 'Ryan Vennell',
    author_email = 'ryan.vennell@gmail.com',
    description = 'A web api providing naïve bayesian text classification and training using simplebayes.',
    long_description = open('README.rst', 'r').read(),
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
    ],
    packages = [
        'scentamint',
        'scentamint.service',
    ],
    package_data = {
        'scentamint': [
            'data/*',
        ],
    },
    entry_points={
        'console_scripts': [
            'scentamint = scentamint.server:launch_server',
        ],
    },
    install_requires=requirements
)
