from setuptools import setup, find_packages

setup(
    name="ezpage",
    version="2.1.0",
    author="Ibrahim Mohsin",
    author_email="codingstudentbruh@gmail.com",
    description="A simple pagination library for Discord.py.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ibrahims-main/EzPage",
    packages=find_packages(),
    install_requires=["discord"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)