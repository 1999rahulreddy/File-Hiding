import os
from tkinter import *
import subprocess as sub
import time
import pickle
from tkinter import filedialog
root = Tk()
root.title("FACE AND GESTURE RECOGNITION")
t=str()
#files={}
#v=''

        
    
def h(f,p,main):
    time.sleep(3)
    pass_manager(f,p)
    main.destroy()

def s(f,p,main):
    time.sleep(3)
    pass_checker(f,p)
    main.destroy()    

def lis(password,main):
    if(password=="123"):
        root1 = Tk()
        root1.geometry('300x300')
        l=Label(root1,text=str(ref()))
        l.pack(pady=10,padx=10)
        b1=Button(root1, text='Refresh', width=25, command=lambda:l.config(text=str(ref())))
        b1.pack(pady=10,padx=10)
        main.destroy()
    else:
        main.destroy()
        print("wrong password")   

def hide():
    root1 = Tk()
    root1.geometry('300x300')
    root1.title("Hide")
    Label(root1,text="enter the path of the file").pack(pady=10,padx=10)
    tb = Entry(root1)
    tb.pack(pady=10,padx=10)
    Label(root1,text="set a password for the file").pack(pady=10,padx=10)
    tb1 = Entry(root1)
    tb1.pack(pady=10,padx=10)
    b1=Button(root1, text='Click to Hide the File', width=25, command=lambda: h(tb.get(),tb1.get(),root1) )
    b1.pack(pady=10,padx=10)
    root.destroy()
    
    
def show():
    root1 = Tk()
    root1.geometry('300x300')
    root1.title("Show")
    Label(root1,text="enter the path of the file").pack(pady=10,padx=10)
    tb = Entry(root1)
    tb.pack(pady=10,padx=10)
    Label(root1,text="enter the password for the file").pack(pady=10,padx=10)
    tb1 = Entry(root1)
    tb1.pack(pady=10,padx=10)
    b1=Button(root1, text='Click to Show the File', width=25, command=lambda: s(tb.get(),tb1.get(),root1) )
    b1.pack(pady=10,padx=10)
    root.destroy()

def filelist():
    root1 = Tk()
    root1.geometry('300x300')
    root1.title("Files List")
    Label(root1,text="enter the password").pack(pady=10,padx=10)
    tb1 = Entry(root1)
    tb1.pack(pady=10,padx=10)
    b1=Button(root1, text='Click to Show the List', width=25, command=lambda: lis(tb1.get(),root1) )
    b1.pack(pady=10,padx=10)
    root.destroy()    
   


def show_picture():
	root1 = Tk()
    root1.geometry('400x400')
    root1.title("Picture")
    Label(root1,text="enter the path of the file").pack(pady=10,padx=10)
    tb = Entry(root1)
    tb.pack(pady=10,padx=10)
    Label(root1,text="enter the password for the file").pack(pady=10,padx=10)
    tb1 = Entry(root1)
    tb1.pack(pady=10,padx=10)
    b1=Button(root1, text='Click to Show the File', width=25, command=lambda: s(tb.get(),tb1.get(),root1) )
    b1.pack(pady=10,padx=10)
    root.destroy()

b1 = Button(root, text='Hide', width=25, command=hide) 
b1.pack(pady=10,padx=10) 
b2 = Button(root, text='Show', width=25, command=show) 
b2.pack(pady=10,padx=10)
b3 = Button(root, text='List Of Files Hidden', width=25, command=filelist)
b3.pack(pady=10,padx=10)

root.mainloop()


	
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
 
 
 
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        super()7675
        self.title("Python Tkinter Dialog Widget")
        self.minsize(640, 400)
        #self.wm_iconbitmap('icon.ico')
 
        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
 
        self.button()
 
 
 
    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)
 
 
    def fileDialog(self):
 
        self.filename = filedialog.askopenfilename(initialdir =  "/home/rahul/", title = "Select A File", filetypes=(("JPG ","*.jpg"),))
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)
 
 
 
 
 
root = Root()
root.mainloop()