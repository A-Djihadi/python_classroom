int_var = 5
float_var = 3.14
str_var = "Hello, World!"
list_var = [1, 2, 3, 4, 5]
dict_var = {"key1": "value1", "key2": "value2"}
tuple_var = (10, 20, 30)
set_var = {1, 2, 3, 4, 5}

# Different types of loop test 

print("For loop examples:")
# Using for loop to iterate over different data structures
print("Counting with range from 0 to 4:")
for i in range(5):
    print(i)
    
print("Looping through a tuple:")
for item in tuple_var:
    print(item)
    
print("Looping through a string:")
for char in str_var:
    print(char)
    
print("While loop examples:")
# Using while loop to count up from 0 to 4
print("Loop for a count up from 0 to 4:")
count = 0
while count < 5:
    print(count)
    count += 1

print("Loop for a count down from 5 to 0:")
# Using while loop to count down from 5 to 0
count = 5
while count >= 0:
    print(count)
    count -= 1

print("Iterating through a list:")
for item in list_var:
    print(item) 

print("Iterating through a dictionary:")
for key, value in dict_var.items():
    print(f"{key}: {value}")

print("Iterating through a set:")
for item in set_var:
    print(item)
    


def print_variables():
    print(f"Integer: {int_var}")
    print(f"Float: {float_var}")
    print(f"String: {str_var}")
    print(f"List: {list_var}")
    print(f"Dictionary: {dict_var}")
    print(f"Tuple: {tuple_var}")
    print(f"Set: {set_var}")
    
    print(range(5))  # Example of range 

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print('You entered:', number )
    
    print("Variables in the script:")
    print_variables()   