
original_string = input('Enter the string: ')
count = 0
new_string = original_string.lower()
result = '' # This will hold the string with vowels removed

for char in new_string:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1 
    else:
        result += char  # Add non-vowel to result

if count == 0:
    print('No vowels found')
else:
    print(f'Total vowels are: {count}')
    #print(f'String after removing vowels: {result}')
    print("Text without vowels:", result)











    ''''
vowel_string ="RadhaKrishna"
#vowel = "aeiouAEIOU"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""#empty string to store the result

for char in vowel_string:
    if char not in vowels:
        result = result + char

print("\nAfter removing Vowels: ", result)
'''
