# fake-bpy-module

Fake bpy module for code completion in eclipse/PyCharm/VSCode etc...

## Usage

1. Get Blender's sources

```
$ git clone git://git.blender.org/blender.git
```

2. Change to the branch/tag which you want to generate fake bpy modules

```
$ cd blender
$ git checkout [branch/tag]
```

3. Generate .rst documents

```
$ blender --background --factory-startup -noaudio --python doc/python_api/sphinx_doc_gen.py
```

4. Convert .rst to .xml

```
$ sphinx-build -b xml doc/python_api/sphinx-in xml-out
```

5. Generate fake bpy modules

```
$ python gen.py -i xml-out -o [output_dir]
```
