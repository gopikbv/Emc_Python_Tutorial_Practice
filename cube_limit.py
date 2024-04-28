limit=int(input("Enter limit:"))
cube=0
for i in range(1,limit+1):
    cube=i*i*i
    print("Number is:"+str(i)+"and Cube of the"+str(i)+"is:",cube)
