#importing libraries
import random
import time

#creating guesses variable
guesses = 0

#printing first lines of text
print("Below, type how many letters long your word is going to be.")
print("")

#opening built-in MacOS dictionary document through wfile variable
wfile = open("/usr/share/dict/words", "r")

#storing the contents of the built-in file into the 'words' variable
if wfile.mode == "r":
    wordlist = wfile.readlines()

#generates random word and takes user input
usrwordl = int(input("Word Length: "))
ranword = random.choice(wordlist)
ranword = ranword.rstrip('\n')
ranword = ranword.lower()
ranwordl = len(ranword)

#checking that the random word matches user input length, has no repeating characters, removes whitespace and uppercase
while ranwordl != usrwordl or (int(len(ranword)) != int(len(set(ranword)))):
    ranword = random.choice(wordlist)
    ranword = ranword.rstrip('\n')
    ranword = ranword.lower()
    ranwordl = len(ranword)
    if (int(len(ranword)) == int(len(set(ranword)))) and (ranwordl == usrwordl):
        break

#prints instructions
print("")
time.sleep(0.75)
print("Ok, a unique, random " + str(usrwordl) + " letter word has been generated.\n")
time.sleep(0.75)

#creates function that displays rules
def printrules():
    print("Rules:\n")
    time.sleep(0.75)
    print("1. You have unlimited guesses to figure out what it is. Clues about the word will be given with each guess.")
    time.sleep(0.75)
    print("2. Your guess must be a real word, have all unique letters, same amount of letters as the chosen word and made of only letters.")
    time.sleep(0.75)
    print("3. If these guessing requirements are not met, 'Try Again' will be printed below your illegitimate guess.")
    time.sleep(0.75)
    print("4. A \U0001F7E8 means a letter is present in your guess and the chosen word but is incorrectly placed.")
    print("5. A \U0001F7E9 means a letter is present in your guess, the chosen word and is correctly placed.")
    time.sleep(0.75)
    print("6. Each clue refers to one letter in your guess but can change in your next guess based on the letter order.\n")

needsrules = input("Do you need to see the rules? Type 'yes' if so: ")
print("")
if needsrules == "yes":
    printrules()

#starts guessing program
guesses = guesses + 1
guess = input("Guess " + str(guesses) + " : ")

while guess != ranword:
    if len(guess) == len(ranword) and len(set(guess)) == len(guess) and guess.isalpha() is True:
        realword = False
        for word in wordlist:
            word = word.rstrip('\n')
            word = word.lower()
            if str(guess) == str(word):
                realword = True
        if realword == True:
            #uses indexes to check for similar characters
            for char in guess:
                if char in ranword:
                    if char in ranword and guess.index(char) == ranword.index(char):
                        #prints green square
                        print("\U0001F7E9", end="")
                    else:
                        #prints yellow square
                        print("\U0001F7E8", end="")
            #guessing again
            print("")
            print("")
            guesses = guesses + 1
            guess = input("Guess " + str(guesses) + " : ")

        else:
            print("Try Again\n")
            guess = input("Guess " + str(guesses) + " : ")

    else:
        print("Try Again\n")
        guess = input("Guess " + str(guesses) + " : ")

#win message
print("\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\n")
if guesses == 1:
    print("\U0001F389 Correct! You guessed the word in one try!")
else:
    print("\U0001F389 Correct! You guessed the word in " + str(guesses) + " tries!")
