print("Calculator")
print("Enter numbers: ")
first_number = int(input())
second_number = int(input())

print("[1] Addition       | [2] Subtraction")
print("[3] Multiplication | [4] Division")
operation = int(input("What operation do you want to do? "))

match operation:
    case 1:
        print("Addition")
        print(f"{first_number} + {second_number} = ", first_number + second_number)
    case 2:
        print("Subtraction")
        print(f"{first_number} - {second_number} = ", first_number - second_number)
    case 3:
        print("Multiplication")
        print(f"{first_number} * {second_number} = ", first_number * second_number)
    case 4:
        print("Division")
        print(f"{first_number} / {second_number} = ", first_number / second_number)