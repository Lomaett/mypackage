from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=["tests"]),
    license="MIT",
    description="EDSA example python package",
    install_requires=['numpy'],
    url="https://github.com/lomaett/TopNumberSorter",
    author="Ajiri Oguh",
    author_email="ajirioguh@gmail.com"
)