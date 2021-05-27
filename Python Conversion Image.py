import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
canvas1 = tk.Canvas(root,width=300,height=300,bg='azur3',relief='raised')
canvas1.pack()

label1=tk.label(root,text='File Conversion Tool',bg='azur3')
label.config(font=('helvetica',20))
canvas1.create_window(150,60,window=label1)

def getPNG():
    global im1
    import_fith_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
