n = int(input("Enter the number of student:"))
students = []
for i in range(n):
    s = {'name': input("student's name:".format(i+1)),
         'roll': int(input("Student's roll:".format(i+1))),
         'marks': int(input("student's marks:".format(i+1)))
         }
    students.append(s)
print("{:<20} {:<10} {:10}".format("name", "roll", "marks"))
for s in students:
    print("{:<20} {:<10} {:}".format(s['name'], s['roll'], s['marks']))

