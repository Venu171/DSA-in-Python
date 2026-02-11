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
count_digits(1234)#4

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
#==============================All Divisors of a Number===========================
def printDivisors(n) :
	i = 1
	while i <= n :
		if (n % i==0) :
			print (i,end=" ")
		i = i + 1
		
# Driver method
print ("The divisors of 100 are: ")
printDivisors(100)
#The divisors of 100 are: 
#1 2 4 5 10 20 25 50 100
#================================Sieve of Eratosthenes==================================
def SieveOfEratosthenes(num):
	prime = [True for i in range(num+1)]
	p = 2
	while (p * p <= num):

		if (prime[p] == True):

			for i in range(p * p, num+1, p):
				prime[i] = False
		p += 1

	for p in range(2, num+1):
		if prime[p]:
			print(p)
SieveOfEratosthenes(20)
# 2 3 5 7 11 13 17 19
#================================Computing Power==================================
def power(x, y):
	temp = 0
	if(y == 0):
		return 1
	temp = power(x, int(y / 2))
	if (y % 2 == 0) :
	    return temp * temp
	else :
	    return x * temp * temp

print(power(2,3))
#================================Diamond Pattern========================================
"""
Problem Description:
You are given an integer n. 
Your task is to return a diamond pattern of '*' 
with n rows for the upper part (the widest row will have 2n - 1 stars), 
and the lower part is the mirrored version of the upper part. 
Each row should be centered with appropriate spaces.
"""
def generate_diamond(n):
    """
    Generates a diamond pattern of a given size (n) as a list of strings.
    The total height of the diamond will be 2*n - 1 lines.
    """
    diamond_lines = []
    # Create the sequence of row indices: 0 to n-1, then n-2 down to 0
    # For n=3, this sequence is [0, 1, 2, 1, 0]
    rows_indices = list(range(n)) + list(range(n - 2, -1, -1))

    for i in rows_indices:
        # Calculate number of spaces: decreases as i increases in the first half
        spaces = ' ' * (n - i - 1)
        # Calculate number of stars: increases by 2 in each step
        stars = '*' * (2 * i + 1)
        # Combine spaces and stars to form the line
        line = spaces + stars
        diamond_lines.append(line)

    return diamond_lines

# Example Usage:
size = 4
diamond = generate_diamond(size)

# The function returns the following list for size = 4:
# ['   *', '  ***', ' *****', '*******', ' *****', '  ***', '   *']
print("\nList representation:")
print(diamond)
#=============================Iterative Power (Binary Exponentiation)==================
def power(x,n) :
    
    res = 1 
    
    while n > 0 :
        if n % 2 != 0 :
            res = res * x 
        x = x * x
        n = n // 2 
    
    return res 
    

x = 4
n = 5
print(power(x,n))#1024###(4**5=10124)
#=============================Mean Of a List==============================
def Average(lst):
	return sum(lst) / len(lst)

lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)

print("Average of the list =", round(average, 2))#Average of the list = 35.75
#========================Separate Even and Odd=============================
def separateEvenOdd(l):
    even = []
    odd = []
    for x in l:
        if x%2==0:
            
            even.append(x)
        else:
            odd.append(x)
            
    return even,odd

l = [100,120,111,165]
even,odd = separateEvenOdd(l)
print(even)#[100, 120]
print(odd)#[111,165]
#==============================Get Smaller Elements==========================
def getSmaller(l, x):
    res = []
    for e in l:
        if e < x:
            res.append(e)
    return res

l = [8, 100, 20, 40, 3, 7]
x = 10
print(getSmaller(l, x))#[8,3,7]
#==========================Largest Element in a List================================
def getMax(l):
    if not l:
        return None
    res = l[0]
    for i in range(1, len(l)):
        if l[i] > res:
            res = l[i]
    return res

l = [1, 2, 3, 4, 5]
print(getMax(l))  # 5
#==========================Second Largest Element in a List===============================
def getMax(l):
    if not l:
        return None
    else:

        res = l[0]                  # assume l[0] is the max
        for i in range(1, len(l)):  # iterate through index 1 to last
            if l[i] > res:           # check whether current element is greater than res
                res = l[i]          # if current element is greater than res ,update res to current
        return res
    
def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = getMax(l)
    slar = None

    for x in l:

        if x != lar:
            if slar == None:
                slar = x
            else:
                slar = max(x, slar)
    return slar

l = [int(x) for x in input().split()]
print(getSecMax(l))#34
#==============Write a function to convert temperatures from Fahrenheit to Celsius.=============
#formula_for_Fahrenheit_to_Celsius=(5/9)*(F-32)
def Fahrenheit_to_Celsius(F):
	formula=(5/9)*(F-32)
	return formula
