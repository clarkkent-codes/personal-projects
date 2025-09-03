def read_lines():
    count = 0
    #add an encoding to let Python know which encoding to use
    with open("file.txt", "r", encoding="utf-8") as file: 
        for line in file:
            count += 1
    print(f"File has {count} of lines")

read_lines()
