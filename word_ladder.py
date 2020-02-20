#!/bin/python3
from collections import deque
from copy import deepcopy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
   A function that creates a word ladder that links one word to another in the quickest possible way
    '''
    wordList = []         #Creating A Stack
    wordList.append(start_word)  #pushing our starting word to the stack
    ourQ = deque()    #starting a queue with our target word
    ourQ.append(wordList)    #enqueuing stack onto queue
   
    f = open(dictionary_file).readlines()
    L = []
    
    for x in f:
        noLines= x.replace("\n","")
        L.append(noLines)
    while len(ourQ) != 0:        #while our queue is non-empty
        i = ourQ.pop()              #dequeu stack from our queue
        for word in L: #for each word in the dictionary
            if _adjacent(word,wordList[0]):          #if the word is adjacent to top of stack
                if word == end_word:                     #if this word is the end word
                    wordList.append(word)            #append the list and this is our word ladder
                    return wordList
                copyList = deepcopy(wordList)
                copyList.append(word)
                ourQ.appendleft(copyList)
                dictionary_file.pop(word)
    return None

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if len(ladder) == 0:
        return False
    for k in range(len(ladder)-1):
        if not _adjacent(ladder[k], ladder[k+1]):
            return False
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
