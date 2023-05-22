from tkinter import filedialog
from tkinter import *


root = Tk()
root.withdraw()
selected_folder = filedialog.askdirectory(title="Select destination folder")
file_name = "file.png"
print(selected_folder+"/"+file_name)
