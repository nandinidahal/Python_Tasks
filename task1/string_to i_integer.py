#Convert list of strings to integers
#string=["2","3","5"]
string=["2","3","5","a"]
new_string = filter(str.isdigit, string)# only num can be converted into int not character
result=list(map(int, new_string))
#result=list(map(int, string))
print(result)