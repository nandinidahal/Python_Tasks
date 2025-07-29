#Find the common elements between two lists
num1=[1,2,3,4,5]
num2=[2,4,6,8]
common_result=list(set(num1) & set(num2))
print("the common element are :\n",common_result)
