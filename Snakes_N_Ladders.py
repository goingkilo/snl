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
from tkinter import Toplevel
from tkinter import IntVar
from tkinter import Radiobutton

top=Tk()

class Player:

        playerPos=0
        
        def _init_(self,name,icon):
                self.name=name
                self.icon=icon

def PressCallBack(NumPlayers):
        #Fi=open("D:/1Data/Data/Personal/Python/copytext.txt","a")
        #Fi.write(Name + "\n")
        #Fi.close()
        IntNumPlayers=int(NumPlayers)
        top.withdraw()
        SubFrame=Toplevel()
        OpenSubFrame(IntNumPlayers,SubFrame)

def CloseSubFrame(SubFrame):
        SubFrame.destroy()
        top.deiconify()

def ValidateandStorePlayerInformation(NumPlayers,Player1Choice,Player2Choice,Player3Choice,Player4Choice):
        PlayerIcons=[0,0,0,0]

        if NumPlayers == 2 or NumPlayers == 3 or NumPlayers == 4:
                PlayerIcons[Player1Choice-1]+=1
                PlayerIcons[Player2Choice-1]+=1

        if NumPlayers == 3 or NumPlayers == 4:
                PlayerIcons[Player3Choice-1]+=1

        if NumPlayers == 4:
                PlayerIcons[Player4Choice-1]+=1

        messagebox.showinfo("Info",str(PlayerIcons[0]))
        messagebox.showinfo("Info",str(PlayerIcons[1]))
        messagebox.showinfo("Info",str(PlayerIcons[2]))
        messagebox.showinfo("Info",str(PlayerIcons[3]))

        if PlayerIcons[0] > 1 or PlayerIcons[1] > 1 or PlayerIcons[2] > 1 or PlayerIcons[3] > 1:
                messagebox.showinfo("Warning","Invalid Choice")
        

