from setuptools import setup

from scrapy_sticky_meta_params import __version__

with open("README.md") as f:
    readme = f.read()

setup(
    name="scrapy-sticky-meta-params",
    version=__version__,
    license="MIT license",
    description="A spider middleware that forwards meta params through subsequent requests.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Luiz Francisco Rodrigues da Silva",
    author_email="luizfrdasilva@gmail.com",
    url="https://github.com/heylouiz/scrapy-sticky-meta-params",
    packages=["scrapy_sticky_meta_params"],
    platforms=["Any"],
    keywords="scrapy meta middleware",
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=["Scrapy>=1.6.0"],
)
