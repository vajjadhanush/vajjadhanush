num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 != 0:
  
    ratio = num1 / num2
    print(f"The ratio of {num1} to {num2} is: {ratio:.2f}")
else:
    print("Error: Division by zero is not allowed. The second number must not be zero.")
