#Ask for 5 students name , append to list and then display afterwards
students= []
for i in range(5):
    name=input("enter name:")
    address=input("enter address:")
    student = {"name": name, "address": address}
    students.append(student)
print("\nList of students:")
for s in students:
    print(s)