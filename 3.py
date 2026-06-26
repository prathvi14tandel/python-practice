# 1. Voting Eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 2. Grade Calculator
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")


# 3. Traffic Light Simulator
color = input("Enter traffic light color (Red/Yellow/Green): ").capitalize()
if color == "Red":
    print("Stop")
elif color == "Yellow":
    print("Wait")
elif color == "Green":
    print("Go")
else:
    print("Invalid color")


# 4. ATM Withdrawal Check
balance = 5000
withdraw_amount = int(input("Enter amount to withdraw: "))
if withdraw_amount <= balance:
    print("Withdrawal successful. Remaining balance:", balance - withdraw_amount)
else:
    print("Insufficient balance")


# 5. Positive, Negative, or Zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 6. Check if Number Lies in a Range
num = int(input("Enter a number: "))
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
if lower <= num <= upper:
    print("Number is within range")
else:
    print("Number is outside range")


# 7. Username & Password Verification
correct_username = "admin"
correct_password = "1234"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")


# 8. Electricity Bill Calculator
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 200 * 7 + (units - 300) * 10
print("Electricity bill: ₹", bill)


# 9. Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")


# 10. Type of Triangle
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")