print(Fahrenheit_to_Celsius(98.6))#37.0
#==========Write a basic generator function that produces the numbers from 1 to 10============
def gen_func():
    for i in range(1,11):
        yield i
for i in gen_func():
    print(i)
#=========Create a generator that produces the Fibonacci sequence infinitely=========
def generate_fibonacci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,b+a
gen=generate_fibonacci(10)
for i in gen:
    print(i)
#==============Use a generator expression to calculate the sum of squares from 1 to 100===========
n=10
generate_sum_of_squares=sum(i**2 for i in range(1,n+1))
print(generate_sum_of_squares) #385
#==========Implement a generator that takes a list and loops over it in reverse order=======
def reverse_func(lst):
    for i in range(len(lst)-1,-1,-1):
        yield lst[i]
gen=reverse_func([1,2,3,4])
for i in gen:
    print(i)
#===========Build a random number generator using Python's random library and generator pattern==================
import random

def generate_random_num(n):
    while True:
        yield random.randint(1,n)
gen=generate_random_num(10)
print(next(gen))#any number between 1,n
#============remove duplicates==========================================
"""
Given a sorted array, the task is to remove the duplicate elements from the array and return its size of reduced array.
"""
def removeDuplicates(arr, n):
    res=1 
    for i in range(1, n):
        if(arr[res-1]!=arr[i]):
            arr[res]=arr[i]
            res+=1
    return res
    
n=7
arr=[10, 20, 20, 30, 30, 30, 30]
print(removeDuplicates(arr, n))#3
#=====================Left Rotate a list by one==============================
def rotateByone(l):
    n = len(l)
    x = l[0]
    for i in range(1, n):
        l[i - 1] = l[i]

    l[n - 1] = x

l = [10, 20, 30, 40]
rotateByone(l)
print(l)#[20, 30, 40, 10]
#====================One Odd Occurring======================================
"""
Given an array of positive integers. All numbers occur an even number of times except one number which occurs an odd number of times. Find the number in O(n) time & constant space.
"""
def findodd(arr) :
    
    for i in arr :
        count = 0 
        
        for j in arr :
            if i == j :
                count += 1 
                
        if count % 2 != 0 :
            return i
arr = [4,3,4,4,4,5,5,3,3]
print(findodd(arr))#3
#====================Print 1 to N using Recursion in Python===========================
def print1toN(n):
    if n == 0:
        return
    print1toN(n - 1)
    print(n)
print1toN(3)# 1 2 3
#====================Print N to 1 using Recursion in Python=============================
def printNto1(n):
    if n <= 0:
        return
    print(n)
    printNto1(n - 1)


n = 3
printNto1(n)#3 2 1
#=========================Sum of Digits using Recursion================================
def dSum(n):
    if n < 10:
        return n
    return dSum(n // 10) + n % 10
print(dSum(253))#10
#====================Palindrome check using Recursion===================================
def isPalRec(st, s, e) :	
	if (s == e):
		return True
	if (st[s] != st[e]) :
		return False
	if (s < e + 1) :
		return isPalRec(st, s + 1, e - 1);
	return True

def isPalindrome(st) :
	n = len(st)
	if (n == 0) :
		return True
	return isPalRec(st, 0, n - 1);
st = "geeg"
if (isPalindrome(st)) :
	print("Yes")
else :
	print("No")
#==========================Sum of natural numbers using recursion=============================
def recurSum(n):
	if n <= 1:
		return n
	return n + recurSum(n - 1)

# Driver code
n = 5
print(recurSum(n))# 15
#=========================Square Root==========================================================
def floorSqrt(x):
	if (x == 0 or x == 1):
		return x
	start = 1
	end = x//2
	while (start <= end):
		mid = (start + end)
		if (mid*mid == x):
			return mid
		if (mid * mid < x):
			start = mid + 1
			ans = mid
		else:
			# If mid*mid is greater than x
			end = mid-1
	return ans
x = 11
print(floorSqrt(x))#3
#=====================Linear Search==========================================================
def search(arr, n, x):
    for i in range(0, n):
      if (arr[i] == x):
        return i
	return -1
arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)
result = search(arr, n, x)
if (result == -1):
    print("Element is not present in array")
else :
    print("Element is present at index", result)
#==================Count Occurrences in Sorted Array===========================================
def search(nums, target, find_start_index):
    answer = -1
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            answer = mid
            if find_start_index:
                end = mid - 1
            else:
                start = mid + 1
    return answer

