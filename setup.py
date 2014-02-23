import os
from setuptools import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "instant_coverage.tests.settings")

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name='django-instant-coverage',
    description='Better-than-nothing testing for Django',
    url='https://github.com/colons/instant-coverage',
    version='0.0.1',
    license="BSD",
    platforms=['any'],
    packages=['instant_coverage'],
    install_requires=[
        'Django',
        'mock',
        'beautifulsoup4',
        'requests',
    ],
    tests_require=['nose'],
    test_suite='nose.collector',
    long_description=README,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing',
    ],
)
