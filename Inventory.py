from pickle import ADDITEMS
from random import random
from tkinter import*
from tkinter import ttk
from tkinter import filedialog
import random
import tkinter.messagebox


class Inventory:

    def __init__(self,root):
        self.root=root
        self.root.title("Inventory System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='white')

        ################ FRAMES #####################

        MainFrame=Frame(self.root, bd=5, width=1350, height=1350, bg="yellow", relief=RIDGE)
        MainFrame.grid()

        #LeftFrame=Frame(MainFrame, bd=5, width=750, height=600,padx=5, bg="light grey", relief=RIDGE)
        #LeftFrame.pack(side=LEFT)

        RightFrame=Frame(MainFrame, bd=5, width=1300, height=1300,padx=5,bg="light grey", relief=RIDGE)
        RightFrame.pack(side=RIGHT)
  
        RightFrame0=Frame(RightFrame, bd=2, width=1350, height=800,padx=5,bg="light grey", relief=RIDGE)
        RightFrame0.grid(row=0, column=0)
        RightFrame1=Frame(RightFrame, bd=2, width=1350, height=800,padx=5,bg="light grey", relief=RIDGE)
        RightFrame1.grid(row=1, column=0)
        RightFrame2=Frame(RightFrame, bd=2, width=1350, height=800,padx=5,bg="light grey", relief=RIDGE)
        RightFrame2.grid(row=2, column=0)

        
  
        def openFile():
                tf = filedialog.askopenfilename(
                        initialdir="C:/Users/MainFrame/Desktop/", 
                        title="Open Text file", 
                        filetypes=(("Text Files", "*.txt"),)
        )  
                tf = open(tf)  # or tf = open(tf, 'r')
                data = tf.read()
                self.txtInventory.insert(END, data)
                tf.close()

        def clearScreen():
            self.txtInventory.delete("1.0", "end")


        def display(x):
                print(x)
                return

        def iExit():
            iExit=tkinter.messagebox.askyesno("Inventory System", "Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def iGo():
                File_object=open("Inventory.txt", "r").read().find(self.txtSearch)
                searchedItem= self.txtSearch.get()
                display(searchedItem)

                return

        def openNewWindow():
            newWindow = Toplevel(root)
            newWindow.title("Add Item")
            newWindow.geometry("500x500")
            newWindow.configure(background="white")
            Label(newWindow,
            text ="").pack()

            newFrame=Frame(newWindow, bd=5, width=450, height=450, bg="yellow", relief=RIDGE)
            newFrame.grid(row=0, column=0)

            self.txtSearch= Entry(newFrame, width= 29, font=('arial', 9, 'bold'))
            self.txtSearch.grid(row=0, column=0)
            return
        
        def AddItems():
                F=open("Inventory.txt", "w+")
                UserInput= input("Enter Item name, quantity and Bay #: ")
                with open(F, "w+") as f:
                    f.write(input())


                return
  
   ################ RightFrame0 for Text Labels, Widget #####################

        self.lblSearch=Label(RightFrame0, font=('arial', 18, 'bold'), text= "Search:" , padx=2, pady=2, bg="light grey")
        self.lblSearch.grid(row=0, column=0, sticky=W)
        self.txtSearch= Entry(RightFrame0, width= 29, font=('arial', 9, 'bold'))
        self.txtSearch.grid(row=0, column=1)
  
  ################ Frames for Text Labels, Widget #####################
        self.txtInventory= Text(RightFrame1, height= 45, width= 185, font=('arial', 9, 'bold'))
        self.txtInventory.grid(row=0, column=0)

        ################ Buttons #######################
        self.btnAddItems= Button(RightFrame2, padx=18, pady=2, bd=2, fg="black", font=('arial', 9, 'bold'), width=9,
                 bg="light grey", text="Add Item(s)",command= openNewWindow).grid(row=0, column=0)
        self.btnShowInventory= Button(RightFrame2, padx=18, pady=2, bd=2, fg="black", font=('arial', 9, 'bold'), width=14,
                 bg="light grey", text="Open Inventory File", command= openFile).grid(row=0, column=1)
        self.btnExit= Button(RightFrame2, padx=18, pady=2, bd=2, fg="black", font=('arial', 9, 'bold'), width=9,
                 bg="light grey", text="Exit",command=iExit).grid(row=0, column=2)
        self.btnClear= Button(RightFrame2, padx=18, pady=2, bd=2, fg="black", font=('arial', 9, 'bold'), width=9,
                 bg="light grey", text="Clear Screen",command=clearScreen).grid(row=0, column=3)
        self.btnGo= Button(RightFrame0, padx=2, pady=2, bd=2, fg="black", font=('arial', 9, 'bold'), width=9,
                 bg="light grey", text="Go",command=iGo).grid(row=0, column=2)





if __name__=='__main__':
        root=Tk()
        application= Inventory(root)
        root.mainloop()
