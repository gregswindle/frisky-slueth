"""
Setup script.
"""

from distutils.core import Command
from setuptools import setup


class Coverage(Command):
    """
    Coverage setup.
    """

    description = (
        "Run test suite against single instance of"
        "Python and collect coverage data."
    )
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import coverage
        import unittest

        cov = coverage.coverage(config_file='.coveragerc')
        cov.erase()
        cov.start()

        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover(start_dir='tests')
        unittest.TextTestRunner().run(test_suite)

        cov.stop()
        cov.save()
        cov.report()
        cov.html_report()


setup(
    author='Greg Swindle',
    author_email='greg@swindle.net',
    description='frisky_sleuth',
    download_url='',
    cmdclass={
        'coverage': Coverage,
    },
    install_requires=[
    ],
    license='Apache License (2.0)',
    name='frisky_sleuth',
    packages=[
        'frisky_sleuth',
    ],
    scripts=[],
    test_suite='tests',
    tests_require=[
        'codecov>=2.0.15',
        'coverage>=4.5.2',
        'Sphinx>=1.8.2',
        'tox>=3.5.3',
        'virtualenv>=16.1.0'
    ],
    url='https://github.com/gregswindle/frisky_sleuth-sleuth#readme',
    version='1.0.0'
)
