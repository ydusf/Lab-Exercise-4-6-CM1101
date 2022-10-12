import string
text = """-- ...Hey! -
    - Yes?!..."""

def remove_punct(text):
    new_text = ""

    for char in text:
        if char in string.punctuation:
            char = ''
        new_text += char
    return new_text

print(remove_punct(text))

# user_input = "Please enter your username"

# for word in user_input.split():
#     print(word)