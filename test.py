# Importing typing tools to help with type annotations
from typing import TypedDict, Union, Optional, Any

# TypedDict is used for creating dictionaries with fixed keys and their types
class Movie(TypedDict):
    name: str   # The movie name must be a string
    year: int   # The release year must be an integer

# Creating an object of type 'Movie'
movie = Movie(name="Avengers Endgame", year=2019)

# -------------------------------
# Union: The variable 'x' can be either int or float
# This ensures that the function can accept both types
def square(x: Union[int, float]) -> float:
    return x * x  # Returns the square of x

# -------------------------------
# Optional: Used when a variable can be of a specific type or None
# In this case, 'name' can be a string or None
def nice_message(name: Optional[str]) -> None:
    if name is None:
        print("Hey random person")  # If no name is given
    else:
        print(f"Hi there {name}")   # If name is given, greet with the name

# -------------------------------
# Any: You can pass any type of value here — no restrictions
def print_value(x: Any):
    print(x)  # Just prints the value as it is

# -------------------------------
# Lambda function: An anonymous (one-line) function
# Equivalent to: def square(x): return x * x
square_lambda = lambda x: x * x

# Call the lambda function with value 10
print(square_lambda(10))  # Output: 100

# -------------------------------
# Example of using lambda with map
nums = [1, 2, 3, 4]  # List of numbers

# map applies the lambda to each element in the list
squares = list(map(lambda x: x * x, nums))

# Print the list of squares
print(squares)  # Output: [1, 4, 9, 16]
 