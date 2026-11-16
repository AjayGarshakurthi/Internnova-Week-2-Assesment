
# Global variable
x = 100

def display():
    # Local variable
    y = 50

    print("Local variable:", y)
    print("Global variable inside function:", x)

display()

print("Global variable outside function:", x)
