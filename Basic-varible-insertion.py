# 1. Basic variable insertion
name = "Clcoding"
print(f"Hello, {name}")

# 2. Multiple variable insertion
x, y = 5, 10
print(f"Hello, {x} and {y}")

# 3. Arithmetic operations
price = 100
quantity = 5
total = price * quantity
print(f"Total price is {total}")

# 4. Multiple variables in one line
x, y, z = 5, 10, 15
print(f"x: {x}, y: {y}, z: {z}")

# 5. Number formatting
pi = 3.141592653589793
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
print(f"Pi rounded to 4 decimal places: {pi:.4f}")

# 6. Debugging with '='
x = 5
print(f"x = {x}")

# 7. Using dictionaries
person = {"name": "Alice", "age": 30}
print(f"Name: {person['name']}, Age: {person['age']}")

# 8. Using lists
fruits = ["apple", "banana", "cherry"]
print(f"My favorite fruits are: {', '.join(fruits)}")

# 9. Using tuples
coordinates = (10, 20, 30)
print(f"Coordinates are x={coordinates[0]}, y={coordinates[1]}, z={coordinates[2]}")

# 10. Inline expressions
a, b = 10, 20
print(f"The sum of {a} and {b} is {a + b}")

# 11. Conditional formatting
score = 85
print(f"You {'passed' if score >= 50 else 'failed'} the test with a score of {score}")

# 12. Formatting with percentages
discount = 0.15
print(f"The discount is {discount:.0%}")

# 13. Formatting large numbers
large_number = 1234567890
print(f"The large number is {large_number:,}")

# 14. Using functions in f-strings
def square(n):
    return n * n

number = 7
print(f"The square of {number} is {square(number)}")

# 15. Nested f-strings
nested = f"Inner value: {f'Nested value: {42}'}"
print(nested)