# basic syntax to read a file is --
f = open("pranav.txt","r")   #we make a file pointer which starts with open//////"r" is the second argument which default, use to read
                                #if i write "rb" ---it will read it as a binary string.
content = f.read()       # fuction to read the file.
print(content)

f.close()           # if a file opened it must be closed.




#################################################################
print("2nd output\n")

g = open("pranav.txt","rt")
cnt= g.read(3)    # here (3) means the 3 character shown only.if you write e.g. g.read(33334323) but there is not this much character in file so, it will print all the character only one time .
print(cnt)

cnt= g.read(3)
print(cnt)
g.close()





########################################################
print("3rd output\n")
# to read content line by line we have to itrate the file text..
f = open("pranav.txt","r")
content = f.read()
for line in content:             #it will print single letter in one line to write a line in one line we have to write variable- f instead of content
    print(line)
f.close()





    ######################
print("4th output ")
f = open("pranav.txt","r")
#content = f.read()
for line in f:
    print(line, end="\n")   # it means new line character do not create another line , it is a default value.
f.close()

    # never write content = f.read() , always write for line f:







#####################################################
print("5th output \n")


f = open("pranav.txt","r")
print(f.readline())      #this will only print first line
print(f.readline())      #this will only print second line  and so on.....
f.close()
###################################





print("6th output \n")

f = open("pranav.txt","r")
print(f.readlines())         #this will make a list of the content written
f.close()

