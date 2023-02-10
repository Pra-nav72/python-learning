f= open("pranav.txt")
#print(f.tell())
print(f.readline()) #this will read first line from the file
#print(f.tell()) #if we want to find the file pointer/curser(now of character printed in a line ) after reading the line .
f.seek(10)    #we use to move file pointer to(10) it will start from the 11th character  ....f.seek(0) is used to reset file pointer, it will retype the first line
print(f.readline())
#print(f.tell())
f.close()
                                #ALWAYS CLOSE THE OPEN FILE.............:)♦