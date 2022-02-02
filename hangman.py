import random
DictFile = open("Dictionary.txt")
dictionary = []
for line in DictFile:
    dictionary.append(line.strip("\n"))
def hangman():

    word = (dictionary[random.randint(0, len(dictionary) - 1)]).lower()
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    attempts = 10
    guessmade = ''
    
    while len(word)> 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + ""
            if main == word:
                print(main)
                print("You win")
                break

            print("Guess the word: ", main)
            guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter valid character")
            guess = input()
        if guess not in word:
            attempts = attempts - 1




name = input("Enter your name: ")
print(f"Welcome {name}! ")
print("You have 10 attempts to guess a word.")

print()
hangman()