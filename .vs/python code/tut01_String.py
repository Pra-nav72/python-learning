n = int(input("Enter a number "))
f = 0
f2 = 1
f3 = None
print(f, f2, end=" ")
for x in range(n):
    f3 = f + f2
    print(f3, end=" ")
    f = f2
    f2 = f3
