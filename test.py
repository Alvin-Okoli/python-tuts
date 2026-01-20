print("Hello WOrld! 🤗")
print(2 + 2)

message = """""
    This is a multi-line string.
    It can span multiple lines.
"""

course = "Python Programming"
print(len(course)) 

# Data Types in Python
x = 10          # Integer
pi = 3.14           # Float
is_active = True    # Boolean
name = "Alice"      # String

# String methods
greeting = "hello, world!"
print(greeting[1:5])  # Slicing
print(greeting.upper())  # Convert to uppercase
print(greeting.title())  # Convert to title case
print(greeting.find("world"))  # Find substring
print(greeting.lower())  # Convert to lowercase
print(greeting.strip())  # remove whitespace
print(greeting.replace("o", 'a'))  # replace string
print("hello" in greeting)  # check substring
print("hello" not in greeting)  # check substring

# Formatted strings
name = "Bob"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Using f-strings for formatting

# Number operations
# operators: +, -, *, /, //, %, **, +=, -=, *=, /=
print(round(3.6))
print(abs(-10))

# Type conversion
print(type(str(100)))  # Convert integer to string
print(type(int("100")))  # Convert string to integer


# Comparison operators
print(10 > 5)   # Greater than
print(10 < 5)   # Less than
print(10 == 10) # Equal to
print(10 != 5)  # Not equal to
print(10 >= 5)  # Greater than or equal to
print(10 <= 5)  # Less than or equal to

# conditional statements
temperature = 30
if temperature > 25:
    print("It's a hot day.")
elif temperature < 15:
    print("It's a cold day.")
else:
    print("It's a moderate day.")
print("Enjoy your day!")

# Tenary operator
result = "It's a cold day."if temperature < 15 else "It's a hot day."
print(result)
