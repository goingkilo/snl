import sys
sys.path.append('C:/Users/a20643/AppData/Local/Programs/Python/Python37-32/Lib/tkinter')
sys.setrecursionlimit(6000)
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
import random
import time
# import winsound

class Player:

        playerPos=1
        playerDir='R'
        playerPos1Count=0
        
        def __init__(self,name,icon):
                self.name=name
                self.icon=icon

class PlayFrame(Toplevel):
    
        def __init__(self,PlayerList,IconList,subFrame):
                Toplevel.__init__(self)

                self.geometry("800x470")
                self.grid_columnconfigure(0,weight=0,uniform="foo")        
                self.grid_columnconfigure(1,weight=0,uniform="foo")
                self.grid_columnconfigure(2,weight=0,uniform="foo")
                self.grid_columnconfigure(3,weight=0,uniform="foo")

                self.ParentWindow=subFrame

                self.resizable(0,0)
                #self.overrideredirect(1)

                CloseButton=Button(self, text="Close", command=lambda: self.CloseSubFrame(subFrame))
                CloseButton.place(x=15,y=440,in_=self)
                CloseButton.configure(foreground="red")

                #self.GameBoardSnakesAndLadders=PhotoImage(file="C:/D-Drive/1Data/Data/Personal/Game-Board-Snakes-and-Ladders.gif")
                self.GameBoardSnakesAndLadders=PhotoImage(file="./Game-Board-Snakes-and-Ladders.gif")
                self.DiePhotoImage=PhotoImage(file="./Die_1000_Single.gif")
                self.DiePhotoImageList=list()
                for i in range(1,7):
                        ImageName="./Die_1000_Single_" + str(i) + ".gif"
                        PhotoImageReference=PhotoImage(file=ImageName)
                        self.DiePhotoImageList.append(PhotoImageReference)
        
                self.PlayerList=PlayerList
                self.IconList=IconList
                self.FirstPlayerReached=0
                self.DieStatus=0
                self.Increment=0
                self.PlayerIconXPlacement=[155,155,155,155]
                self.PlayerIconYPlacement=[370,370,370,370]
                self.SnakeAndLadderPos=[38,0,0,14,0,0,0,0,31,0,0,0,0,0,0,0,7,0,0,0,42,0,0,0,0,0,0,84,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,67,0,0,34,0,0,0,0,0,0,0,19,0,60,0,0,0,0,0,0,91,0,0,0,0,0,0,0,0,100,0,0,0,0,0,0,24,0,0,0,0,0,73,0,75,0,0,79,0,0]
                self.PlayerFinishXIncrement=0
                self.PlayerFinishYIncrement=50
                self.PlayerIconLabelList=list()
                self.SetPlayerBoard()
                

        def SetPlayerBoard(self):

                j=0
                i=0
                xvalue=100
                yvalue=425

                GameBoardLabel=Label(self,image=self.GameBoardSnakesAndLadders)
                #GameBoardLabel.grid(row=i+1,column=4)
                GameBoardLabel.place(x=150,y=50,in_=self)
                
                #for i in range(len(self.PlayerList)):

                        #PlayerLabel="Player" + str(i+1) + "NameLabel"
                        #PlayerIcon="Player" + str(i+1) + "Icon"
                        #PlayerIconGameBoard="Player" + str(i+1) + "IconGameBoard"

                        #PlayerLabel=Label(self,text=self.PlayerList[i].name)
                        #PlayerLabel.grid(row=i,column=j)

                        #messagebox.showinfo("Info",str(PlayerIconGameBoard))

                        #PlayerIcon=Label(self,image=self.IconList[self.PlayerList[i].icon-1])
                        #PlayerIcon.grid(row=i,column=j+1)

                        #self.PlayerIconGameBoard=Label(self,image=self.IconList[self.PlayerList[i].icon-1])
                        #self.PlayerIconGameBoard.place(x=xvalue,y=yvalue)

                        #xvalue-=30

                if len(self.PlayerList)==2 or len(self.PlayerList)==3 or len(self.PlayerList)==4 :

                        Player1NameLabel=Label(self, text=self.PlayerList[0].name)
                        Player1NameLabel.place(x=60,y=50,in_=self)

                        Player1Icon=Label(self,image=self.IconList[self.PlayerList[0].icon-1])
                        Player1Icon.place(x=30,y=50,in_=self)

                        Player1IconGameBoard=Label(self,image=self.IconList[self.PlayerList[0].icon-1])
                        Player1IconGameBoard.place(x=110,y=375,in_=self)
                        self.PlayerIconLabelList.append(Player1IconGameBoard)

                        Player2NameLabel=Label(self, text=self.PlayerList[1].name)
                        Player2NameLabel.place(x=60,y=80,in_=self)

                        Player2Icon=Label(self,image=self.IconList[self.PlayerList[1].icon-1])
                        Player2Icon.place(x=30,y=80,in_=self)

                        Player2IconGameBoard=Label(self,image=self.IconList[self.PlayerList[1].icon-1])
                        Player2IconGameBoard.place(x=80,y=375,in_=self)
                        self.PlayerIconLabelList.append(Player2IconGameBoard)

                        self.PlayerFinishXIncrement=35

                if len(self.PlayerList)==3 or len(self.PlayerList)==4 :

                        i+=1

                        Player3NameLabel=Label(self, text=self.PlayerList[2].name)
                        Player3NameLabel.place(x=60,y=110,in_=self)

                        Player3Icon=Label(self,image=self.IconList[self.PlayerList[2].icon-1])
                        Player3Icon.place(x=30,y=110,in_=self)

                        Player3IconGameBoard=Label(self,image=self.IconList[self.PlayerList[2].icon-1])
                        Player3IconGameBoard.place(x=50,y=375,in_=self)
                        self.PlayerIconLabelList.append(Player3IconGameBoard)

                        self.PlayerFinishXIncrement=70

                if len(self.PlayerList)==4 :

                        i+=1

                        Player4NameLabel=Label(self, text=self.PlayerList[3].name)
                        Player4NameLabel.place(x=60,y=140,in_=self)

                        Player4Icon=Label(self,image=self.IconList[self.PlayerList[3].icon-1])
                        Player4Icon.place(x=30,y=140,in_=self)

                        Player4IconGameBoard=Label(self,image=self.IconList[self.PlayerList[3].icon-1])
                        Player4IconGameBoard.place(x=20,y=375,in_=self)
                        self.PlayerIconLabelList.append(Player4IconGameBoard)

                        self.PlayerFinishXIncrement=105
                      

                DieStatusLabel=Label(self,image=self.DiePhotoImage)
                DieStatusLabel.place(x=550,y=100,in_=self)

                DieRollPlayerTurnLabel=Label(self,text=self.PlayerList[self.Increment].name + "'s Turn")
                DieRollPlayerTurnLabel.place(x=600,y=250,in_=self)

                self.DieRollButton=Button(self, text="Roll Die", command=lambda: self.RollDie(DieRollPlayerTurnLabel,DieStatusLabel))
                self.DieRollButton.place(x=700,y=247,in_=self)
                self.DieRollButton.configure(foreground="brown")

                #DieRollStatusCanvas=Label(self,image=self.DieStatus)
                #DieRollStatusCanvas.place(x=500,y=80,in_=self)
                                
                #GameBoardLabel.image="D:/1Data/Data/Personal/Game-Board-Snakes-and-Ladders.gif"

        def RollDie(self,DieRollPlayerTurnLabel,DieStatusLabel):

                self.DieRollButton.config(state="disabled")

                xincrement=35
                yincrement=35
            
                for i in range(1,7):
                        DieRandNum=random.randint(1,6)
                        #messagebox.showinfo("Info",str(self.DieStatus))
                        DieStatusLabel.config(image=self.DiePhotoImageList[DieRandNum-1])
                        DieStatusLabel.update_idletasks()
                        #DieStatusLabel.after(1000,self.StatusDie(DieStatusLabel))
                        time.sleep(1)

                if (self.PlayerList[self.Increment].playerPos + DieRandNum) > 100:
                                DieRollPlayerTurnLabel.config(text="Player cannot score higher than 100")
                                DieRollPlayerTurnLabel.update_idletasks()
                                time.sleep(2)
                else:
                        for i in range(1,DieRandNum+1):
                                
                                #self.PlayerList[self.Increment].playerPos+=1
                                #messagebox.showinfo("Info",str(self.PlayerList[self.Increment].playerPos))
                                #messagebox.showinfo("Info",str(int((self.PlayerList[self.Increment].playerPos)/10)%2))
                                if self.PlayerList[self.Increment].playerPos == 1:
                                        if self.PlayerList[self.Increment].playerPos1Count == 0:
                                                #if self.Increment == 0:
                                                self.PlayerIconLabelList[self.Increment].place(x=self.PlayerIconXPlacement[self.Increment],y=self.PlayerIconYPlacement[self.Increment],in_=self)
                                                        #self.Player1IconGameBoard.place(x=self.PlayerIconXPlacement[0],y=self.PlayerIconYPlacement[0],in_=self)
                                                self.update()
                                                time.sleep(1)
                                                #elif self.Increment == 1:
                                                        #self.Player2IconGameBoard.place(x=self.PlayerIconXPlacement[1],y=self.PlayerIconYPlacement[1],in_=self)
                                                        #self.update()
                                                        #time.sleep(1)
                                                #elif self.Increment == 2:
                                                        #self.Player3IconGameBoard.place(x=self.PlayerIconXPlacement[2],y=self.PlayerIconYPlacement[2],in_=self)
                                                        #self.update()
                                                        #time.sleep(1)
                                                #elif self.Increment == 3:
                                                        #self.Player4IconGameBoard.place(x=self.PlayerIconXPlacement[3],y=self.PlayerIconYPlacement[3],in_=self)
                                                        #self.update()
                                                        #time.sleep(1)
                                                self.PlayerList[self.Increment].playerPos1Count+=1
                                                if i==DieRandNum:
                                                        self.ClimbOrSlide()
                                                        if (self.PlayerList[self.Increment].playerPos)%10 == 0:
                                                                self.PlayerList[self.Increment].playerDir='U'
                                                        elif int((self.PlayerList[self.Increment].playerPos)/10)%2 == 0:
                                                                self.PlayerList[self.Increment].playerDir='R'
                                                        else:
                                                                self.PlayerList[self.Increment].playerDir='L'
                                                continue
                                
                                                                     
                                if self.PlayerList[self.Increment].playerDir=='R':
                                        self.PlayerIconXPlacement[self.Increment]+=xincrement
                                        self.PlayerIconLabelList[self.Increment].place(x=self.PlayerIconXPlacement[self.Increment],y=self.PlayerIconYPlacement[self.Increment],in_=self)
                                        self.update()
                                        time.sleep(1)

                                if self.PlayerList[self.Increment].playerDir=='U':
                                        self.PlayerIconYPlacement[self.Increment]-=yincrement
                                        self.PlayerIconLabelList[self.Increment].place(x=self.PlayerIconXPlacement[self.Increment],y=self.PlayerIconYPlacement[self.Increment],in_=self)
                                        self.update()
                                        time.sleep(1)

                                if self.PlayerList[self.Increment].playerDir=='L':
                                        self.PlayerIconXPlacement[self.Increment]-=xincrement
                                        self.PlayerIconLabelList[self.Increment].place(x=self.PlayerIconXPlacement[self.Increment],y=self.PlayerIconYPlacement[self.Increment],in_=self)
                                        self.update()
                                        time.sleep(1)
                                        
                                self.PlayerList[self.Increment].playerPos+=1

                                if i==DieRandNum:
                                        self.ClimbOrSlide()
                                                

                                if (self.PlayerList[self.Increment].playerPos)%10 == 0:
                                        self.PlayerList[self.Increment].playerDir='U'
                                elif int((self.PlayerList[self.Increment].playerPos)/10)%2 == 0:
                                        self.PlayerList[self.Increment].playerDir='R'
                                else:
                                        self.PlayerList[self.Increment].playerDir='L'


                                if self.PlayerList[self.Increment].playerPos == 100:
                                        if self.FirstPlayerReached == 0:
                                                DieRollPlayerTurnLabel.config(text=self.PlayerList[self.Increment].name + " Wins !")
                                                self.FirstPlayerReached+=1
                                        else:
                                                DieRollPlayerTurnLabel.config(text=self.PlayerList[self.Increment].name + " Finishes !")
                                        self.PlayerIconLabelList[self.Increment].place(x=self.PlayerIconXPlacement[self.Increment],y=self.PlayerIconYPlacement[self.Increment],in_=self)
                                        DieStatusLabel.update_idletasks()
                                        time.sleep(2)
                                        self.PlayerIconXPlacement[self.Increment]=self.PlayerIconXPlacement[self.Increment]-self.PlayerFinishXIncrement
                                        #if self.FirstPlayerReached == 0:
                                        self.PlayerIconYPlacement[self.Increment]=self.PlayerIconYPlacement[self.Increment]-self.PlayerFinishYIncrement
                                                #self.FirstPlayerReached+=1
                                        self.PlayerIconLabelList[self.Increment].place(x=self.PlayerIconXPlacement[self.Increment],y=self.PlayerIconYPlacement[self.Increment],in_=self)
                                        self.PlayerFinishXIncrement=self.PlayerFinishXIncrement-35
                                        del self.PlayerList[self.Increment]
                                        del self.PlayerIconXPlacement[self.Increment]
                                        del self.PlayerIconYPlacement[self.Increment]
                                        del self.PlayerIconLabelList[self.Increment]
                                        self.Increment-=1
                                        break

                if len(self.PlayerList) > 0:
                        self.Increment+=1
                        if self.Increment == len(self.PlayerList):
                                self.Increment=0
                        DieRollPlayerTurnLabel.config(text=self.PlayerList[self.Increment].name + "'s Turn")
                        self.DieRollButton.config(state="normal")

        def ClimbOrSlide(self):
                
                xincrement=35
                yincrement=35
                #messagebox.showinfo("Info",str(self.SnakeAndLadderPos[self.PlayerList[self.Increment].playerPos - 1]))
                if self.SnakeAndLadderPos[self.PlayerList[self.Increment].playerPos - 1] != 0:
                        # if (self.SnakeAndLadderPos[self.PlayerList[self.Increment].playerPos - 1] < self.PlayerList[self.Increment].playerPos):
                        #         winsound.PlaySound("./sadtrombone.wav",winsound.SND_ASYNC)
                        # else:
                        #         winsound.PlaySound("./woohooooohhhh.wav",winsound.SND_ASYNC)
                        self.PlayerIconYPlacement[self.Increment]=370
                        self.PlayerIconXPlacement[self.Increment]=155
                        j=0
                        k=0
                        units_pos=(self.SnakeAndLadderPos[self.PlayerList[self.Increment].playerPos - 1])%10
                        tens_pos=int((self.SnakeAndLadderPos[self.PlayerList[self.Increment].playerPos - 1])/10)
                        if tens_pos%2 == 0:
                                direction='R'
                        else:
                                direction='L'
                        if units_pos == 0:
                                while j < (tens_pos-1):
                                        self.PlayerIconYPlacement[self.Increment]-=yincrement
                                        j+=1
                        else:
                                while j < tens_pos:
                                        self.PlayerIconYPlacement[self.Increment]-=yincrement
                                        j+=1
                        if direction=='L':
                                while k < (10-units_pos):
                                        self.PlayerIconXPlacement[self.Increment]+=xincrement
                                        k+=1
                        if direction=='R':
                                while k < (units_pos-1):
                                        self.PlayerIconXPlacement[self.Increment]+=xincrement
                                        k+=1
                        self.PlayerIconLabelList[self.Increment].place(x=self.PlayerIconXPlacement[self.Increment],y=self.PlayerIconYPlacement[self.Increment],in_=self)
                        self.PlayerList[self.Increment].playerPos=self.SnakeAndLadderPos[self.PlayerList[self.Increment].playerPos - 1]
                        #messagebox.showinfo("PlayerPosition",str(self.PlayerList[self.Increment].playerPos))
                                                

                

        def StatusDie(self,DieStatusLabel):

                while self.DieStatus < 6:
                        DieRandNum=random.randint(1,6)
                        #messagebox.showinfo("Info",str(self.DieStatus))
                        DieStatusLabel.config(image=self.DiePhotoImageList[DieRandNum-1])
                        DieStatusLabel.update_idletasks()
                        self.DieStatus+=1
                        #DieStatusLabel.after(1000,self.StatusDie(DieStatusLabel))
                        time.sleep(1)

        def CloseSubFrame(self,subFrame):
                self.destroy()
                subFrame.deiconify()

