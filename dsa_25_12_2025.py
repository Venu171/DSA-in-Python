#=======================# 1. Sum of natural numbers========================================

def sum_of_natural_numbers(n):
    return (n*(n+1))//2
print(sum_of_natural_numbers(10))#55

#=======================# 2. Count Digits==================================================

def count_digits(n):
    count=0
    while n>0:
        n//=10
        count+=1
    return count
count_digits(123)#3

#========================# 3. Palindrome Number============================================
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

#=======================# 4. Factorial Of Number===========================================

def factorial_of_number(n):
    """
    n!=n*(n-1)*(n-2)*-----*1
    """
    factorial_res=1# since 0!=1
    for i in range(n,1,-1):
        factorial_res*=i
    return factorial_res
print(factorial_of_number(5))

#========================# 5. Trailing zeros in a factorial==============================

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

#=========================# 6. GCD or HCF of two numbers==================================
# Optimized Euclidian method
def gcd(a, b):
    # Everything divides 0
    if a == 0:
        return b
    if b == 0:
        return a

    # Base case
    if a == b:
        return a

    # a is greater
    if a > b:
        if a % b == 0:
            return b
        return gcd(a - b, b)
    if b % a == 0:
        return a
    return gcd(a, b - a)

# Driver code
a = 98
b = 56
print(f"GCD of {a} and {b} is {gcd(a, b)}")# 14
#======= LCM Of Two Numbers========================================
# GCD and HCF of two numbers
# Efficient

def gcd(a,b):
    
    if b == 0 :
        return a
    return gcd(b, a % b)
    
def lcm(a,b) :
    return a * b // gcd(a,b)

a = 12
b = 15
print(lcm(a,b))#60

#=============================Check for prime======================
# Efficient

def isprime(n) :
    if n == 1 :
        return False
        
    if n == 2 or n == 3 :
        return True
        
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    i = 5
    while (i * i <= n) :
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True
    

n = 7
print(isprime(n))
#=====================Prime Factorization======================
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(n):
    for i in range(2, n + 1):
        if is_prime(i):
            while n % i == 0:
                print(i, end=' ')
                n //= i
prime_factors(100)#2 2 5 5
#========================Check Whether string Is palindrome Or Not==========================
def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]

print(is_palindrome("A man a plan a canal Panama"))#True
print(is_palindrome("Hello"))#False
#=============================Square of side 'N'========================================================
"""
Problem Description: You are given an integer n. 
Your task is to return a square pattern of size n x n made up of the character '*', 
represented as a list of strings.
""""
def square_of_side(n):
    res_arr=[]
    for i in range(1,n+1):
        res_arr.append("*"*n)
    return res_arr
square_of_side(4)#['****', '****', '****', '****']
#======================Hollow Square of side 'N'========================================
"""
You are given an integer n. 
Your task is to return a hollow square pattern of size n x n made up of the character '*', 
represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' 
in the middle (except for side lengths of 1 and 2).
"""
def hollow_square_of_side_n(n):
    res_arr=[]
    for i in range(1,n+1):
        if i==1 or i==n:
            res_arr.append("*"*n)
        else:
            string="*"+" "*int(n-2)+"*"
            res_arr.append(string)
    return res_arr
print(hollow_square_of_side_n(3))#['***', '* *', '***']
#======================Rectangle Pattern==================================
"""
You are given two integers, n and m. 
Your task is to return a rectangle pattern of '*', 
where n represents the number of rows (length) and 
m represents the number of columns (breadth).
"""
def rectangle_pattern(n,m):
    res_arr=[]
    for i in range(n):
        res_arr.append("*"*m)
    return res_arr
print(rectangle_pattern(4,5))#['*****', '*****', '*****', '*****']
#==============================Right Angled Triangle============================
"""
You are given an integer n. 
Your task is to return a right-angled triangle pattern of '*'
where each side has n characters, represented as a list of strings. 
The triangle has '*' characters, starting with 1 star in the first row, 
2 stars in the second row, and so on until the last row has n stars.
"""
def right_angled_triangle(n):
    res_arr=[]
    for i in range(1,n+1):
        res_arr.append("*"*i)
    return res_arr
print(right_angled_triangle(5))#['*', '**', '***', '****', '*****']
#======================================Inverted Right Angled Triangle====================================
"""
You are given an integer n. 
Your task is to return an inverted right-angled triangle pattern of '*' 
where each side has n characters, represented as a list of strings. 
The first row should have n stars, the second row n-1 stars, and so on, 
until the last row has 1 star.
"""
def inverted_right_angled_triangle(n):
    res_arr=[]
    for i in range(n,0,-1):
        res_arr.append("*"*i)
    return res_arr
print(inverted_right_angled_triangle(5))#['*****', '****', '***', '**', '*']
#======================================Pyramid Pattern======================
"""
Problem Description:
You are given an integer n. 
Your task is to return a pyramid pattern of '*' where each side has n rows, 
represented as a list of strings. The pyramid is centered, with 1 star in the first row, 
3 stars in the second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.
"""
def pyramid_pattern(n):
    formula=2*n-1
    res_arr=[]
    for i in range(1,n+1):
        res_string="*"*(2*i-1)
        res_arr.append(res_string.center(formula))
    return res_arr
print(pyramid_pattern(5))#['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']
#======================================Inverted Pyramid Pattern======================
"""
You are given an integer n. 
Your task is to return an inverted pyramid pattern of '*', 
where each side has n rows, represented as a list of strings. 
The first row has 2n - 1 stars, the second row has 2n - 3 stars, and so on, 
until the last row has 1 star, with each row centered using spaces.
"""
def inverted_pyramid_pattern(n):
    formula=2*n-1
    res_arr=[]
    for i in range(n,0,-1):
        res_string="*"*(2*i-1)
        res_arr.append(res_string.center(formula))
    return res_arr
print(inverted_pyramid_pattern(3))#['*****', ' *** ', '  *  ']
#===================================Right Angled Triangle with Numbers============================
"""
Problem Description:
You are given an integer n. 
Your task is to return a right-angled triangle pattern 
where each row contains repeated digits. 
The first row contains the number 1 repeated once, 
the second row contains the number 2 repeated twice, 
and so on until the nth row contains the number n repeated n times.
"""
def right_angled_triangle_numbers(n):
    res_arr=[]
    for i in range(1,n+1):
        res_string=f"{i}"*i
        res_arr.append(res_string)
    return res_arr
print(right_angled_triangle_numbers(5))#['1', '22', '333', '4444', '55555']
#=====================================Floyds Triangle================================
"""
Problem Description:
You are given an integer n. 
Your task is to return the first n rows of Floyd’s Triangle, 
represented as a list of strings. 
Floyd's Triangle is a triangular array of natural numbers 
where the first row contains 1, the second row contains 2 and 3, 
the third row contains 4, 5, and 6, and so on.
"""
def floyd_triangle(n):
    res_arr=[]
    current_num=1
    for i in range(1,n+1):
        res_string=""
        for j in range(current_num,current_num+i):
            if j==current_num+i-1:
                res_string+=f"{j}"+''
                current_num=j+1
            else:
                res_string+=f"{j}"+' '
        res_arr.append(res_string)
    return res_arr
print(floyd_triangle(3))#['1', '2 3', '4 5 6']
#================================Diamond Pattern========================================
"""
Problem Description:
You are given an integer n. 
Your task is to return a diamond pattern of '*' 
with n rows for the upper part (the widest row will have 2n - 1 stars), 
and the lower part is the mirrored version of the upper part. 
Each row should be centered with appropriate spaces.
"""
