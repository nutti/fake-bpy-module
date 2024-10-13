<!-- markdownlint-disable MD024 -->

# Generate Modules

This document shows the procedure for generating modules by yourself.  
You can choose the method to generate modules.

1. [Case 1: Use utility script](#case-1-use-utility-script)
2. [Case 2: Do it yourself all procedures](#case-2-do-it-yourself-all-procedures)
3. [Case 3: Do Case 2 inside Docker](#case-3-do-case-2-inside-docker)

## Pre-requirement

### Python Version

The generating script can be run on Python >= 3.12.
Check your Python version is >= 3.12.

### Install requirement packages

The generating script uses the packages listed on
[requirements.txt](../src/requirements.txt).  
Execute below command to install requirement packages.

For fake-bpy-module:

```bash
git clone https://github.com/nutti/fake-bpy-module.git
cd fake-bpy-module
pip install -r src/requirements.txt
```

For fake-bge-module:

```bash
git clone https://github.com/nutti/fake-bge-module.git
cd fake-bge-module
pip install -r src/requirements.txt
```

### Setup IDE

After generating modules, you need to setup IDE to enable a code completion.

* [PyCharm](docs/setup_pycharm.md)
* [Visual Studio Code](docs/setup_visual_studio_code.md)
* [All Text Editor (Install as Python module)](docs/setup_all_text_editor.md)

## Case 1: Use utility script

### 1. Download Blender/UPBGE binary

From below sites, download Blender or UPBGE binary whose version is the
version you try to generate modules.

* Blender: [https://download.blender.org/release/](https://download.blender.org/release/)
* UPBGE: [https://upbge.org/](https://upbge.org/)

### 2. Download Blender/UPBGE sources

For fake-bpy-module:

```bash
git clone https://projects.blender.org/blender/blender.git
```

For fake-bge-module:

```bash
git clone https://github.com/UPBGE/upbge.git
```

### 3. Download fake-bpy-module/fake-bge-module sources

Download the fake-bpy-module/fake-bge-module sources from GitHub.  
Use Git to clone repository.

For fake-bpy-module:

```bash
export TARGET=bpy
```

For fake-bge-module:

```bash
export TARGET=bge
```

```bash
git clone https://github.com/nutti/fake-${TARGET}-module.git
```

Or, you can download .zip file from GitHub.

* fake-bpy-module: [https://github.com/nutti/fake-bpy-module/archive/main.zip](https://github.com/nutti/fake-bpy-module/archive/main.zip)
* fake-bge-module: [https://github.com/nutti/fake-bge-module/archive/main.zip](https://github.com/nutti/fake-bge-module/archive/main.zip)

### 4. Run script

<!-- markdownlint-disable MD013 -->
```bash
cd fake-${TARGET}-module/src
bash gen_module.sh <source-dir> <blender-dir> <target> <branch/tag/commit> <target-version> <output-dir> [<mod-version>]
```
<!-- markdownlint-enable MD013 -->

* `<source-dir>`: Specify Blender/UPBGE sources directory.
* `<blender-dir>`: Specify Blender/UPBGE binary directory.
* `<target>`: `blender` or `upbge`.
* `<branch/tag/commit>`: Specify target Blender/UPBGE source's branch for the
  generating modules.
  * If you want to generate modules for 2.79, specify `v2.79`
  * If you want to generate modules for newest Blender/UPBGE version, specify `main`
* `<target-version>`: Specify target version.
* `<output-dir>`: Specify directory where generated modules are output.
* `<mod-version>`: Modify APIs by using patch files located in `mods` directory.
  * If you specify `2.80`, all patch files under `mods/2.80` will be used.
  * Files located in `mods/common` directories will be used at any time.

#### Specify Python interpreter

By default, this command uses Python interpreter by calling `python` command.  
If you want to use other Python interpreter, you can specify by `PYTHON_BIN`
environment variable.

<!-- markdownlint-disable MD013 -->
```bash
PYTHON_BIN=/path/to/python3.12 bash gen_module.sh <source-dir> <blender-dir> <target> <branch/tag/commit> <target-version> <output-dir> [<mod-version>]
```
<!-- markdownlint-enable MD013 -->

## Case 2: Do it yourself all procedures

### 1. Download Blender/UPBGE binary

From below sites, download Blender or UPBGE binary whose version is the
version you try to generate modules.

* Blender: [https://download.blender.org/release/](https://download.blender.org/release/)
* UPBGE: [https://upbge.org/](https://upbge.org/)

Place Blender/UPBGE binary to some directory.  
In this tutorial, Blender/UPBGE binary assumes to be placed on
`/workspace/blender-bin`. (i.e. Blender executable is located on
`/workspace/blender-bin/blender`)

```bash
export WORKSPACE=/workspace
export BLENDER_BIN=${WORKSPACE}/blender-bin
export BLENDER_SRC=${WORKSPACE}/blender
```

For fake-bpy-module:

```bash
export TARGET=bpy
```

For fake-bge-module:

```bash
export TARGET=bge
```

### 2. Download Blender/UPBGE sources

For fake-bpy-module:

```bash
git clone https://projects.blender.org/blender/blender.git
```

For fake-bge-module:

```bash
git clone https://github.com/UPBGE/upbge.git
```

### 3. Change to the target branch/tag/commit

Be sure to match the version between sources and binary.
If you try to generate modules for v2.79, you should use `git checkout v2.79`.

```bash
cd ${BLENDER_SRC}
git checkout [branch/tag/commit]
```

### 4. Generate .rst documents

Generated .rst documents are located on `${BLENDER_SRC}/doc/python_api/sphinx-in`.

<!-- markdownlint-disable MD013 -->
```bash
${BLENDER_BIN}/blender --background --factory-startup -noaudio --python-exit-code 1 --python doc/python_api/sphinx_doc_gen.py
```
<!-- markdownlint-enable MD013 -->

### 5. Download fake-bpy-module sources

Download the fake-bpy-module sources from GitHub.  
Use Git to clone repository.

```bash
cd ${WORKSPACE}
git clone https://github.com/nutti/fake-${TARGET}-module.git
```

Or, you can download .zip file from GitHub.

* fake-bpy-module: [https://github.com/nutti/fake-bpy-module/archive/main.zip](https://github.com/nutti/fake-bpy-module/archive/main.zip)
* fake-bge-module: [https://github.com/nutti/fake-bge-module/archive/main.zip](https://github.com/nutti/fake-bge-module/archive/main.zip)

### 6. Generate mod files

<!-- markdownlint-disable MD013 -->
```bash
cd fake-${TARGET}-module/src

mkdir -p mods/generated_mods
${BLENDER_BIN}/blender --background --factory-startup -noaudio --python-exit-code 1 --python gen_modfile/gen_external_modules_modfile.py -- -m addon_utils -o mods/generated_mods/gen_modules_modfile -f json
${BLENDER_BIN}/blender --background --factory-startup -noaudio --python-exit-code 1 --python gen_modfile/gen_external_modules_modfile.py -- -m keyingsets_builtins -a -o mods/generated_mods/gen_startup_modfile -f json

mkdir -p mods/generated_mods/gen_bgl_modfile
python gen_modfile/gen_bgl_modfile.py -i ${BLENDER_SRC}/source/blender/python/generic/bgl.cc -o mods/generated_mods/gen_bgl_modfile/bgl.json -f json
```
<!-- markdownlint-enable MD013 -->

### 7. Generate modules

<!-- markdownlint-disable MD013 -->
```bash
python gen.py -i <input-dir> -o <output-dir> -f <format> -T <target> -t <target-version> -m <mod-version> -l <log-level>
```
<!-- markdownlint-enable MD013 -->

* `-i <input-dir>`: Specify input directory (The directory where .rst files are
  located in process 4). In this document, `<input-dir>` should be
  `${BLENDER_SRC}/doc/python_api/sphinx-in`.
* `-o <output-dir>`: Specify output directory. (The directory where generated
  files will be located)
* `-f <format>`: Format the generated code by `<format>` convention.
  * `none`: Don't format generated code.
  * `yapf`: Format generated code with yapf.
  * `ruff`: Format generated code with ruff.
* `-T <target>`: Target (`blender` or `upbge`).
* `-t <target-version>`: Specify target version.
* `-m <mod-version>`: Modify APIs by using patch files located in `mods` directory.
  * If you specify `2.80`, all patch files under `mods/2.80` will be used.
  * Files located in `mods/common` directories will be used at any time.
* `-l <log-level>`: Specify log level (`debug`, `info`, `notice`, `warn`, `err`).

## Case 3: Do Case 2 inside Docker

### Run script

<!-- markdownlint-disable MD013 -->
```bash
bash tools/gen_module/run_gen_module_in_docker.sh <blender-version>
```
<!-- markdownlint-enable MD013 -->

* `<blender-version>`: Specify Blender/UPBGE version.

`<mod-version>` is automatically determined by `<blender-version>` version.

### Results

| Directory | Contents |
|----|----|
| `build/blender-bin` | Blender/UPBGE binaries |
| `build/blender-src` | Blender/UPBGE source code |
| `build/examples` | Blender/UPBGE Python API sample code |
| `build/results` | Result `*.pyi` files |
| `build/sphinx-in` | Blender/UPBGE Python API documents |
| `build/sphinx-in-tmp` | ??? |
| `downloads` | Blender/UPBGE archives |
