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
