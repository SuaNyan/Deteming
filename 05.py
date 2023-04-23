import re
str = "I am an NLPer"
list = str.split()
N = int(input())

def letter_N_gram(N, sentence):
    splited_str = [sentence[x:x+2] for x in range(0, len(sentence), 2)]
    return splited_str



print(letter_N_gram(N, list))
#for i in range(len(N)):
    