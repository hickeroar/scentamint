# coding: utf-8
import subprocess
from distutils import log
from setuptools import setup
from setuptools.command.install import install


class ScentamintInstall(install):
    """
    Extension of setuptools install class for post-install scripting
    """

    def run(self):
        """
        Runs the install and post-install actions
        """
        install.run(self)

        log.info('Creating Cache Directory.')
        command = 'mkdir -p /var/lib/scentamint/'
        subprocess.call(command, shell=True)

        log.info('Creating default config file (/etc/scentamint.ini).')
        command = 'cp '+self.install_lib+'data/scentamint.ini /etc/scentamint.ini'
        subprocess.call(command, shell=True)

        log.info('Done!')


setup (
    cmdclass = {
        'install': ScentamintInstall
    },
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
