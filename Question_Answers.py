#!/usr/bin/env python
# coding: utf-8
"""
---------------------------------------------------------------------------------------------------------------------------------------------------
1. Reverse the string using for loop.
    string = "Python"
    Expected output = "nohtyP"
----------------------------------------------------------------------------------------------------------------------------------------------------
"""
# In[1]:


def reverse_string(s):
  reversed_str = ""
  for char in s:
    reversed_str = char + reversed_str
  return reversed_str

user_input = input("Enter the Name to Check: ")
print(reverse_string(user_input))


# In[2]:


def reverse_string(string : str) -> str:
    if not isinstance(string,str):
        raise TypeError("Input must be string")

    reversed_str = ""

    """
    This function is used to reverse a string.
    input: should be in a string.
    return: it will also come in string

    TypeError if input is not a string
    VaalueError if input string is empty.
    """
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

if __name__ == "__main__" :
    try:
        user_input = input("Enter the Name to Check: ")
        print(reverse_string(user_input))

    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)

"""
---------------------------------------------------------------------------------------------------------------------------------------------------
2. Find the Largest Element in a List using for loop.
    Write a function to find the largest element in a list without using built-in sorting.
    
        Example
            Input: [7, 5, 8, 2, 10, 9]
            Expected Output: 10
        Example
            Input: [4, 4, 4, 4]
            Expected Output: None
----------------------------------------------------------------------------------------------------------------------------------------------------
"""
# In[3]:


def find_largest(lst):
  if not lst or all(x == lst[0] for x in lst):
    return None

  largest = lst[0]
  for num in lst:
    if num > largest:
      largest = num
  return largest


print(find_largest([7, 5, 8, 2, 10, 9]))
print(find_largest([4, 4, 4, 4]))


# In[4]:


def find_largest(lst):
    """
    This Function is for finding largest number in the list.
    Input: should be in integer
    Return value will be in integer. Will also the largest number form list

    TypeError if input is not a string
    VaalueError if input string is empty.
    """
    if not isinstance(numbers,list):
        raise TypeError("Input must be integer")
    if not numbers:
        raise ValueError("List should not be Empety")


    if not lst or all(x == lst[0] for x in lst):
        return None

    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

if __name__ == "__main__" :
    #numbers = [23,45,78,54,87,55,48]
    #numbers = [40,40,40,40,40]
    numbers = [7, 5, 8, 2, 10, 9]
    try:
        result = largest_num(numbers)
        print(result)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)

"""
---------------------------------------------------------------------------------------------------------------------------------------------------
3. Take the input from user and find whether number is prime or not?
        Prime numbers are number which are divide by 1 or themselves only.
    
            Example: 13 is a prime number.
            Example: 97 is a prime number 
----------------------------------------------------------------------------------------------------------------------------------------------------
"""
# In[5]:


def check_prime(num: int) -> bool:

  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

user_input = int(input("Enter a number: "))
if check_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")


# In[6]:


def check_prime(num: int) ->int:
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

        if check_prime(user_input):
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)

"""
---------------------------------------------------------------------------------------------------------------------------------------------------
4. Find all Prime numbers between 100 and 200?
	All prime numbers between 100 and 200 are:
    101, 103, 107, 109, 113,127, 131, 137, 139,149, 151, 157,163, 167,173, 179, 181,191, 193, 197, 199
----------------------------------------------------------------------------------------------------------------------------------------------------
"""
# In[7]:


def prime_num_range():
  primes = []
  for num in range(100, 201):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(num)
  return primes


print(prime_num_range())


# In[8]:


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
        print("all prime number between 100 to 200 are:-",end = " ")
        for number in range(100,201):
            if prime_num_range(number):
                print(number, end = " ")

    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)

"""
---------------------------------------------------------------------------------------------------------------------------------------------------
5. Calculate factorial of a number
    Write a function calculate_factorial that takes a number as input and returns its factorial. Handle cases where the input is not a 
    non-negative integer or zero.

    Example: If number is 5 factorials will be (5x4x2x3x2x1=120)
        Expected output: 120 if number is 5
----------------------------------------------------------------------------------------------------------------------------------------------------
"""
# In[9]:


def factorial_num(number: int)-> int:

    factorial = 1
    for i in range(1,number + 1):
        factorial *= i
    return factorial


num_input = int(input("Enter a Number : "))
result = factorial_num(num_input)
print(f"{result} if number is {num_input}")


# In[10]:


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

"""
---------------------------------------------------------------------------------------------------------------------------------------------------

6. Palindrome Check (String Problem)
Write a function to check whether a given string is a palindrome using for loop Take the input from user. (a string that reads the same forward and backward is called palindrome). 
    String = “mom” 
    If we reverse this string, we get the same Output “mom”.
    Expected output: string is a palindrome.

----------------------------------------------------------------------------------------------------------------------------------------------------
"""
# In[11]:


def palandrom_check(name: str) -> bool:
  rev_string = ""
  for char in name:
    rev_string = char + rev_string
  return name == rev_string


user_input = input("Enter the Name to Check: ")


if palandrom_check(user_input):
  print(f"{user_input} is a palindrome")
else:
  print(f"{user_input} is not a palindrome")



# In[12]:


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
# In[13]:


def count_vowels(text: str) -> int:

    vowel = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowel:
            count = count + 1
    return count


users_input = input("Enter your string : ")
result = count_vowels(users_input)
print(result)


# In[14]:


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
# In[15]:


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


print(second_largest_number([4, 4, 4, 4]))
print(second_largest_number([7, 5, 8, 2, 10, 9]))


# In[16]:


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
        print(second_largest_number([4, 4, 4, 4]))
        print(second_largest_number([7, 5, 8, 2, 10, 9]))

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)

"""
----------------------------------------------------------------------------------------------------------

9. Sum of Digits
	Write a function that takes an integer as input and returns the sum of its digits.
	Example: sum_of_digits(123) -> 6

-----------------------------------------------------------------------------------------------------------
"""
# In[17]:


def sum_of_digits(n: int) -> int:

    n = abs(n)  
    total = 0
    while n > 0:
        total += n % 10  
        n //= 10         
    return total


print(sum_of_digits(123))


# In[18]:


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
        str1 = int(input("input string")) 
        print(sum_of_digits(str1))

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)

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
# In[19]:


def remove_duplicates(list1: list) -> list:
    seen = {}
    result = []
    for item in list1:
        if item not in seen:
            seen[item] = True
            result.append(item)
    return result



