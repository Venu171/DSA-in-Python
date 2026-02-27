"""
1. Pure vs. Impure Functions
Task: Write a pure function and an impure function for the following scenario:

Calculate the total cost of ordering n cups of chai, where each cup costs 10 rupees.
For the impure function, use a global variable to keep track of the total cost across multiple function calls.
"""
# Pure function
def pure_chai_cost(n):
    return n*10

# Impure function
total_cost = 0
def impure_chai_cost(n):
    global total_cost
    total_cost+=pure_chai_cost(n)
    return total_cost

print(impure_chai_cost(5))#50
print(impure_chai_cost(5))#100

"""
2. Recursion
Task: Write a recursive function to calculate the factorial of a number n.

The factorial of n is the product of all positive integers less than or equal to n.
Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.
"""

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))#120

"""
3. Lambda Functions
Task: Use a lambda function to filter out all even numbers from a list of integers.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_numbers = list(filter(lambda x: x%2==0, numbers))
print(even_numbers)

"""
4. Built-in Functions
Task: Use the map() function to convert a list of temperatures from Celsius to Fahrenheit.

Formula: Fahrenheit = (Celsius * 9/5) + 32.
"""

celsius_temps = [0, 10, 20, 30, 40]

fahrenheit_temps = list(map(lambda x: (x*9/5)+32, celsius_temps))
print(fahrenheit_temps)

"""
5. Docstrings
Task: Write a function called calculate_discount that calculates 
the final price of an item after applying a discount. 
Include a detailed docstring explaining the function's 
purpose, parameters, and return value.
"""
def calculate_discount(original_price, discount_percentage):
    """
    Calculate the final price of the item after applying the discount

    Parameters:
    original_price(int): Original price of the product.Expects the price of the product.
    discount_percentage(int): Percentage of the discount on the product.

    Returns:
    final_price(float): Final price after applying discount.
    """
    final_price=original_price*(100-discount_percentage)/100
    return final_price

print(calculate_discount(100,25))#75.0

"""
6. Dunder Methods
Task: Write a function called greet that prints 
a greeting message. 
Use the __name__ dunder method to print the function's 
name inside the function.
"""

def greet(name):
    return f"Hello, {name}! Have a great day!"

print(greet("Venu"))
print(greet.__name__)

#7. Using help()
#Task: Use the help() function to explore the documentation 
# of the sorted() built-in function. 
# Write down what it does and provide an 
# example of how to use it.
print(help(sorted))#This help() function give the details of the built in funtion in python.

"""
8. Combining Concepts
Task: Write a function called filter_long_words 
that uses a lambda function to filter out words longer 
than 5 characters from a list of words. 
Include a docstring for the function.

words = ["apple", "banana", "cherry", "dragonfruit", "elderberry"]
"""

def filter_long_words(word_list):
    """
    Filter the words in the list based on the condition

    Parameters:
    wort_list(list[str]): It contains list of words

    Returns:
    larger_strings(list[str]):List of string which satisfies the condition i.e. len(string) >5
    """
    larger_strings=list(filter(lambda x:len(x)>5,word_list))
    return larger_strings


print(filter_long_words(["apple", "banana", "berry", "dragonfruit", "elderberry"]))

#['banana', 'dragonfruit', 'elderberry']

===========Guessing Game=========================
"""
- Write a function (guessing_game) that takes no arguments.
- When run, the function chooses a random integer between 0 and 100 (inclusive).
- Each time the user enters a guess, the program indicates one of the following: 
   – Too high 
   – Too low 
   – Just right
- If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
- The program only exits after the user guesses correctly.
"""
import random

def guessing_game():
    random_num=random.randint(0,100)
    guess=0
    while True:
        try:
            user_guess=int(input("Enter the number b/w 0 to 100: "))
            guess+=1
            status=""
            if user_guess==random_num:
                print("Just right🦀!")
                break
            elif user_guess>random_num:
                print(f"No.of Guesses: {guess}.\nToo High!\nSorry your guess =={user_guess}== is incorrect.Please try your luck again!🙌")
                continue
            elif user_guess<random_num:
                print(f"No.of Guesses: {guess}.\nToo Low!\nSorry your guess =={user_guess}== is incorrect.Please try your luck again!🙌")
                continue
        except Exception as e:
            print(f"Error Occured⚠️! {str(e)}.\n Enter your guess again!")
guessing_game()
#=============================Pig_Latin_sentence=================================
def pig_latin(inp):
    vowel_lst=['a','e','i','o','u']
    if inp[0] in vowel_lst:
        return inp+"way"
    else:
        return inp[1:]+inp[0]+'ay'

def pl_sentence(sentence):
    lst=sentence.split(" ")
    res=[]
    for i in lst:
        stc=pig_latin(i)
        res.append(stc)
    return " ".join(res)
print(pl_sentence("this is a test translation"))#histay isway away esttay ranslationtay
#========Ubbi-Dubbi====================================================================
def ubbi_dubbi(string):
    res_str=list(string)
    vowelcount=0
    for i,j in enumerate(string):
        if j in ['a','e','i','o','u']:
            if vowelcount:
                res_str.insert(i+vowelcount,'ub')
            else:
                res_str.insert(i,'ub')
            vowelcount+=1
    print(res_str)
    return ''.join(res_str)
print(ubbi_dubbi("translation"))#trubanslubatubiubon
