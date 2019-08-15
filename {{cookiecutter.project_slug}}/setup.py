#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""
import re
import codecs
import os


from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    {%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=6.0',{%- endif %}
]

setup_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %} ]

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest',{%- endif %} ]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_pakcage_info(info, *file_paths):
    info_file = read(*file_paths)

    match = re.search(r"^__" + re.escape(info) + r"__ = ['\"]([^'\"]*)['\"]", info_file, re.M)

    if match:
        return match.group(1)
    raise RuntimeError("Unable to find {} string.".format(info))

setup(
    author=find_pakcage_info('author', 'src', '{{ cookiecutter.project_slug }}', '__init__.py'),
    author_email=find_pakcage_info('email', 'src', '{{ cookiecutter.project_slug }}', '__init__.py'),
    version=find_pakcage_info('version', 'src', '{{ cookiecutter.project_slug }}', '__init__.py'),

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    package_dir={"":"src"},
    packages=find_packages(
        where="src",
        exclude=["contrib", "docs", "tests*", "tasks"],
    ),
    # package_data={'yourpackage': ['*.txt', 'path/to/resources/*.txt']},
    description="{{ cookiecutter.project_short_description }}",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
        ],
    },
    {%- endif %}
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
)
