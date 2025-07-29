#Sum of all integers in a list

number=[1,2,3]
sum=0
for num in number:
    sum += num

if (sum==0):
    print("no sum")
else:
    print("the sum is:", sum)

'''
# user defined
n=int(input("how many number you want to add:"))
number=[]
for i in range(n):
    number_add=int(input("enter number:"))
    number.append(number_add)  # Add the number to the list
sum=0
for num_add in number:
    sum+=num_add
if (sum==0):
    print("no sum")
else:
    print("the sum is:", sum)
    
    '''
    
    