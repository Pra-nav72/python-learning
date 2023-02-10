import turtle
t= turtle.Turtle()
s= turtle.screen()
s.bgcolor('black')
t.pencolor('red')
t.speed(0)

for i in range (150):
	t.circle (190-i,90)
	t.lt(90)
	t.circle (190-i,90)
	t.lt(18)  
	
	
	#there is a error showing in line 3 i.e. 						Traceback (most recent call last):
					#  File "/data/user/0/ru.iiec.pydroid3/files/					temp_iiec_codefile.py", line 3, in <module>
 					#   s= turtle.screen()
					#AttributeError: module 'turtle' has no 							attribute 'screen'