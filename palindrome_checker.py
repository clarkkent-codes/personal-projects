word = str(input("Enter your word: "))

reversed_word = "".join(reversed(word))

if word == reversed_word:
    print(word + " is a Palindrome")
else:
    print(word + " is not a Palindrome")