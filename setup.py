"""Setup file for the package/project."""
from setuptools import find_packages, setup

setup(
    name='pytk',
    version='0.0.1',
    description='Python toolkit which contains common scripts.',
    long_description='Python toolkit which contains common scripts',
    author='Ankur Srivastava, Nitish Reddy Koripalli',
    author_email='best.ankur@gmail.com , nitish.k.reddy@gmail.com',
    url='https://github.com/nitred/pytk',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
)
