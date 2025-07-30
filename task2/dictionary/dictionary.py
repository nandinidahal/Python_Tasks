#1.Create a dictionary with 3 key-value pairs of student names and marks.
std_dic={
    "Radha":50, # keyi.e name and value i.e marks
    "Krishna":51,
    "ram":52
}
print("original dictionary:")
print( std_dic)

#2.Add a new key-value pair to an existing dictionary.
print("\nAfter adding a new std sita  to std_dic.")
std_dic["sita"] = 80  # Add new dict 
print(std_dic)

#3.Update the value of an existing key in a dictionary.
std_dic["Radha"] = 90
print("\nAfter updating marks of radha:")
print(std_dic)

#4.Delete a key from the dictionary.
del std_dic["ram"]
print("\nAfter deleting ram from dictionary:")
print(std_dic)

#5.Check if a key exists in the dictionary.
if "Krishna" in std_dic:
    print("\nKrishna is in the dictionary.")
    print("Marks:",std_dic["Krishna"])
else:
    print("\nKrishna is not in the dictionary.")

#Loop through all keys and values in a dictionary.
print("\nThe name and marks in dictonary are:")
for name, mark in std_dic.items():
    #print("{name}: {mark}")
    print(f"{name}: {mark}")

##Get the key with the highest value in a dictionary.
max_key = max(std_dic, key=std_dic.get)
print(f"\nHighest score std is : {max_key} with marks {std_dic[max_key]}")



