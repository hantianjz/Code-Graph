import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
    name="code_graph",
    version="0.0.1",
    author="HJZ",
    author_email="hjz@hackjumpzero.ca",
    description="A visualization tool for graphing relationships of a C/Cpp code base",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hantianjz/Code-Graph",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix / Linux",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': ['cgraph=code_graph:main',],
    },
)
