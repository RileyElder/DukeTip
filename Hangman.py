import numpy
word_list=['potato', 'jazz', 'spectacular', 'fox']#dictionary to pull words from
letter_list1=['p', 'o', 't', 'a']
letter_list2=['j','a','z']
letter_list3=['s','p' 'e', 'c,','t','a' 'u', 'l','r',]
letter_list4=['f','o','x']
"""I know this is bad
and non-scalable, but I have no other solution"""
current_word=numpy.random.choice(word_list) #chooses random word
all_letters=0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8
letters_wrong=0 #letters wrong counter
if current_word[0]=='p':
    l_d=letter_list1
elif current_word[0]=='j':
    l_d=letter_list2
elif current_word[0]=='s':
    l_d=letter_list3
else:
    l_d=letter_list4
#ASCII art below
a_h=['_______','|     |','|','|','|','|','|','|____________']
ascii_hang_origin = a_h[0]+ "\n" + a_h[1] + "\n" + a_h[2] + "\n"+a_h[3] +"\n"+ a_h[4] +"\n"+ a_h[5] +"\n"+ a_h[6] +"\n"+ a_h[7]
print ascii_hang_origin
print "_ "*len(current_word)#creates correct number of underlines
letter=raw_input('Please input letter:')
for letter in l_d:
    if letter==(l_d[0] or l_d[1] or l_d[2] or l_d[3] or l_d[4] or l_d[5] or l_d[6] or l_d[7] or l_d[8]):
        print 'Correct'
    else:
        letters_wrong+1
if letters_wrong>0: #adds hangman as wrong guesses increase
   print (a_h[2]+'      0')
if letters_wrong>1:
    print (a_h[3]+'      |')
if letters_wrong>2:
    print (a_h[4]+"     \\")
if letters_wrong>3:
    print (a_h[4]+'        /')
if letters_wrong>4:
    print (a_h[5]+'      |')
if letters_wrong>5:
    print (a_h[6]+'     /')
if letters_wrong>6:
    print (a_h[6]+'        \\')