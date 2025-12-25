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

