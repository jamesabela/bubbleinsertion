"""
In A-level you will NOT be expected to make a GUI like this, but its useful for you
to be able to compare and contrast the two sorts.
"""


import random
import datetime
from tkinter import *
root=Tk()
random_list=[]
number_size=4

bottom = Frame(root)      #tkinter setup
bottom.pack(side=BOTTOM)
top = Frame(root)
top.pack(side=TOP)

rand_button=Button(root, text='Random Numbers', command=lambda : random_generator())
rand_button.pack(in_=bottom, side=LEFT)

bubble_button=Button(root, text='Bubble Sort (AS)', command=lambda : bubble_sort())
bubble_button.pack(in_=bottom, side=LEFT)

insertion_button=Button(root, text='Insertion Sort (A2)', command=lambda : insertionSort())
insertion_button.pack(in_=bottom, side=LEFT)

rand_number_label = Label(root,text='Random Number')

textbox=Text(root)
textbox.pack()
root.title('Bubble & insertion Sort')
root.geometry("800x650")

def scale_value(val): #This has to go before the tkinter slider
    global number_size
    number_size = int(val)

scale = Scale(orient='horizontal', from_=4, to=24, command=scale_value)
scale.pack(in_=top, side=LEFT)

def random_generator():
    global random_list
    random_list = [random.randint(100, 999) for c in range(number_size)]
    rand_number_label.configure(text = "Random numbers: "+str(random_list))
    rand_number_label.pack(in_=top, side=LEFT)


def redirector(inputStr):
    textbox.insert(INSERT, inputStr)

def pretty_print(number_swapping, alist): #Puts stars around number being swapped
    pretty_text =""
    for i in alist:

        if number_swapping != i:

            pretty_text = pretty_text +' ' + str(i)+" "

        else:
            pretty_text = pretty_text + '*' + str(i) + '*'
    print(pretty_text)


def bubble_sort():
    alist = random_list[:]
    textbox.delete('1.0', END)
    print(" Bubble sort")
    print(" ------ ----\n")
    start_time = datetime.datetime.now() # Get initial time
    for passnum in range(len(alist)-1,0,-1): #This counts from 8 down to 1
        for i in range(passnum):             # Loop within a loop
            pretty_print(alist[i], alist)           # Prints list showing swaps

            if alist[i] > alist[i+1]:
                temp = alist[i]              # shorter code: alist[i], alist[i+1] = alist[i+1], alist[i]
                alist[i] = alist[i+1]        # But no Pseudocode for that.
                alist[i+1] = temp
    finish_time = datetime.datetime.now()    #Get finish time
    reaction_time = finish_time - start_time # difference in time
    print("\nIt took the PC: ",reaction_time.microseconds,"microseconds ")
    print ("microsecond = 1 millionth of a second")


def insertionSort():
    alist = random_list[:]
    textbox.delete('1.0', END)
    print(" Insertion sort")
    print(" --------- ----\n")
    start_time = datetime.datetime.now() # Get initial time

    for index in range(1,len(alist)):   #For A2 students notice how it uses insertion to keep organised
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
            pretty_print(alist[position], alist) #prints with stars
        alist[position]=currentvalue

    finish_time = datetime.datetime.now()    #Get finish time
    reaction_time = finish_time - start_time # difference in time
    print("\nIt took the PC: ",reaction_time.microseconds,"microseconds ")
    print ("microsecond = 1 millionth of a second")

# Runs the GUI
sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.
textbox.config(width = 400, height=600, font=("Courier",16))
root.mainloop()
