def is_your_number_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    number = int(input("Enter a number to check if it's prime: "))
    if is_your_number_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")