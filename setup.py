import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stringfunctions",
    version="0.1.0",
    author="Jakob Majkilde",
    author_email="jakob@mjakilde.dk",
    description="String functions for Python 3",
    long_description=long_description,
    url="https://github.com/majkilde/stringfunctions.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)