from collections import deque
from copy import deepcopy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
   A function that creates a word ladder that links one word to another in the quickest possible way
    '''
    if start_word == end_word:
        return [start_word]

    ourStack = []         #Creating A Stack
    ourStack.append(start_word)  #pushing our starting word to the stack
    ourQ = deque()    #starting a queue with our target word
    ourQ.appendleft(ourStack)    #enqueuing stack onto queue
    word_file = open(dictionary_file).readlines()
    words = []

    for x in word_file:
        words.append(x.strip("\n"))

    while len(ourQ) > 0:        #while our queue is non-empty
        top = ourQ.popleft()
        lastWord = top[-1]
        for word in words: #for each word in the dictionary
            if _adjacent(word,lastWord):
                stackCopy = copy.copy(top)
                stackCopy.append(word)
        #        print("stackCopy=", stackCopy)
                ourQ.appendleft(stackCopy)
       #         print("Len(Words)=",len(words))
                if end_word == word:
                    return stackCopy
                words.remove(word)
    #I think my issue stems from me changing the words file itself and after one iteration there ceases to be any words left in the list!
    return

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if ladder == []:
        return False
    for word1,word2 in zip(ladder, ladder[1:]):
        if not _adjacent(word1, word2):
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
