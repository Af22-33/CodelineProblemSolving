def sum_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The sum of {num1} and {num2} is {sum_two_numbers(num1, num2)}.")