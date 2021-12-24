from setuptools import setup, find_packages
import yamltool

with open("README.rst", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="yamltool",
    version=yamltool.__version__,
    description=yamltool.__doc__.splitlines()[0],
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://git.shore.co.il/nimrod/yamltool",
    author="Nimrod Adar",
    author_email="nimrod@shore.co.il",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
    ],
    keywords="yaml",
    packages=find_packages(),
    install_requires=[
        "ruamel.yaml>=0.15.0",
    ],
    entry_points={"console_scripts": ["yt=yamltool.__main__:main"]},
)
