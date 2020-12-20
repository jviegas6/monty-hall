from setuptools import find_packages, setup
import os


VERSION = '0.0.1'
PACKAGE_NAME = 'montyHall'
AUTHOR = 'Jose Viegas'
AUTHOR_EMAIL = 'jviegas6@gmail.com'
URL = 'https://github.com/jviegas6/montyHall'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Describe your package in one sentence'
with open('README.md', 'r') as fi:
    LONG_DESCRIPTION = fi.read()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'random'
      , 'pandas'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      python_requires='>=3.6'
      )