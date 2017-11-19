# DynaEditor
Dynamic attribute editor for maya 2017 and up
### About
Artist often need to change attributes on multiple Maya objects at the same
and to avoid them having to do it one by one (which is tedious and time consuming)
i've created this tool. The editor is being filled dynamically when active in Maya
based on the current selection of the user. 
<br><br>
![example window](/rsc/example_window.png)
### Usage
* Install the repository
* start the tool by running the main module
### Feature overview
* apply attributes to all selected object
* apply attributes to selected object and all there children
* apply to only same type object or any type objects
* Support for the following maya attribute types:
  * bool
  * short
  * float
  * float2
  * float3
  * long
  * long2
  * long3
  * double
  * double2
  * double3
  * byte
* attribute hiding
* attribute searching
* stores attribute display preferences
### easy install
To easy install the tool without using pip, please do the following steps:
* download the repository
* copy the dynaeditor and bin directory over to your maya scripts directory
* start the tool with the following snippet
```python
from dynaeditor import main
app = main.main()
```
### Notes
* only usable in Autodesk Maya 2017 and up due to usage of PySide2
* reburies PyTest to run unit tests
* if you run into any bugs feel always feel free to create an issue or shoot me an email at: alexanderberx@gmail.com
