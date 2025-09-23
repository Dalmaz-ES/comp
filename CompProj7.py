j=2.0
for i in range(10):
    j=j-0.2
    print(j)


# Factorial of a number with for loop
n = int(input("Enter a number: "))
factorial = 1
if n >= 1:
    for i in range(1, n + 1):
        factorial *= i
print("Factorial of the given number is", factorial)