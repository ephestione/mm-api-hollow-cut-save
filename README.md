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






mm.export_mesh(remote,save_path)

export only works on mesh files (I checked .obj and .stl). MIX instead can't work. It saves the scene instead of an object (including stuff like Complex objects, Pivots, Target ....)

If you really want to save to that special format we would need to use

mm.save_mix(remote, save_path)

For export one could solve that:

def Save_File(path_to_file):
    path_out = path_to_file.split('.')
    save_path = path_out[0] + '_hollowed.' + path_out[1]
    if path_out[1] == 'mix':
        mm.save_mix(remote, save_path)
    else:
        mm.export_mesh(remote,save_path)

But a mix may come with several objects. So for the processing part we would need to detect new objects and iterate through this list to do hollowing/cutting for each. Doable but maybe not the straight way. 
