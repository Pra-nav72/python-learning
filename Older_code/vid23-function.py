#a = 3
#b = 35
#c = sum((a,b))
#print(c)                  #this simple function will add the value of a and b.

                        #types of function
                        # 1. builtin function - like sum(above) , divided.
                        # 2. user difined function - which is defined by the users, we use def keyboard here
def funct1():
    print("hi this is user defined function")
print(funct1())     # output will show none becoz of print() function. if we don't use print none will dissapear.
# if you want to write this even 10x, just write funct1() 10x.



funct1()
 # it also take input for example ...
def fuct(a, b):
    print("hello you are in function ", a+b)
fuct(5, 7)    #here this fuction add a and b as 5 and 7.  but this is not a well organised function.

                    #THESE FUNCTION DID'NT RETURN ANYTHING
def function2(a, b):
    """This is a function which will calculate average of two numbers
    This number doesn't work with three digit."""     #this is called doc string (f irst string written under any function )
    average = (a+b)/2
    return average
#v = function2(5, 2)
#print(v)            #here output wil not show any none becoz function (5, 2) is used as variable. it takes some input and return it after processing.
print(function2.__doc__)   #this will print the doc string......THIS IS GOING TO HELP IN FUTURE A LOT..

