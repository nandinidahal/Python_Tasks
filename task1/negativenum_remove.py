#Remove all negative numbers from a list
numbers=[1,2,3,4,-9,5,7,-1,-2,6]
new_num=[]
for num in numbers:
    if num>=0:
        new_num.append(num)
print(new_num)
