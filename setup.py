# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
        install_requires = f.read().strip().split('\n')

# get version from __version__ variable in zatca2024/__init__.py
from newapp import __version__ as version

setup(
        name='net_contract',
        version=version,
        description='net_contract',
        author='Ahmed',
        author_email='info@qp.sa',
        packages=find_packages(),
        zip_safe=False,
        include_package_data=True,
        install_requires=install_requires
)

