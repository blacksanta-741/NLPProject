from nltk import pos_tag
from nltk.tokenize import word_tokenize

file1 = open("song1.txt","r")
file2 = open("song2.txt","r")
file3 = open("song3.txt","r")
res = open("ResultPOS.txt","w+")
token1 = ""
token2 = ""
token3 = ""
i = 0
document_0 = file1.read()
document_1 = file2.read()
document_2 = file3.read()
all_documents = [document_0, document_1, document_2]
tokens_pos = [token1,token2,token3]

for d in all_documents:
    tokens = word_tokenize(d)
    tokens_pos[i] = pos_tag(tokens)
    res.write(str(tokens_pos[i]))
    i=i+1


