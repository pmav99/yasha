import re
import ast
from setuptools import setup, find_packages

# _version_re = re.compile(r'__version__\s+=\s+(.*)')
#
# with open('yasha/yasha.py', 'rb') as f:
#     __version__ = str(ast.literal_eval(_version_re.search(
#         f.read().decode('utf-8')).group(1)))

__version__ = "5.0.1"

setup(
    name="yasha",
    author="Kim Blomqvist",
    author_email="kblomqvist@iki.fi",
    version=__version__,
    description="A command-line tool to render Jinja templates",
    keywords=["jinja", "code generator"],
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "Click",
        "Jinja2>=2.11",
        "pytoml",
        "pyyaml",
        "xmltodict",
    ],
    entry_points='''
        [console_scripts]
        yasha=yasha.cli:cli
    ''',
    classifiers=[
        "Topic :: Software Development :: Code Generators",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    url="https://github.com/kblomqvist/yasha",
    download_url="https://github.com/kblomqvist/yasha/tarball/" + __version__,
)
