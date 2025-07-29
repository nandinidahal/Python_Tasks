#Q. Count vowels in a string
original_string = input('Enter the string :')
count = 0
new_string = original_string.lower()
for char in new_string:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u': #'aeiou'

        count+=1

if count == 0:
    print('No vowels found')
else:
    #print('Total vowels are :' + str(count))
    print(f'Total vowels are: {count}')



'''
vowel_string ="RadhaKrishna"
vowel = "aeiouAEIOU"

'''