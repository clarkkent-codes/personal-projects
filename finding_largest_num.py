number_list = [12,45,7,34,89,2]

largest = number_list[0]

for current_number in number_list:
    if current_number > largest:
        largest = current_number
    
print("Largest number: ", largest)