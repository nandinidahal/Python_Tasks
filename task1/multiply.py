#Multiply all numbers in a list
number=[1,2,3]
product=1
for num in number:
    product*=num
if(product==0):
    print("the product is 0")
else:
    print("the product is ",product)
