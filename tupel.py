a=(1,2,3,4,5)
print(a)
#Tuples cannot be modified like list
#a[0]=100
#print(a)
#Tuples can be converted to list for modification
b=list(a)
print(b)
print(type(a))
print(type(b))
b.pop()
print(a)
print(b)