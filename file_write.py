# w ->overwrite the content in the file
# a -> add the new content with the existing content
# r+ -> both read and write can be done
#f=open("fruits.txt","w")
f=open("fruits.txt","a")
f.write("\nHi\n")
f.write("Bye")
f.close()

f=open("fruits.txt","r+")
print(f.read())
