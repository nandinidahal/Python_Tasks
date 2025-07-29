#Find the maximum value in a list
number=[1,2,3]
maximum_num=number[0]# num 0 is connsidered as max at first
for num in number:
    if num > maximum_num:
        maximum_num=num
print("The maximum number is:", maximum_num)

# using function
'''
list_num=[1,2,3,4,5]
result=max(list_num)
print("maximum list using function :",result)
'''