def count_occurrences(nums, x):
    first_index = search(nums, x, True)
    last_index = search(nums, x, False)
    if first_index != -1 and last_index != -1:
        return last_index - first_index + 1
    else:
        return 0

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
c = count_occurrences(arr, x)
print(c)#4
#===================Chocolate Distribution Problem===============================
def minDiff(arr,m) :
    if (m == 0 or len(arr) == 0) :
        return 0
    if (len(arr)<m) :
        return -1
    arr.sort()
    res = arr[m-1] - arr[0]
    for i in range(1, len(arr)- m+1) :
        res = min(res,abs(arr[i + m-1] - arr[i]))
    print(res)
    
arr = [7,3,1,8,9,12,56]
minDiff(arr,3)#2
#========================Cycle Sort==============================================
def cyclesortdist(arr) :
    w = 0
    for cs in range(len(arr) - 1) :
        item = arr[cs]
        pos = cs
        for i in range(cs+1, len(arr)) :
            if arr[i] < item :
                pos = pos + 1 
        if pos == cs :
            continue
        
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        w += 1
        
        while pos != cs :
            pos = cs 
            for i in range(cs+1, len(arr)) :
                if arr[i] < item :
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            w += 1
    return arr

arr = [20,40,30,10,50]
n = len(arr)
print(cyclesortdist(arr))#[10,20,30,40,50]
#====================Kth Smallest=============================
def partition(arr, l, r):
 
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i
def kthsmallest(arr, k) :
    l = 0 
    r = len(arr) - 1 
    while l <= r :
        p = partition(arr,l,r) 
        if p == k-1 :
            return p 
                
        elif p > k-1 :
            r = p - 1 
                
        else :
            l = p + 1 
    return -1
arr = [10,4,5,8,6,26]
k = 5 
print(kthsmallest(arr, k))#4
#===========================Bucket Sort======================================
def insertionSort(b):
	for i in range(1, len(b)):
		up = b[i]
		j = i - 1
		while j >= 0 and b[j] > up:
			b[j + 1] = b[j]
			j -= 1
		b[j + 1] = up	
	return b	
			
def bucketSort(x):
	arr = []
	slot_num = 10 # 10 means 10 slots, each
				# slot's size is 0.1
	for i in range(slot_num):
		arr.append([])
		
	# Put array elements in different buckets
	for j in x:
		index_b = int(slot_num * j)
		arr[index_b].append(j)
	
	# Sort individual buckets
	for i in range(slot_num):
		arr[i] = insertionSort(arr[i])

	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			k += 1
	return x

x = [0.897, 0.565, 0.656,
	0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(x))#[0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]
#==================Print matrix in snake pattern===========================
M = 4
N = 4
def printf(mat):
	global M, N
	# Traverse through all rows
	for i in range(M):
		if i % 2 == 0:
			for j in range(N):
				print(str(mat[i][j]),
					end=" ")

		else:
			for j in range(N - 1, -1, -1):
				print(str(mat[i][j]),
					end=" ")

mat = [[10, 20, 30, 40],
	[15, 25, 35, 45],
	[27, 29, 37, 48],
	[32, 33, 39, 50]]
printf(mat)
#===================Simple Linked List Implementation in Python==================================
class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)

temp1.next = temp2
temp2.next = temp3

head = temp1
print(head.key)#10
print(head.next.key)#20
print(head.next.next.key)#30
#=================Traversal of a Linked List=======================
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
def printList(head):
    curr = head
    while curr!= None:
        print(curr.key)
        curr = curr.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)
printList(head)# 10 20 15 30
#===================Search in Linked List======================================
class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def search(head, x):
    pos = 1
    curr = head
    while curr != None:
        if curr.key == x:
            return pos
        pos = pos + 1
        curr = curr.next
    return -1

head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(25)
x = 20
print(search(head, x))#3
#======================Check if a String is Subsequence of Other=====================================
def issubseq(s1,s2) :
    i, j = 0, 0
    while(i < len(s1) and j < len(s2)) :
        if s1[i] == s2[j] :
            j = j + 1 
        i += 1 
    if j == len(s2) :
        return True
    else :
        return False
        
s1 = "ABCDEF"
s2 = "ADE"
print(issubseq(s1,s2))#True
#=====================Check for Anagram in Python======================
s1= input("Enter a String:\n")
s2= input("Enter a String:\n")

def areAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    count=[0]*256
    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1
    for x in count:
        if x!=0:
            return False
    return True
