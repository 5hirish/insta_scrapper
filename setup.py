import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

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
            'instascrape.web']
EXCLUDE = ["tests", "*.tests", "*.tests.*", "tests.*"]

CLASSIFIERS = [
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ]

# What packages are required for this module to be executed?
REQUIRED = [
    'lxml', 'requests',
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

TEST_REQS = [] if has_mock else ['mock']


# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=EXCLUDE),
    install_requires=[],
    extras_require={},
    include_package_data=True,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    test_requires=TEST_REQS,
    keywords=KEYWORDS,
    cmdclass={
        'upload': UploadCommand,
    },
)
