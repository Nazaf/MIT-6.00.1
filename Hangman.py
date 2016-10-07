#Is word guessed
#To check is the secret word is in Guessed word or not.

def isWordGuessed(secretWord, lettersGuessed):
     return all(letter in lettersGuessed for letter in secretWord)


# 2. Printing out the Users gusses. if the guess doesn't match, it replaces the string with _

def getGuessedWord(secretWord, lettersGuessed):
    newWord = ""
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            newWord += secretWord[i]
        else:
            newWord += " _ "
    return newWord
