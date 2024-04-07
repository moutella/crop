from setuptools import setup, find_packages

setup(
    name="crop",
    version="0.0.1",
    description="Image Cropper CLI.",
    packages=find_packages(),
    install_requires=["Pillow"],
    entry_points={"console_scripts": ["crop=fastcrop.cli:main"]},
)
