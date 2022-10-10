import setuptools

setuptools.setup(
    name = "pushed_py",
    version="v1.0.1",
    url="https://github.com/claudiosTime/get-pushed-python",
    author="claudiosTime",
    author_email="c.tappia@gmail.com",
    description="Package that enable interactions with get pushed service",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.8.13',
    ],
)