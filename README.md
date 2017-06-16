# DukeTip
#Hangman Python
import numpy
word_list=['potato', 'jazz', 'spectacular' 'fox']#dictionary to pull words from
letter=raw_input('PLease input letter:')
current_word=numpy.random.choice(word_list)

#ASCII art below
print      '-------'
print      '|     |'
print      '|'
print      '|'
print      '|'
print      '|'
print      '|'
print      '|____________'
