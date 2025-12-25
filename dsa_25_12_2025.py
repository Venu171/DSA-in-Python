=======================# 1. Sum of natural numbers========================================

def sum_of_natural_numbers(n):
    return (n*(n+1))//2
print(sum_of_natural_numbers(10))#55

=======================# 2. Count Digits==================================================

def count_digits(n):
    count=0
    while n>0:
        n//=10
        count+=1
    return count
count_digits(123)#3

========================# 3. Palindrome Number============================================
"""
Approach 1:
Here, we are usig the below approach to solve the problem
`reverse*10 + temp%10`.
Approach 2:
convert the number to streng and then reverse it to compare with original number
"""
def is_palindrome_number(n):
    temp=n
    reverse=0
    while temp!=0:
        reverse=reverse*10+temp%10
        temp=temp//10
    return reverse==n
print(is_palindrome_number(121))#True

=======================# 4. Factorial Of Number===========================================

def factorial_of_number(n):
    """
    n!=n*(n-1)*(n-2)*-----*1
    """
    factorial_res=1# since 0!=1
    for i in range(n,1,-1):
        factorial_res*=i
    return factorial_res
print(factorial_of_number(5))

========================# 5. Trailing zeros in a factorial==============================

def trailing_zeros_in_factorial(n):
    """
    trailing_zeros_in_factorial=n/5+n/25+n/125+-------
    """
    count=0
    i=5
    while n//i>=1:
        count+=n//i
        i*=5
    return count
print(find_trailing_zeros(100))#24

=========================# 6. GCD or HCF of two numbers==================================

