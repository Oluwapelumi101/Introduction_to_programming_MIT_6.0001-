# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <Azeez>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string
import copy
from copy import deepcopy

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME , 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
# print(get_frequency_dict('applee'))
# (end of helper code)
# -----------------------------------

# This is a function to check if word is in hand
def check_hand(word, hand):
    hand_copy = deepcopy(hand)
    for i in word.lower():
        if (hand_copy.get(i, False) == False) or (hand_copy.get(i, False) == 0):
            return(False)
        else:
            hand_copy[i] = hand_copy[i] - 1
    return(True)
        
# print(check_hand('Rapture', {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}))
#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word.lower()
    comp_one = 0
    comp_two = 0

    # component one
    for i in word.lower():
        comp_one += SCRABBLE_LETTER_VALUES[i]
    # component Two
    comp_two = (7 * len(word)) - (3 * (n- len(word)))
    # print(comp_one, comp_two)
    if comp_two <= 0:
        comp_two = 1
    # final score
    score = comp_one * comp_two
    return(score)

# print(get_word_score( 'was', n=7))

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={'*':1,}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand
# print(deal_hand(7))
#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = {}
    hand_copy = deepcopy(hand)
    word_formatted = word.lower()
    for i in hand:
        if (i in word_formatted) & ((hand_copy[i] - word_formatted.count(i)) != 0):
            new_hand[i] = new_hand.get(i, 0) + 1
        elif(i not in word_formatted):
            new_hand[i] = new_hand.get(i, 0) + 1
    return(new_hand)

# new_hand = update_hand({'h': 1, 'e': 1, 'l': 2, 'o': 1}, 'HELLO')
#
# Problem #3: Test word validity
#

# Changes string to list
def string_to_list(word):
    string_to_list = []
    for i in word:
        string_to_list.append(i)
    return(string_to_list)

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word_formatted = word.lower()
    options = []
# for word with wildcard
    if "*" in word_formatted:
        for i in VOWELS:
            option = word_formatted.replace('*' ,i)
            options.append(option)
        for option in options:
            if (option in word_list) & (check_hand(word_formatted, hand) == True ):
                # print(option)
                return(True)
        return(False)
    # for word without wildcard
    if (word_formatted in word_list) & (check_hand(word_formatted, hand) == True ):
        return(True)
    else:
        return(False)
 
# print(is_valid_word('h*ney', {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}, load_words()))

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    counter = 0
    for i in hand:
        counter += hand[i]
    return(counter)
    
    pass  # TO DO... Remove this line when you implement this function
# calculate_handlen( {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2})

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function
    total_score = 0
    # print("Welcome to a Game of Scrabble")
    while hand != {}:
        print("-------------")
        print("Current Hand:", end= " ")
        display_hand(hand)
        word = input("Enter word, or '!!'' to indicate that you are finished:")
# Check to cancel game
        if word == "!!":
            print(f"Game Over. Total score: {total_score}")
            break
        # Check word validity
        elif (is_valid_word(word, hand, word_list) == True):
            total_score += get_word_score(word, calculate_handlen(hand))
            print(f"You have {get_word_score(word, calculate_handlen(hand))} points from {word} and total points of {total_score}")
        else:
            print(f" {word} is not a valid ")
        hand = update_hand(hand, word)
# end sequence
    if hand == {}:
        print(f"Ran out of letters. Total score: {total_score}")
        return(total_score)

# play_hand({'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}, load_words())
#
# Problem #6: Playing a game
# 

#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    letters = []
    n = hand[letter]

    for i in VOWELS:
        if i not in hand:
            letters.append(i)
    for i in CONSONANTS:
        if i not in hand:
            letters.append(i)

    hand[random.choice(letters)] = hand[letter]
    del hand[letter]
    print(hand)
    # new_hand = {random.choice(letters):n}
    # for i in (hand):
    #     if i != letter:
    #         new_hand[i] = new_hand.get(i, 0) + 1
    # print(new_hand)
    return hand
       
# substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')

def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    print("Welcome to a Game of Scrabble")
    rounds = int(input("Enter total number of hands: "))
    sum = 0

    while rounds > 0:
        hand = deal_hand(HAND_SIZE)
        display_hand(hand)
        sub = input("Would you like to subtitute a letter in the hand: ")
        if sub == "yes":
            letter = input("What letter would you like to substitute: ")
            substitute_hand(hand, letter)
        sum += play_hand(hand,word_list)
        print(sum)
        rounds -= 1
   
        replay = input("Would you like to replay the hand? ")
        while replay == "yes" and (rounds != 0):
            sum += play_hand(hand,word_list)
            rounds -= 1
    print(f"Total score for this all hands: {sum}")


    

    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
