from setuptools import find_packages
from setuptools import setup

NAME = "phonebook"
VERSION = "0.0.7"

setup(
    name=NAME,
    version=VERSION,
    author="Vladimir Bondarevskiy",
    author_email="vbondarevsky@gmail.com",
    url="https://github.com/vbondarevsky/phonebook",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    python_requires=">=3.7.1",
    install_requires=[
        "pyyaml",
        "aiohttp",
        "SQLAlchemy",
        "passlib",
    ],
    zip_safe=True,
    entry_points={
        "console_scripts": [
            "phonebook = phonebook.main:run"
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.7.1",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
