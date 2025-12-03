# Define a sample string
text = "  hello python world  "

# Built-in functions
print("Original String:", text)
print("Length of string:", len(text))        # len() - number of characters
print("Max character:", max(text))           # max() - highest character (lexicographically)
print("Min character:", min(text))           # min() - lowest character (lexicographically)

# String methods
print("Capitalized:", text.capitalize())     # capitalize() - first letter uppercase
print("Count of 'o':", text.count('o'))      # count() - number of occurrences
print("Encoded:", text.encode())             # encode() - convert to bytes
print("Index of 'python':", text.index('python'))  # index() - position of substring
print("Replaced 'python' with 'java':", text.replace('python', 'java'))  # replace()
print("Uppercase:", text.upper())            # upper()
print("Lowercase:", text.lower())            # lower()
print("Title case:", text.title())           # title()
print("Split:", text.split())                # split() - split into list
print("Find 'world':", text.find('world'))   # find() - index (or -1 if not found)
print("Stripped:", text.strip())             # strip() - remove leading/trailing spaces

# join() - join list elements into a string
words = ['Python', 'is', 'fun']
print("Joined:", " ".join(words))            # join()

# decode() example (after encoding)
encoded_text = text.encode()
decoded_text = encoded_text.decode()
print("Decoded:", decoded_text)
