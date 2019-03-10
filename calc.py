import re
from pathlib import Path
import os,  tkinter.filedialog, tkinter.messagebox

root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
thisfile = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
path1 = Path(thisfile).parent

os.chdir(path1)
files = os.listdir()

for file in files:
    result = re.search('\d{8}',file)
    if result:
        start = result.start()
        os.renames(file, file[start:start+8] + "\\" + file)
