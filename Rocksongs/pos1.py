from nltk import pos_tag
from nltk.tokenize import word_tokenize
 
s = "This is a sample sentence. Brown corpus is used here ."
tokens = word_tokenize(s) # Generate list of tokens
tokens_pos = pos_tag(tokens) 
 
print(tokens_pos)
