list1= ["pranav", "piyush", "shanu", "mohit", "rohit"]

for item in list1:     #when we use this sentence then a loop get 						run that print every item from the list 							whether its 1 or 1lakh item in it.
	print(item)





list2= [["pranav",2],["piyush",4],["shanu",5],
       ["mohit",3], ["rohit",33]]   #this is list of list.

for item, number in list2:
	print(item,"is number", number)

dict= dict(list2)    #we have change the list into dictionary.
print(dict)




# using dict.item() function to print the same as in line 13


for item, number in dict.items():
	print(item,"is number", number)

for item in dict:
	print(item)  #it will print only the items from the dictionary.
	
	
	
	
					#QUIZ


# Q. make a list and using a loop print the number that is greater than 6 from the list.



list0= [float, "ram", 4,23, "pranav", "kumar", 55, 65, 32, 6,         100, "mohan", 1, 0]
for item in list0:
	if str(item).isnumeric() and item>6:
		print(item)
		
		
		#we use str(item) to change all the element to string, .             isnumeric() to convert into integer if eligible.