class SubFrame(Toplevel):

    
        def __init__(self,NumPlayers,mainFrame):
                Toplevel.__init__(self)

                self.NumPlayers=NumPlayers

                if self.NumPlayers == 2:
                        self.geometry("500x200")
                elif self.NumPlayers == 3:
                        self.geometry("500x250")
                else:
                        self.geometry("500x300")

                self.resizable(0,0)

                self.grid_columnconfigure(0,weight=0,uniform="foo")        
                self.grid_columnconfigure(1,weight=0,uniform="foo")
                self.grid_columnconfigure(2,weight=0,uniform="foo")
                self.grid_columnconfigure(3,weight=0,uniform="foo")

                CloseButton=Button(self, text="Close", command=lambda: self.CloseSubFrame(mainFrame))
                if self.NumPlayers == 2:
                        CloseButton.place(x=20,y=170,in_=self)
                elif self.NumPlayers == 3:
                        CloseButton.place(x=20,y=220,in_=self)
                else:
                        CloseButton.place(x=20,y=270,in_=self)

                CloseButton.configure(foreground="red")

                self.BlueMonsterIconFileName=PhotoImage(file="./blue-monster-icon.gif")
                self.RedMonsterIconFileName=PhotoImage(file="./red-monster-icon.gif")
                self.GreenMonsterIconFileName=PhotoImage(file="./green-monster-icon.gif")
                self.YellowMonsterIconFileName=PhotoImage(file="./yellow-monster-icon.gif")
                
                self.PresentOptionsSubFrame()

        def CloseSubFrame(self,mainFrame):
                self.destroy()
                mainFrame.deiconify()

        def PresentOptionsSubFrame(self):
              
                varGRP1=IntVar()
                        
                Player1Label=Label(self, text="Name Of Player 1")
                Player1Label.grid(row=0,column=0)

                self.Player1Entry=Entry(self)
                self.Player1Entry.grid(row=0,column=1)

                Player1RadioButtonGroupBlue=Radiobutton(self,image=self.BlueMonsterIconFileName,variable=varGRP1,value=1)
                Player1RadioButtonGroupBlue.image=self.BlueMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player1RadioButtonGroupBlue.grid(row=1,column=0)

                Player1RadioButtonGroupRed=Radiobutton(self,image=self.RedMonsterIconFileName,variable=varGRP1,value=2)
                Player1RadioButtonGroupRed.image=self.RedMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player1RadioButtonGroupRed.grid(row=1,column=1)

                Player1RadioButtonGroupGreen=Radiobutton(self,image=self.GreenMonsterIconFileName,variable=varGRP1,value=3)
                Player1RadioButtonGroupGreen.image=self.GreenMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player1RadioButtonGroupGreen.grid(row=1,column=2)

                Player1RadioButtonGroupYellow=Radiobutton(self,image=self.YellowMonsterIconFileName,variable=varGRP1,value=4)
                Player1RadioButtonGroupYellow.image=self.YellowMonsterIconFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                Player1RadioButtonGroupYellow.grid(row=1,column=3)

                varGRP1.set(1)
                        

                if self.NumPlayers==2 or self.NumPlayers==3 or self.NumPlayers==4 :

                        varGRP2=IntVar()

                        Player2Label=Label(self, text="Name Of Player 2")
                        Player2Label.grid(row=3,column=0)

                        self.Player2Entry=Entry(self)
                        self.Player2Entry.grid(row=3,column=1)

                        Player2RadioButtonGroupBlue=Radiobutton(self,image=self.BlueMonsterIconFileName,variable=varGRP2,value=1)
                        Player2RadioButtonGroupBlue.image=self.BlueMonsterIconFileName
                        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                        Player2RadioButtonGroupBlue.grid(row=4,column=0)

                        Player2RadioButtonGroupRed=Radiobutton(self,image=self.RedMonsterIconFileName,variable=varGRP2,value=2)
                        Player2RadioButtonGroupRed.image=self.RedMonsterIconFileName
                        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                        Player2RadioButtonGroupRed.grid(row=4,column=1)

                        Player2RadioButtonGroupGreen=Radiobutton(self,image=self.GreenMonsterIconFileName,variable=varGRP2,value=3)
                        Player2RadioButtonGroupGreen.image=self.GreenMonsterIconFileName
                        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                        Player2RadioButtonGroupGreen.grid(row=4,column=2)

                        Player2RadioButtonGroupYellow=Radiobutton(self,image=self.YellowMonsterIconFileName,variable=varGRP2,value=4)
                        Player2RadioButtonGroupYellow.image=self.YellowMonsterIconFileName
                        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                        Player2RadioButtonGroupYellow.grid(row=4,column=3)

                        varGRP2.set(2)

                if self.NumPlayers==3 or self.NumPlayers==4 :

                        varGRP3=IntVar()

                        Player3Label=Label(self, text="Name Of Player 3")
                        Player3Label.grid(row=6,column=0)

                        self.Player3Entry=Entry(self)
                        self.Player3Entry.grid(row=6,column=1)

                        Player3RadioButtonGroupBlue=Radiobutton(self,image=self.BlueMonsterIconFileName,variable=varGRP3,value=1)
                        Player3RadioButtonGroupBlue.image=self.BlueMonsterIconFileName
                        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                        Player3RadioButtonGroupBlue.grid(row=7,column=0)

                        Player3RadioButtonGroupRed=Radiobutton(self,image=self.RedMonsterIconFileName,variable=varGRP3,value=2)
                        Player3RadioButtonGroupRed.image=self.RedMonsterIconFileName
                        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                        Player3RadioButtonGroupRed.grid(row=7,column=1)

                        Player3RadioButtonGroupGreen=Radiobutton(self,image=self.GreenMonsterIconFileName,variable=varGRP3,value=3)
                        Player3RadioButtonGroupGreen.image=self.GreenMonsterIconFileName
                        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                        Player3RadioButtonGroupGreen.grid(row=7,column=2)

                        Player3RadioButtonGroupYellow=Radiobutton(self,image=self.YellowMonsterIconFileName,variable=varGRP3,value=4)
                        Player3RadioButtonGroupYellow.image=self.YellowMonsterIconFileName
                        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                        Player3RadioButtonGroupYellow.grid(row=7,column=3)

                        varGRP3.set(3)
                
                if self.NumPlayers==4 :

                        varGRP4=IntVar()

                        Player4Label=Label(self, text="Name Of Player 4")
                        Player4Label.grid(row=9,column=0)

                        self.Player4Entry=Entry(self)
                        self.Player4Entry.grid(row=9,column=1)

                        Player4RadioButtonGroupBlue=Radiobutton(self,image=self.BlueMonsterIconFileName,variable=varGRP4,value=1)
                        Player4RadioButtonGroupBlue.image=self.BlueMonsterIconFileName
                        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                        Player4RadioButtonGroupBlue.grid(row=10,column=0)

                        Player4RadioButtonGroupRed=Radiobutton(self,image=self.RedMonsterIconFileName,variable=varGRP4,value=2)
                        Player4RadioButtonGroupRed.image=self.RedMonsterIconFileName
                        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                        Player4RadioButtonGroupRed.grid(row=10,column=1)

                        Player4RadioButtonGroupGreen=Radiobutton(self,image=self.GreenMonsterIconFileName,variable=varGRP4,value=3)
                        Player4RadioButtonGroupGreen.image=self.GreenMonsterIconFileName
                        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                        Player4RadioButtonGroupGreen.grid(row=10,column=2)

                        Player4RadioButtonGroupYellow=Radiobutton(self,image=self.YellowMonsterIconFileName,variable=varGRP4,value=4)
                        Player4RadioButtonGroupYellow.image=self.YellowMonsterIconFileName
                        #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                        Player4RadioButtonGroupYellow.grid(row=10,column=3)

                        varGRP4.set(4)

                if self.NumPlayers == 2:
                        ContinueButton=Button(self, text="Continue", command=lambda: self.ValidateandStorePlayerInformation(varGRP1.get(),varGRP2.get(),0,0))
                        ContinueButton.place(x=420,y=170,in_=self)
                if self.NumPlayers == 3:
                        ContinueButton=Button(self, text="Continue", command=lambda: self.ValidateandStorePlayerInformation(varGRP1.get(),varGRP2.get(),varGRP3.get(),0))
                        ContinueButton.place(x=420,y=220,in_=self)
                if self.NumPlayers == 4:
                        ContinueButton=Button(self, text="Continue", command=lambda: self.ValidateandStorePlayerInformation(varGRP1.get(),varGRP2.get(),varGRP3.get(),varGRP4.get()))
                        ContinueButton.place(x=420,y=270,in_=self)

                ContinueButton.configure(foreground="green")

        def ValidateandStorePlayerInformation(self,Player1Choice,Player2Choice,Player3Choice,Player4Choice):
                PlayerIcons=[0,0,0,0]
                InvalidChoice=0
                PlayerNameEmpty=0
        
                if self.NumPlayers == 2 or self.NumPlayers == 3 or self.NumPlayers == 4:
                        PlayerIcons[Player1Choice-1]+=1
                        PlayerIcons[Player2Choice-1]+=1

                if self.NumPlayers == 3 or self.NumPlayers == 4:
                        PlayerIcons[Player3Choice-1]+=1

                if self.NumPlayers == 4:
                        PlayerIcons[Player4Choice-1]+=1

                #messagebox.showinfo("Info",str(PlayerIcons[0]))
                #messagebox.showinfo("Info",str(PlayerIcons[1]))
                #messagebox.showinfo("Info",str(PlayerIcons[2]))
                #messagebox.showinfo("Info",str(PlayerIcons[3]))

                if self.NumPlayers == 2:                  
                        if self.Player1Entry.get() == "":
                                messagebox.showinfo("Warning","Please enter name of Player 1")
                                self.Player1Entry.focus_set()
                                PlayerNameEmpty=1
                        elif self.Player2Entry.get() == "":
                                messagebox.showinfo("Warning","Please enter name of Player 2")
                                self.Player2Entry.focus_set()
                                PlayerNameEmpty=1
                if self.NumPlayers == 3:                  
                        if self.Player1Entry.get() == "":
                                messagebox.showinfo("Warning","Please enter name of Player 1")
                                self.Player1Entry.focus_set()
                                PlayerNameEmpty=1
                        elif self.Player2Entry.get() == "":
                                messagebox.showinfo("Warning","Please enter name of Player 2")
                                self.Player2Entry.focus_set()
                                PlayerNameEmpty=1
                        elif self.Player3Entry.get() == "":
                                messagebox.showinfo("Warning","Please enter name of Player 3")
                                self.Player3Entry.focus_set()
                                PlayerNameEmpty=1
                if self.NumPlayers == 4:                  
                        if self.Player1Entry.get() == "":
                                messagebox.showinfo("Warning","Please enter name of Player 1")
                                self.Player1Entry.focus_set()
                                PlayerNameEmpty=1
                        elif self.Player2Entry.get() == "":
                                messagebox.showinfo("Warning","Please enter name of Player 2")
                                self.Player2Entry.focus_set()
                                PlayerNameEmpty=1
                        elif self.Player3Entry.get() == "":
                                messagebox.showinfo("Warning","Please enter name of Player 3")
                                self.Player3Entry.focus_set()
                                PlayerNameEmpty=1
                        elif self.Player4Entry.get() == "":
                                messagebox.showinfo("Warning","Please enter name of Player 4")
                                self.Player4Entry.focus_set()
                                PlayerNameEmpty=1

                if PlayerIcons[0] > 1 or PlayerIcons[1] > 1 or PlayerIcons[2] > 1 or PlayerIcons[3] > 1:
                        messagebox.showinfo("Warning","Invalid Choice")
                        InvalidChoice=1

                if InvalidChoice == 0 and PlayerNameEmpty == 0:
                        if self.NumPlayers == 2 or self.NumPlayers == 3 or self.NumPlayers == 4:
                                Player1=Player(self.Player1Entry.get(),Player1Choice)
                                Player2=Player(self.Player2Entry.get(),Player2Choice)
                                PlayerList=[Player1,Player2]

                        if self.NumPlayers == 3 or self.NumPlayers == 4:
                                Player3=Player(self.Player3Entry.get(),Player3Choice)
                                PlayerList.append(Player3)

                        if self.NumPlayers == 4:
                                Player4=Player(self.Player4Entry.get(),Player4Choice)
                                PlayerList.append(Player4)

                        IconList=[self.BlueMonsterIconFileName,self.RedMonsterIconFileName,self.GreenMonsterIconFileName,self.YellowMonsterIconFileName]
                        #messagebox.showinfo("Info",str(PlayerList[0].icon))
                        #messagebox.showinfo("Info",str(PlayerList[1].icon))
                        #messagebox.showinfo("Info",str(PlayerList[2].icon))
                        #messagebox.showinfo("Info",str(PlayerList[3].icon))

                        self.withdraw()
                        playFrame=PlayFrame(PlayerList,IconList,self)


