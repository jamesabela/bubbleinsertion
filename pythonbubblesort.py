"""
This is a basic bubble sort. Note that it will run even after a list is fully sorted.
"""

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1): #This counts from 8 down to 1
        for i in range(passnum):             # Loop within a loop
            print(alist)                     # Optional to show sorting
            if alist[i] > alist[i+1]:
                temp = alist[i]              # shorter code: alist[i], alist[i+1] = alist[i+1], alist[i]
                alist[i] = alist[i+1]        # But no Pseudocode for that.
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