print(remove_duplicates([1, 3, 2, 3, 4, 1, 5]))
print(remove_duplicates([4, 4, 4, 4]))


# In[20]:


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
        print(remove_duplicates([1, 3, 2, 3, 4, 1, 5]))
        print(remove_duplicates([4, 4, 4, 4]))

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)

"""
----------------------------------------------------------------------------------------------------------------------
11. Factorial Using Recursion
	Write a recursive function to calculate the factorial of a given number.
    	
        Example
            Input: n = 5
            Expected Output: 120 (since 5×4×3×2×1=120)
    	Example
            Input: n = 0
            Expected Output: 1 
-----------------------------------------------------------------------------------------------------------------------
"""
# In[21]:


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


# In[22]:


print(factorial(0))


# In[23]:


def factorial(n: int) -> int:

    """
    The function is used to find the factorial of the given numbers.
    Input should be in the integer form.
    Returns the integer Value.

    TypeError if input is not a string
    VaalueError if input string is empty.
    """

    if not isinstance(n, int):
        raise TypeError("Input should be in a string")
    if n < 0:
        raise ValueError("Input string should not be Empety")


    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    try:
        string1 = int(input("input string")) 
        print(factorial(string1))

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)

"""
-----------------------------------------------------------------------------------------------------------------------------
12. Count Occurrences of Each Character in a String
	Take a string as input and count the occurrences of each character.

        Example:
            Input: "hello"
            Expected Output: { 'h': 1, 'e': 1, 'l': 2, 'o': 1 }
    	Example:
            Input: "apple"
            Expected Output: { 'a': 1, 'p': 2, 'l': 1, 'e': 1 }
-----------------------------------------------------------------------------------------------------------------------------

"""
# In[24]:


def character_count(user_input: str) -> int:
    count = {}
    for char in user_input:
        count[char] = count.get(char,0) + 1
    return count     


# In[25]:


print(character_count("apple"))


# In[26]:


def character_count(user_input: str) -> int:

    """
    The function is used to count the number of character in a string.
    Input should be in the String form.
    Returns the integer Value.

    TypeError if input is not a string
    VaalueError if input string is empty.
    """

    if not isinstance(user_input, str):
        raise TypeError("Input should be in a string")
    if user_input == 0:
        raise ValueError("Input string should not be Empety")


    count = {}
    for char in user_input:
        count[char] = count.get(char,0) + 1
    return count   

if __name__ == "__main__":
    try:
        string = input("input string") 
        print(character_count(string))

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)

"""
-----------------------------------------------------------------------------------------------------------------------------
13. Check for Anagram
	Write a function to check if two input strings are anagrams of each other.
	An anagram is a word or phrase that is formed by rearranging the letters of another word or phrase. To be anagrams, two strings must contain the       exact same characters in the same quantities, but in any order.
    
        Example: "listen" and "silent" are anagrams.
-----------------------------------------------------------------------------------------------------------------------------

"""
# In[27]:


def are_anagrams(str1, str2):
  return sorted(str1) == sorted(str2)


# In[28]:


print(are_anagrams("listen", "silent"))


# In[29]:


def are_anagrams(str1: str, str2: str)->bool :

    """
    The function is used to check the anagrams of given string.
    Input should be in the String form.
    Returns the integer Value.

    TypeError if input is not a string
    VaalueError if input string is empty.
    """
    if not isinstance(str1, str) or not isinstance(str2,str):
        raise TypeError("Input should be in a string")
    if str1 == "" or str2 == "":
        raise ValueError("Input string should not be Empety")

    return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    try:
        print(are_anagrams("listen", "silent"))

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)

"""
-----------------------------------------------------------------------------------------------------------------------------
14. Fibonacci Sequence (Iterative)
	Write a function that prints the first n numbers in the Fibonacci sequence.
	Use an iterative approach.
    	Example
            Input: n = 6
            Expected Output: 0, 1, 1, 2, 3, 5
        Example
            Input: n = 1
            Expected Output: 0
-----------------------------------------------------------------------------------------------------------------------------

"""
# In[30]:


def fibonacci_iterative(n):
  if n <= 0:
    return []
  if n == 1:
    return [0]

  sequence = [0, 1]
  for _ in range(2, n):
    sequence.append(sequence[-1] + sequence[-2])
  return sequence


# In[31]:


print(fibonacci_iterative(6))


# In[32]:


def fibonacci_iterative(n: int) -> int:

    """
    The function is used to Fibonacci Sequence (Iterative) .
    Input should be in the Integer form.
    Returns the integer Value.

    TypeError if input is not a string
    VaalueError if input string is empty.
    """
    if not isinstance(n, int):
        raise TypeError("Input should be in a string")
    if n<= 0:
        raise ValueError("Input string should not be Empety")


    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    try:
        print(fibonacci_iterative(6))
        print(fibonacci_iterative(1))

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)

"""
-----------------------------------------------------------------------------------------------------------------------------
15. Check for Leap Year
	Write a function to check if a given year is a leap year.
	A leap year is divisible by 4, but not by 100, unless also divisible by 400.
	Divisible by 4: If a year can be evenly divided by 4 (like 2020), it might be a leap year.
	Not Divisible by 100: However, if that year can also be evenly divided by 100 (like 1900), then it's not a leap year.
	Unless Divisible by 400: If the year is divisible by 100, it could still be a leap year if it can also be evenly divided by 400 (like 2000).

    	Example
            Input: year = 2020
            Expected Output: True (2020 is a leap year)
    	Example
            Input: year = 1900
            Expected Output: False (1900 is not a leap year)
    	Example
            Input: year = 2000
            Expected Output: True (2000 is a leap year)

-----------------------------------------------------------------------------------------------------------------------------

"""
# In[33]:


def is_leap_year(year: int)-> (int,str):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  return False

user_input = int(input("Enter a year: "))

if is_leap_year(user_input):
    print(f"{user_input} is a leap year")
else:
    print(f"{user_input} is not a leap year")


# In[34]:


def is_leap_year(year: int)-> (int,str):

    """
    The function is used to find the leap year .
    Input should be in the Integer form.
    Returns the string Value.

    TypeError if input is not a string
    VaalueError if input string is empty.
    """

    if not isinstance(year, int):
        raise TypeError("Input should be in a string")
    if year <= 0:
        raise ValueError("Year must be greater than 0")

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False



if __name__ == "__main__":
    try:
        user_input = int(input("Enter a year: "))

        if is_leap_year(user_input):
            print(f"{user_input} is a leap year")
        else:
            print(f"{user_input} is not a leap year")

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)

