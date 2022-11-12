# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
from itertools import count
from mailbox import MMDFMessage
from ntpath import join
import random
import string
import warnings

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    hold = list(letters_guessed)
    for i in secret_word:
      if i in hold:
        hold.remove(i)
      else: 
        return(False)    
    return(True)
# is_word_guessed('apple', ["a", "i" ,"p", "p", "e"])

def is_letter_guessed(guess, secret_word, letters_guessed):
    '''
    check letter
    '''
    if (guess in secret_word) & (guess != " "):
      return True
    else: 
      return(False)    

def get_guessed_word(secret_word, letters_guessed):
  '''
  secret_word: string, the word the user is guessing
  letters_guessed: list (of letters), which letters have been guessed so far
  returns: string, comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
  '''
  # FILL IN YOUR CODE HERE AND DELETE "pass"
  hold = list(letters_guessed)
  guessed_word = []
  for i in secret_word:
    if i in hold:
      guessed_word.append(i)
      hold.remove(i)
    else:
      guessed_word.append("_") 
  return(" ".join(guessed_word))

# get_guessed_word('apple', ["m", "i" ,"k", "p", "e"])
# multiple append
def multi_append(guess, secret_word, letters_guessed):
  for i in secret_word:
    if i == guess:
      letters_guessed.append(guess)
  # print(letters_guessed)

# multi_append('p', 'apple', letters_guessed = [])
def get_available_letters(letters_guessed = " "):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = []
    for i in string.ascii_lowercase:
      if i not in letters_guessed:
        all_letters.append(i)
    return(all_letters)
    
# get_available_letters()

# Python3 code to remove whitespace
def remove(string):
    return "".join(string.split())

# print(remove("a_ _ le"))
def hangman(secret_word):

  '''
  secret_word: string, the secret word to guess.
  
  Starts up an interactive game of Hangman.
  
  * At the start of the game, let the user know how many 
    letters the secret_word contains and how many guesses s/he starts with.
    
  * The user should start with 6 guesses

  * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.
  
  * Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a letter!
  
  * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computer's word.

  * After each guess, you should display to the user the 
    partially guessed word so far.
  
  Follows the other limitations detailed in the problem write-up.
  '''
  # FILL IN YOUR CODE HERE AND DELETE "pass"
  # Varaibles
  count = 0
  num_of_guess = 6
  warnings = 3
  letters_guessed = []
  bin = []
  consonants = "bcdfghjklmnpqrstvwxyz"
  vowels = "aeiou"
  unique_letter = 0


  #  Count secret word
  for i in secret_word:
    count += 1
  
  # Welcome interaction
  print("Welcome to the Game HangMan 😃")
  print(f"I am thinking of a that is {count} letters long")
  print("-------------")
  print(f"You have {num_of_guess} guesses")
  print(f"Available ketters: {get_available_letters()}")
  print("Goodluck")

  # Getting user input
  while (is_word_guessed(secret_word, letters_guessed) != True) & (num_of_guess > 0):
    guess = input("Please guess a letter: ")
    # Formatting user input
    guess.lower()
    # check if guess is an alphabet
    if guess not in string.ascii_lowercase:
      print(f"{guess} is not an alphabet, you can only guess alphabets")
      if warnings > 0:
        warnings -= 1
      else:
        num_of_guess -= 1
      # print(f"you have {warnings} Warnings and {num_of_guess} Guesses left")
    # checks is guess has been made before
    elif guess in bin:
      print(f"You have already guessed this letter")
      if warnings > 0:
        warnings -= 1
      else:
        num_of_guess -= 1
      # print(f"you have {warnings} Warnings and {num_of_guess} Guesses left")
    #checks guess validity
    else:
      bin.append(guess)
      if is_letter_guessed(guess, secret_word, letters_guessed) == True:
        multi_append(guess, secret_word, letters_guessed)
        print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        unique_letter += 1
      else:
        if guess in consonants:
          num_of_guess -= 1
        elif guess in vowels:
          num_of_guess -= 2
        print(f"Oops! That letter is not in my word:: {get_guessed_word(secret_word, letters_guessed)}")
    print("-------------")
    print(f"you have {warnings} Warnings and {num_of_guess} Guesses left")
    print(f"Available ketters: {get_available_letters(bin)}")
  
  #Game end
  # Unique letters
  
  # unique_letter = 0
  score = num_of_guess * unique_letter
  if is_word_guessed(secret_word, letters_guessed) == True:
    print(f"You won, your total score is {score} ")
  else:
    print(f"You are out of Guesses, the word is {secret_word}")

