"""Install the package."""
from setuptools import setup  # type: ignore

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pylint_absolute_imports',
    version='1.0.1',
    packages=['pylint_absolute_imports'],
    url='https://github.com/quentinn42/pylint_absolute_imports',
    license='MIT License',
    author='Quentin Lieumont',
    author_email='quentin@lieumont.fr',
    description=(
        'Pylint plugin which adds linter error for relatives imports.'
        'Read more about imports at https://peps.python.org/pep-0008/#imports'
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
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
