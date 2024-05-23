'''
To create a basic calcultor; assign values to a variable/ containers;
For the operations, nums 1 and 2;
Create an if conditional statement that checks multiple statements;
If non are met print out an error for invalid/ not a valid operator;
'''

# Defining variables and assigning them respective values;
math_operators = input("Please enter a math operator (+, -, *, /, **, //): ")
num1 = float(input("Enter first number here: "))
num2 = float(input("Enter second number here: "))


# Creating a conditional statement for each operator;
if math_operators == "+":
    results = num1 + num2
    print (round(results, 4))
    
elif math_operators == "-":
    results = num1 - num2
    print (round(results, 4))
    
elif math_operators == "/":
    results = num1 / num2
    print (round(results, 4))

elif math_operators == "**":
    results = num1 ** num2
    print (round(results, 4))
    
elif math_operators == "//":
    results = num1 // num2
    print (round(results, 4))
    
else:
    print(f"{math_operators} is an INVALID operator")