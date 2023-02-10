L1= "my name is pranav kumar"
print(L1)
print(len(L1))   #this len() function is used to find total length of the line.
#if you want to show only few character from the above line . then you have to write -
print(L1[0:5]) #it select only first five character i.e. my na.
#here 0=m, 1=y, 2=_ , 3= n, 4=a.............22=r.
print(L1[6])  #[6] means only 6th character starting from 0.

#however if you write print(L1[66]).......it will show an error becuz the above line has only 23 character but if you write print(L1[0:66]) or print(L1[0:]) , then it will show full length of line.
#if you print(L1[:5]), it will automatically take 0 at begining. if you write print(L1[0::5])
print(L1[0:66])


print(L1[0:7:2])  #here :2 represent that it willl gap the second words after each count.
print(L1[::]) #it means print (L1[0:23:1]), if  you remove any integer it will print same.
print(L1[::5])  #it misses 4 character after each alphabet.


""" 0    1    2  3   4  5  6   7  8   9 10
     p    r    a  n   a  v  k   u  m  a  r
   -11  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1       
   print (L1[0:5]) is same as print(L1[-12:-6])
   """
print(L1[-12:-6]) #here -12 is excluded and -6 is included.
print(L1[::-1]) # it will reverse the line.



								#FUNCTION


print (L1.endswith("kumar"))  #it is boolean function to find if the line ends with kumar.
print(L1.count("a"))   #it how many times 'a' come in the sentences.
print (L1.capitalize())  #it capital the first letter of the sentences.
print (L1.upper())  #it makes capital all the letter.
print (L1.lower())  #it makes all the letter in lower case.
print(L1.replace("is", "are"))  #it replace the word 'is' with 'are'.


#google 'string function ' to find out more function.