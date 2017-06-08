# l = [1, 4, 5, 6]

# print l[0] # -->  Random Access

# for x in range(len(l)):
# 	print l[x]


# def binarySearch(myList, item):
# 	found = False
# 	myIndex = len(myList)//2

# 	while myIndex > 1 and not found:
# 		if myList[myIndex] == item:
# 			found = True
# 		elif myList[myIndex] > item:
# 			myIndex = len(myList[:myIndex])//2
# 		else:
# 			myIndex = len(myList[myIndex:])//2
# 	print(found)		

# binarySearch(l,15)			


# Bubble Sort

# lst = [4, 7, 6, -2, 1]
# def bubbleSort(myList):

# 	for j in range(len(myList)):
# 		for i in range(len(lst)-1):
# 			if lst[i+1] < lst[i]:
# 				tmp = lst[i]
# 				lst[i] = lst[i+1]
# 				lst[i+1]=tmp


# import random, time
# r = random.sample(range(0,160000),160000)

# s = int(round(time.time() * 1000))
# bubbleSort(r)	
# e = int(round(time.time() * 1000))

# print e-s
import numpy as np
lst = [5, 6, 7, 9]

def multi_ply(l):
	lstOut = []
	for i in range(len(l)):
		lstOut.append(np.prod((l[:i]+l[i+1:])))
	print lstOut
multi_ply(lst)

