from setuptools import setup, find_packages

setup(
    name="train_db",
    version="0.1",
    packages=find_packages(include=["train_db", "train_db.*"]),
    install_requires=[
        "requests",
    ],
)
