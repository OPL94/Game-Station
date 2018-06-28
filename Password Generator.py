#The code below is used to generate strong passwords.

#the dictionaries word_dict and numb_dict below associates a letter with a number.
from random import *

word_dict = {'a':1,
             'b':2,
             'c':3,
             'd':4,
             'e':5,
             'f':6,
             'g':7,
             'h':8,
             'i':9,
             'j':10,
             'k':11,
             'l':12,
             'm':13,
             'n':14,
             'o':15,
             'p':16,
             'q':17,
             'r':18,
             's':19,
             't':20,
             'u':21,
             'v':22,
             'w':23,
             'x':24,
             'y':25,
             'z':26}

#numb_dict is a dictionary that associates all keys (numbers) with values (characters).
numb_dict = {0:'£',
             1:'a',
             2:'b',
             3:'c',
             4:'d',
             5:'e',
             6:'f',
             7:'g',
             8:'h',
             9:'i',
             10:'j',
             11:'k',
             12:'l',
             13:'m',
             14:'n',
             15:'o',
             16:'p',
             17:'q',
             18:'r',
             19:'s',
             20:'t',
             21:'u',
             22:'v',
             23:'w',
             24:'x',
             25:'y',
             26:'z',
             27:'!',
             28:'$',
             29:'1',
             30:'2',
             31:'3',
             32:'4',
             33:'5',
             34:'6',
             35:'7',
             36:'8',
             37:'9',
             38:'0'}
             

#Requests the user to input the desired length of the password             
pass_len = int(input("Please state how many characters you would like your password to have: "))
pass_gen = []

#Loops to generate random numbers to create password.
for x in range(1,pass_len + 1):
    pass_gen_number = randint(0,38)
    pass_gen.append(pass_gen_number)

#Adds the letters from the pass_gen list to the new_pass (actual password string)
new_pass = ""
for y in pass_gen:
    new_pass = new_pass + numb_dict[y]

print(new_pass)
print(pass_gen)
