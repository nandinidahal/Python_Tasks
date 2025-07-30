#Find the longest word in a list of strings
subject = ["math", "science", "occupation", "english"] 

longest_word_subject = ""# empty string  first with 0 len

for word in subject:
    if len(word) > len(longest_word_subject):
        longest_word_subject = word

print("The longest word is:", longest_word_subject)

'''
subject = ["math", "science", "occupation", "english"]  

l = max(subject, key=len)  # len(math) =4
print(l)
'''

