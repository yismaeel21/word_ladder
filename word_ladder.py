#!/bin/python3
from collections import deque
from copy import deepcopy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
   A function that creates a word ladder that links one word to another in the quickest possible way
    '''
    wordList = []         #Creating A Stack
    wordList.append(start_word)  #pushing our starting word to the stack
    ourQueue = deque()    #starting a queue with our target word
    ourQueue.append(wordList)    #enqueuing stack onto queue
   
    f = open(dictionary_file)
    f.readlines()
    while len(ourQueue) > 0:        #while our queue is non-empty
        i = ourQueue.pop()              #dequeu stack
        for x in range(len(f)): #for each word in the dictionary
            current = f[x]
            if _adjacent(current,i):          #if the word is adjacent to top of stack
                if current == end_word:                     #if this word is the end word
                    wordList.append(current)            #append the list and this is our word ladder
                    return wordList
                copyList = deepcopy(wordList)
                copyList.append(current)
                ourQueue.appendleft(copyList)
                f[x]=''
    return None

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if len(ladder) == 0:            #if it's an empty list, return false
        return False
    for x in range(len(ladder)-1):  #for loop that runs the entire length of the ladder list
        current = ladder[x]         #setting our current value
        nxt = ladder[x+1]           #setting our neighboring value
        if _adjacent(current, nxt) == False:    #checking if they're not adjacent
            return False                        #if not returns false, otherwise keep going
    return True

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise
    '''
    
    if len(word1)== len(word2):  #checks if both words are the same length
        numdifs = 0              #assuming there are no differences between the two words   
        for x,y in zip(word1, word2):      #pairing the words one for one and seeing if they're similar
            if x!= y:              #if they're not similar, we increment numdifs by one
                if numdifs:         #if numdifs is 1 or greater, they're not adjacent
                    return False
                numdifs +=1
        return True
    else:
        return False