print(areAnagram(s1,s2))
"""
Enter a String:
venu
Enter a String:
uenv
True
"""
#===============Leftmost Repeating Character===============================
import sys
CHAR = 256
def leftmost(st) :
    findex = [-1] * CHAR
    res = sys.maxsize
    for i in range(len(st)) :
        if (findex[ord(st[i])]==-1) :
            findex[ord(st[i])] = i
        else :
            res = min(res,findex[ord(st[i])])
    if res == sys.maxsize :
        return -1
    else :
        return res
        
st = "abccbd"
print(leftmost(st))
#===========================Leftmost Non-Repeating Element========================
# Python program to print the first non-repeating character

NO_OF_CHARS = 256

def getCharCountArray(string):
	count = [0] * NO_OF_CHARS
	for i in string:
		count[ord(i)]+= 1
	return count

def firstNonRepeating(string):
	count = getCharCountArray(string)
	index = -1
	k = 0

	for i in string:
		if count[ord(i)] == 1:
			index = k
			break
		k += 1

	return index

string = "geeksforgeeks"
index = firstNonRepeating(string)
if index == 1:
	print ("Either all characters are repeating or string is empty")
else:
	print ("First non-repeating character is" , string[index])
#First non-repeating character is f
#============================================Reverse words in a string====================================================================
def reverse_word(s, start, end):
	while start < end:
		s[start], s[end] = s[end], s[start]
		start = start + 1
		end -= 1
s = "Welcome to dsa"
s = list(s)
start = 0
while True:
	try:
		end = s.index(' ', start)
		reverse_word(s, start, end - 1)
		start = end + 1
	except ValueError:
		reverse_word(s, start, len(s) - 1)
		break
s.reverse()
s = "".join(s)
print(s)#dsa to Welcome
#================================== Bubble Sort Algorithm=============================
def bubbleSort(l):
    n = len(l)

    for i in range(n-1):

        for j in range(n - i-1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


l = [10, 8, 20, 5]

bubbleSort(l)

print(*l)#5 8 10 20
#===================================Count Inversions in Array=================================
# Python3 program to count
# inversions in an array


def getInvCount(arr, n):

	inv_count = 0
	for i in range(n):
		for j in range(i + 1, n):
			if (arr[i] > arr[j]):
				inv_count += 1

	return inv_count


# Driver Code
arr = [1, 20, 6, 4, 5]
n = len(arr)
print("Number of inversions are",getInvCount(arr, n))# Number of inversions are 5
#===================Display the Longest Name=======================================
def find_longest_names(arr):
    sorted_arr = sorted(arr, key=lambda x: len(x), reverse=True)
    max_length = len(sorted_arr[0])
    longest_names = []
    for name in sorted_arr:
        if len(name) == max_length:
            longest_names.append(name)
        else:
            break

    return longest_names
arr=["toggle","Stackoverflow","Origin","Alternatively"]
print(find_longest_names(arr))#['Stackoverflow', 'Alternatively']
#===========================Indexes of Subarray Sum======================================
def subarraySum(arr, target):
    start = 0
    current_sum = 0
    n = len(arr)
    
    for end in range(n):
        current_sum += arr[end]
        
        while current_sum > target and start < end:
            current_sum -= arr[start]
            start += 1
            
        if current_sum == target:
            return [start + 1, end + 1]
            
    return [-1]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 15
print(subarraySum(arr, target)) # Output: [1, 5]
#=============Kandane's Algorithm=======================================================
"""
You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].
"""
def maxSubarraySum(arr):
    res = arr[0]
    
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        res = max(res, maxEnding)
    
    return res

arr = [2, 3, -8, 7, -1, 2, 3]
print(maxSubarraySum(arr))#11
#=======================Equilibrium Point=====================================================
def equilibrium_point(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        if left_sum == total_sum - left_sum - arr[i]:
            return i
        left_sum += arr[i]

    return -1

print(equilibrium_point([-7, 1, 5, 2, -4, 3, 0]))#3
#=================================Moving all zeros to end of array=================================
def pushZerosToEnd(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
    return arr
arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(pushZerosToEnd(arr))# [1, 2, 4, 3, 5, 0, 0, 0]
#==============================Minimum Jumps=====================================
def minJumps(arr):
    n = len(arr)

    dp = [float('inf')] * n
    dp[n - 1] = 0

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, min(i + arr[i] + 1, n)):
            if dp[j] != float('inf'):
                dp[i] = min(dp[i], 1 + dp[j])

    if dp[0] == float('inf'):
        return -1

    return dp[0]

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(arr))#3
