#!python

import setuptools

setuptools.setup(
    name='my_ci_test',
    version='0.0.1',
    author='Bruno Quint',
    author_email='bquint@gemini.edu',
    description='A package created to test RTD and CI',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independentent",
    ],
)
