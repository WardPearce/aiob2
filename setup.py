import os
import re


from setuptools import setup


def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


def get_long_description():
    with open("README.md", encoding="utf8") as f:
        return f.read()


def get_version(package):
    with open(os.path.join(package, "__init__.py")) as f:
        return re.search(
            "__version__ = ['\"]([^'\"]+)['\"]", f.read()
        ).group(1)


setup(
    name='aiob2',
    version=get_version("aiob2"),
    url="https://github.com/WardPearce/aiob2",
    description='Backblaze B2 Asynchronous Wrapper.',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author='WardPearce',
    author_email="wardpearce@protonmail.com",
    install_requires=get_requirements(),
    license='Apache License 2.0',
    packages=[
        'aiob2',
        'aiob2.bucket',
        'aiob2.file',
        'aiob2.source_file'
    ],
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False
)
