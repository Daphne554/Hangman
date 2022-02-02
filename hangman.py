import random

def hangman():

    word = ( "Nigeria","Ethiopia","Democratic Republic of the Congo","Egypt","South Africa","Tanzania","Kenya",\
             "Uganda","Algeria","Sudan","Morocco","Angola","Ghana","Cameron","Madagascar","Mozambique","IvoryCoast",\
             "Niger","Mali","BurkinaFaso","Malawi","Chad","Somalia","Zimbabwe","Zambia","Senegal","South Sudan",\
             "Rwanda","Guinea","Benin","Tunisia","Burundi","SierraLeone","Togo","Libya","Congo""Liberia",\
             "CentralAfricanRepublic","Mauritania","Eritrea","Namibia","Gambia","Botswana","Gabon","Lesotho",\
             "Guinea-Bissau","EquatorialGuinea","Mauritius","Eswatini","Djibouti","Comoros","CapeVerde","WesternSahara"\
                 ,"Mayotte","Seychelles")
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
hangman()
print()