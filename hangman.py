import random
DictFile = open("Dictionary.txt")
dictionary = []
for line in DictFile:
    dictionary.append(line.strip("\n"))
def hangman():

    word = (dictionary[random.randint(0, len(dictionary) - 1)]).lower()

name = input("Enter your name: ")
print(f"Welcome {name}! ")
print("You have 10 attempts to guess a word.")

print()