# subtracting wrong guess
# 

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

# secret_word = choose_word(wordlist)
# hangman(secret_word)


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # rubbish solution
    my_word_list =[]
    other_word_list =[]

    # remove space
    no_space = remove(my_word)

    # changing from strings to list
    for i in no_space:
      my_word_list.append(i)
    for i in other_word:
      other_word_list.append(i)
  
    # comparing words
    if len(no_space) == len(other_word):
      for i in no_space:
        if (i != "_"):
          if (my_word_list[0] != other_word_list[0]):
            return(False)
          elif (no_space.count(i) != other_word.count(i)):
            return False
        my_word_list.pop(0)
        other_word_list.pop(0)
      return True

# Tests
# print(match_with_gaps("te_ t", "tact"))
# print(match_with_gaps("app _e", "apple"))
# print(match_with_gaps("ap _ le", "apple"))
# print(match_with_gaps("t_ _ t", "tits"))



#  & (is_letter_guessed(i, other_word, my_word_list) == True) & (i != "_") & my_word_list.count(i) != other_word.count(i)
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_string = "".join(my_word)
    collection = []
    for word in wordlist:
      if match_with_gaps(my_string, word) == True:
        collection.append(word)
    return(collection)

# show_possible_matches("t_ _ t")

def hangman_with_hints(secret_word):
  '''
  secret_word: string, the secret word to guess.
  
  Starts up an interactive game of Hangman.
  
  * At the start of the game, let the user know how many 
    letters the secret_word contains and how many guesses s/he starts with.
    
  * The user should start with 6 guesses
  
  * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.
  
  * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
    
  * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computer's word.

  * After each guess, you should display to the user the 
    partially guessed word so far.
    
  * If the guess is the symbol *, print out all words in wordlist that
    matches the current guessed word. 
  
  Follows the other limitations detailed in the problem write-up.
  '''
  # FILL IN YOUR CODE HERE AND DELETE "pass"
  count = 0
  num_of_guess = 6
  warnings = 3
  letters_guessed = []
  bin = []
  consonants = "bcdfghjklmnpqrstvwxyz"
  vowels = "aeiou"
  unique_letter = 0


  #  Count secret word
  for i in secret_word:
    count += 1
  
  # Welcome interaction
  print("Welcome to the Game HangMan 😃")
  print(f"I am thinking of a that is {count} letters long")
  print("-------------")
  print(f"You have {num_of_guess} guesses")
  print(f"Available ketters: {get_available_letters()}")
  print("Goodluck")

  # Getting user input
  while (is_word_guessed(secret_word, letters_guessed) != True) & (num_of_guess > 0):
    guess = input("Please guess a letter: ")
    # Formatting user input
    guess.lower()
    # check if guess is an alphabet
    if guess == "*":
      # print(letters_guessed)
      print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
    elif guess not in string.ascii_lowercase:
      print(f"{guess} is not an alphabet, you can only guess alphabets")
      if warnings > 0:
        warnings -= 1
      else:
        num_of_guess -= 1
      # print(f"you have {warnings} Warnings and {num_of_guess} Guesses left")
    # checks is guess has been made before
    elif guess in bin:
      print(f"You have already guessed this letter")
      if warnings > 0:
        warnings -= 1
      else:
        num_of_guess -= 1
      # print(f"you have {warnings} Warnings and {num_of_guess} Guesses left")
    #checks guess validity
    else:
      bin.append(guess)
      if is_letter_guessed(guess, secret_word, letters_guessed) == True:
        multi_append(guess, secret_word, letters_guessed)
        print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        unique_letter += 1
      else:
        if guess in consonants:
          num_of_guess -= 1
        elif guess in vowels:
          num_of_guess -= 2
        print(f"Oops! That letter is not in my word:: {get_guessed_word(secret_word, letters_guessed)}")
    print("-------------")
    print(f"you have {warnings} Warnings and {num_of_guess} Guesses left")
    print(f"Available ketters: {get_available_letters(bin)}")
  
  #Game end
  # Unique letters
  
  # unique_letter = 0
  score = num_of_guess * unique_letter
  if is_word_guessed(secret_word, letters_guessed) == True:
    print(f"You won, your total score is {score} ")
  else:
    print(f"You are out of Guesses, the word is {secret_word}")

# subtracting wrong guess
# 

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

# secret_word = choose_word(wordlist)
# hangman(secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
# secret_word = choose_word()
hangman_with_hints("tilt")
