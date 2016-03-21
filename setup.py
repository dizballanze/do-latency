# -*- coding: utf-8 -*-

from setuptools import setup
import re
import os
import io

def read(fname):
    return io.open(os.path.join(os.path.dirname(__file__), fname), encoding="UTF-8").read()

version = re.search('^__version__\s*=\s*"(.*)"',
                    open('do_latency/__init__.py').read(), re.M).group(1)

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='do-latency',
    version=version,
    author='Yuri Shikanov',
    author_email='dizballanze@gmail.com',
    packages=['do_latency'],
    # scripts=[],
    url='https://github.com/dizballanze/do-latency',
    license='MIT',
    description='Digital Ocean latency checker helps to find fastest DO region from your location.',
    long_description=read('README.rst'),
    install_requires=required,
    data_files=[('', ['LICENSE', 'README.rst'])],
    entry_points={
        "console_scripts": ['do-latency = do_latency.do_latency:main']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='digital ocean latency ping connection speed ICMP'
)
