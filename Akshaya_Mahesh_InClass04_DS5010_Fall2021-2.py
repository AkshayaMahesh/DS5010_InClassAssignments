
print('Part A')
# Function to find the factorial of a number
def my_factorial(n):
    if n==0 or n==1:
        return 1
    else:
     return n*my_factorial(n-1)
# Prompting user for input
k= int(input('Enter a number : '))
# Factorial Function Called
my_factorial(k)
print('The factorial of the number is: ',my_factorial(k))
print('\n')

print('Part B')
# Function to find the kth Fibonacci Number
def my_fibonacci(k):
    if (k==0 or k==1):
        return 1
    else:
        return my_fibonacci(k-1)+my_fibonacci(k-2)
# Prompting user for input
kth_fib=int(input('Enter a number : '))
# Function Called
my_fibonacci(kth_fib)
print('the fib no. is',my_fibonacci(kth_fib))
print('\n')

print('Part C')
#Function to find factorial and Fibonacci of the given two integers
def test_assignment(n,k):
    while n < 0 or k < 0:
        n = int(input('n must be non negative number,enter n: '))
        k= int(input('k must be non negative integer, enter k: '))

    a= my_factorial(n)
    b=my_fibonacci(k)
    print(str(n)+'! = '+str(a))
    print('F('+str(k)+') ='+str(b))
# Prompting user for input
a = int(input('Enter n:'))
# Prompting user for input
b= int(input('Enter k: '))
# Calling the function
test_assignment(a,b)


