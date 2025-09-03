def check_if_prime(number):
    if number < 2:
        print(f"{number} is not a Prime")
        return
            
    else:
        for i in range(2, number - 1):
            if number % i == 0:
                print(f"{number} is not a Prime")
                return

        print(f"{number} is a Prime")


number = int(input("Enter a number: "))

check_if_prime(number)