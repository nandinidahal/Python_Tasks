#Remove duplicates from a list
integers_num=[1,2,2,1,3,4]
#1 method using set
# but here  original order of the list is not guarantee
result=list(set(integers_num))
print("using set",result)
#2 using dictonary
# maintain order and convert it back to a list.
result2=list(dict.fromkeys(integers_num))
print("using dict",result2)