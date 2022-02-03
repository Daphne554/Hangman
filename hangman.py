import random

def hangman():

    word = random.choice(["nigeria","ethiopia","congo","egypt","southafrica","tanzania","kenya",
             "uganda","algeria","sudan","morocco","angola","ghana","cameron","madagascar","mozambique","ivorycoast",
             "niger","mali","burkinafaso","malawi","chad","somalia","zimbabwe","zambia","senegal","southsudan",
             "rwanda","guinea","benin","tunisia","burundi","sierraleone","togo","libya","congo","liberia",
             "centralafricanrepublic","mauritania","eritrea","namibia","gambia","botswana","gabon","lesotho",
             "guineabissau","equatorialguinea","mauritius","eswatini","djibouti","comoros","capeverde","westernsahara"
                 ,"mayotte","seychelles"])

    validLetters = "abcdefghijklmnopqrstuvwxyz"
    attempts = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win")
            break

        print("Guess the word: " , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter valid character")
            guess = input()

        if guess not in word:
            attempts = attempts - 1
            if attempts == 9:
                print("9 turns left")
                print("-------------")
            if attempts == 8:
                print("8 turns left")
                print("-------------")
                print("      0      ")
            if attempts == 7:
                print("7 turns left")
                print("-------------")
                print("      0      ")
                print("      |      ")
            if attempts == 6:
                print("6 turns left")
                print("-------------")
                print("      0      ")
                print("      |      ")
                print("     /       ")
            if attempts == 5:
                print("5 turns left")
                print("-------------")
                print("      0      ")
                print("      |      ")
                print("     / \     ")

            if attempts == 4:
                print("4 turns left")
                print("-------------")
                print("    \ 0      ")
                print("      |      ")
                print("     / \     ")

            if attempts == 3:
                print("3 turns left")
                print("-------------")
                print("    \ 0 /    ")
                print("      |      ")
                print("     / \     ")

            if attempts == 2:
                print("2 turns left")
                print("-------------")
                print("    \ 0_ /   ")
                print("      |      ")
                print("     / \     ")

            if attempts == 1:
                print("1 turn left")
                print("-------------")
                print("    \ 0_|/   ")
                print("      |      ")
                print("     / \     ")

            if attempts == 0:
                print("You lose ")
                print("You let a kind man die")
                print("------------")
                print("      0_|  ")
                print("     /|\    ")
                print("     / \     ")


name = input("Enter your name: ")
print(f"Welcome {name}! ")
print("You have 10 attempts to guess a word.")
hangman()
print()
