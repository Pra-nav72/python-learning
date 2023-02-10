grocery= ["tomato", "ketchup", "lollypop", "deo", 77, "sprite", "lays"]
print(grocery)
print(grocery[3]) #[3] means the third element from the list.


number = [1, 23, 35, 15, 56, 28]
number.sort()   #it arrange the numbers in ascending order.
number.reverse()   #it arrange the numbers in descending order.
print(number)



						#LIST SLICING......
print(number[0:6])  #it will slice all the numbers from 0-6. [:], [:5] will print the same thing. Slicing print the new list.
print(number[::]) #it is called extends slicing. third column automatically takes the number '1'.
print(number[::2])  #it will leave the second letter after each and create a new list. you can use '-1' in place of '2' to reverse the list. you should not take -2, -3,... etc bcoz it shows nothing on the input.



  # print(max(number)) ---to find the maximum numbers in the list.
  # print(min(number)) ---to find the minimum number in the list.
  # print(len(number)) ---to find the length of the list.


number.append(99)  #it is used to add any number at the end of the list.
number.insert(1,44)  #this used to add any number between the list. here '1' is the index i.e. place where you want to insert that number(0=1st place, 1= 2nd place, 2= 3rd place...so on) and '44' the number.
number.remove(23)  #this is used to remove any number.
number.pop()   #this will remove the last number.
print(number)


				# THERE 2 TYPES OF WORD
				#  1.MUTABLE(that can be changed)i.e LIST
				#  2. IMMUTABLE(that can't be changed)i.e TUPLE
# tuple have paranthesis() but list have square brackers[]. value of tuple can't be changed.

tp=(1,)  # you have to use comma ',' after element, if there is single element in tuple.
print(tp) 

a= 2 
b= 6
a,b= b,a  #if you want to change the value of a and b then use this simple thing only in python.
print(a,b)
				