import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="phonetizer-fr-dan", # Replace with your own username
    version="0.0.1",
    author="Dan Ringwald",
    author_email="dan.ringwald12@gmail.com",
    description="Translates French text to phonetics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/biggoron/phonetizer",
    packages=['phonetizer'],
    package_dir={'phonetizer': 'phonetizer'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pytest',
        'pandas >= 0.22.0',
        'numpy >= 1.16.0'
    ],
    scripts=['./scripts/word_to_phonem', './scripts/phonetizer-test'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
