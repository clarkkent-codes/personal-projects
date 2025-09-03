numbers = []

def populating_list(count):
    for i in range(1, count + 1):
        number = int(input(f"Input number [{i}]: "))
        numbers.append(number)

def print_even_numbers():
    for j in numbers:
        if j % 2 == 0:
            print("\nEven number:",j)
        else:
            continue
        
count = int(input("Input how many numbers you want: "))

populating_list(count)
print_even_numbers()
