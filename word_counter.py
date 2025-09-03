sentence = str(input("Enter your sentence: "))

count = 0
for word in sentence.split():
    count += 1

print("Wrod Count: ", count)