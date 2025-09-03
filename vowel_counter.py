vowels = 'aeiou'

word = str(input("Enter a word: ")).lower()

counter = 0

for i in word:
    if i in vowels:
        counter += 1
    
print("Vowels: ", counter)