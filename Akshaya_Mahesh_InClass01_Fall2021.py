#Question 1

print("1.a) Python Lists are mutable")
print("1.b) Python Tuples are immutable")
print("1.c) Python Dictionaries are mutable and immutable")
print("1.d) Python Strings are immutable")

# Question 2
print("2.a) No error  because list is mutable")
print("2.b) Error  because String object is immutable and does not support item assignment")
print("2.c) Error because String object is immutable and does not support item assignment")
print("2.d) No Error because the key value pair gets deleted when 'del' is used and prints the remaining dictionary items")

#Question 3
start_point = int(input("Enter the start point: "))
end_point = int(input("Enter the end point: "))
diff = start_point - end_point
for i in range(start_point,end_point,2):
    k =(i**2)
    print('The alternating elements are:',k)






