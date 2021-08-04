#implementation of many functions on files

#//
##translitrating the pos file
import re
import json
import transliteration
import posTranslit

y_text = open("posfile.txt", 'r', encoding="utf8")
pos_text = y_text.read()
y_text.close()

new_text = translitration.translit(pos_text)

with open("pos_file.txt", "w", encoding="utf-8") as f:
    f.write(new_text)

#//

##Tigrinya Word List
word_text = open("wordlist_file.txt", 'r', encoding="utf8")
word_li = word_text.read()
word_text.close()

regex = '[0-9]+\s*'        
word_li = re.sub(regex, '', word_li)

with open("word_list.txt", "w", encoding="utf-8") as f:
    f.write(word_li)

word_li = word_li.split('\n')

#//

##orginizing the pos_file into dictionaries in list, keys  to words and values to POS.
import re

#reading the pos_file which is translitrated
my_text = open("pos_file.txt", 'r', encoding="utf8")
pos_text = my_text.read()
my_text.close()

new_text = pos_text.replace('\n', '') #remove newlines
new_text = new_text.replace('<s', '') #remove '<s'
new_text = new_text.replace(' ', '') #remove spaces
new_text = new_text.replace('type=', '') #remove 'type='

#each sentence in a list
sentence_list = new_text.split('</s>')[1:-1] #remove the first and the last empyt elements of the sentence list

#all the POSes 
#[N, N_V, N_PRP, PRO, V, V_PRF, V_IMF, V_IMV, V_GER, V_AUX, V_REL, ADJ, ADV, PRE, CON, INT, NUM, PUN, FW, UNC]

#a pattern that picks words and thier pos value
pattern = '"(N|N_V|N_PRP|PRO|V|V_PRF|V_IMF|V_IMV|V_GER|V_AUX|V_REL|ADJ|ADV|PRE|CON|INT|NUM|PUN|FW|UNC)">(.*?)<'

sente_organized = []
for sente in sentence_list:
    match = re.findall(pattern, sente)
    sente_organized.append(match)

senten_in_dict = []
for list_ in sente_organized:
    keys_ = []
    values_ = []
    for set_ in list_:
        values_.append(set_[0])
        keys_.append(set_[1])
    senten_in_dict.append(dict(zip(keys_, values_)))
    keys_ = []
    values_ = []

#save the sente_in_dict file as json
with open('dicted_sentence.json', 'w') as file:
    json.dump(senten_in_dict, file)


#//

##all gerundive verbs

v_aux = []
v_ger_geez = []
keys__ = list(posTranslit.pos_dict.keys())
values__ = list(posTranslit.pos_dict.values())

p = 0
while p < len(keys__):
    if values__[p] =='V_AUX':
        v_aux.append(keys__[p])
        #v_ger_geez_.append(posTranslit.translitration.revers_translit(keys__[p]))
    p += 1


#//
