#Check if a string is a palindrome

#num = 1221
num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10 # floor division operator i.e discards decimal or fractional part.
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")
