# Setup IDE: PyCharm

![Code Completion (PyCharm)](images/code_completion_pycharm.png)


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


#### 3. Include the module as the external library

Launch PyCharm and do all below procedures.

1. Click *File* > *Settings* to show *Settings* window.
2. Select *Project: <Your Project>* > *Project Interpreter*.
3. Click *Setting* icon on the right next to *Project Interpreter:* and Click *More...*.
4. In *Project Interpreters* window, click the bottom icon to show *Interpreter Paths* window.
5. Click *Add* icon to show *Select Path* window.
6. Select the path premade module is located, and click *OK*.
7. Click *OK* repeatedly until *Settings* window is closed.
8. Now, you can complete the code related to the Blender Python API.
