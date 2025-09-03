def get_average(numbers):
    average = 0
    if len(numbers) == 0:
        print("No numbers to average")
    else:
        for number in numbers:
            average += number
        average = average / len(numbers)
        print("Average: ", average)

def append_numbers(count):
    if count > 0:
        for i in range(count):
            number = int(input("Enter numbers: "))
            numbers.append(number)
        print(numbers)
    else:
        print("No numbers to enter.")

numbers = []

count = int(input("How many numbers you want to list: "))

append_numbers(count)

get_average(numbers)
