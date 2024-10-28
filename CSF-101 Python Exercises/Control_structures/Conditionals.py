number = 0
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

score = 85
if score >= 90:
    Grade = "A"
elif score >= 80:
    Grade = "B"
elif score >= 70:
    Grade = "C"
elif score >= 60:
    Grade = "D"
else:
    Grade = "F"
print(f"Your grade is {Grade}")

number = 7
result = "even" if number % 2 == 0 else "odd"
print(f"The number is {result}")

num1 = 10 
num2 = 5
operator = "+"
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Error division by zero"
else:
    result = "Error: Invalid Operator"
print(f"Result: {result}")