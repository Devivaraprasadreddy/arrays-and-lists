# Question 1:
# Write a program to rotate a given array by N steps in the clockwise direction

# Sample input one

# Array:- 3,1,2,5,7

# N:- 2

# Sample output one

#  5,7,3,1,2

# Sample input Two

# Array:- 1,2,3,4,5

# N:- 1

# Sample output two

#  5,1,2,3,4




Array = list(map(int,input("Enter an Array Elements : ").split()))
N = int(input("Enter a number : "))
Array_rotated = Array[-N:] + Array[:-N]
print("Rotated Arrayay:", Array_rotated)