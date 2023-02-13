# Question 4:
# Write a program to check whether a String is a palindrome or not.



# Note: A Palindrome String is a string that is the same as the reverse.



# Example: LOL, MADAM.

str = input("Enter a String : ")
res = ""
for i in str:
    res = i + res
if(str == res):
    print("Palindrome Number!")
else:
    print("Not a Palindrome Number!")        