Last login: Thu Feb 20 09:47:18 on ttys001

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) Yusufs-MacBook-Pro:~ yasoofy2$ ssh yismaeel@134.173.191.241 -p 5055
yismaeel@134.173.191.241's password: 
Last login: Thu Feb 20 09:47:31 2020 from 134.173.248.16
 _____________________________________________________________________________
/ For the fashion of Minas Tirith was such that it was built on seven levels, \
| each delved into a hill, and about each was set a wall, and in each wall    |
| was a gate.                                                                 |
|                 -- J.R.R. Tolkien, "The Return of the King"                 |
|                                                                             |
|         [Quoted in "VMS Internals and Data Structures", V4.4, when          |
|          referring to system overview.]                                     |
\                                                                             /
 -----------------------------------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
yismaeel@lambda-server:~$ ls
cmc-csci046  firstrepo  fraction  README.md
yismaeel@lambda-server:~$ cd cmc-csci046/
yismaeel@lambda-server:~/cmc-csci046$ ls
hw1  hw2  hw3  lecture_notes  README.md  word_ladder  word_ladder.py
yismaeel@lambda-server:~/cmc-csci046$ vim scope.py
yismaeel@lambda-server:~/cmc-csci046$ ls
hw1  hw2  hw3  lecture_notes  README.md  word_ladder  word_ladder.py
yismaeel@lambda-server:~/cmc-csci046$ cd lecture_notes/
yismaeel@lambda-server:~/cmc-csci046/lecture_notes$ ls
balanced_parens_2.py  examply.py        __pycache__  scope.py
balanced_parens.py    list_vs_deque.py  runtime.py
yismaeel@lambda-server:~/cmc-csci046/lecture_notes$ vim scope.py
yismaeel@lambda-server:~/cmc-csci046/lecture_notes$ vim stacktrace.py
yismaeel@lambda-server:~/cmc-csci046/lecture_notes$ ls
balanced_parens_2.py  examply.py        __pycache__  scope.py
balanced_parens.py    list_vs_deque.py  runtime.py   stacktrace.py
yismaeel@lambda-server:~/cmc-csci046/lecture_notes$ cd..
cd..: command not found
yismaeel@lambda-server:~/cmc-csci046/lecture_notes$ cd ..
yismaeel@lambda-server:~/cmc-csci046$ ls
hw1  hw2  hw3  lecture_notes  README.md  word_ladder  word_ladder.py
yismaeel@lambda-server:~/cmc-csci046$ cd word_ladder/
yismaeel@lambda-server:~/cmc-csci046/word_ladder$ ls
README.md  requirements.txt  tests  word_ladder.py  words5.dict
yismaeel@lambda-server:~/cmc-csci046/word_ladder$ vim word_ladder.py 
yismaeel@lambda-server:~/cmc-csci046/word_ladder$ vim word_ladder.py
yismaeel@lambda-server:~/cmc-csci046/word_ladder$ vim word_ladder.py
yismaeel@lambda-server:~/cmc-csci046/word_ladder$ vim word_ladder.py
yismaeel@lambda-server:~/cmc-csci046/word_ladder$ packet_write_wait: Connection to 134.173.191.241 port 5055: Broken pipe
(base) Yusufs-MacBook-Pro:~ yasoofy2$ ssh yismaeel@134.173.191.241 -p 5055
yismaeel@134.173.191.241's password: 
Last login: Thu Feb 20 14:47:59 2020 from 134.173.248.16
 _________________________________________________
/ For years a secret shame destroyed my peace--   \
| I'd not read Eliot, Auden or MacNiece.          |
| But now I think a thought that brings me hope:  |
| Neither had Chaucer, Shakespeare, Milton, Pope. |
\                 -- Justin Richardson.           /
 -------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
yismaeel@lambda-server:~$ cd cmc-csci046/
yismaeel@lambda-server:~/cmc-csci046$ ls
hw1  hw2  hw3  lecture_notes  README.md  word_ladder  word_ladder.py
yismaeel@lambda-server:~/cmc-csci046$ cd word_ladder/
yismaeel@lambda-server:~/cmc-csci046/word_ladder$ vim word_ladder.py 
yismaeel@lambda-server:~/cmc-csci046/word_ladder$ vim word_ladder.py 
yismaeel@lambda-server:~/cmc-csci046/word_ladder$ vim word_ladder.py 
yismaeel@lambda-server:~/cmc-csci046/word_ladder$ vim word_ladder.py 
yismaeel@lambda-server:~/cmc-csci046/word_ladder$ vim word_ladder.py 
yismaeel@lambda-server:~/cmc-csci046/word_ladder$ vim word_ladder.py 

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
    '''
    if word1 == word2:
        return False
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
                         
