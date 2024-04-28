a=[]
avg=0
sum=0
num=0
for i in range(1,11):
    num=int(input("Enter num"+" "+str(i)+":"))
    a.append(num)
for j in a:
    sum=sum+j
    avg=sum/j
print(sum)
print(avg)