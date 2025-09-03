import random

def coin_toss(flip):
    heads_count = 0
    tails_count = 0
    for i in range(flip):
        result = random.randint(0, 1)
        if result == 0:
            print("Heads")
            heads_count += 1
        else:
            print("Tails")
            tails_count += 1

    print("Times of Heads Appeared: ", heads_count)
    print("Times of Tails Appeared: ", tails_count)

flip = int(input("How many flip/s you want: "))

coin_toss(flip)