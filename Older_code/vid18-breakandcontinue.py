i= 0

while(True):

		       
	print(i+1, end=" ")
	if (i==44):
		
		break
	i = i + 1	
#using while(True)or (1) will cotinue the loop.

#loop will stop(using break) when i=44, otherwise it will keep running.


#CONTINUE FUNCTION
p= 0
while(True):
	
	if p+1<5:
		p = p + 1
		continue
		
		
	print(p+1, end=" ")
	if (p==32):
		
		break
	p = p + 1
	

	# here continue function is used to not print the number less than 5 given condition is p=p+1, loop will not continue till the number p=p+1 is 5.
		#break- it is used to stop the loop. while CONTINUE is used leave the current titration in the loop i.e. it will forget everything written after the continue.
		
		
		
		#	QUIZ
		
#Q. take input till the number print is 100.

while(True):
	inp=int(input("write the number\n"))
	if inp>100:
		print("congrats! your answer is right.\n")
		break
	
	else:
		print("try again!!\n")
		continue