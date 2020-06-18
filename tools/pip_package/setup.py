import os
import glob
import datetime
from setuptools import setup, find_packages

# module name
cur_dir = os.getcwd().replace("\\", "/")
blender_version = cur_dir.split('/')[-1].split('-')[-1]
module_name = "fake-bpy-module-{}".format(blender_version)

# release version
if "RELEASE_VERSION" in os.environ:
    print("Environment variable 'RELEASE_VERSION' exists, so use it as release version")
    release_version = os.environ["RELEASE_VERSION"]
else:
    print("Environment variable 'RELEASE_VERSION' does not exist, so use date as release version")
    release_version = datetime.datetime.today().strftime("%Y%m%d")

# long_description
try:
    readme_path = "{}/README.rst".format(os.path.dirname(os.path.abspath(__file__)).replace("\\", "/"))
    with open(readme_path, "r") as f:
        long_description = f.read()
except IOError:
    long_description = ""

# find python module.
py_modules = list(set(glob.glob("*.py")) - {"setup.py"})
py_modules = [os.path.splitext(m)[0] for m in py_modules]

setup(
    name=module_name,
    version=release_version,
    url="https://github.com/nutti/fake-bpy-module",
    author="nutti",
    author_email="nutti.metro@gmail.com",
    maintainer="nutti",
    maintainer_email="nutti.metro@gmail.com",
    description="Collection of the fake Blender Python API module for the code completion.",
    long_description=long_description,
    py_modules=py_modules,
    packages=find_packages(),
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
