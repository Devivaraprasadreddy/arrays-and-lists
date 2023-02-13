# Question 2 : 
# Write a program to print duplicate elements of a list.



# Sample_input : [1,1,2,3,3,4,5,6,6]



# Sample_ouptut : 1,3,6

lst = list(map(int,input("Enter an Elements : ").split()))

duplicates = list(set([x for x in lst if lst.count(x) > 1]))
print("Duplicate elements:", duplicates)