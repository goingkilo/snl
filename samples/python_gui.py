import sys
sys.path.append('C:/Users/a20643/AppData/Local/Programs/Python/Python37-32/Lib/tkinter')
import tkinter
from tkinter import messagebox
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import LEFT
from tkinter import Entry
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import E


top=Tk()

class Player:
        def _init_(self,name,icon):
                self.name=name
                self.icon=icon

def PressCallBack(Name):
        #tkinter.messagebox.showinfo("Please Study", Name)
        #La1=Label(top, text="Name").grid(row=4,column=4)
        Fi=open("./copytext.txt","a")
        Fi.write(Name + "\n")
        Fi.close()

def main():        

    
    top.geometry("1000x800")

    top.grid_columnconfigure(0,weight=0,uniform="foo")        
    top.grid_columnconfigure(1,weight=0,uniform="foo")

    La=Label(top, text="Enter Name")
    La.grid(row=1,column=0)
    
    #La.pack(side=LEFT)

    En=Entry(top)
    En.grid(row=1,column=1)

    #Ca=Canvas(top)
    #Ca.grid(row=4,column=3,rowspan=5)
    #Ca.pack()
    #filename=PhotoImage(file="D:/1Data/Data/Personal/Game-Board-Snakes-and-Ladders.gif")
    #Ca.create_image(0,0,image=filename)

    SLfilename=PhotoImage(file="../images/Game-Board-Snakes-and-Ladders.gif")
    SL=Label(top,image=SLfilename)
    SL.grid(row=3,column=1,rowspan=10,columnspan=10)

    BMfilename=PhotoImage(file="../images/blue-monster-icon.gif")
    BM=Label(top,image=BMfilename)
    BM.place(x=700,y=40,in_=top)
    
    Bu=Button(top, text="Click Me", command=lambda: PressCallBack(En.get())).grid(row=3,column=2)
    #Bu.pack()
    #Bu.flash()

    top.mainloop()

main()
