#Remove all negative numbers from a list
numbers=[1,2,3,4,5,6,-1,-2]
positive_numbers = []
for num in numbers:
    if num>=0:
        positive_numbers.append(num)

print("List without negative numbers:", positive_numbers)