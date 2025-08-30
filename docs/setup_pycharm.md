# Setup IDE: PyCharm

![Code Completion (PyCharm)](images/code_completion_pycharm.png)

*Note: For PyCharm users, change the value `idea.max.intellisense.filesize` in
`idea.properties` file to more than 6000 because some modules have the issue of
being too big for intelliSense to work.*

## 1. Check the generated modules location

Check the location of the generated modules.  

## 2. Include the modules as the external library

Launch PyCharm and do all below procedures.

<!-- markdownlint-disable MD007 MD029 MD032 MD033 -->

1. Show *Settings* (Windows) or *Preferences* (macOS) window.
   * (Windows) Click *File* > *Settings*
   * (macOS) Click *Pycharm Menu* > *Preferences*
2. Select *Project: <Your Project>* > *Project Interpreter*.
3. Click *Gear* icon on the right next to *Project Interpreter:*, and a popup
   menu is shown.
4. Click *More...* on the popped up menu.
5. In *Project Interpreters* window, click the bottom icon
   *Show paths for the selected Interpreter* to show *Interpreter Paths* window.
6. Click *+* icon, and a file browser is launched.
7. Select the path where generated modules are located, and click *OK*.
8. Click *OK* repeatedly until *Settings* (Windows) or *Preferences* (macOS)
   window is closed.
9. Now, you can complete the code related to the Blender/UPBGE Python API.

<!-- markdownlint-enable MD007 MD029 MD032 MD033 -->

## More information

* [Stack Overflow: PyCharm import external library](https://stackoverflow.com/questions/24197970/pycharm-import-external-library)
* [Blender – Interplanety: Using external IDE PyCharm for writing Blender scripts](https://b3d.interplanety.org/en/using-external-ide-pycharm-for-writing-blender-scripts/)
