"""f = open("pranav2.txt", "w")                # there is already a file called pranav.txt so it will change its content otherwise it will create a new file a wrote in it.
f.write("pranav bahut achha insann hai")
f.close()"""

"""
# to add any text in file we use append "a" function
f= open("pranav2.txt", "a")
a = f.write("aur btao kya chal rha hai zindagi mein\n")
print(a)#it will continuosly adding after every run
f.close()               #if we want a return value i.e. how many character did this print then we use f.write as a variable(above..a= ...)


f= open("pranav.txt", "w")                #since we wrote here w that's why it will erase all data to write something new
a = f.write("aur btao kya chal rha hai zindagi mein\n")
print(a)
f.close()
"""


#Handle read and write both
f= open("pranav2.txt", "r+")
print(f.read())  #this will print read the file content
f.write("thank you") #this will write thank you in the file but not show in output
