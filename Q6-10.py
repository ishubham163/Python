#!/usr/bin/env python
# coding: utf-8
"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

6. Palindrome Check (String Problem)
Write a function to check whether a given string is a palindrome using for loop Take the input from user. (a string that reads the same forward and backward is called palindrome). 
    String = “mom” 
    If we reverse this string, we get the same Output “mom”.
    Expected output: string is a palindrome.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
# In[17]:


def palandrom_check(name: str) -> str:
    """
    This Function is for checking the Palindrom.
    Input Should be in string.

    TypeError if input is not a string
    VaalueError if input string is empty.
    """
    if not isinstance(name,str):
        raise TypeError("Input should be in a string")
    if name.strip() == "":
        raise ValueError("Input string should not be Empety")
    else:
        name = name.strip()

    rev_string = ""
    for char in name:
        rev_string = char + rev_string
    return name == rev_string

if __name__ == "__main__":
    try:
        user_input = input("Enter the Name to Check : ")
        if palandrom_check(user_input):
            print(f"{user_input} is a Palandrom")
        else:
            print(f"{user_input} is not a Palandrom")
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)









"""
-----------------------------------------------------------------------------------------------------------

7. Count Vowels in a String
	Take a string as input and count the number of vowels (a, e, i, o, u) in it.
	Ignore case (i.e., count both uppercase and lowercase vowels).
	Example: “Python” word has 1 vowel sound(o)

----------------------------------------------------------------------------------------------------------
"""
# In[31]:


def count_vowels(text: str) -> int:
    """
    This function is for counting the vowel for the user input
    Input should be in string

    TypeError if input is not a string
    VaalueError if input string is empty.
    """
    if not isinstance(text,str):
        raise TypeError("Input should be in a string")
    if text.strip() == "":
        raise ValueError("Input string should not be Empety")
    else:
        text = text.strip()

    vowel = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowel:
            count = count + 1
    return count

if __name__ == "__main__":
    try:
        users_input = input("Enter your string : ")
        result = count_vowels(users_input)
        print(result)

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)





"""
-------------------------------------------------------------------------------------------------------

8. Find the Second Largest Element in a List using for loop.
Write a function to find the second largest element in a list without using built-in sorting.
    Example
        Input: [7, 5, 8, 2, 10, 9]
        Expected Output: 9
    Example
        Input: [4, 4, 4, 4]
        Expected Output: None

------------------------------------------------------------------------------------------------------------
"""
# In[13]:


def second_largest_number(numbers):

    if len(numbers) < 2:
        return None

    largest = float("-inf")
    second_largest = float("-inf")

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float("-inf") else None


# In[14]:


print(second_largest_number([4, 4, 4, 4]))


# In[15]:


print(second_largest_number([7, 5, 8, 2, 10, 9]))


# In[22]:


def second_largest_number(numbers):

    """
    This function is for finding secont largest number from the list.

    TypeError if input is not a string
    VaalueError if input string is empty.
    """
    if not isinstance(numbers,list):
        raise TypeError("Input should be in a string")
    if len(numbers) == 0:
        raise ValueError("Input string should not be Empety")


    if len(numbers) < 2:
        return None

    largest = float("-inf")
    second_largest = float("-inf")

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float("-inf") else None

if __name__ == "__main__":
    try:
        pass

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)


# In[23]:


print(second_largest_number([7, 5, 8, 2, 10, 9]))





"""
----------------------------------------------------------------------------------------------------------

9. Sum of Digits
	Write a function that takes an integer as input and returns the sum of its digits.
	Example: sum_of_digits(123) -> 6

-----------------------------------------------------------------------------------------------------------
"""

# In[27]:


def sum_of_digits(n: int) -> int:

    n = abs(n)  
    total = 0
    while n > 0:
        total += n % 10  
        n //= 10         
    return total


# In[28]:


print(sum_of_digits(123))


# In[33]:


def sum_of_digits(n: int) -> int:
    """
    Calculates the sum of the digits of an integer n.
    Input Should be always integer value.
    Return the Integer Value.

    TypeError if input is not a string
    VaalueError if input string is empty.
    """

    if not isinstance(n,int):
        raise TypeError("Input should be in a string")
    if n < 0:
        raise ValueError("Input string should not be Empety")


    n = abs(n)  
    total = 0
    while n > 0:
        total += n % 10  
        n //= 10         
    return total

if __name__ == "__main__":
    try:
        pass

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)


# In[35]:


print(sum_of_digits(123567))





"""
-----------------------------------------------------------------------------------------------------------

10. Remove Duplicates from a List while maintaining the original order. Don’t use set method.
	Write a function that removes duplicates from a list while maintaining the original order.
    
	Example
        Input: [1, 3, 2, 3, 4, 1, 5]
        Expected Output: [1, 3, 2, 4, 5]
	Example
        Input: [4, 4, 4, 4]
        Expected Output: [4]

----------------------------------------------------------------------------------------------------------------
"""

# In[45]:


def remove_duplicates(list1: list) -> list:
    seen = {}
    result = []
    for item in list1:
        if item not in seen:
            seen[item] = True
            result.append(item)
    return result


# In[46]:


print(remove_duplicates([1, 3, 2, 3, 4, 1, 5]))


# In[47]:


print(remove_duplicates([4, 4, 4, 4]))


# In[51]:


def remove_duplicates(list1: list) -> list:

    """
    Calculates the sum of the digits of an integer n.
    Input Should be always integer value.
    Return the Integer Value.

    TypeError if input is not a string
    VaalueError if input string is empty.
    """

    if not isinstance(list1, list):
        raise TypeError("Input should be in a string")
    if len(list1) == 0:
        raise ValueError("Input string should not be Empety")


    seen = {}
    result = []
    for item in list1:
        if item not in seen:
            seen[item] = True
            result.append(item)
    return result

if __name__ == "__main__":
    try:
        pass

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)


# In[52]:


print(remove_duplicates([1, 3, 2, 3, 4, 1, 5]))


# In[53]:


print(remove_duplicates([4, 4, 4, 4]))


# In[ ]:




