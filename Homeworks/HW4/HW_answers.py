import random
x = random.sample(xrange(5000), 400)

#1: MySort: In an effort to be creative, I created my own sorting algorithm.
def mysort(unsorted):
    sorted_list=[]#empty list
    sorted_list.append(unsorted.pop())#append last element of the original list to the empty list

    while len(unsorted) > 0:#while there are elements in the original list, do the following:
        tmp = unsorted.pop()#get the last element in the original list (at this point, the second last element)
        for a in range(len(sorted_list)):
            if sorted_list[a] > tmp:#if first element of the new list is greater than the (second-)last item of the original list
                sorted_list.insert(a, tmp)#then append it to the new list and restart the loop
                break
            elif sorted_list[-1-a] < tmp:#if the last element of the new list is lower than the (second-)last item of the original list
                sorted_list.insert(len(sorted_list)-a, tmp)#then,  insert it at the beginning of the new list
                break
            else:
                continue#if the original item is not either lower than the first or greater than the last, then restart but it will now try whether it is lower than the second or the second-last item in the new list
    return sorted_list#do this until the element finds its place in the list

mysort(x)#it works

##2 Bubble Sort
def bubble_sort(unsorted):
	k = len(unsorted) - 1
	for i in xrange(k):
		for j in xrange(k, i, -1): # loop backword from k to i 
			if unsorted[j - 1] > unsorted[j]: # if the jth element is smaller than its left-side element, replace
				temp = unsorted[j]
				unsorted[j] = unsorted[j - 1]
				unsorted[j - 1] = temp
	return unsorted

x = random.sample(xrange(5000), 400)

bubble_sort(x)

#3 Quick Sort
def quick_sort(x):
    if len(x) < 2:
        return x
    pivot = x.pop(len(x)/2) # determine the pivot element
    less = [] # list of elements smaller than the pivot
    greater = [] # list of elements greater than the pivot
    for i in x:
        if i < pivot + 1: # if i is smaller than the pivot value, add to the smaller list
            less.append(i)
        else:
            greater.append(i) # if i is greater than the pivot value, append to the greater list
    return quick_sort(less) + [pivot] + quick_sort(greater) # combine 2 list and the pivot

x = random.sample(xrange(5000), 400)

quick_sort(x)

# Graphing
import csv
import time
import random

sumtime0 = []
list0 = []
num_items0 = []
for n in range(10, 2010): # range of the length of the list 0-2000
	list0.append(random.sample(xrange(100000), n))# generate random values within the list
	num_items0.append(n)

for i in range(len(list0)):
    begin = time.clock() # start clock
    mysort(list0[i])
    end = time.clock() # end clock
    sumtime0.append(end - begin) # how long it takes from start to end

len(num_items0)

sumtime = []
list1 = []
num_items = []
for n in range(10, 2010): # range of the length of the list 0-2000
	list1.append(random.sample(xrange(100000), n))# generate random values within the list

for i in range(len(list1)):
    begin = time.clock() # start clock
    bubble_sort(list1[i])
    end = time.clock() # end clock
    sumtime.append(end - begin) # how long it takes from start to end


sumtime2 = []
list2 = []
num_items2 = []
for n in range(10, 2010): # range of the length of the list 0-2000
	list2.append(random.sample(xrange(100000), n))# generate random values within the list

for i in range(len(list2)):
    begin = time.clock() # start clock
    quick_sort(list2[i])
    end = time.clock() # end clock
    sumtime2.append(end - begin) # how long it takes from start to end


import numpy as np
from IPython.html.widgets import interact
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig = plt.figure()
ax = plt.axes()

plt.title("Comparing sorting algorithms")
plt.xlabel("Size of the set to sort (N)")
plt.ylabel("Computing Time")
plt.plot(num_items0, sumtime0, color='orange')
plt.plot(num_items0, sumtime, color='blue')
plt.plot(num_items0, sumtime2, color='green')
or_patch = mpatches.Patch(color='orange', label='MySort')
blue_patch = mpatches.Patch(color='blue', label='BubbleSort')
green_patch = mpatches.Patch(color='green', label='QuickSort')
plt.legend(handles=[or_patch, blue_patch, green_patch])

plt.show()

