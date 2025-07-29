#Count how many times each element appears in a list
number=[1,2,3,5,3,'apple', 'banana','apple']
counts = {}
for value in number:
    if value in counts:
        counts[value] += 1  
    else:
        counts[value] = 1  

print("the num of count are :",counts)

















'''
result=number.count(1)
print("the number of time for 1 is:",result)
result2=number.count(3)
print("number of time for 3 is:",result2)
'''
'''
for num in number:
    counts[num] = number.count(num)

print(counts)
'''
