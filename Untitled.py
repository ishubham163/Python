#!/usr/bin/env python
# coding: utf-8
def function
type hint
small doc string
Exception handling
if __name__
try:
    test your code
except Exception

-----------------------------------------------
#Q1. Reverse the string using for loop.
#string = "Python"
#Expected output = "nohtyP"
----------------------------------------------------
# In[8]:


def reverse_string(string : str) -> str:
    if not isinstance(string,str):
        raise TypeError("Input must be string")

    rev_str = ""

    """
    This function is used to reverse a string.
    input: should be in a string.
    return: it will also come in string
    """
    for char in string:
        rev_str = char + rev_str
    return rev_str
if __name__ == "__main__" :
    srting = "Python"
    try:
        result = reverse_string(string)
        print(result)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)

-----------------------------------------------------------------------------------------------
#Q2. Find the Largest Element in a List using for loop.
#Write a function to find the largest element in a list without using built-in sorting.
#Example
#Input: [7, 5, 8, 2, 10, 9]
#Expected Output: 10
#Example
#Input: [4, 4, 4, 4]
#Expected Output: None
------------------------------------------------------------------------------------------------------
# In[18]:


def largest_num (numbers: list) -> int:
    """
    This Function is for finding largest number in the list.
    Input: should be in integer
    Return value will be in integer. Will also the largest number form list
    """
    if not isinstance(numbers,list):
        raise TypeError("Input must be integer")
    if not numbers:
        raise ValueError("List should not be Empety")

    if len(numbers) != len(set(numbers)):
        return None

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
if __name__ == "__main__" :
    #numbers = [23,45,78,54,87,55,48]
    numbers = [40,40,40,40,40]
    try:
        result = largest_num(numbers)
        print(result)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


---------------------------------------------------------------------------------------------
#Q3. Take the input from user and find whether number is prime or not?
#              Prime numbers are number which are divide by 1 or themselves only.
#Example: 13 is a prime number.
#Example: 97 is a prime number 
------------------------------------------------------------------------------------------------
# In[24]:


def prime_number(num: int) ->int:
    """
    The function is used for finding prime number.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
if __name__ == "__main__" :
    try:
        user_input = int(input("Enter the number : "))

        if prime_number(user_input):
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


-------------------------------------------------------------------------------------------------------
#Q4. Find all Prime numbers between 100 and 200?
#	All prime numbers between 100 and 200 are:
#101, 103, 107, 109, 113,127, 131, 137, 139,149, 151, 157,163, 167,173, 179, 181,191, 193, 197, 199
------------------------------------------------------------------------------------------------------------
# In[36]:


def prime_num_range(num: int) ->int:
    """
    The function is used for finding prime number.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__" :
    try:
        for number in range(100,201):
            if prime_num_range(number):
                print("all prime number between 100 to 200 are:-",number)
                #print(number)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Q5. Calculate factorial of a number
#Write a function calculate_factorial that takes a number as input and returns its factorial. Handle cases where the input is not a non-negative integer or zero.
#Example: If number is 5 factorials will be (5x4x2x3x2x1=120)
#Expected output: 120 if number is 5
---------------------------------------------------------------------------------------------------------------------------------------------------------------
# In[41]:


def factorial_num(number: int)-> int:
    """
    This Function is used to calculatr the factorial of Number.
    input should be in a number.
    return the factorial of on-negative integer.
    """
    if not isinstance(number,int):
        raise TypeError("Input must be number")
    if number < 0 :
        raise ValueError("Input must be non-negative integer or zero")

    factorial = 1
    for i in range(1,number + 1):
        factorial *= i
    return factorial

if __name__ == "__main__" :
    try:
        num_input = int(input("Enter a Number : "))
        result = factorial_num(num_input)
        print(f"{result} if number is {num_input}")

    except ValueError:
        print("Error: Input must be a valid non-negative integer.")
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)


# In[ ]:




