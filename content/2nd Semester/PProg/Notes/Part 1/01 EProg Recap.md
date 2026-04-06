When an object is passed as a parameter, the object is not copied.
The parameter refers to the same object. If the parameter is modified, it will affect the original object. 

Static variables are shared by all the instances of the class.

Static constants are final variables shared by all the instances of the class.

Class methods are marked by the static keyword Class methods are not called via an object reference but directly via the class Can be called from a static context (e.g., main method). Class methods often serve as utility function They’re generic and need no access to object variables and methods