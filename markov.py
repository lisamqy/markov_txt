"""Generate Markov text from text files."""

from hashlib import new
from random import choice



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text = open(file_path).read()
    return text


def make_chains(text):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    
    for word in text: #for every element in the txt file
        word = text.split() #split by whitespace
        

    for i in range(len(word)-2): #for every index in the word list
        
        #get the current word + the word next to it and create a tuple called current_key
        current_key = (word[i], word[i+1]) 
        
        #check if key alrdy exists in chains dict...
        if current_key not in chains: 
            chains[current_key] = [word[i+2]] #add new key:value to chains dict if not alrdy existing
        else:
            chains[current_key].append(word[i+2]) #if alrdy existing, append value to existing key

            #⬆️ is the same as ⬇️ ; below just has more steps

            # current_list =  chains[current_key]
            # current_list.append(word[i+2])        
        
        
    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    #get a random key from chains by using choice()
    #turn the dict_keys into a list so we can then ⬆️
    current_key = choice(list(chains.keys())) #prints current_key as tuple
    # print(current_key)
    chosen_words = [current_key[0], current_key[1]] #force the two words into a list
    # print(chosen_words)
    value = choice(chains[current_key]) #get random value from current key
    # print(value,9)
    
    while value != "I": 
        current_key = (current_key[1],value) 
        words.append(value)
        value = choice(chains[current_key])
    # print (words)    

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
