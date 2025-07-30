#Merge two dictionaries into one.
#1.by using update
dic1 = {'str1': "hello", 'str2': 2}
dic2 = {'str2': "world!", 'str3': 4}

dic1.update(dic2)# update all the value of dic2 in dic 1
print(dic1)

#2. by using operator
d1 = {'A': 77, 'B': 79}
d2 = {'B': 78, 'D': 80}
d3 = d1 | d2#creates a new dictionary without modifying the original dictionary.
print(d3)

#3.Dictionary Unpacking (**)
dic1 = {'X': 4, 'Y': 2}
dic2 = {'X': 1, 'Z': 3}
dic4 = {**dic1, **dic2}#Dictionary unpacking allows us to merge dictionaries into a new one.
print(dic4)
