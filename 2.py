#Print numbers from 1 to 10. Display multiplication table for a given number. Find factorial of a number. Generate the first N Fibonacci numbers. Check if a number is prime. Reverse a number (e.g., 123 → 321). Count digits in a number. Find sum of even numbers between 1–100. Print a pyramid pattern. Find all divisors of a number.

#Q1
for i in range(1,11):
    print(i)

#Q2
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Q3
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

#Q4
n = int(input("Enter N: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Q5
num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#Q6
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed Number =", rev)

#Q7
num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print("Digits =", count)

#Q8
sum_even = 0

for i in range(2, 101, 2):
    sum_even += i

print("Sum =", sum_even)

#Q9
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)

#Q10
num = int(input("Enter a number: "))

print("Divisors are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)

