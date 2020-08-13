from setuptools import find_packages, setup

__package_name__ = "software_testing"
__version__ = "0.1.0"
__repository_url__ = "https://github.com/rafaelleinio/software_testing"

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name=__package_name__,
    description="Repository for the 2020 class of Software Engineering at UNIFESP.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="software testing tests",
    version=__version__,
    url=__repository_url__,
    packages=find_packages(
        exclude=(
            "docs",
            "tests",
            "tests.*",
            "pipenv",
            "env",
            "examples",
            "htmlcov",
            ".pytest_cache",
        )
    ),
    license="MIT",
    author="Rafael Leinio Pereira",
    install_requires=requirements,
    python_requires=">=3.7, <4",
)
