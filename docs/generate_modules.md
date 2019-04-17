# Generate Modules

This document shows the procedure for generating modules by yourself.  
You can choose the method to generate modules.

1. [Case 1: Use utility script](#case-1-use-utility-script)
2. [Case 2: Do it yourself all procedures](#case-2-do-it-yourself-all-procedures)


### Pre-requirement

#### Python Version

The generating script can be run on Python >= 3.5.  
Ensure that Python version is >= 3.5 on your environment.


#### Install requirement packages

The generating script uses the packages listed on [requirements.txt](../requirements.txt).  
Execute below command to install requirement packages.

```bash
$ pip install -r requirements.txt
```


### Setup IDE

After generating modules, you need to setup IDE to enable a code completion.

* [PyCharm](docs/setup_pycharm.md)
* [Visual Studio Code](docs/setup_visual_studio_code.md)
* [All Text Editor (Install as Python module)](docs/setup_all_text_editor.md)


## Case 1: Use utility script

#### 1. Download Blender binary

Download Blender binary from [Blender official download site](https://download.blender.org/release/).
Download Blender whose version is the version you try to generate modules.


#### 2. Download Blender sources

```
$ git clone git://git.blender.org/blender.git
```


#### 3. Download fake-bpy-module sources

Download the fake-bpy-module sources from GitHub.

Use Git and clone fake-bpy-module repository.

```
$ git clone https://github.com/nutti/fake-bpy-module.git
```

or

Download .zip file from GitHub.

https://github.com/nutti/fake-bpy-module/archive/master.zip


#### 4. Run script

```
$ cd fake-bpy-module/src
$ sh gen_module.sh <source-dir> <blender-dir> <branch/tag/commit> <output-dir>
```

* `<source-dir>`: Specify Blender sources directory.
* `<blender-dir>`: Specify Blender binary directory.
* `<branch/tag/commit>`: Specify target Blender source's branch for the generating modules.
  * If you want to generate modules for 2.79a, specify v2.79a
  * If you want to generate modules for newest Blender version, specify master
* `<output-dir>`: Specify directory where generated modules are output.


## Case 2: Do it yourself all procedures

#### 1. Download Blender binary

Download Blender binary from [Blender official download site](https://download.blender.org/release/).
Download Blender whose version is the version you try to generate modules.


#### 2. Download Blender sources

```
$ git clone git://git.blender.org/blender.git
```


#### 3. Change to the target branch/tag/commit

Be sure to match the version between sources and binary.
If you try to generate modules for v2.79, you should use `git checkout v2.79`.

```
$ cd blender
$ git checkout [branch/tag/commit]
```


#### 4. Generate .rst documents

Generated .rst documents are located on `doc/python_api/sphinx-in`.

```
$ blender --background --factory-startup -noaudio --python doc/python_api/sphinx_doc_gen.py
```


#### 5. Convert .rst to .xml

```
$ sphinx-build -b xml doc/python_api/sphinx-in <xml-out>
```


#### 6. Download fake-bpy-module sources

Download the fake-bpy-module sources from GitHub.

Use Git and clone fake-bpy-module repository.

```
$ git clone https://github.com/nutti/fake-bpy-module.git
```

or

Download .zip file from GitHub.

https://github.com/nutti/fake-bpy-module/archive/master.zip


#### 7. Generate modules

```
$ cd fake-bpy-module/src
$ python gen.py -i <input-dir> -o <output-dir> -t <target> -f <format>
```

* `-i <input-dir>`: Specify input directory. (the directory .xml files are located by process 5)
* `-o <output-dir>`: Specify output directory. (the directory generated files will be located)
* `-t <target>`: Specify IDE target. If this option is specified, the optimized modules will be generated.
  * `pycharm`: Optimized for PyCharm
* `-d`: Dump internal data structures to `<output-dir>` as the files name with suffix `-dump.json`
* `-f <format>`: Format the generated code using format
  * `pep8`: Format generated code using pep8 format
