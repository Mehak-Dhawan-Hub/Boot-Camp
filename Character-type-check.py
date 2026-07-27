# Arithmetic Operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)

# Relational Operator
print("a > b =", a > b)

# Logical Operator
print("a > 0 and b > 0 =", a > 0 and b > 0)

# If-else ladder
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Excellent")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")