def OpenSubFrame(NumPlayers,SubFrame):

        SubFrame.geometry("800x800")
        SubFrame.grid_columnconfigure(0,weight=0,uniform="foo")        
        SubFrame.grid_columnconfigure(1,weight=0,uniform="foo")
        SubFrame.grid_columnconfigure(2,weight=0,uniform="foo")
        SubFrame.grid_columnconfigure(3,weight=0,uniform="foo")

        CloseButton=Button(SubFrame, text="Close", command=lambda: CloseSubFrame(SubFrame))
        CloseButton.grid(row=12,column=2)

        BlueMonsterIconFileName=PhotoImage(file="D:/1Data/Data/Personal/blue-monster-icon.gif")
        RedMonsterIconFileName=PhotoImage(file="D:/1Data/Data/Personal/red-monster-icon.gif")
        GreenMonsterIconFileName=PhotoImage(file="D:/1Data/Data/Personal/green-monster-icon.gif")
        YellowMonsterIconFileName=PhotoImage(file="D:/1Data/Data/Personal/yellow-monster-icon.gif")

        varGRP1=IntVar()
                
        Player1Label=Label(SubFrame, text="Name Of Player 1")
        Player1Label.grid(row=0,column=0)

        Player1Entry=Entry(SubFrame)
        Player1Entry.grid(row=0,column=1)

        Player1RadioButtonGroupBlue=Radiobutton(SubFrame,image=BlueMonsterIconFileName,variable=varGRP1,value=1)
        Player1RadioButtonGroupBlue.image=BlueMonsterIconFileName
        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
        Player1RadioButtonGroupBlue.grid(row=1,column=0)

        Player1RadioButtonGroupRed=Radiobutton(SubFrame,image=RedMonsterIconFileName,variable=varGRP1,value=2)
        Player1RadioButtonGroupRed.image=RedMonsterIconFileName
        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
        Player1RadioButtonGroupRed.grid(row=1,column=1)

        Player1RadioButtonGroupGreen=Radiobutton(SubFrame,image=GreenMonsterIconFileName,variable=varGRP1,value=3)
        Player1RadioButtonGroupGreen.image=GreenMonsterIconFileName
        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
        Player1RadioButtonGroupGreen.grid(row=1,column=2)

        Player1RadioButtonGroupYellow=Radiobutton(SubFrame,image=YellowMonsterIconFileName,variable=varGRP1,value=4)
        Player1RadioButtonGroupYellow.image=YellowMonsterIconFileName
        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
        Player1RadioButtonGroupYellow.grid(row=1,column=3)

        varGRP1.set(1)
                

        if NumPlayers==2 or NumPlayers==3 or NumPlayers==4 :

                varGRP2=IntVar()

                Player2Label=Label(SubFrame, text="Name Of Player 2")
                Player2Label.grid(row=3,column=0)

                Player2Entry=Entry(SubFrame)
                Player2Entry.grid(row=3,column=1)

                Player2RadioButtonGroupBlue=Radiobutton(SubFrame,image=BlueMonsterIconFileName,variable=varGRP2,value=1)
                Player2RadioButtonGroupBlue.image=BlueMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player2RadioButtonGroupBlue.grid(row=4,column=0)

                Player2RadioButtonGroupRed=Radiobutton(SubFrame,image=RedMonsterIconFileName,variable=varGRP2,value=2)
                Player2RadioButtonGroupRed.image=RedMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player2RadioButtonGroupRed.grid(row=4,column=1)

                Player2RadioButtonGroupGreen=Radiobutton(SubFrame,image=GreenMonsterIconFileName,variable=varGRP2,value=3)
                Player2RadioButtonGroupGreen.image=GreenMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player2RadioButtonGroupGreen.grid(row=4,column=2)

                Player2RadioButtonGroupYellow=Radiobutton(SubFrame,image=YellowMonsterIconFileName,variable=varGRP2,value=4)
                Player2RadioButtonGroupYellow.image=YellowMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player2RadioButtonGroupYellow.grid(row=4,column=3)

                varGRP2.set(2)

                ContinueButton=Button(SubFrame, text="Continue", command=lambda: ValidateandStorePlayerInformation(2,varGRP1.get(),varGRP2.get(),0,0))
                ContinueButton.grid(row=13,column=2)

        if NumPlayers==3 or NumPlayers==4 :

                varGRP3=IntVar()

                Player3Label=Label(SubFrame, text="Name Of Player 3")
                Player3Label.grid(row=6,column=0)

                Player3Entry=Entry(SubFrame)
                Player3Entry.grid(row=6,column=1)

                Player3RadioButtonGroupBlue=Radiobutton(SubFrame,image=BlueMonsterIconFileName,variable=varGRP3,value=1)
                Player3RadioButtonGroupBlue.image=BlueMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player3RadioButtonGroupBlue.grid(row=7,column=0)

                Player3RadioButtonGroupRed=Radiobutton(SubFrame,image=RedMonsterIconFileName,variable=varGRP3,value=2)
                Player3RadioButtonGroupRed.image=RedMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player3RadioButtonGroupRed.grid(row=7,column=1)

                Player3RadioButtonGroupGreen=Radiobutton(SubFrame,image=GreenMonsterIconFileName,variable=varGRP3,value=3)
                Player3RadioButtonGroupGreen.image=GreenMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player3RadioButtonGroupGreen.grid(row=7,column=2)

                Player3RadioButtonGroupYellow=Radiobutton(SubFrame,image=YellowMonsterIconFileName,variable=varGRP3,value=4)
                Player3RadioButtonGroupYellow.image=YellowMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player3RadioButtonGroupYellow.grid(row=7,column=3)

                ContinueButton=Button(SubFrame, text="Continue", command=lambda: ValidateandStorePlayerInformation(3,varGRP1.get(),varGRP2.get(),varGRP3.get(),0))
                ContinueButton.grid(row=13,column=2)

        if NumPlayers==4 :

                varGRP4=IntVar()

                Player4Label=Label(SubFrame, text="Name Of Player 4")
                Player4Label.grid(row=9,column=0)

                Player4Entry=Entry(SubFrame)
                Player4Entry.grid(row=9,column=1)

                Player4RadioButtonGroupBlue=Radiobutton(SubFrame,image=BlueMonsterIconFileName,variable=varGRP4,value=1)
                Player4RadioButtonGroupBlue.image=BlueMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player4RadioButtonGroupBlue.grid(row=10,column=0)

                Player4RadioButtonGroupRed=Radiobutton(SubFrame,image=RedMonsterIconFileName,variable=varGRP4,value=2)
                Player4RadioButtonGroupRed.image=RedMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player4RadioButtonGroupRed.grid(row=10,column=1)

                Player4RadioButtonGroupGreen=Radiobutton(SubFrame,image=GreenMonsterIconFileName,variable=varGRP4,value=3)
                Player4RadioButtonGroupGreen.image=GreenMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player4RadioButtonGroupGreen.grid(row=10,column=2)

                Player4RadioButtonGroupYellow=Radiobutton(SubFrame,image=YellowMonsterIconFileName,variable=varGRP4,value=4)
                Player4RadioButtonGroupYellow.image=YellowMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player4RadioButtonGroupYellow.grid(row=10,column=3)

                ContinueButton=Button(SubFrame, text="Continue", command=lambda: ValidateandStorePlayerInformation(4,varGRP1.get(),varGRP2.get(),varGRP3.get(),varGRP4.get()))
                ContinueButton.grid(row=13,column=2)

def main():
    
    top.geometry("1000x800")

    top.grid_columnconfigure(0,weight=0,uniform="foo")        
    top.grid_columnconfigure(1,weight=0,uniform="foo")

    NumPlayersLabel=Label(top, text="Enter the number of players")
    NumPlayersLabel.grid(row=1,column=0)

    NumPlayersEntry=Entry(top)
    NumPlayersEntry.grid(row=1,column=1)
    
    #SLfilename=PhotoImage(file="D:/1Data/Data/Personal/Game-Board-Snakes-and-Ladders.gif")
    #SL=Label(top,image=SLfilename)
    #SL.grid(row=3,column=1,rowspan=10,columnspan=10)

    BlueMonsterIconFileName=PhotoImage(file="D:/1Data/Data/Personal/blue-monster-icon.gif")
    BlueMonsterIcon11=Label(top,image=BlueMonsterIconFileName)
    BlueMonsterIcon11.place(x=700,y=40,in_=top)
    
    Bu=Button(top, text="Continue", command=lambda: PressCallBack(NumPlayersEntry.get())).grid(row=3,column=2)
    #Bu.pack()
    #Bu.flash()

    top.mainloop()

main()
