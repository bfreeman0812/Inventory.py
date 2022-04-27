from pickle import ADDITEMS
from random import random
from tkinter import*
from tkinter import ttk
from tkinter import filedialog
import random
import tkinter.messagebox
import pandas as pd
import csv


class Inventory:

    def __init__(self,root):
        self.root=root
        self.root.title("Inventory System")
        self.root.geometry("1360x810+0+0")
        self.root.configure(background='white')

        ################ FRAMES #####################

        MainFrame=Frame(self.root, bd=5, width=1350, height=800, bg="yellow", relief=RIDGE)
        MainFrame.grid()
        MainFrame.grid_propagate(0)

        FrameMain=Frame(MainFrame, bd=5, width=1340, height=790,padx=5,bg="light grey", relief=RIDGE)
        FrameMain.grid(row=0, column=0,sticky=NW)
        FrameMain.grid_propagate(0)

        TreeviewFrame=Frame(FrameMain, bd=2,width=1330, height=750,padx=5,bg="light grey", relief=RIDGE)
        TreeviewFrame.grid(row=0, column=0,sticky=N+S+W+E)
        TreeviewFrame.grid_propagate(0)

        fr_x = ttk.Frame(TreeviewFrame)
        fr_x.pack(side='top', fill='x')

        ButtonFrame=Frame(FrameMain, bd=2, width=1325, height=33,padx=5,bg="light grey", relief=RIDGE)
        ButtonFrame.grid(row=1, column=0, sticky=SW)
        ButtonFrame.grid_propagate(0)

        self.tree=ttk.Treeview(TreeviewFrame, height=34)
      
        label=Label(TreeviewFrame, text='Excel File Will Show Here')
        label.pack()
        label.grid_propagate(0)

        treeScrollBar=ttk.Scrollbar(fr_x, orient= "horizontal", command=self.tree.xview)
        treeScrollBar.pack(expand='yes', fill='x')

        self.tree.configure(xscroll=treeScrollBar.set)
        self.tree.pack(fill='both', expand='yes')

        # self.tree.configure(xscroll=treeScrollBar.set)
        # self.tree.pack(fill='both', expand='yes')
        
        
  
        def openFile():
                filename = filedialog.askopenfilename(
                        title="Open a File", 
                        filetype=(("xlxs files", ".*xlsx"),("All Files", "*.*"))
                )
                if filename:
                        try:
                                filename = r"{}".format(filename)
                                df = pd.read_excel(filename)
                        except ValueError:
                                self.label.config(text="File could not be opened")
                          # Clear all the previous data in tree
                clear_treeview()

                # Add new data in Treeview widget
                self.tree["column"] = list(df.columns)
                self.tree["show"] = "headings"

   # For Headings iterate over the columns
                for col in self.tree["column"]:
                        self.tree.heading(col, text=col)
                        self.tree.column("# 1",anchor=CENTER, stretch=NO, width=100)

   # Put Data in Rows
                df_rows = df.to_numpy().tolist()
                for row in df_rows:
                        self.tree.insert("", "end", values=row)

               

                self.tree.pack()
            
        def display(x):
                print(x)
                return

        def iExit():
            iExit=tkinter.messagebox.askyesno("Inventory System", "Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        # def iGo():
        #         File_object=open("Inventory.txt", "r").read().find(self.txtSearch)
        #         searchedItem= self.txtSearch.get()
        #         display(searchedItem)

        #         return

        def openNewWindow():
            newWindow = Toplevel(root)
            newWindow.title("Add Item")
            newWindow.geometry("500x500")
            newWindow.configure(background="white")
            label=Label(newWindow,
            text ="").pack()

            newFrame=Frame(newWindow, bd=5, width=450, height=450, bg="yellow", relief=RIDGE)
            newFrame.grid(row=0, column=0)

            self.searchEntry= Entry(newFrame, width= 29, font=('arial', 9, 'bold'))
            self.searchEntry.grid(row=0, column=0)
            return
        
        def clear_treeview():
                self.tree.delete(*self.tree.get_children())

        def updateEntry():
                pass

        def saveFile():
                cols = ['ID CARD','NAME','SURNAME', 'DATE']
                path = 'read.csv'
                excel_name = filedialog.asksaveasfilename(title='Save location',defaultextension=[('Excel','*.xlsx')],filetypes=[('Excel','*.xlsx')]) 
                lst = []
                with open(path, "w", newline='') as myfile:
                        csvwriter = csv.writer(myfile, delimiter=',')
                        for row_id in self.tree.get_children():
                                row = self.tree.item(row_id,'values')
                                lst.append(row)
                        lst = list(map(list,lst))
                        lst.insert(0,cols)
                        for row in lst:
                                csvwriter.writerow(row)

                writer = pd.ExcelWriter(excel_name)
                df = pd.read_csv(path)
                df.to_excel(writer,'sheetname')
                writer.save() 


  
   ################ RightFrame0 for Text Labels, Widget #####################

        #self.lblSearch=Label(Frame0, font=('arial', 18, 'bold'), text= "Search:" , padx=2, pady=2, bg="light grey")
        #self.lblSearch.grid(row=0, column=0, sticky=W)
       # self.txtSearch= Entry(Frame0, width= 29, font=('arial', 9, 'bold'))
       # self.txtSearch.grid(row=0, column=1)
        
  
  ################ Frames for Text Labels, Widget #####################
       # self.txtInventory= Text(RightFrame1, height= 45, width= 185, font=('arial', 9, 'bold'))
       # self.txtInventory.grid(row=0, column=0)
      
        ################ Buttons #######################
        self.btnUpdate= Button(ButtonFrame, padx=18, pady=2, bd=2, fg="black", font=('arial', 9, 'bold'), width=9,
                 bg="light grey", text="Update Entry", command= updateEntry).grid(row=1, column=0)
        self.btnSave= Button(ButtonFrame, padx=18, pady=2, bd=2, fg="black", font=('arial', 9, 'bold'), width=9,
                 bg="light grey", text="Save",command= saveFile).grid(row=1, column=1)
        self.btnAddItems= Button(ButtonFrame, padx=18, pady=2, bd=2, fg="black", font=('arial', 9, 'bold'), width=9,
                 bg="light grey", text="Add Item(s)",command= openNewWindow).grid(row=1, column=2)
        self.btnShowInventory= Button(ButtonFrame, padx=18, pady=2, bd=2, fg="black", font=('arial', 9, 'bold'), width=14,
                 bg="light grey", text="Open Inventory File", command= openFile).grid(row=1, column=3)
        self.btnExit= Button(ButtonFrame, padx=18, pady=2, bd=2, fg="black", font=('arial', 9, 'bold'), width=9,
                 bg="light grey", text="Exit",command=iExit).grid(row=1, column=4)
        self.btnClear= Button(ButtonFrame, padx=18, pady=2, bd=2, fg="black", font=('arial', 9, 'bold'), width=9,
                 bg="light grey", text="Clear Screen",command=clear_treeview).grid(row=1, column=5)
      
       # self.btnGo= Button(Frame0, padx=2, pady=2, bd=2, fg="black", font=('arial', 9, 'bold'), width=9,
        #         bg="light grey", text="Go",command=iGo).grid(row=0, column=2)





if __name__=='__main__':
        root=Tk()
        application= Inventory(root)
        root.mainloop()
