# Task 1 - Beginner Python Programs

# 1. Sum of Two Numbers
a = 10
b = 20
sum = a + b
print("Sum =", sum)

# 2. Odd or Even Checker
num = 15
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# 3. Factorial Calculation
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("Factorial of", num, "=", factorial)

# 4. Fibonacci Sequence
n = 10
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# 5. String Reverse
text = "Python"
reversed_text = text[::-1]
print("Original String:", text)
print("Reversed String:", reversed_text)

# 6. Palindrome Check
word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 7. Leap Year Check
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# 8. Armstrong Number Check
num = 153
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
