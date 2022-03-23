import tkinter as tk
from tkinter import Button, Frame, Grid, Label, Scrollbar, Toplevel, filedialog, Text
import os
from tkinter.constants import BOTH, RIGHT, TOP, X,END 
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkinter import messagebox as msb
from numpy.lib.function_base import insert
from predition import *

root = tk.Tk()
root.title("QuickNotepad")

ico = Image.open('notes.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

canvas = tk.Canvas(root, height = 600, width= 1100, bg= "#faf2ff" )
canvas.pack(fill=BOTH, expand=True)


text = Label(canvas, text="Welcome to our page!", bg= "#faf2ff",font = ("Times New Roman", 20))
text2 = Label(canvas, text= "QuickNotepad was made for people who want to create correct notes in English."
                            " To predict the next possible words, click on the 'Next words' button. "
                            , bg= "#faf2ff",font = ("Times New Roman", 15))

text3 = Label(canvas, text="Space for your notes:", bg= "#faf2ff",foreground="#5a0896", font = ("Times New Roman", 15) )
text4 = tk.Text(root, height = 13, width= 150,  bg= "#faf2ff" , font = ("Times New Roman", 12))
text5 = Label (canvas, text="Next possible words: ", bg= "#faf2ff",  font = ("Times New Roman", 15))

sb_text = tk.Scrollbar(root)
sb_text.place(in_ =text4, relx = 1, rely = 0, relheight = 1)
sb_text.config(command = text4.yview)
text4.config(yscrollcommand = sb_text.set)

text_box = tk.Text(root, height = 1, width= 70,  bg= "#faf2ff", font = ("Times New Roman", 12))


text.place(x=20,y=40)
text2.place(x=20,y=90)
text3.place(x=20, y= 150)
text4.place(x=20, y= 200)
text5.place(x = 20, y= 470)
text_box.place(x=20, y= 500)

def input_text():
    q = text4.get(1.0, tk.END+"-1c")
    seq = " ".join(tokenizer.tokenize(q.lower())[0:5])
    x = predict_completions(seq, 5)
    text_box.insert(1.0, f'{x}')
    text_box.after(8000, delete_w)
    
def delete_w():
    text_box.delete('1.0', END)

def save_file():
        filename = fd.asksaveasfilename(filetypes=[("Plik tekstowy","*.txt")], defaultextension = "*.txt")
        
        if filename:
            with open(filename, "w", -1, "utf-8") as file:
                file.write(text4.get(1.0, tk.END))


button1 = tk.Button( text = "Save", command = save_file, height= 2, width= 15 )
button1.place(x= 20, y = 600)       

button2 = tk.Button( text = "Next words",command = input_text, height= 1, width= 15 )
button2.place(x= 600, y = 498) 

root.mainloop()


