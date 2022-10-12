import string
text = "-- ...Hey!  - Yes?!..."

def remove_punct(text):
    for char in text:
        if char in string.punctuation:
            text.replace(char, '')
    return text
print(remove_punct(text))