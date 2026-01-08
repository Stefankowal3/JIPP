vowels = 0
consonants = 0

text = "Programowanie Pythona"
for char in text:
    if char.lower() in 'aeiouąęó':
        vowels += 1
    elif char.isalpha():
        consonants += 1
        
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")

