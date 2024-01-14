# update 1 


# def alternatingSum(myList): 
# 	positive = myList[::2]
# 	negative = myList[1::2]
# 	result = sum(positive) - sum(negative)
# 	return result

# # print(alternatingSum([5,3,8,4]))  --> answer = + 5 - 3 + 8 - 4



# given a list, rotate elements n spots to the left 
# listRotate([0, 1, 2, 3, 4, 5], 4)  --> # [4,5,0,1,2,3]

# def listRotate(L, n): 
#   # print( L[n:])
#   # print( L[:n] )
#   return L[n:]+L[:n]





# smallestDifference 
# ([19,2,83,6,27])		 answer = 4 


def smallestDifference(a): 
	minDiff = 100 ** 2000
	for i in range(0, len(a) - 1): 
		for j in range(i + 1, len(a)): 
			if abs(a[i] - a[j]) < minDiff: 
				minDiff = abs(a[i] - a[j]) 
	return minDiff


# print(smallestDifference([19,2,83,6,27]))
## Median ## 
# def median(a): 
# 	a.sort()
# 	if len(a) % 2 == 1: 
# 		return a[len(a)//2]
# 	else: 
# 		upper = (a[len(a)//2])
# 		lower = (a[len(a)//2 - 1])
# 		return (upper + lower) / 2


# print(median([5,3,4,2,1,7]))

# import copy 

# def median2(b): 
# 	a = copy.copy(b)			# non-destructive 
# 	for i in range(0, len(a) - 1): 
# 		for j in range(i + 1, len(a)): 
# 			if a[i] > a[j]: 
# 				a[i], a[j] = a[j], a[i]
	
# 	if len(a) % 2 == 1: 			# odd num of elements 
# 		return a[len(a)//2]
# 	else: 							# even --> average 
# 		upper = (a[len(a)//2])
# 		lower = (a[len(a)//2 - 1])
# 		return (upper + lower) / 2

# print(median2([6,1,2,4,3,5]))


# def removeRepeat(L): 
# 	newList = []
# 	for i in range(0, len(L)): 
# 		if L.count(L[i]) == 1 and L[i] not in newList: 
# 			newList.append(L[i])
# 	print(newList)


# print(removeRepeat([1,2,4,4,2,9,76,2,1,1,45]))

# def removeRepeat(L): 
# 	for i in range(len(L) - 1, -1, -1): 
# 		if L.count(L[i]) > 1: 
# 			L.pop(i)
# 	return L 

# print(removeRepeat([1,2,4,4,2,9,76,2,1,1,45]))



### 2D Lists ### 

# L = [ 1,2,3, True, 4,5, "apple"]
# t = (1,2,3,4,5)

# print(type(t), type(L))

a = [ [ 2, 3, 4 ] , [ 5, 6, 7 ] ]
# print(a)
# print(len(a))
# print(type(a))

# print(a[0][0])

# lPiece = [[True, False, False], [True, True, True]]


import copy

# # Create a 2d list
# a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]

# # Try to copy it
# b = copy.deepcopy(a) # Correct!

# # At first, things seem ok
# print("At first...")
# print("   a =", a)
# print("   b =", b)

# # Now modify a[0][0]
# a[0][0] = 9
# print("And after a[0][0] = 9")
# print("   a =", a)
# print("   b =", b)


## Sets ## 
# s = set([2,3,5])
# print(s)
# print(3 in s)          # prints True
# print(4 in s)          # prints False
# for x in range(7):
#     if (x not in s):
#         print(x)       # prints 0 1 4 6

# s = set()
# print(s)     # prints set()

# s = set(["cat", "cow", "dog"])
# print(s)     # prints {'cow', 'dog', 'cat'}

# s = { 2, 3, 5 }
# print(s)    # prints { 2, 3, 5 }

## Difference set vs. list 
#1. sets are unordered 
s = set([2,4,8])
print(s)          # prints {8, 2, 4} in standard Python 
for element in s: # prints 8, 2, 4
    print(element)

# 2. no duplicates 
s = set([2,2,2])
print(s)          # prints {2}
print(len(s))     # prints 1

## Sets are Very Efficient ## 


import time
n = 1000

# 1. Create a list [2,4,6,...,n] then check for membership
# among [1,2,3,...,n] in that list.

# don't count the list creation in the timing
a = list(range(2,n+1,2))

print("Using a list... ", end="")
start = time.time()
count = 0
for x in range(n+1):
    if x in a:
        count += 1
end = time.time()
elapsed1 = end - start
print("count=", count," and time = %0.4f seconds" % elapsed1)

# 2. Repeat, using a set
print("Using a set.... ", end="")
start = time.time()
s = set(a)
count = 0
for x in range(n+1):
    if x in s:
        count += 1
end = time.time()
elapsed2 = end - start
print("count=", count," and time = %0.4f seconds" % elapsed2)
print("With n=%d, sets ran about %0.1f times faster than lists!" %
      (n, elapsed1/elapsed2))




