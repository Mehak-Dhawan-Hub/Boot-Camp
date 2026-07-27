# Arithmetic Operators
a = 10
b = 5

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)

# Relational Operators
print(a > b)
print(a < b)
print(a == b)

# Logical Operators
print(a > 0 and b > 0)
print(a > 0 or b < 0)
print(not(a > b))

# If-else ladder to check character type
ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")
