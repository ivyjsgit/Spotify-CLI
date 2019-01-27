import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    install_requires=[
        'spotipy'
    ],
    dependency_links=[
        'git+https://github.com/plamere/spotipy.git#egg=spotipy'
    ],
    name="SpotifyCLI",
    version="0.1.1.4",
    author="Ivy Jackson",
    author_email="ivyjs@hendrix.edu",
    description="This program controls Spotify!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ivyjsgit/Spotify-CLI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    scripts=['bin/SpotifyCLI'],
)
