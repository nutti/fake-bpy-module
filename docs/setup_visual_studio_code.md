# Setup IDE: Visual Studio Code

![Code Completion (Visual Studio Code)](images/code_completion_visual_studio_code.png)


#### 1. Download the premade module

Download the premade module from GitHub.

Use Git and clone fake-bpy-module repository.

```
$ git clone https://github.com/nutti/fake-bpy-module.git
```

or

Download .zip file from GitHub.

https://github.com/nutti/fake-bpy-module/archive/master.zip


#### 2. Check premade module location

Check the location of premade module and remember it because we use it process 3.  
The premade module is located in `premade_modules`.
You can see each version of the premade module on there.


#### 3. Download the visual studio code extension

Download [the visual studio code extension for Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and restart the visual studio code.


#### 4. Add Auto Complete path

Add the path for the auto completion from Visual Studio.

1. Click *File* > *Preferences* > *Settings*.
2. On `settings.json` page, add premade module path to `python.autoComplete.extraPaths`

* Example of settings.json

```json
{
    "python.autoComplete.extraPaths": [
        "<path-to-repository>/fake-bpy-module/premade_modules/2.79"
    ]
}
```
