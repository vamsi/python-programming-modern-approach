# Take the inputs
file_name = input("Enter the file name: ")
input_file = open(file_name, 'r')
text = input_file.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + \
    text.count(':') + text.count(';') + \
    text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
for word in text.split():
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        syllables += word.count(vowel)

for ending in ['es', 'ed', 'e']:
    if word.endswith(ending):
        syllables -= 1

if word.endswith('le'):
    syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / float(sentences)) - \
    84.6 * (syllables / words)
level = int(round(0.39 * (words / float(sentences)) + 11.8 *
                  (syllables / float(words)) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")
