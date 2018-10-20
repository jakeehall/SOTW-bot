import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SOTW-bot",
    version="1.0.0",
    author="Jacob Hall",
    author_email="jakeehall@gmail.com",
    description="A Reddit bot that selects random songs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: MIT License",
        "Operating System :: Linux",
    ],
)
