text = input("Enter the text: ")
vowel_count = 0
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        vowel_count += 1

print("vowels= ",vowel_count)