"""
-----------------------------------------------------------------------------------------------------------------------------
16. Calculate Power without Using ** Operator
	Write a function that calculates xy  (x raised to the power of y) without using Python’s power operator (**).
    	Example
            Input: x = 2, y = 3
            Expected Output: 8 (since 23 =8)

-----------------------------------------------------------------------------------------------------------------------------

"""
# In[35]:


def power(x, y):
  result = 1
  if y < 0:
    x = 1 / x
    y = -y
  for _ in range(y):
    result *= x
  return result

x = float(input("Enter the base (x): "))
y = int(input("Enter the exponent (y): "))

print(f"{x} to the power of {y} is {power(x, y)}")


# In[36]:


def power(x: int, y: int)-> str:
    """
    The function is used to Calculate Power without Using ** Operator .
    Input should be in the Integer form.
    Returns the string Value.

    TypeError if input is not a string
    VaalueError if input string is empty.
    """

    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Input should be in a string")
    if x <= 0 or y <= 0:
        raise ValueError("Year must be greater than 0")


    result = 1
    if y < 0:
        x = 1 / x
        y = -y
    for _ in range(y):
        result *= x
    return result


if __name__ == "__main__":
    try:
        x = int(input("Enter the base (x): "))
        y = int(input("Enter the exponent (y): "))

        print(f"{x} to the power of {y} is {power(x, y)}")

    except TypeError as e:
       print(e)
    except ValueError as e:
       print(e)

"""
-----------------------------------------------------------------------------------------------------------------------------
17. Generate List of Even Numbers
	Create a function that generates a list of even numbers up to a given number.
    	Example
            Input: n = 10
            Expected Output: [2, 4, 6, 8, 10]
    	Example
            Input: n = 7
            Expected Output: [2, 4, 6]
-----------------------------------------------------------------------------------------------------------------------------

"""
# In[37]:


n = int(input("Enter a number: "))
evens = list(range(2, n + 1, 2))

print(f"Even numbers up to {n}: {evens}")


# In[38]:


def generate_evens(n):
  return list(range(2, n + 1, 2))

user_input = int(input("Enter a number (n): "))

result = generate_evens(user_input)
print(f"Even numbers up to {user_input}: {result}")


# In[39]:


def generate_evens(n: int) -> list:
    """
    The function is used to Generate List of Even Numbers .
    Input should be in the Integer form.
    Returns the List Value.

    TypeError if input is not a string
    VaalueError if input string is empty.
    """

    if not isinstance(n, int):
        raise TypeError("Input should be in a string")
    if x <= 0:
        raise ValueError("Year must be greater than 0")

    return list(range(2, n + 1, 2))

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number (n): "))
        result = generate_evens(user_input)
        print(f"Even numbers up to {user_input}: {result}")

    except TypeError as e:
       print(e)
    except ValueError as e:
       print("Please enter a valid integer.")

"""
-----------------------------------------------------------------------------------------------------------------------------
18. Binary Search Implementation
	Write a function that performs binary search on a sorted list and returns the index of the target element or -1 if not found.
    	Example
            Input: sorted_list = [1, 2, 3, 4, 5, 6], target = 4
            Expected Output: 3 (since 4 is at index 3)
    	Example
            Input: sorted_list = [10, 20, 30, 40, 50], target = 25
            Expected Output: -1 (since 25 is not in the list)

-----------------------------------------------------------------------------------------------------------------------------

"""
# In[40]:


