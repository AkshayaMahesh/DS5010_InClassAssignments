#Question 1
#Function to find the largest integer in list
def my_max(in_list=[]):
    max_value=in_list[0]
    for ele in in_list:
        if (ele>max_value):
            max_value=ele
    return max_value
# Question 2
# Function to find if a number is a power of 2 or not
def power2(num):
    if num==0:
        return False
    while (num!=1):
        if (num %2 !=0):
            return False
        num=num//2
    return True
# Question 3
# Calling the functions and printing outputs
print("Question 1 output:")
k=my_max([21, 5, -3, 47, 14, 4])
print("The maximum number in the list is",k)
print("Question 2 output:")
num=int(input("Enter a number:"))
l=power2(num)
print(l)