class MainFrame:
        def __init__(self,ParentWindow):
                self.mainFrame=ParentWindow           
                self.mainFrame.geometry("500x150")
                self.mainFrame.grid_columnconfigure(0,weight=0,uniform="foo")
                self.mainFrame.grid_columnconfigure(1,weight=0,uniform="foo")

                self.mainFrame.resizable(0,0)
            

                NumPlayersLabel=Label(self.mainFrame, text="Choose the number of players")
                NumPlayersLabel.grid(row=1,column=0)

                self.mainFrame.twoPawnsFileName=PhotoImage(file="./2pawns.gif")
                self.mainFrame.threePawnsFileName=PhotoImage(file="./3pawns.gif")
                self.mainFrame.fourPawnsFileName=PhotoImage(file="./4pawns.gif")
                
                #NumPlayersEntry=Entry(self.mainFrame)
                #NumPlayersEntry.grid(row=1,column=1)
                
                NumPlayers=IntVar()

                NumPlayers2=Radiobutton(self.mainFrame,image=self.mainFrame.twoPawnsFileName,variable=NumPlayers,value=2)
                NumPlayers2.image=self.mainFrame.twoPawnsFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                NumPlayers2.grid(row=4,column=0)

                NumPlayers3=Radiobutton(self.mainFrame,image=self.mainFrame.threePawnsFileName,variable=NumPlayers,value=3)
                NumPlayers3.image=self.mainFrame.threePawnsFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                NumPlayers3.grid(row=4,column=1)

                NumPlayers4=Radiobutton(self.mainFrame,image=self.mainFrame.fourPawnsFileName,variable=NumPlayers,value=4)
                NumPlayers4.image=self.mainFrame.fourPawnsFileName
                #Player1RadioButtonGroupBlue=Radiobutton(SubFrame,text="Option1",variable=varGRP1,value=1)
                NumPlayers4.grid(row=4,column=2)

                NumPlayers.set(2)


                BuContinue=Button(self.mainFrame, text="Continue", command=lambda: self.ContinueButton(NumPlayers.get()))
                BuClose=Button(self.mainFrame, text="Close", command=lambda: self.CloseButton())     

                BuContinue.place(x=430,y=120,in_=self.mainFrame)
                BuClose.place(x=15,y=120,in_=self.mainFrame)

                BuContinue.configure(foreground="green")
                BuClose.configure(foreground="red")

        def ContinueButton(self,NumPlayers):
                self.NumPlayers=int(NumPlayers)
                self.mainFrame.withdraw()
                subFrame=SubFrame(self.NumPlayers,self.mainFrame)
                #OpenSubFrame(IntNumPlayers,SubFrame)
        
        def CloseButton(self):
                self.mainFrame.destroy()
                
def main():
        top=Tk()
        app=MainFrame(top)
        top.mainloop()

main()
