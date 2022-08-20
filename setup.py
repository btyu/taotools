import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="taotools", # Replace with your own username
    version="0.0.2",
    author="HappyCtest",
    author_email="happyctest@foxmail.com",
    description="Small tools for more easy-use Python by HappyCtest. Evolving...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HappyCtest/taotools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)