# dictionary is nothing but a key value pair. 
# it's element is written under this bracket "{}".
d1= {}  #it won't print anything bcoz its empty.
print(d1)
#OUTPUT 01
   

d2= {"pranav":"burger", "piyush":"chicken", "ram":"roti",
 "mohan":{"b":"boiled egg", "l":"rice", "d":"roti"}} # here mohan 						is an another dictionary in the dictionary.
print(d2)  # it will print whole dictionary.
#OUTPUT 02


print(d2["pranav"]) # it will show the word associated with the 	#OUTPUT 03						word "pranav".
		
	

print(d2["mohan"]) # it will print all the element of mohan 		#OUTPUT 04						dictionary.

  

print(d2["mohan"]["b"])  # it will print the specific value of "b" #OUTPUT 05							from the dictionary mohan.

d2["ankit"]= "soup"  # to add any key value further, you can also 					change the keyword from "ankit" to whatever.
print(d2)	  # Or you can use .function here --- d2.				#OUTPUT 06			update({"ankit":"soup"}) to add any function.


del d2["ankit"]  #to delete any key value.
print (d2)
#OUTPUT 07

print(d2.keys())  #to find all the keys i.e., pranav, piyush, mohan #OUTPUT 08					etc
# key can be a list, dictionary(mohan, b, l...etc) or a tupple but key value should must be a STRING(burger, rice, roti...etc) OR NUMBER.
