a=[1,2,3,4,5]
b=[30,40,50,60]
print(a)
print(b)
a.append(10)  #append() will add the element into the last index in the list
a.append(20)
print(a)  
a.extend(b)   #extend() helps to merge a list into another list
print(a)
a.pop()   #pop() delet the element in the  last index of the list if the index is not mentioned
print(a)
a.pop(9)
print(a)
#direct element assignment using list index
a[0]=100
print(a)
#element assignment using insert()
a.insert(0,"EMC")  #1st argument as index , 2nd argument as data to insert
print(a)