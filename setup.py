from setuptools import setup, find_packages

setup(
    name='ynab-sdk-python',
    description='A minimal Python API client for YNAB',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    install_requires=['requests'],
    python_requires='>=3, <4'
)