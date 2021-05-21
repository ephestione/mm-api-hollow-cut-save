#As an alternative you may try to use askdirectory instead. This version asks for a directory, loads all .obj and .stl files within that directory and saves to a subfolder "Hollowed":

import os

from Tkinter import *
from tkFileDialog   import askdirectory
import Tkinter as tk

import mmapi
from mmRemote import *
import mm

remote = mmRemote()
remote.connect()

thickness_hollow = 2.5

def Load_File():
    input_dir = askdirectory(parent = root)
    if input_dir is "":
        return
    supported_extensions = ['obj','stl']
    file_List = [fn for fn in os.listdir(input_dir)if any(fn.endswith(ext) for ext in supported_extensions)]
    for i in file_List:
        mm.append_objects_from_file(remote,input_dir+'/'+i)
        Hollow()
        Cut()
        Save_File(i, input_dir)
        
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


def Save_File(i, input_dir):
    out_dir = input_dir + '/Hollowed/'
    try:
        os.mkdir(input_dir + '/Hollowed')
    except:
        None
    ext = i.split('.')
    save_path = out_dir + ext[0] +'_hollowed.' + ext[1]
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

