text = str(input("Enter your string to be reversed: "))

reversed_text = ''

for ch in text:
    reversed_text = ch + reversed_text

print(reversed_text)