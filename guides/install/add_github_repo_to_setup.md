# To install a package by adding it as a requirement in setup.py
```
"""Setup file for the package/project."""

from setuptools import find_packages, setup

setup(
    name='mocker',
    version='0.0.2',
    description='A library to generate mock `change of value` or `dataframe` data.',
    long_description='A library to generate mock `change of value` or `dataframe` data.',
    author='Nitish Reddy Koripalli',
    author_email='nitish.k.reddy@recogizer.de',
    url='https://bitbucket.org/recogizer/mocker',
    install_requires=['pylogging==0.1.0'],
    dependency_links=['https://github.com/ansrivas/pylogging/tarball/master#egg=pylogging-0.1.0'],
    packages=find_packages(),
    include_package_data=True,
)
```

### The key parts are:
```
install_requires=['pylogging==0.1.0'],
dependency_links=['https://github.com/ansrivas/pylogging/tarball/master#egg=pylogging-0.1.0'],
```