def binary_search(sorted_list, target):
  left, right = 0, len(sorted_list) - 1

  while left <= right:
    mid = (left + right) // 2
    if sorted_list[mid] == target:
      return mid
    elif sorted_list[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1

print(binary_search([1, 2, 3, 4, 5, 6], 4))
print(binary_search([10, 20, 30, 40, 50], 25))


# In[41]:


def binary_search(sorted_list: list, target:int) -> int:

    """
    The function is used to find Binary Search Implementation .
    Input should be in the List form.
    Returns the Integer Value.

    TypeError if input is not a string
    VaalueError if input string is empty.
    """

    if not isinstance(sorted_list, list) or not isinstance(target, int):
        raise TypeError("Input should be in a List")
    if target <= 0:
        raise ValueError("Year must be greater than 0")

    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
          right = mid - 1

    return -1

if __name__ == "__main__":
    try:
        print(binary_search([1, 2, 3, 4, 5, 6], 4))
        print(binary_search([10, 20, 30, 40, 50], 25))

    except TypeError as e:
       print(e)
    except ValueError as e:
       print("Please enter a valid integer.")

"""
-----------------------------------------------------------------------------------------------------------------------------
19. Reverse Words in a Sentence
Note: Don’t use split or join.
	Write a function to reverse the order of words in a sentence, keeping the words themselves intact (sentence should not be 
    changed or altered in any way; they should remain exactly as they are,).
    
    Example
        Input: "Python is fun"
        Expected Output: "fun is Python"

-----------------------------------------------------------------------------------------------------------------------------

"""
# In[42]:


def reverse_words(sentence):
  words = []
  current_word = ""

  for char in sentence:
    if char == " ":
      if current_word:
        words.append(current_word)
        current_word = ""
    else:
      current_word += char
  if current_word:
    words.append(current_word)

  reversed_sentence = ""
  for i in range(len(words) - 1, -1, -1):
    reversed_sentence += words[i]
    if i > 0:
      reversed_sentence += " "

  return reversed_sentence

user_input = input("Enter a sentence: ")

result = reverse_words(user_input)
print(f"Reversed words: {result}")


# In[43]:


def reverse_words(sentence: str) -> str:
    """
    The function is used to Reverse Words in a Sentence .
    Input should be in the String form.
    Returns the string Value.

    TypeError if input is not a Integer
    VaalueError if input string is empty.
    """

    if not isinstance(sentence, str):
        raise TypeError("Input should be in a List")
    if sentence == "":
        raise ValueError("Year must be greater than 0")

    words = []
    current_word = ""

    for char in sentence:
        if char == " ":
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
          current_word += char
    if current_word:
        words.append(current_word)

    reversed_sentence = ""
    for i in range(len(words) - 1, -1, -1):
        reversed_sentence += words[i]
        if i > 0:
            reversed_sentence += " "

    return reversed_sentence


if __name__ == "__main__":
    try:
        user_input = input("Enter a sentence: ")
        result = reverse_words(user_input)
        print(f"Reversed words: {result}")

    except TypeError as e:
       print(e)
    except ValueError as e:
       print("Please enter a valid integer.")

"""
-----------------------------------------------------------------------------------------------------------------------------
20. Calculate GCD.
	Write a function to find the Greatest Common Divisor (GCD).
    
    	Example
            Input: a = 48, b = 18
            Expected Output: 6 (the GCD of 48 and 18 is 6)
    	Example
            Input: a = 56, b = 98
            Expected Output: 14 (the GCD of 56 and 98 is 14)
-----------------------------------------------------------------------------------------------------------------------------

"""
# In[44]:


def gcd_calculation(a : int , b : int) -> int:
    while b:
        a,b = b, a%b
    return a

print(gcd_calculation(48,18))
print(gcd_calculation(56,98))


# In[45]:


def calculate_gcd(a: int, b: int) -> int:
    """
    The function is used to Calculate GCD .
    Input should be in the Integer form.
    Returns the Integer Value.

    TypeError if input is not a Integer
    VaalueError if input string is empty.
    """

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Input should be in a List")
    if a <= 0 or b <= 0:
        raise ValueError("Year must be greater than 0")


    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        result = calculate_gcd(num1, num2)
        print(f"The GCD of {num1} and {num2} is: {result}")

    except TypeError as e:
       print(e)
    except ValueError as e:
       print("Please enter a valid integer.")

"""
21. Calculate GCD Using recursion.
•	Write a function to find the Greatest Common Divisor (GCD) of two numbers using recursion.
•	Example
Input: a = 48, b = 18
Expected Output: 6 (the GCD of 48 and 18 is 6)
•	Example
Input: a = 56, b = 98
Expected Output: 14 (the GCD of 56 and 98 is 14)

"""
# In[46]:


def gcd_cal_recursion(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd_cal_recursion(b, a%b)

print(gcd_cal_recursion(48,18))
print(gcd_cal_recursion(56,98))


# In[47]:


def gcd_cal_recursion(a : int , b : int) -> int:
    """
    This Function is used to calculate the GCD.
    Input Value should be in a Integer.
    Returns the integer value.

    TypeError if input is not in String.
    ValueError if input string is Empety.
    """

    if not isinstance(a,int) or not isinstance(b,int):
        raise TabError("Input must be in Integer")
    if a < 0 or b < 0:
        raise ValueError("Input String should not be Empety")
    if b == 0:
        return a
    return gcd_cal_recursion(b, a%b)
if __name__ == "__main__":
    try:
        print(gcd_calculation(48,18))
        print(gcd_calculation(56,98))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
22. Convert Decimal to Binary (Without using bin () function)
•	Write a function to convert a given decimal number to its binary representation.
•	Example
Input: decimal = 10
Expected Output: 1010 (the binary representation of 10 is 1010)
•	Example
Input: decimal = 5
Expected Output: 101 (the binary representation of 5 is 101)

"""
# In[48]:


def decimal_to_binary(num: int)-> int:
    if num == 0:
        return 0 
    binary = ""
    n = num

    while n>0:
        binary = str(n%2) + binary
        n //= 2
    return binary

print(decimal_to_binary(10))


# In[49]:


def decimal_to_binary(num: int)-> int:
    """
    This Function is used to convert decimal number into binary number.
    Input Value should be in a Integer.
    Returns the integer value.

    TypeError if input is not in String.
    ValueError if input string is Empety.
    """

    if not isinstance(num,int):
        raise TabError("Input must be in Integer")
    if num < 0:
        raise ValueError("Input String should not be Empety")

    if num == 0:
        return 0 
    binary = ""
    n = num

    while n>0:
        binary = str(n%2) + binary
        n //= 2
    return binary

if __name__ == "__main__":
    try:
        dec_value = int(input("Enter the Number"))
        result = decimal_to_binary(dec_value)
        print(result)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
23. Find Intersection of Two Lists
•	Write a function that returns the intersection of two lists without using set operations.
•	Example:
Input: list1 = [1, 2, 3, 4, 5], list2 = [4, 5, 6, 7, 8]
Expected Output: [4, 5]
•	Example:
Input: list1 = ['apple', 'banana', 'cherry'], list2 = ['cherry', 'date', 'apple']
Expected Output: ['apple', 'cherry']

"""
# In[50]:


def find_intersection(list1: list, list2: list)-> list:
    intersection = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection

print(find_intersection([1, 2, 3, 4, 5],[4, 5, 6, 7, 8]))
print(find_intersection(['apple', 'banana', 'cherry'],['cherry', 'date', 'apple']))


# In[51]:


def find_intersection(list1: list, list2: list)-> list:
    """
    This Function is used to find intersection of two list.
    Input Value should be in a list.
    Returns the list .

    TypeError if input is not in list.
    ValueError if input string is Empety.
    """

    if not isinstance(list1,list) or not isinstance(list2,list):
        raise TabError("Input must be in List")
    if list1 == 0 or list2 == 0:
        raise ValueError("Input String should not be Empety")

    intersection = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection


if __name__ == "__main__":
    try:
        print(find_intersection([1, 2, 3, 4, 5],[4, 5, 6, 7, 8]))
        print(find_intersection(['apple', 'banana', 'cherry'],['cherry', 'date', 'apple']))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)


"""
24. Remove All Whitespace from a String
•	Write a function that removes all whitespace characters (spaces, tabs, newlines) from a given string.
•	Example:
Input: "      Hello, World!       "
Expected Output: "Hello, World!"
•	Example:
Input: "       Python         is         fun "
Expected Output: "Python is fun"
"""
# In[52]:


def clean_whitespace(string: str) -> str:
    return " ".join(string.split())

print(clean_whitespace("     Hello, World!      "))
print(clean_whitespace("       Python       is         fun "))


# In[53]:


def clean_whitespace(string: str) -> str:
    """
    This Function is used to remove the extra space from the given sentence.
    Input Value should be in a string.
    Returns the string .

    TypeError if input is not in string.
    ValueError if input string is Empety.
    """

    if not isinstance(string,str):
        raise TabError("Input must be in string")
    if string == 0:
        raise ValueError("Input String should not be Empety")

    return " ".join(string.split())

if __name__ == "__main__":
    try:
        print(clean_whitespace("     Hello, World!      "))
        print(clean_whitespace("       Python       is         fun "))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
25. Calculate Sum of a List of Numbers Using Recursion
•	Write a recursive function to calculate the sum of a list of numbers.
•	Example:
Input: [1, 2, 3, 4, 5]
Expected Output: 15
•	Example:
Input: [10, 20, 30]
Expected Output: 60
"""
# In[54]:


def recursive_sum(list1:list) -> int:
    if not list1:
        return 0
    return list1[0] + recursive_sum(list1[1:])

print(recursive_sum([1, 2, 3, 4, 5]))
print(recursive_sum([10, 20, 30]))


# In[55]:


def recursive_sum(list1: list) -> int:
    """
    This Function is used to Calculate Sum of a List of Numbers Using Recursion.
    Input Value should be in a list.
    Returns the string .

    TypeError if input is not in list.
    ValueError if input string is Empety.
    """

    if not isinstance(list1, list):
        raise TabError("Input must be in list")
    if list1 == 0:
        raise ValueError("Input String should not be Empety")

    if not list1:
        return 0
    return list1[0] + recursive_sum(list1[1:])

if __name__ == "__main__":
    try:
        print(recursive_sum([1, 2, 3, 4, 5]))
        print(recursive_sum([10, 20, 30]))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
26. sort a list  
	Example:
        Input: [45, 20, 3, 40, 5,20]
        Expected Output: [3,4,5,20,20,45]
"""
# In[56]:


def sort_list(lst: list)-> list:
    length = len(lst)
    for i in range(length):
        for j in range(0,length-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

print(sort_list([45, 20, 3, 40, 5,20]))


# In[57]:


def sort_list(lst: list)-> list:
    """
    This Function is to Short a List.
    Input must be in a list.
    Returns a list with short output.

    TypeError if input is not a list.
    ValueError if input string is Empety.
    """
    if not isinstance(lst,list):
        raise TypeError("Input should be in a list")
    if lst == 0:
        raise ValueError("Input string should not be Empety")

    length = len(lst)
    for i in range(length):
        for j in range(0,length-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst
if __name__ == "__main__":
    try:
        print(sort_list([45, 20, 3, 40, 5,20]))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
27. Merge Two Sorted Lists
	Write a function to merge two sorted lists into a single sorted list.
    	Example:
            Input: list1 = [1, 3, 5], list2 = [2, 4, 6]
            Expected Output: [1, 2, 3, 4, 5, 6]
    	Example:
            Input: list1 = [10, 20, 30], list2 = [15, 25, 35]
            Expected Output: [10, 15, 20, 25, 30, 35]
"""
# In[58]:


def merge_two_short_list(list1: list ,list2: list)-> list:
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i = i + 1
        else:
            merged_list.append(list2[j])
            j = j + 1

    while i < len(list1):
        merged_list.append(list1[i])
        i = i + 1
    while j < len(list2):
        merged_list.append(list2[j])
        j = j + 1
        return(merged_list)

print(merge_two_short_list([1, 3, 5], [2, 4, 6]))


# In[59]:


def merge_two_short_list(list1: list ,list2: list)-> list:
    """
    This Function is to Merge Two Sorted Lists.
    Input must be in a list.
    Returns a list with merge and short output.

    TypeError if input is not a list.
    ValueError if input string is Empety.
    """
    if not isinstance(list1,list) or not isinstance(list2,list):
        raise TypeError("Input should be in a list")
    if list1 == 0 or list2 == 0:
        raise ValueError("Input string should not be Empety")

    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i = i + 1
        else:
            merged_list.append(list2[j])
            j = j + 1

    while i < len(list1):
        merged_list.append(list1[i])
        i = i + 1
    while j < len(list2):
        merged_list.append(list2[j])
        j = j + 1
        return(merged_list)

if __name__ == "__main__":
    try:
        print(merge_two_short_list([1, 3, 5], [2, 4, 6]))
        print(merge_two_short_list([10, 20, 30], [15, 25, 35]))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
28. Check if List is Sorted
	Write a function that checks if a list is sorted in ascending order.
    	
        Example:
            Input: [1, 2, 3, 4, 5]
            Expected Output: True
    	Example:
            Input: [5, 3, 4, 2, 1]
            Expected Output: False
"""
# In[60]:


def is_sorted_ascending(lst: list)-> bool:
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


print(is_sorted_ascending([1, 2, 3, 4, 5]))
print(is_sorted_ascending([5, 3, 4, 2, 1]))


# In[61]:


def is_sorted_ascending(lst: list)-> bool:
    """
    This Function is to Check if List is Sorted.
    Input must be in a list.
    Returns a boolen value.

    TypeError if input is not a list.
    ValueError if input string is Empety.
    """
    if not isinstance(lst,list):
        raise TypeError("Input should be in a list")
    if lst == 0 :
        raise ValueError("Input string should not be Empety")

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

if __name__ == "__main__":
    try:
        print(is_sorted_ascending([1, 2, 3, 4, 5]))
        print(is_sorted_ascending([5, 3, 4, 2, 1]))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
29. Count Frequency of Each Word in a Text File
	Write a program to read a text file and count the frequency of each word.

        Example: File content 
                    Hello world   
                    Hello again
                    Goodbye world
        Expected Output:
                    Hello: 2
                    world: 2 
                    again: 1 
                    Goodbye: 1
"""
# In[62]:


def count_words_in_file(filename: str)-> str:
    word_counts = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                for word in line.split():
                    word_counts[word] = word_counts.get(word, 0) + 1
        return word_counts

    except FileNotFoundError:
        return "Error: File not found."

count_words_in_file("info.txt")


# In[63]:


def count_words_in_file(filename: str)-> str:
    """
    This Function is to Count Frequency of Each Word in a Text File.
    Input must be in a string.
    Returns a string value.

    TypeError if input is not a String.
    ValueError if input string is Empety.
    """
    if not isinstance(filename,str):
        raise TypeError("Input should be in a list")
    if filename == "" :
        raise ValueError("Input string should not be Empety")

    word_counts = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                for word in line.split():
                    word_counts[word] = word_counts.get(word, 0) + 1
        return word_counts

    except FileNotFoundError:
        return "Error: File not found."
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    print(count_words_in_file("info.txt"))

"""
30. Find Missing Number in Consecutive List
	Write a function to find the missing number in a list of consecutive numbers.
    	
        Example:
            Input: [1, 2, 3, 5, 6]
            Expected Output: 4
    	Example:
            Input: [10, 11, 12, 14, 15]
            Expected Output: 13
"""
# In[64]:


def find_missing_number(list1: list)-> int:
    for i in range(len(list1) - 1):
        if list1[i + 1] - list1[i] > 1:
            return list1[i] + 1
    return None

print(find_missing_number([1, 2, 3, 5, 6]))
print(find_missing_number([10, 11, 12, 14, 15]))


# In[65]:


def find_missing_number(list1: list)-> int:
    """
    This Function is to Find Missing Number in Consecutive List.
    Input must be in a list.
    Returns a Integer value.

    TypeError if input is not a list.
    ValueError if input string is Empety.
    """
    if not isinstance(list1,list):
        raise TypeError("Input should be in a list")
    if list1 == 0 :
        raise ValueError("Input string should not be Empety")

    for i in range(len(list1) - 1):
        if list1[i + 1] - list1[i] > 1:
            return list1[i] + 1
    return None

if __name__ == "__main__":
    try:
        print(find_missing_number([1, 2, 3, 5, 6]))
        print(find_missing_number([10, 11, 12, 14, 15]))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
31. Calculate Sum of Squares of First n Natural Numbers
	Write a function to calculate the sum of squares of the first n natural numbers.

        Example:
            Input: n = 3
            Expected Output: 14
            (Calculation: 12 + 22 + 32 =14)
"""
# In[66]:


def sum_of_squares(n: int)-> int:
    return sum(i**2 for i in range(1, n + 1))

print(sum_of_squares(3))


# In[67]:


def sum_of_squares(n: int)-> int:
    """
    This Function is to Calculate Sum of Squares of First n Natural Numbers.
    Input must be in a Integer.
    Returns a Integer value.

    TypeError if input is not a Integer.
    ValueError if input string is Empety.
    """
    if not isinstance(n,int):
        raise TypeError("Input should be in a list")
    if n <= 0 :
        raise ValueError("Input string should not be Empety")

    return sum(i**2 for i in range(1, n + 1))

if __name__ == "__main__":
    try:
        print(sum_of_squares(3))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
32. Reverse Integer
	Write a function that takes an integer and returns its digits reversed.

        Example:
            Input: 12345
            Expected Output: 54321
    	Example:
            Input: -6789
            Expected Output: -9876
"""
# In[68]:


def reverse_integer(n: int)->int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return sign * rev


print(reverse_integer(12345))
print(reverse_integer(-6789))


# In[69]:


def reverse_integer(n: int)->int:
    """
    This Function is to Calculate Sum of Squares of First n Natural Numbers.
    Input must be in a Integer.
    Returns a Integer value.

    TypeError if input is not a Integer.
    ValueError if input string is Empety.
    """
    if not isinstance(n,int):
        raise TypeError("Input should be in a list")
    if n == 0 :
        raise ValueError("Input string should not be Empety")

    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return sign * rev

if __name__ == "__main__":
    try:
        print(reverse_integer(12345))
        print(reverse_integer(-6789))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
33. Implement a Stack using List
	Create a stack with push, pop, and peek operations using a list.
    Stack: A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means that the last element 
    added to thestack is the first one to be removed. Think of it like a stack of plates; you can only add or remove plates from the top.
    List: A list is a more general data structure that can store a collection of items. It allows for random access and can be used to 
    store elementin any order. Lists do not have strict rules about how elements are added or removed.

    	Example:
            Stack Operations:
                	Push: stack.push(10)
                	Push: stack.push(20)
                	Push: stack.push(30)
                	Peek: stack.peek()
            
            Expected Output: 30
                	Pop: stack.pop()
            Expected Output: 30
                	Peek: stack.peek()
            Expected Output: 20
                	Pop: stack.pop()
            Expected Output: 20
                	Pop: stack.pop()
            Expected Output: 10
                	Pop: stack.pop()
                    
        Expected Output: None (or an indication that the stack is empty)
"""
# In[78]:


class Stack:
    def __init__(self):
        self.stack = []

    #push operation
    def push(self, value):
        self.stack.append(value)
        print(f"{value} pushed to stack")
    #Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        return self.stack.pop()
    #peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return(self.stack)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Peek :", stack.peek())
    print("PoP :", stack.pop())
    print("PoP :", stack.pop())
    print("PoP :", stack.pop())



# In[74]:


class Stack:

  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.items:
      return None
    return self.items.pop()

  def peek(self):
    if not self.items:
      return None
    return self.items[-1]


s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())  # Output: 30
print(s.pop())
print(s.peek())

"""
34. Find the Longest Word in a Sentence
	Write a function that finds and returns the longest word in a given sentence.

        Example:
            Input: "Python programming is fun and interesting"
            Expected Output: "programming"
"""
# In[79]:


def longest_word(sentence: str)->str:
    words = sentence.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("Python programming is fun and interesting"))


# In[80]:


def longest_word(sentence: str)->str:
    """
    This Function is to Find the Longest Word in a Sentence.
    Input must be in a String.
    Returns a String value.

    TypeError if input is not a String.
    ValueError if input string is Empety.
    """
    if not isinstance(sentence,str):
        raise TypeError("Input should be in a String")
    if sentence == 0 :
        raise ValueError("Input string should not be Empety")

    words = sentence.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

if __name__ == "__main__":
    try:
        print(longest_word("Python programming is fun and interesting"))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
35. Check if a Number is a Power of 2
	Write a function that checks if a given number is a power of 2 and return How many powers.
    
        Example:
            Input: 16
            Expected Output: True
            (Explanation: 24=16)
            
    	Example:
            Input: 18
            Expected Output: False
            (Explanation: 18 is not a power of 2)
"""
# In[81]:


def check_power_of_two(n:int)-> bool:
    if n <= 0:
        return False, 0
    temp = n
    power = 0
    while temp % 2 == 0:
        temp //= 2
        power += 1
    if temp == 1:
        return True, power
    return False, 0


print(check_power_of_two(16))
print(check_power_of_two(18))


# In[82]:


def check_power_of_two(n:int)-> bool:
    """
    This Function is to Check if a Number is a Power of 2.
    Input must be in a Integer.
    Returns a Boolen value.

    TypeError if input is not a Integer.
    ValueError if input string is Empety.
    """
    if not isinstance(n,int):
        raise TypeError("Input should be in a Integer")
    if n <= 0 :
        raise ValueError("Input string should not be Empety")

    if n <= 0:
        return False, 0
    temp = n
    power = 0
    while temp % 2 == 0:
        temp //= 2
        power += 1
    if temp == 1:
        return True, power
    return False, 0

if __name__ == "__main__":
    try:
        print(check_power_of_two(16))
        print(check_power_of_two(18))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
36. Flatten a Nested List
	Write a function to flatten a list that contains nested lists of integers.

        Example:
            Input: [1, [2, [3, 4], 5], 6]
            Expected Output: [1, 2, 3, 4, 5, 6]
    	Example:
            Input: [[1, 2], [3, [4, 5]], 6]
            Expected Output: [1, 2, 3, 4, 5, 6]
"""
# In[83]:


def flatten_list(lst:list)->list:
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


print(flatten_list([1, [2, [3, 4], 5], 6]))


# In[84]:


def flatten_list(lst:list)->list:
    """
    This Function is to Flatten a Nested List.
    Input must be in a List.
    Returns a List value.

    TypeError if input is not a List.
    ValueError if input string is Empety.
    """
    if not isinstance(lst,list):
        raise TypeError("Input should be in a List")
    if lst == 0 :
        raise ValueError("Input string should not be Empety")

    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

if __name__ == "__main__":
    try:
        print(flatten_list([1, [2, [3, 4], 5], 6]))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
37. Find Pairs with Given Sum in a List
	Write a function to find all pairs in a list that sum up to a given number. 

        Example
        	Input:
                List: [1, 2, 3, 4, 5, 6]
                Target Sum: 7
        	Expected Output:
                [(1, 6), (2, 5), (3, 4)]

    In this example, the pairs (1, 6), (2, 5), and (3, 4) all add up to the target sum of 7.
"""
# In[85]:


def find_pairs(lst: list, out: int)-> dict:
    pairs = []
    seen = set()
    for num in lst:
        complement = out - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs



print(find_pairs([1, 2, 3, 4, 5, 6], 7))


# In[86]:


def find_pairs(lst: list, out: int)-> dict:
    """
    This Function is to Flatten a Nested List.
    Input must be in a List and integer.
    Returns a dictnort value.

    TypeError if input is not a List and integer.
    ValueError if input string is Empety.
    """
    if not isinstance(lst,list) and not isinstance(out,int):
        raise TypeError("Input should be in a List and integer")
    if lst == 0 and out <= 0:
        raise ValueError("Input string should not be Empety")

    pairs = []
    seen = set()
    for num in lst:
        complement = out - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs


if __name__ == "__main__":
    try:
        print(find_pairs([1, 2, 3, 4, 5, 6], 7))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
38. Convert List of Tuples to Dictionary
	Write a function to convert a list of tuples into a dictionary.

        Example:
        	Input:
                [(‘a’, 1), (‘b’, 2), (‘c’, 3), (‘d’, 4)]
        	Expected Output:
                {'a': 1, 'b': 2, 'c': 3, 'd': 4}
"""
# In[87]:


def tuples_to_dict(tup_list:tuple)->tuple:
    return dict(tup_list)


input_tuples = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
print(tuples_to_dict(input_tuples))


# In[88]:


def tuples_to_dict(tup_list:list)->tuple:
    """
    This Function is to Convert List of Tuples to Dictionary.
    Input must be in a List.
    Returns a Tuple value.

    TypeError if input is not a Tuple.
    ValueError if input string is Empety.
    """
    if not isinstance(tup_list,list):
        raise TypeError("Input should be in a List")
    if tup_list == 0 :
        raise ValueError("Input string should not be Empety")

    return dict(tup_list)

if __name__ == "__main__":
    try:
        input_tuples = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
        print(tuples_to_dict(input_tuples))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
39. Implement Queue using List
	Create a queue with enqueue, dequeue, and peek operations using a list.
    
        Example Scenario
                1.	Enqueue Operations:
                    o	Add elements to the queue in the order: 10, 20, 30.
                2.	Dequeue Operation:
                    o	Remove the front element of the queue (FIFO principle).
                3.	Peek Operation:
                    o	View the element at the front of the queue without removing it.
        
        Expected Output
                Given the above operations, the sequence would look like this:
                    •	After enqueuing 10, 20, and 30:
                        Queue: [10, 20, 30]
                    •	After calling peek (without removing any item):
                        Output: 10
                    •	After calling dequeue twice:
                        Queue: [30]
                    •	After calling peek again:
                        Output: 30
                    •	After calling dequeue one more time (emptying the queue):
                        Queue: []
                    •	If attempting to dequeue on an empty queue:
                
            Output: "Queue is empty, cannot dequeue."
"""
# In[128]:


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self,value):
        self.queue.append(value)
        print(f"{value} enqueued. Queue {self.queue}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empety, can not dequeue")
        else:
            remove = self.queue.pop(0)
            print(f"{remove} deuqued. Queue {self.queue}")

    def peek(self):
        if self.is_empty():
            print("Queue is empety")
        else:
            print(f"Front element : {self.queue[0]}")

q = Queue()


# In[129]:


q.is_empty()


# In[130]:


q.enqueue(10)


# In[131]:


q.enqueue(20)


# In[132]:


q.enqueue(30)


# In[133]:


q.peek()


# In[134]:


q.dequeue()


# In[135]:


q.dequeue()


# In[136]:


q.dequeue()


# In[ ]:





# In[89]:


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            return "Queue is empty, cannot dequeue."
        return self.items.pop(0)

    def peek(self):
        if not self.items:
            return "Queue is empty."
        return self.items[0]

    def get_queue(self):
        return self.items


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.get_queue())
print(q.peek())
q.dequeue()
q.dequeue()
print(q.get_queue())

"""
40. Find the Median of a List of Numbers
	Write a function to calculate the median of a list of numbers.

        Example:
        	Input:
                [1, 3, 5, 7, 9]
            Expected Output:
                5
        	
            Input:
                [2, 4, 6, 8]
            Expected Output:
                5.0
"""
# In[90]:


def find_median(lst:list)->float:
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 != 0:
        return sorted_lst[mid]
    else:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2.0


print(find_median([1, 3, 5, 7, 9]))
print(find_median([2, 4, 6, 8]))


# In[91]:


def find_median(lst:list)->float:
    """
    This Function is to Convert List of Tuples to Dictionary.
    Input must be in a List.
    Returns a Float value.

    TypeError if input is not a List.
    ValueError if input string is Empety.
    """
    if not isinstance(lst,list):
        raise TypeError("Input should be in a List")
    if lst == 0 :
        raise ValueError("Input string should not be Empety")

    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 != 0:
        return sorted_lst[mid]
    else:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2.0

if __name__ == "__main__":
    try:
        print(find_median([1, 3, 5, 7, 9]))
        print(find_median([2, 4, 6, 8]))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

"""
41. Sort Dictionary by Value
	Write a function to sort a dictionary by its values.

        Example:
        	Input:
                {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}
        	Expected Output (sorted by values in ascending order):
                {'banana': 2, 'date': 3, 'apple': 5, 'cherry': 8}
"""
# In[92]:


def sort_dict_by_value(d:tuple)->tuple:
    return dict(sorted(d.items(), key=lambda item: item[1]))


input_dict = {"apple": 5, "banana": 2, "cherry": 8, "date": 3}
print(sort_dict_by_value(input_dict))


# In[ ]:




"""
42. Find LCM of two numbers 

    Example:
    	Input:
            num1 = 24
            Num2 = 9
        Expected Output:
            Lcm is 72
"""
# In[93]:


import math
def find_lcm(num1:int, num2:int)->int:
    return abs(num1 * num2) // math.gcd(num1, num2)


print(find_lcm(24, 9))


# In[ ]:




"""
43. Convert Binary to Decimal
	Write a function to convert a binary number (as a string) to a decimal.

        Example:
        	Input:
                "1011"
            Expected Output:
                11
"""
# In[94]:


def binary_to_decimal(bin_str:int)->int:
    return int(bin_str, 2)



print(binary_to_decimal("1011"))


# In[ ]:




"""
44. Swap Two Variables Without Temporary Variable
	Write a program to swap the values of two variables without using a temporary variable.

        Example:
        	Input:
                a = 5
                b = 10
        	Expected Output (after swapping):
                a should become 10
                b should become 5
"""
# In[95]:


def swap_variables(a:int, b:int)->str:
    a, b = b, a
    return a, b


a, b = 5, 10
a, b = swap_variables(a, b)
print(f" a should become {a} \n b should become {b}")


# In[ ]:




"""
45. Find Common Elements in Three Lists
	Write a function to find elements common in three lists.

        Example:
        	Input:
                list1 = [1, 2, 3,78, 4, 5,5,2,3]
                list2 = [3, 4, 5, 6, 7,78]
                list3 = [5, 6, 7, 8, 9,78]
        	Expected Output:
                [5,78]
"""
# In[96]:


def common_in_three(list1:list, list2:list, list3:list)->list:
    return list(set(list1) & set(list2) & set(list3))


list1 = [1, 2, 3, 78, 4, 5, 5, 2, 3]
list2 = [3, 4, 5, 6, 7, 78]
list3 = [5, 6, 7, 8, 9, 78]
print(common_in_three(list1, list2, list3))


# In[ ]:




"""
46. Remove Nth Occurrence of a Character from a String
	Write a function that removes the nth occurrence of a character from a string.

        Example:
        	Input:
                string = "example example example"
                char = 'e'
                n = 2
        	Expected Output:
                "example xample example"
"""
# In[97]:


def remove_nth_occurrence(s:str, char:int, n:int)->str:
    count = 0
    result = []
    for c in s:
        if c == char:
            count += 1
            if count == n:
                continue
        result.append(c)
    return "".join(result)


print(remove_nth_occurrence("example example example", "e", 2))


# In[ ]:




"""
47. Find the First Non-Repeated Character in a String
	Write a function to return the first non-repeated character in a string.

        Example:
        	Input:
                string = "swiss"
            Expected Output:
                'w'
        	
            Input:
                string = "repeated"
            Expected Output:
                'r'

    Explanation:
        The function should scan the input string and return the first character that does not repeat. 
        If all characters are repeated, it should return None or an appropriate message indicating that there are no non-repeated characters.
"""
# In[98]:


def first_non_repeated(s:str)->str:
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c in s:
        if counts[c] == 1:
            return c
    return None


print(first_non_repeated("swiss"))
print(first_non_repeated("repeated"))


# In[ ]:




"""
48. Check if String Contains Only Digits
	Write a function that checks if a string contains only numeric characters.

        Example:
        	Input:
            string = "123456"
        Expected Output:
            True
    	
        Input:
            string = "123a56"
    	Expected Output:
            False
"""
# In[99]:


def is_only_digits(s:str)->bool:
    return s.isdigit()


print(is_only_digits("123456"))
print(is_only_digits("123a56"))


# In[ ]:




"""
49. Check if Number is Armstrong Number
	Write a function that checks if a number is an Armstrong number.
	
        Example: 153 is an Armstrong number 
                 because 13+53+33=153.

    Explanation:
        An Armstrong number (also known as a narcissistic number) for a given number of digits is an integer such 
        that the sum of its own digits raised to the power of the number of digits is equal to the number itself.
"""
# In[100]:


def is_armstrong(n:int)->str:
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)

    if total == n:
        return f"{n} is an Armstrong number"
    else:
        return f"{n} is an Not Armstrong number"



print(is_armstrong(153))


# In[ ]:




"""
50. Reverse an Array (List) 
    The function should not return a new array; 
    it should modify the original input List do not create new list.
    The solution should run in O(n) time complexity.
    The space complexity should be O(1) (constant extra space).
"""
# In[101]:


def reverse_array_in_place(arr:list)->list:
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


nums = [1, 2, 3, 4, 5]
reverse_array_in_place(nums)
print(nums)


# In[ ]:




"""
51. Check if Subsequence Exists in List
	Write a function to check if a smaller list is a subsequence of a larger list.

        Example:
        	Input:
                larger_list = [1, 3, 5, 7, 9]
                smaller_list = [3, 7]
            Expected Output:
                True
        	
            Input:
                larger_list = [1, 3, 5, 7, 9]
                smaller_list = [3, 8]
            Expected Output:
                False
"""
# In[102]:


def is_subsequence(smaller_list:list, larger_list:list)->bool:
    i = j = 0
    while i < len(smaller_list) and j < len(larger_list):
        if smaller_list[i] == larger_list[j]:
            i += 1
        j += 1
    return i == len(smaller_list)


print(is_subsequence([3, 7], [1, 3, 5, 7, 9]))
print(is_subsequence([3, 8], [1, 3, 5, 7, 9]))


# In[ ]:




"""
52. Generate All Subsets of a Set
	Write a function to generate all possible subsets of a given set (list) of numbers.

        Example:
        	Input:
                numbers = [1, 2, 3]
        	Expected Output:
                [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""
# In[103]:


def generate_subsets(nums:list)->list:
    subsets = [[]]
    for num in nums:
        subsets += [curr + [num] for curr in subsets]
    return subsets

print(generate_subsets([1, 2, 3]))


# In[ ]:




