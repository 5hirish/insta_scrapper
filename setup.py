try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    import unittest.mock

    has_mock = True
except ImportError:
    has_mock = False

# Package meta-data.
NAME = 'instascrape'
DESCRIPTION = 'A client interface for the private Instagram API.'
KEYWORDS = 'Instagram scrapper'
URL = 'https://github.com/5hirish/insta_scrapper'
EMAIL = 'shirishkadam35@gmail.com'
ORIGINAL_AUTHOR = 'ping <lastmodified@gmail.com>'
AUTHOR = 'Shirish Kadam'
REQUIRES_PYTHON = '>=3.5.*'
VERSION = '1.6.0'
LICENSE = 'mit'

PACKAGES = ['instascrape',
            'instascrape.endpoints',
            'web']
EXCLUDE = ["tests", "*.tests", "*.tests.*", "tests.*"]

test_reqs = [] if has_mock else ['mock']

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    url=URL,
    install_requires=[],
    test_requires=test_reqs,
    keywords=KEYWORDS,
    description=DESCRIPTION,
    packages=PACKAGES,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.5',
    ]
)
