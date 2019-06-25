import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="puzzle",
    version="1.0.0",
    description="Engine Group Coding Assessment",
    long_description=readme,
    packages=find_packages(),
    install_requires=["flask"]
)