
def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    num = int(input("Enter a number to find its factorial: "))
    result = factorial(num)
    if result is None:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {num} = {result}")

    limit = int(input("\nEnter how many Fibonacci terms to generate: "))
    print("Fibonacci series:", end=" ")
    for i in range(limit):
        print(fibonacci(i), end=" ")
    print()

main()
