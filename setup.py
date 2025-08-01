from setuptools import setup, find_packages

setup(
    name="sound_converter",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "sound_convert=sound_converter.sound_converter:main",
        ],
    },
    author="jtsoco",
    description="A utility to convert files using ffmpeg.",
)
