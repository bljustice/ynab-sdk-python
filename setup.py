from setuptools import setup, find_packages

from ynab import __version__

setup(
    name='ynab-sdk-python',
    description='A minimal Python API client for YNAB',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    install_requires=['requests'],
    python_requires='>=3, <4'
)
