text = input("Enter a text: ")

text_lower = text.lower()

r_text  = text_lower[::-1]

if text_lower == r_text:
    print(f"'{text}' is a Palindrome")
else:
    print(f"'{text}' is not Palindrome")