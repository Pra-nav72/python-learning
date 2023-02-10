"""
var1= 6
var2= 56

var3= int(input())

if var3>var2:
	print("greater")
elif var3==var2:          
	print("equal")
else:
	print("lesser")

"""
	
	
							#we can also use else in line 8 but let assume there is hundreds of else statement here then if we use else instead of elif it will continuosly checking all the statement(which is waste of time) even if its already  find the true statement.
							

list1= [1,2,3,4,5]
if 5 in list1:    #'in' is a function which means if that element 					is in list 
	print("yes, it is in list.")
if 44 not in list1:				 #'not in' is a function which 					means if that element is not in list.
	print("no, its not in list.")
	
	
	
	#QUIZ

print ("what is your age?")
m= int(input())
if m>18:
	print("you are eligible for driving.")
elif m==18:
	print("you have to register yourself for driving.")
else:
	print("you are not eligible for driving.")
print("thank you")
