# Generate Modules

This document shows the procedure for generating modules by yourself.  
You can choose the method to generate modules.

1. [Case 1: Use utility script](#case-1-use-utility-script)
2. [Case 2: Do it yourself all procedures](#case-2-do-it-yourself-all-procedures)


### Pre-requirement

#### Python Version

The generating script can be run on Python >= 3.7.
Check your Python version is >= 3.7.


#### Install requirement packages

The generating script uses the packages listed on [requirements.txt](../requirements.txt).  
Execute below command to install requirement packages.

```bash
git clone https://github.com/nutti/fake-bpy-module.git
cd fake-bpy-module
pip install -r requirements.txt
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

```bash
git clone git://git.blender.org/blender.git
```


#### 3. Download fake-bpy-module sources

Download the fake-bpy-module sources from GitHub.

Use Git and clone fake-bpy-module repository.

```bash
git clone https://github.com/nutti/fake-bpy-module.git
```

Or, you can download .zip file from GitHub.

https://github.com/nutti/fake-bpy-module/archive/master.zip


#### 4. Run script

```bash
cd fake-bpy-module/src
bash gen_module.sh <source-dir> <blender-dir> <branch/tag/commit> <output-dir> <mod-version>
```

* `<source-dir>`: Specify Blender sources directory.
* `<blender-dir>`: Specify Blender binary directory.
* `<branch/tag/commit>`: Specify target Blender source's branch for the generating modules.
  * If you want to generate modules for 2.79, specify `v2.79`
  * If you want to generate modules for newest Blender version, specify `master`
* `<output-dir>`: Specify directory where generated modules are output.
* `<mod_version>`: Modify APIs by using patch files located in `mods` directory.
  * If you specify `2.80`, all patch files under `mods/2.80` will be used.
  * Files located in `mods/common` directories will be used at any time.


## Case 2: Do it yourself all procedures

#### 1. Download Blender binary

Download Blender binary from [Blender official download site](https://download.blender.org/release/).  
Download Blender whose version is the version you try to generate modules.  
Place Blender binary to some directory.  
In this tutorial, Blender binary assumes to be placed on `/workspace/blender-bin`. (i.e. Blender executable is located on `/workspace/blender-bin/blender`)

```bash
export WORKSPACE=/workspace
export BLENDER_BIN=${WORKSPACE}/blender-bin
export BLENDER_SRC=${WORKSPACE}/blender
```


#### 2. Download Blender sources

```bash
cd ${WORKSPACE}
git clone git://git.blender.org/blender.git
```


#### 3. Change to the target branch/tag/commit

Be sure to match the version between sources and binary.
If you try to generate modules for v2.79, you should use `git checkout v2.79`.

```bash
cd ${BLENDER_SRC}
git checkout [branch/tag/commit]
```


#### 4. Generate .rst documents

Generated .rst documents are located on `${BLENDER_SRC}/doc/python_api/sphinx-in`.

```bash
${BLENDER_BIN}/blender --background --factory-startup -noaudio --python doc/python_api/sphinx_doc_gen.py
```


#### 5. Download fake-bpy-module sources

Download the fake-bpy-module sources from GitHub.

Use Git and clone fake-bpy-module repository.

```bash
cd ${WORKSPACE}
git clone https://github.com/nutti/fake-bpy-module.git
```

Or, you can download .zip file from GitHub.

https://github.com/nutti/fake-bpy-module/archive/master.zip


#### 6. Generate mod files

```bash
cd fake-bpy-module/src

mkdir -p mods/generated_mods
${BLENDER_BIN}/blender --background --factory-startup -noaudio --python gen_modfile/gen_modules_modfile.py -- -m addon_utils -o mods/generated_mods/gen_modules_modfile

mkdir -p mods/generated_mods/gen_startup_modfile
python gen_modfile/gen_startup_modfile.py -i ${BLENDER_BIN}/<blender-version>/scripts/startup -o mods/generated_mods/gen_startup_modfile/bpy.json

mkdir -p mods/generated_mods/gen_bgl_modfile
python gen_modfile/gen_bgl_modfile.py -i ${BLENDER_SRC}/source/blender/python/generic/bgl.c -o mods/generated_mods/gen_bgl_modfile/bgl.json
```

* `<blender-version>`: Specify Blender version.


#### 7. Generate modules

```bash
python gen.py -i <input-dir> -o <output-dir> -f <format> -m <mod-version>
```

* `-i <input-dir>`: Specify input directory (The directory where .rst files are located in process 4). In this document, `<input-dir>` should be `${BLENDER_SRC}/doc/python_api/sphinx-in`.
* `-o <output-dir>`: Specify output directory. (The directory where generated files will be located)
* `-d`: Dump internal data structures to `<output-dir>` as the files name with suffix `-dump.json`
* `-f <format>`: Format the generated code by `<format>` convention.
  * `pep8`: Format generated code by pep8.
* `-m <mod_version>`: Modify APIs by using patch files located in `mods` directory.
  * If you specify `2.80`, all patch files under `mods/2.80` will be used.
  * Files located in `mods/common` directories will be used at any time.
