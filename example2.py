#This one allows multiple input. It loads, processes, saves and deletes the objects in the scene one by one:

from Tkinter import *
from tkFileDialog   import askopenfilenames
import Tkinter as tk

import mmapi
from mmRemote import *
import mm

remote = mmRemote()
remote.connect()

thickness_hollow = 2.5

path_to_file = ""

def Load_File():
    input_files = askopenfilenames(parent = root)
    if input_files is "":
        return
    else:
        file_List = root.tk.splitlist(input_files)        
        for i in file_List:
            mm.append_objects_from_file(remote,i)
            path_to_file = i
            Hollow()
            Cut()
            Save_File(path_to_file)


def Hollow():
    mm.begin_tool(remote, "hollow")
    mm.set_toolparam(remote, "offsetDistanceWorld", thickness_hollow)
    mm.tool_utility_command(remote, "update")    
    mm.accept_tool(remote)
 

def Cut():
    (fMin,fMax) = mm.get_selected_bounding_box(remote)
    cut_height = fMin[1] +  (fMax[1]-fMin[1])/3
    mm.begin_tool(remote, "planeCut")    
    mm.set_toolparam(remote, "origin", (0.0, cut_height, 0.0))
    mm.accept_tool(remote)


def Save_File(path_to_file):
    path_out = path_to_file.split('.')
    save_path = path_out[0] + '_hollowed.' + path_out[1]
    mm.export_mesh(remote,save_path)
    cmd = mmapi.StoredCommands()
    cmd.AppendSceneCommand_DeleteSelectedObjects();
    remote.runCommand(cmd)
   
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
