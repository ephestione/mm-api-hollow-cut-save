#Here's a code building a tiny window in your screen's upper right. Hitting its Run button you can select an input file.

#It automatically appends this object to an existing scene (You might simply open the default plane object), performs its hollowing at 2.5 , cutting at a third of its height and saves the file in the same format adding "_mod" to its name to the same directory as it was loaded from (to avoid an additional SaveTo dialog):

from Tkinter import *
from tkFileDialog   import askopenfilename, asksaveasfilename
import Tkinter as tk

import mmapi
from mmRemote import *
import mm

remote = mmRemote()
remote.connect()

thickness_hollow = 2.5

path_to_file = ""

def Load_File():
    path_to_file = askopenfilename(parent = root)
    if path_to_file is "":
        return
    else:
        mm.append_objects_from_file(remote,path_to_file)
        Hollow(path_to_file)

def Hollow(path_to_file):
    mm.begin_tool(remote, "hollow")
    mm.set_toolparam(remote, "offsetDistanceWorld", thickness_hollow)
    mm.tool_utility_command(remote, "update")    
    mm.accept_tool(remote)
    Cut(path_to_file)

def Cut(path_to_file):
    (fMin,fMax) = mm.get_selected_bounding_box(remote)
    cut_height = fMin[1] +  (fMax[1]-fMin[1])/3
    mm.begin_tool(remote, "planeCut")    
    mm.set_toolparam(remote, "origin", (0.0, cut_height, 0.0))
    mm.accept_tool(remote)
    Save_File(path_to_file)

def Save_File(path_to_file):
    path_out = path_to_file.split('.')
    save_path = path_out[0] + '_mod.' + path_out[1]
    mm.export_mesh(remote,save_path)
    
# Setup a tiny GUI window:    
root = Tk()
root.title("Hollow and Cut")
w = 240 
h = 30 
ws = root.winfo_screenwidth() 
x = ws - w
y = 0
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.attributes("-topmost", True)

buttonLoad = Button(root, text="Run", command = Load_File)
buttonLoad.pack()

def on_closing():
    remote.shutdown()
    root.destroy()    
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
