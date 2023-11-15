import os
import glob
import datetime
from setuptools import setup, find_packages

# module name
cur_dir = os.getcwd().replace("\\", "/")
blender_version = cur_dir.split('/')[-1].split('-')[-1]
module_name = f"fake-bpy-module-{blender_version}"

# release version
if "RELEASE_VERSION" in os.environ:
    print("Environment variable 'RELEASE_VERSION' exists, "
          "so use it as release version")
    release_version = os.environ["RELEASE_VERSION"]
else:
    print("Environment variable 'RELEASE_VERSION' does not exist, "
          "so use date as release version")
    release_version = datetime.datetime.today().strftime("%Y%m%d")

# long_description
try:
    readme_path = "{}/README.rst".format(
        os.path.dirname(os.path.abspath(__file__)).replace("\\", "/"))
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()
except IOError:
    long_description = ""   # pylint: disable=C0103

# find python module.
py_modules = list(set(glob.glob("*.py")) - {"setup.py"})
py_modules = [os.path.splitext(m)[0] for m in py_modules]

# find python packages and setup package data
packages = find_packages()
package_data = {pkg: ["py.typed"] for pkg in packages}

setup(
    name=module_name,
    version=release_version,
    url="https://github.com/nutti/fake-bpy-module",
    author="nutti",
    author_email="nutti.metro@gmail.com",
    maintainer="nutti",
    maintainer_email="nutti.metro@gmail.com",
    description="Collection of the fake Blender Python API module for "
                "the code completion.",
    long_description=long_description,
    project_urls={
        "Bug Tracker": "https://github.com/nutti/fake-bpy-module/issues",
        "Documentation": "https://github.com/nutti/fake-bpy-module/blob/"
                         "master/README.md",
        "Source Code": "https://github.com/nutti/fake-bpy-module",
    },
    platforms=["Windows", "Linux", "Mac OS-X"],
    py_modules=py_modules,
    package_data=package_data,
    packages=packages,
    zip_safe=False,
    python_requires=">=3.7",
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
