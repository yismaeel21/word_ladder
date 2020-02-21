from collections import deque
import copy

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
    while len(ourQ) != 0:        #while our queue is non-empty
        top = ourQ.pop()
        for word in words: #for each word in the dictionary
            to_remove=[]
            if _adjacent(word,top[-1]):
                stackCopy = copy.deepcopy(top)
                stackCopy.append(word)
                #ourQ.appendleft(stackCopy) 
                if word == end_word:
                    for i in range(1,len(stackCopy)-2):
                        if _adjacent(top[i-1],top[i+1]):
                            stackCopy.pop(i)
                    return (stackCopy)
                ourQ.appendleft(stackCopy)
                words.remove(word)


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
"word_ladder.py" 65L, 2415C written                                     31,44         Top
