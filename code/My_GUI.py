from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter as tk
from typing import Sized
from InsertionSort import main_insertion
from MergeSort import main_merge, merge
from HeapSort import main_heap
from quickSort import main_quick
from Bubble_sort import main_bubble
import matplotlib.pyplot as plt
import tkinter.font as tkFont

window=Tk()
window.title("Algorithm Sorting App")
window.geometry("600x550")
window.config(bg='#152238')
fontStyle = tkFont.Font(family="Amaranth", size=30)
fontStyle1 = tkFont.Font(family="Amaranth", size=25)
fontbutton=tkFont.Font(family="Amaranth", size=15)
header_frame=Frame(window).pack(padx=200)
header=Label(header_frame,text="Data Structure & Algorithms",bg='#152238',pady=10,fg="#FFFFFF",font=fontStyle).pack(fill=X)


def insertion(a):
    main_insertion(a)
    if(a==0):
        plt.show()
def Merge(a):
    main_merge(a)
    if(a==0):
        plt.show()
def Heap(a):
    main_heap(a)
    if(a==0):
        plt.show()
def quick(a):
    main_quick(a)
    if(a==0):
        plt.show()
def bubble(a):
    main_bubble(a)
    if(a==0):
        plt.show()
      
def openNewWindow():
    newWindow = Toplevel(window)
    newWindow.title("Sorting Algorithm App")
    # newWindow.iconbitmap("university.ico")
    newWindow.geometry("600x500")
    newWindow.config(bg="#152238")
    fontStyle2 = tkFont.Font(family="Amaranth", size=20)
    Label(newWindow,text ="Choose 2 or More",fg="white",bg='#152238',font=fontStyle2).pack()
    def compare():
            fig = plt.figure()
            if(var1.get()==1):                    
                insertion(1)
            if(var2.get()==1):
                Merge(1)
            if(var3.get()==1):
                Heap(1)
            if(var7.get()==1):
                quick(1)
            if(var8.get()==1):
                bubble(1)
            plt.legend()                    
            plt.show()
          
        
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    var5 = tk.IntVar()
    var6 = tk.IntVar()
    var7 = tk.IntVar()
    var8 = tk.IntVar()
    c1 = tk.Checkbutton(newWindow, text='Insertion Sort',variable=var1, onvalue=1, offvalue=0 ,selectcolor="black",font=fontbutton,fg="white",bg="#800000", width=12).pack(pady=10)
    c2 = tk.Checkbutton(newWindow, text='Merge Sort',variable=var2, onvalue=1, offvalue=0,font=fontbutton,selectcolor="black",fg="white",bg="#800000", width=12).pack(pady=10)
    
    c3 = tk.Checkbutton(newWindow, text='Heap Sort',variable=var3, onvalue=1, offvalue=0,selectcolor="black",font=fontbutton,fg="white",bg="#800000", width=12).pack(pady=10)

    c7 = tk.Checkbutton(newWindow, text='Quick Sort',variable=var7, onvalue=1, offvalue=0,font=fontbutton,selectcolor="black",fg="white",bg="#800000", width=12).pack(pady=10)
    c8 = tk.Checkbutton(newWindow, text='Bubble Sort',variable=var8, onvalue=1, offvalue=0,font=fontbutton,selectcolor="black",fg="white",bg="#800000", width=12).pack(pady=10)
    
    Show_comparison=Button(newWindow,text="Show Comparison",bg="#006400",font=("Amaranth",15),fg="white",pady=30,relief=RAISED,command=compare).pack(pady=50)




""" buttons """
body=Frame(window).pack(padx=10,pady=10)
# choose=Label(body,text="CHOOSE AN ALGORITHM",font=fontStyle1,fg="#FFFFFF",bg='#E67E22').pack()
insertion_button=Button(body,text="Insertion Sort",bg="#800000",font="Amaranth",pady=10,fg="#FFFFFF",command=lambda : insertion(0),relief=RAISED, width=12).pack(pady=2)
Mergesort_button=Button(body,text="Merge Sort",bg="#800000",font="Amaranth",pady=10,fg="#FFFFFF",command=lambda : Merge(0),relief=RAISED, width=12).pack(pady=2)
Heapsort_button=Button(body,text="Heap Sort",bg="#800000",font="Amaranth",pady=10,fg="#FFFFFF",command=lambda : Heap(0),relief=RAISED, width=12).pack(pady=2)
Quick_button=Button(body,text="Quick Sort",bg="#800000",font="Amaranth",pady=10,fg="#FFFFFF",relief=RAISED,command=lambda : quick(0), width=12).pack(pady=2)
Bubble_button=Button(body,text="Bubble Sort",bg="#800000",font="Amaranth",pady=10,fg="#FFFFFF",relief=RAISED,command=lambda : bubble(0), width=12).pack(pady=2)


next_window =Button(
    body,text="Compare Algorithms",
    bg="#006400",
    fg="white",
    font=fontbutton,
    pady=10,command=openNewWindow).pack(pady=20)





window.mainloop()