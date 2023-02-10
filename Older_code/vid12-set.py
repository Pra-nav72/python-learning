s = set()
#l = [1,2,3,4]  				 #this a list
#s_from_list = set(l)		  #now this is a set.
#print(s_from_list)
#print(type(s_from_list))	  #here you can see the class is SET.

s.add(1)  #to add any element, to remove type  s.remove(1).
s.add(2)

t= s.intersection({1,2,3})
print(s, t)

tt = s.union({1,2})
print(s,tt, t)


#some function below
print(len(s))  #to print length of s.
print(min(s))  #to find minimum value.
print(max(s))  #to find maximum value.

				# TO KNOW MORE ABOUT SET READ CLASS 11 AND 12 MATHS.