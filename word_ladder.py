#!/bin/python3
from collections import deque

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    ourStack = []
    ourStack.append(start_word)
    ourQueue = deque(end_word)
    
    while len(ourQueue >0):
        ourLadder = ourQueue.popleft()
        nxtWord = dictionary_files[ourLadder[-1]]
        for x in nxtWord:
            if _adjacent(start_word,end_word):
                wordList = list(ladder)
                wordList.append(nxtWord)
            if nxt_word == end_word:
                return wordList
            if nxt_word not in ourStack:
                ourStack.append(nxt_word)
                ourQueue.append(wordList)
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
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
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
