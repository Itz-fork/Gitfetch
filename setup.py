# Copyright (c) 2021 - Itz-fork
# Project: Gitfetch
import os

from gitfetch_tools import __version__ as version
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Readme
if os.path.isfile('README.md'):
  with open(('README.md'), encoding='utf-8') as readmeh:
    project_description = readmeh.read()
else:
  project_description = "Gitfetch is a simple tool to get github user details"

setup(name='Gitfetch',
version=version,
description=project_description,
url='https://github.com/Itz-fork/Gitfetch',
author='Itz-fork',
author_email='itz-fork@users.noreply.github.com',
license='MIT',
packages=find_packages(),
scripts=['gitfetch'],
include_package_data=True,
download_url=f"https://github.com/Itz-fork/Gitfetch/releases/tag/Gitfetch-{version}",
keywords=['python', 'bash', 'github', 'gitfetch'],
long_description=project_description,
long_description_content_type='text/markdown',
install_requires=['requests'],
classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
  ]
)