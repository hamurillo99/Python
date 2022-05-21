import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

#TOOLBOX (Part 1)
#Defining a function
from cmath import cos, sin
from unittest import result

def square():
      new_value = 4**2
      print(new_value)
square(4)   

def square(value):
      new_value = value ** 2
      print(new_value)

def square(value):
    new_value = value ** 2
    return new_value
num = square(4)
print(num)

#DOCSTRINGS 
def square(value):
    """Return the square of value."""
    new_value = value ** 2
    return new_value

#EXAMPLE
def shout():
    """Print a string with three exclamation marks"""
    shout_word = 'congratulations' + '!!!'
    print(shout_word)
shout()

def shout(word):
    """Print a string with three exclamation marks"""
    shout_word = word + '!!!'
    print(shout_word)
shout('congratulations')

def shout(word):
    """Return a string with three exclamation marks"""
    shout_word = word + '!!!'
    return shout_word
yell = shout('congratulations')
print(yell)

#Multiple funtion parameters 
def raise_to_power(value1,value2):
    """Raise value1 to the power of value2."""
    new_value = value1 ** value2
    return new_value
raise_to_power = (2,3)
print(result)

#Unpacking tuples 
even_nums = (2, 4, 6)
a, b, c = even_nums

#Returning multiple values
def raise_both(value1, value2):
    """Raise value1 to the power of value2
    and vice versa."""
    
    new_value1 = value1 ** value2 + np.sin(value1)
    new_value2 = value2 ** value1 + np.cos(value2)
    
    new_tuple = (new_value1, new_value2)
    return new_tuple
result = raise_both(5,4)
print(result)


# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    """Return a tuple of strings"""
    shout1 = word1 + '!!!'
    shout2 = word2 + '!!!'
    shout_words = (shout1, shout2)
    return shout_words
yell1, yell2 = shout_all('congratulations', 'you')
print(yell1)
print(yell2)

#Global vs local scope 
new_val = 10

def square():
    """Returns the square of a number"""
    new_value2 = new_val ** 2
    return new_value2
square(3)

#Nested functions 
def outer():
    """Nested funtion"""
    x = ...
    
    def inner():
        """Inner function"""
        y = x ** 2
    return ...    

def mod2plus5(x1, x2, x3):
    """Returns the remainder plus 5 of three values."""
    new_x1 = x1 % 2 + 5
    new_x2 = x2 % 2 + 5
    new_x3 = x3 % 2 + 5
    
    return(new_x1, new_x2, new_x3)

def mod2plus5(x1, x2, x3):
    """Returns the remainder plus 5 of three values."""
    
    def inner(x):
        """Returns the remainder plus 5 of a value"""
        return x % 2 + 5
    
    return (inner(x1), inner(x2), inner(x3))
print(mod2plus5(1, 2, 3))

def raise_val(n):
    """Return the inner function."""
    
    def inner(x):
        """Raise x to the power of n."""
        raised = x ** n
        return raised 
    return inner 

square = raise_val(2)
cube = raise_val(3)
print(square(2), cube(4))

#Using nonlocal 
def outer():
    """Print the value n."""
    n = 1
    
    def inner():
        nonlocal n   
        n = 2 
        print(n)
        
    inner()
    print(n)      
    
#SCOPES SEARCHED 
#Local Scope
#Enclosing functions 
#Global 
#Built-in  

#Add a default argument 
def power(number, pow = 1):
    """Raise number to the power od pow."""
    new_value = number ** pow 
    return new_value

#Flexible arguments: *args(1)
def add_all(*args):
    """Sum all values in *args together."""
    #Initialize sum
    sum_all = 0
    #Accumulate the sum
    for num in args:
        sum_all += num
    return sum_all

def print_all(**kargs):
    """Print out key-value pairs in **kwargs."""    
    
    #Print out the key-value pairs 
    for key, value in kwargs.items():
        print(key + ":" + value)

#Lambda functions 
raise_to_power = lambda x, y: x** y
raise_to_power(2,3)

#Anonymous functions 
nums = [48, 6, 9, 21, 1]
square_all = map(lambda num: num ** 2, nums)
print(square_all)
print(list(square_all))

#Passing invalid error 

def sqrt(x):
    """Returns the square root of a number."""
    try:
        return x ** 0.5
    except:
        print('x must be an int or float')
sqrt(4)     

#Erors and exceptions 
def sqrt(x):
    if x < 0:
        raise ValueError('x must be non-negative')
    try:
        return x ** 0.5
    except TypeError:
        print('x must be an int or float')   