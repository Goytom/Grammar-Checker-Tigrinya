## Sentence Tokenization
import re
from posTranslit import*
from transliteration import*

#Reading input data
"""my_text = open("input_text.txt", 'r', encoding="utf8")
text = my_text.read()
my_text.close()"""

def sentence_tokenizer(input_te):
    input_te = re.sub("(\n){1,3}", '', input_te, re.MULTILINE) #remove one or more newlines
    input_te = re.sub('\. *', ' ._', input_te)
    input_te = re.sub('\? *', ' ?_', input_te)
    input_te = re.sub('\! *', ' !_', input_te)
    sentence_token = input_te.split('_')
    
    n = 0
    while n < len(sentence_token):
        sentence_token[n] = sentence_token[n].split(' ')
        n += 1
    sentence_token = sentence_token[:-1]          #remove the last empty string element
    
    return sentence_token

## POS Tagging, with an input of a list of words tokenized
def pos_tagger(tokenized):
    s = len(tokenized)
    pos_tagged = []
    k = 0
    while k < s:
        try:
            pos_tagged.append(pos_dict[tokenized[k]])
        except:
            pos_tagged.append('**')
        k += 1
    return pos_tagged



gg = translit("""ነቲ እንኮ ሓቀኛ ኣምላኽ ኢዮም ዘምልኹ ነይሮም ።""")
gg_ = gg.split()

#print(dict(zip(gg_, pos_tagger(gg_))))
print(pos_tagger(gg_))

