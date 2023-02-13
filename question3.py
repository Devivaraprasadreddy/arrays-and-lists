# Question 3 : 
# Write a program to find the element with the highest frequency in the list.



# Sample_input :[1,2,4,3,2,4,2,5,7,2]



# Sample_output :2

def find_mode(lst):
    max_count = 0
    mode = None
    for item in lst:
        count = lst.count(item)
        if count > max_count:
            max_count = count
            mode = item
    return mode

lst = list(map(int,input("Enter the list elements separated by space: ").split()))
mode = find_mode(lst)
print("Element with highest frequency:", mode)