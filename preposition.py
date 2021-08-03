#//

preposition = {'qedemi': '*', 'nāye': '*', 'ıābe': '*', 'nābe': '*', 'nāyezi': 'PRP_Ssm3', 'kābe': '*', 'kabābi': '*', 'kesābe': '*', 'leüeli': '*', 'reıesi': '*', 'nelāüeli': '*',
 'majamaretā': '*', 'teḥeti': '*', 'dadeḥeriıu': 'PRP_sm3', 'kenedeıu': 'PRP_sm3 ', 'deḥeri': '*', 'neleüeli': '*', 'wešeṭi': '*', 'mawadāıetā': '*', 'ṭeöā': 'PRP_sm3',
 'ċāfe': '*', 'wayo': '*', 'qedeme': '*', 'wešeṭene': '*', 'beöedemi': '*', 'bedeḥeri': '*', 'bedeḥeriıu': 'PRP_sm3', 'manego': '*', 'neıegeramagadenā': 'PRP_p-1', 
 'goni': '*', 'fitafite': '*', 'neneyawe': '*', 'māıekalāye': '*', 'lāüelene': '*', 'tāḥetene': '*', 'leüeliıu': 'PRP_sm3', 'newešeṭi': '*', 'segeru': '*', 
 'bemaneguıome': '*', 'yamāne': '*', 'ṣagāme': '*', 'netāḥeti': '*', 'segere': '*', 'maneGa': '*', 'māüedo': '*', 'be': '*', 'ne': '*', 'lāüeli': '*', 
 'lāüelu': '*', 'kakābe': '*', 'nenāye': '*', 'dāregā': '*', 'benāye': '*', 'gonexi': 'PRP_sf2', 'wešeṭā': 'PRP_sf3', 'nedaga': '*', 'qedemite': '*', 'wešeṭu': 'PRP_sm3', 
 'leüelaıā': 'PRP_sf3', 'deḥāre': '*', 'qedemaıā': 'PRP_sf3', 'fitu': 'PRP_sm3', 'fite': '*', 'ṭeqāıā': 'PRP_sf3', 'dāḥāresi': '*', 'qedemiıome': 'PRP_pm3', 'māıekalome': 'PRP_pm3', 
 'teḥetiıome': 'PRP_pm3', 'leüeliıome': 'PRP_pm3', 'beyamāna-ṣagāme': '*', 'dāḥerāye': '*', 'neyamāna-ṣagāme': '*', 'yamāna-ṣagāme': '*', 'nedeḥerite': '*', 
 'nedaḥāre': '*', 'nanābe': '*', 'mawadāıetāse': '*', 'nedeḥeri': '*', 'bedeḥerite': '*', 'leüelanā': '*', 'ıegerā': 'PRP_sf3', 'qedemiıā': 'PRP_sf3', 'teḥetene': '*', 
 'deḥerene': '*', 'keneyo': '*', 'kino': '*', 'monego': '*', 'goni-goni': '*', 'leüeléxā': 'PRP_sm3', 'māüera-māüera': '*', 'beleüelene': '*', 'bewešeṭene': '*', 
 'bemāüedo': '*', 'yamānene': '*', 'ṣagāmene': '*', 'nedeḥeréxā': '*', 'neöedeméxā': 'PRP_sm3', 'ıāgā': '*', 'majamaretāne': '*', 'mawadāıetāne': '*', 
 'qedeméxā': 'PRP_sm3', 'majamareyā': '*', 'waṣāıine': '*', 'ıābaya': '*', 'mawadāıetāıu': 'PRP_sm3', 'moneGa': '*', 'qedemaıu': 'PRP_sm3', 'monegonā': '*', 'begoni': '*', 
 'zāgiteka': '*', 'keneyawe': '*', 'qadādeme': '*', 'gaṣaye': '*', 'qedemaye': '*', 'leüeliıā': 'PRP_sf3', 'mawadāıeteıu': 'PRP_sm3', 'mawadāıetāxa': 'PRP_sm2', 
 'ıāneṣārekā': 'PRP_sm2', 'beöedemaxā': 'PRP_sm2', 'neöedeme': '*', 'godenu': 'PRP_sm3', 'qedemine': '*', 'deḥerine': '*', 'beleüeli': '*', 'Kino': '*', 'nemāıekele': '*', 
 'Gani': '*', 'leüeliıune': 'PRP_sm3', 'beċāfu': 'PRP_sm3', 'beöedemite': '*', 'bemāıekale': '*', 'deḥerite': '*', 'ıāıābe': '*', 'reıesiıu': 'PRP_sm3', 'kineyeıu': 'PRP_sm3', 
 'kābene': '*', 'nābene': '*'}



def morphPrep(word):
    return preposition[word]

print(morphPrep('wešeṭaye'))

