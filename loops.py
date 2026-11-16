
n = int(input("Enter a number N: "))

print("Numbers from 1 to N:")
for i in range(1, n + 1):
    print(i, end=" ")

print("\nNumbers from N to 1:")
i = n
while i >= 1:
    print(i, end=" ")
    i -= 1

print("\nMultiplication Table:")
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
