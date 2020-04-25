import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devito4pytorch",
    version="0.0.4",
    author="Ali Siahkoohi",
    author_email="alisk@gatech.edu",
    description="Integrating Devito into PyTorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.gatech.edu/asiahkoohi3/Devito4PyTorch",
    license='MIT',
    packages=setuptools.find_packages()
)