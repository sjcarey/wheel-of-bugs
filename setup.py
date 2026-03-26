"""
Setup script for Wheel of Bugs application
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text() if (this_directory / "README.md").exists() else ""

# Read requirements
requirements = []
if (this_directory / "requirements.txt").exists():
    with open(this_directory / "requirements.txt") as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="wheel-of-bugs",
    version="1.0.0",
    description="A fun web application for spinning the wheel of software bugs!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/wheel_of_bugs",
    py_modules=["wheel_of_bugs"],
    include_package_data=True,
    package_data={
        "": ["bugs_config.json", "requirements.txt"],
    },
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "wheel-of-bugs=wheel_of_bugs:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9", 
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development",
    ],
    python_requires=">=3.8",
)