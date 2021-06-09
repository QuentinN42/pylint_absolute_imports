# coding: utf-8
from setuptools import setup


setup(
    name='pylint-relative-imports',
    version='0.0.1',
    package_dir={'': 'src'},
    packages=['pylint_relative_imports'],
    url='',
    license='MIT License',
    author='Andrey Chernykh',
    author_email='moonquiz@ya.ru',
    description=(
        'Pylint plugin for Django projects which adds linter error '
        'for relative import from another Django app'
    ),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ),
    install_requires=(
        'pylint>=2.5.0,<3',
    )
)