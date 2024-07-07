import datetime
import os

from setuptools import setup

# release version
if "RELEASE_VERSION" in os.environ:
    print("Environment variable 'RELEASE_VERSION' exists, "
          "so use it as release version")
    release_version = os.environ["RELEASE_VERSION"]
else:
    print("Environment variable 'RELEASE_VERSION' does not exist, "
          "so use date as release version")
    release_version = datetime.datetime.now(tz=datetime.UTC).strftime("%Y%m%d")

setup(
    version=release_version,
    install_requires=[
        'typing_extensions>=4.7,<5',
    ],
)
