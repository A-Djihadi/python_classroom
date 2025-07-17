def max_in_list(numbers):
    """Returns the maximum number in a list."""
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def min_in_list(numbers):
    """Returns the minimum number in a list."""
    if not numbers:
        return None
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number


def sum_of_list(numbers):
    """Returns the sum of all numbers in a list."""
    total = 0
    for number in numbers:
        total += number
    return total

def average_of_list(numbers):
    """Returns the average of all numbers in a list."""
    if not numbers:
        return None
    total = sum_of_list(numbers)
    return total / len(numbers)

def sort_list(numbers):
    """Returns a sorted version of the list."""
    return sorted(numbers)

def reverse_list(numbers):
    """Returns the list in reverse order."""
    return numbers[::-1]

def list_operations():
    print("Welcome to the List Operations Program!")
    print("Select an operation:")
    print("1. Find Maximum")
    print("2. Find Minimum")
    print("3. Calculate Sum")
    print("4. Calculate Average")
    print("5. Sort List")
    print("6. Reverse List")

    choice = input("Enter your choice (1-6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

        if choice == '1':
            print(f"Maximum: {max_in_list(numbers)}")
        elif choice == '2':
            print(f"Minimum: {min_in_list(numbers)}")
        elif choice == '3':
            print(f"Sum: {sum_of_list(numbers)}")
        elif choice == '4':
            print(f"Average: {average_of_list(numbers)}")
        elif choice == '5':
            print(f"Sorted List: {sort_list(numbers)}")
        elif choice == '6':
            print(f"Reversed List: {reverse_list(numbers)}")
    else:
        print("Entrée invalide")
        
        
if __name__ == "__main__":
    list_operations()