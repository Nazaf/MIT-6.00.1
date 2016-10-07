#Is word guessed
#To check is the secret word is in Guessed word or not.

def isWordGuessed(secretWord, lettersGuessed):
     return all(letter in lettersGuessed for letter in secretWord)
