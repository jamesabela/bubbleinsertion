"""
Insertion sort. 
This generally outperforms a bubble sort and is particularly efficient with nearly sorted lists.
"""

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index
     print(alist) # Optional shows progress

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
