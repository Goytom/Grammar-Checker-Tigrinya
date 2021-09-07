##Reorganizing the POS File -pos_file.txt-

import re 
import transliteration

##Organizing in a dictionary file, the words as keys and the POS -
##tag as their values
my_text = open("pos_file.txt", 'r', encoding="utf8")
pos_text = my_text.read()
my_text.close()

regex = '"(.{,10}">.*)<'     
match = re.findall(regex, pos_text)
pos_text_out = str(list(match))[1:-2]

list_ = pos_text_out.split(",")

i = 0
new_list = []
while i < len(list_):
    x = list_[i].split('\">')
    new_list.append(x)
    i += 1

k = 0
pos_keys = []
pos_values = []
pos_dict = {}  #the dictionary file of pos
while k < len(list_):
    pos_keys.append(new_list[k][1][:-1])
    pos_values.append(new_list[k][0][2:])
    k += 1

pos_dict = dict(zip(pos_keys, pos_values))

#print(pos_dict[translitration.translit('ከደ')])
