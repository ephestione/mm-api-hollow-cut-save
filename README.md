# mm-api-hollow-cut-save
juicy sauce:
https://forums.autodesk.com/t5/meshmixer/meshmixer-scripting-for-repetive-task/td-p/9274151


Please check whether mmApi does its job first:

On WIN:

1. Open MM and load the bunny.

2. Go to your mmApi download directory. Within mm-api-master go to distrib/python and open test.py with python IDLE

3. IDLE should show the Shell and the Code windows. Give the focus to the code and run the code via menu:Run/RunModule.

>>> In MM the bunny should be cut in half

On MAC:

same procedure but in step two go to distrib/python_osx

 

Now if the bunny is cut via test.py:

Go to mm-api-master/python and copy the folder named "mm".

Paste it into mm-api-master/distrib/python (on WIN) or mm-api-master/distrib/python_osx (on MAC)

 

Now the .py codes using mmApi stored in mm-api-master/distrib/python (or mm-api-master/distrib/python_osx) should work.

 

To run the codes posted above create a new file in python IDLE and paste the code. Now running that Code via menu Run/RunModule you will be asked to save the file first. Save it to (name isn't important) mm-api-master/distrib/python (on WIN) or mm-api-master/distrib/python_osx (on MAC). Now the little Tkinter window should pop up. Use its Run button to load the objects and process them. The results will be stored in the same directory you loaded the files from.
