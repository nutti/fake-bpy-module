import os
import datetime
from setuptools import setup, find_packages

# module name
cur_dir = os.getcwd().replace("\\", "/")
blender_version = cur_dir.split('/')[-1].split('-')[-1]
module_name = "fake-bpy-module-{}".format(blender_version)

# version
version = datetime.datetime.today().strftime("%Y%m%d")

# long_description
try:
    readme_path = "{}/README.rst".format(os.path.dirname(os.path.abspath(__file__)).replace("\\", "/"))
    with open(readme_path, "r") as f:
        long_description = f.read()
except IOError:
    long_description = ""


setup(
    name=module_name,
    version=version,
    url="https://github.com/nutti/fake-bpy-module",
    author="Nutti",
    author_email="nutti.metro@gmail.com",
    maintainer="Nutti",
    maintainer_email="nutti.metro@gmail.com",
    description="Collection of the fake Blender Python API module for the code completion.",
    long_description=long_description,
    py_modules=[
        "bgl",
        "blf",
        "aud"
    ],
    packages=find_packages(),
    install_requires=["typing>=3.6.2"],
    license="MIT",
    classifiers=[
        "Topic :: Multimedia :: Graphics :: 3D Modeling",
        "Topic :: Multimedia :: Graphics :: 3D Rendering",
        "Topic :: Text Editors :: Integrated Development Environments (IDE)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)