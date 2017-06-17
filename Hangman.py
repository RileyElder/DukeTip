import numpy
import sys
word_list=['potato', 'jazz', 'spectacular', 'fox']#dictionary to pull words from
"""I know this is bad
and non-scalable, but I have no other solution"""
current_word=numpy.random.choice(word_list) #chooses random word
letters_wrong=0 #letters wrong counter
letters_correct=[]
#ASCII art below
a_h=['_______','|     |','|','|','|','|','|','|____________']

while letters_wrong<=7:
    if letters_wrong>=0: #adds hangman as wrong guesses increase
       print (a_h[0]+ "\n" + a_h[1] + "\n" + a_h[2]+'     0'+ "\n"+a_h[3] +"\n"+ a_h[4] +"\n"+ a_h[5] +"\n"+ a_h[6] +"\n"+ a_h[7])

    if letters_wrong>=1:
        print (a_h[0]+ "\n" + a_h[1] + "\n" + a_h[2]+'     0' + "\n"+a_h[3] +'     |'+"\n"+ a_h[4] +"\n"+ a_h[5] +"\n"+ a_h[6] +"\n"+ a_h[7])

    if letters_wrong>=2:
        print (a_h[0]+ "\n" + a_h[1] + "\n" + a_h[2]+'     0' + "\n"+a_h[3]+'     |'+"\n"+ a_h[4]+'      \\' +"\n"+ a_h[5] +"\n"+ a_h[6] +"\n"+ a_h[7])

    if letters_wrong>=3:
        print (a_h[0]+ "\n" + a_h[1] + "\n" + a_h[2]+'     0' + "\n"+a_h[3]+'     |' +"\n"+ a_h[4] +'    /'+' \\'+"\n"+ a_h[5] +"\n"+ a_h[6] +"\n"+ a_h[7])

    if letters_wrong>4:
        print (a_h[0]+ "\n" + a_h[1] + "\n" + a_h[2]+'     0' + "\n"+a_h[3]+'     |' +"\n"+ a_h[4]+'    /'+' \\'+"\n"+ a_h[5]+'     |' +"\n"+ a_h[6] +"\n"+ a_h[7])

    if letters_wrong>5:
        print (a_h[0]+ "\n" + a_h[1] + "\n" + a_h[2]+'     0' + "\n"+a_h[3]+'     |' +"\n"+ a_h[4]+'    /'+' \\'+"\n"+ a_h[5]+'     |'+"\n"+ a_h[6]+'    /' +"\n"+ a_h[7])

    if letters_wrong>6:
        print (a_h[0]+ "\n" + a_h[1] + "\n" + a_h[2]+'     0' + "\n"+a_h[3]+'     |' +"\n"+ a_h[4]+'    /'+' \\'+"\n"+ a_h[5]+'     |'+"\n"+ a_h[6]+'    /'+' \\' +"\n"+ a_h[7])

    solved=True
    for letter in current_word:
        if letter in letters_correct:
            print letter+' ',
        else:
            print "_ ",
            solved=False
    print''
    if solved==True:
        sys.exit('Congratulations!')

    letter=''
    while len(letter)!=1:
        letter=raw_input('Please input letter:')
    letter=letter.lower()
    if letter in current_word.lower():
       print 'Correct'
       letters_correct.append(letter)
    else:
        letters_wrong=letters_wrong+1
else:
    sys.exit('Try Again') #ends game if hangman is completed