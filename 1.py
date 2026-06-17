#1. Write a program to print your name, age, and city in one line. 2. Take user input for two numbers and print their sum. 3. Write a program to convert temperature from Celsius to Fahrenheit. 4. Store your name in a variable and print it in uppercase. 5. Ask the user for their birth year and calculate their current age. 6. Write a program to swap the values of two variables. 7. Create a program to calculate the area of a rectangle from user inputs. 8. Write a program to check if a number is positive or negative. 9. Ask for two numbers and print their average.

#Q1
name = "Prathvi Tandel"
age = 20
city = "Valsad, Kosamba"
print("My name is", name, ", I am", age, "years old and I live in", city)

#Q2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum =", sum)

#Q3
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)

#Q4
name = input("Enter your name: ")
print("Uppercase =", name.upper())

#Q5
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print("Your age is", age, "years")

#Q6
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
print("Before swap — a =", a, "b =", b)
temp = a
a = b
b = temp
print("After swap — a =", a, "b =", b)

#Q7
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle =", area)

#Q8
num = int(input("Enter a number: "))
if num > 0:
    print(num, "is Positive")
elif num < 0:
    print(num, "is Negative")
else:
    print("Number is Zero")

#Q9
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
average = (num1 + num2) / 2
print("Average =", average)
