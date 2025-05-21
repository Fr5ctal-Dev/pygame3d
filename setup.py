from setuptools import setup, find_packages

# Read the long description from README.md
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pygame3d",
    version="0.1",
    description="A library for 3D rendering in PyGame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Fr5ctal",
    author_email="fr5ctal@gmail.com",
    url="https://github.com/Fr5ctal-Projects/pygame3d",
    license="MIT",
    packages=find_packages(where="src") if False else find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "panda3d>=1.10.15",
        "panda3d-gltf>=1.2.1",
        "pygame>=2.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
