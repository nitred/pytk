"""Setup file for the package/project."""

from setuptools import setup, find_packages

setup(
    name='pytk',
    version='0.0.0.dev1',
    description='Python toolkit which contains common scripts.',
    long_description='Python toolkit which contains common scripts',
    author='Nitish Reddy Koripalli',
    author_email='nitish.k.reddy@gmail.com',
    url='https://github.com/nitred/pynrtk',
    classifiers=[
        'Development Status :: 1 - Basics',
        'Programming Language :: Python :: 2.7',
    ],
    license='MIT',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
)
