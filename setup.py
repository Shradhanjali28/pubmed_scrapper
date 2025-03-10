from setuptools import setup, find_packages

setup(
    name="pubmed_scraper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "pubmed_scraper=cli:main",
        ],
    },
    author="Your Name",
    author_email="your_email@example.com",
    description="A PubMed scraper for extracting papers with non-academic authors.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pubmed_scraper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
