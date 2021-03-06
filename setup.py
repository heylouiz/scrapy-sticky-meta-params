#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

requirements = []

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

setup(
    name='scrapy-sticky-meta-params',
    version='0.1.0',
    description="A spider middleware that forwards meta params through subsequent requests.",
    author='Luiz Francisco Rodrigues da Silva',
    author_email='luizfrdasilva@gmail.com',
    url='https://github.com/heylouiz/scrapy-sticky-meta-params',
    packages=find_packages(include=['scrapy_sticky_meta_params']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='scrapy meta middleware',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
