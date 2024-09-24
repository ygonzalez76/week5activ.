# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
magic = "abracadabra"
print(magic[-7])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find('c'))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:13:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote =  "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote[-15:])
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
string = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
print(string.find('subjective'))
print(string[36:-1])
# b. Extract every third word.
words = string.split()
every_third_word = words[::3]
result = ' '.join(every_third_word)
print(result)
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
reversed_string = ' '.join(string.split()[::-1])
print(reversed_string)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
info = "MAY THE FORCE BE WITH YOU."
print(info.lower())

# String Joining and Splitting:
# Given the list 
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
joined_sentence = " ".join(motto)
print(joined_sentence)
# b. Now, split the string at every occurrence of the letter 'a'.
split_sentence = " ".join(motto).split('a')
print(" ".join(motto))  # joined string
print(split_sentence)   
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
sentence = "Life is what happens when you are busy making other plans."
print(sentence.replace("busy","distracted").replace("plans" , "mistakes"))
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
result = "Iteration " * 7
print(result)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
def word_search(quote, word):
    return word in quote
quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word_to_search = "moonlight"
if word_search(quote, word_to_search):
    print(f'The word "{word_to_search}" is in the quote.')
else:
    print(f'The word "{word_to_search}" is NOT in the quote.')
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
phrase = "Supercalifragilisticexpialidocious"
num_characters = len(phrase)
print(f'The word/phrase has {num_characters} characters.')

# b. Count the number of times the letter 'i' appears in the same word/phrase.
count_i = phrase.count('i')
print(f'The letter "i" appears {count_i} times.')
