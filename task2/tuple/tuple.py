#Create a tuple with 5 numbers.
numbers = (20, 40, 60, 80, 100,80)
print("original tuple:",numbers)

#Access the 2nd and 4th elements from a tuple. 
second_element = numbers[1]   # index 1 → 2nd element
fourth_element = numbers[3]   # index 3 → 4th element
print("Second element:", second_element)
print("Fourth element:", fourth_element)

#Count how many times a number appears in a tuple.
r=numbers.count(80)
r2=numbers.count(100)
print("80 appears", r, "times.")
print("80 appears", r2, "times.")

#Find the index of an element in a tuple.
i=numbers.index(80)
i2=numbers.index(100)
print("index of 80 is =", i)
print("index of 100 is =", i2)
