from name_function import *

print("Enter 'q' at any time to quit")
while True:
    first = input("First name ")
    if first == 'q':
        break
    last = input("Last name ")
    if last == 'q':
        break
        
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
    