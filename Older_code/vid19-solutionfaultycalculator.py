#design a faulty calculator,43*3=777, 56+9 =77, 56/6= 4.


print("choose the operater","+","-","/","*")
print("enter operator")
op= input()

print("enter first number")
num1= int(input())

print("enter second number")
num2= int(input())

if op=='*'  and num1==43 and num2==3:
	print("your answer is", 777)  
elif op=='+' and num1==56 and num2==9:
	print("your answer is",77)
elif op=='/' and num1==56 and num2==6:
	print("your answer is",4)
elif op=='+':
	N=num1+num2
	print("your answer is",N)
elif op=='-':
	AN=num1-num2
	print("your answer is",AN)
elif op=='*':
	nN=num1*num2
	print("your answer is",nN)
elif op=='/':
	Nn=num1/num2
	print("your answer is",int(Nn))
	
else:
	print("error! invalid input :(")
	
	
