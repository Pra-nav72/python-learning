#pattern printing
"""
Input= Integer (n)
Boolean= True or False
if True n=4
*
**
***
****

if False n
*****
***
**
*
"""



print("pattern printing")
num= int(input("how many rows you wanna print: "))
print("enter 0 or 1")
bool= input("1 for increasing order or o for decreasing order: ")
if bool=="1":
    for int in range(0,num+1):
        print("*"* int)

if bool=="0":
    for int in range(num,0,-1):
        print("*"* int)





