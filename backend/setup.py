# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

setup(
    name="epagneul",
    version="0.1.0",
    description="Yes",
    long_description="long desc",
    author="",
    author_email="epagneul",
    url="http://",
    license="",
    packages=find_packages(),
    install_requires=[
        "pandas==1.3.5",
        "dynaconf==3.1.4",
        "loguru==0.5.3",
        "pydantic==1.8.2",
        "lxml==4.7.1",
        "fastapi==0.66.0",
        "uvicorn==0.14.0",
        "python-multipart==0.0.5",
        "aiofiles==0.7.0",
        "evtx==0.7.2",
        "neo4j==4.3.1",
        "scipy==1.7.3",
        "numpy==1.21.5",
    ],
    extras_require={
        "dev": [
            "coverage[toml]",
            "tox==3.23.0",
            "mock==4.0.3",
            "pytest==6.2.2",
            "flake8==3.9.0",
            "black==20.8b1",
            "mypy==0.812",
            "bandit==1.7.0",
            "pydocstyle==6.0.0",
            "pylint==2.7.4",
            "isort==5.8.0",
            "pygount==1.2.4",
            "coverage-badge==1.0.1",
        ],
    },
    python_requires=">=3.8.*, <3.9",
)
