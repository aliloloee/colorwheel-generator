import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="colorwheel",
    version="1.0.0",
    description="Generate multi-color colorwheels",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/aliloloee/colorwheel-generator",
    author="Ali L.Jahromi",
    author_email="aliloloee82@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["colorwheel"],
    include_package_data=True,
    install_requires=["pathlib", "numpy", "opencv-python"],
)