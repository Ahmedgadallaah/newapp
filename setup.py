# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
        install_requires = f.read().strip().split('\n')

setup(
        name='net_contract',
        version='',
        description='net_contract',
        author='Ahmed',
        author_email='info@qp.sa',
        packages=find_packages(),
        zip_safe=False,
        include_package_data=True,
        install_requires=install_requires
)

