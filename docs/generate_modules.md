# Generate Modules

This document shows the procedure for generating module by yourself.
You can choose the method to generate module.

1. [Case 1: Use utility script](#case-1-use-utility-script)
2. [Case 2: Do it yourself all procedures](#case-2-do-it-yourself-all-procedures)


## Case 1: Use utility script

#### 1. Download Blender binary

Download Blender binary from [Blender official download site](https://download.blender.org/release/).
Download Blender whose version is the version you try to generate modules.


#### 2. Download Blender sources

```
$ git clone git://git.blender.org/blender.git
```


#### 3. Run script

```
# sh gen_module.sh <source-dir> <blender-dir> <version>
```

* `<source-dir>`: Specify Blender sources directory.
* `<blender-dir>`: Specify Blender binary directory.
* `<version>`: Specify Blender version.


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


#### 6. Generate modules

```
$ python gen.py -i <input-dir> -o <output-dir> -t <target> -f <format>
```

* `-i <input-dir>`: Specify input directory. (the directory .xml files are located by process 5)
* `-o <output-dir>`: Specify output directory. (the directory generated files will be located)
* `-t <target>`: Specify IDE target. If this option is specified, the optimized modules will be generated.
  * `pycharm`: Optimized for PyCharm
* `-d`: Dump internal data structures to `<output-dir>` as the files name with suffix `-dump.json`
* `-f <format>`: Format the generated code using format
  * `pep8`: Format generated code using pep8 format
