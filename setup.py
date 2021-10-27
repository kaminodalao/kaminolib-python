import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kaminolib",
    version="0.0.1",
    author="kamino",
    author_email="kamino@imea.me",
    description="kamino's persional libiaries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamino-space/kaminolib-python",
    packages=setuptools.find_packages(),
)
