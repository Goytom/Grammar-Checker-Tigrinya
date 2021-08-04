#Dictionary of prnouns with pos and morphological features tagged

pron_dict = {'kābetome':'PRO_pm3','kābeti':'PRO_sm3','bayenome':'PRO_pm3','beıu':'PRO_sm3','neüānāne':'PRO_p-1',
            'kābeıu': 'PRO_sm2-', 'ıezome': 'PRO_pm3', 'ıeti': 'PRO_sm3', 'neüeıu':'PRO_sm3', 'ıāna': 'PRO_s-1',
            'kameziıome': 'PRO_pm3', 'nati': 'PRO_sm3', 'kāleıote': 'PRO_pm3', 'kameziıā': 'PRO_sf3', 'kameıu': 'PRO_sm3',
            'kābezome': 'PRO_pm3', 'nesu': 'PRO_sm3', 'bayenexā': 'PRO_sm2', 'ıābeti': 'PRO_sm3', 'nābeti': 'PRO_sm3',
            'batome': 'PRO_pm3', 'neüāxā': 'PRO_sm2', 'nesexā': 'PRO_sm2', 'negazāıe-nabesexā': 'PRO_sm2','nātaye': 'PRO_s-1',
            'nenafesewakafenā': 'PRO_p-1', 'neüānā': 'PRO_p-1', 'kābānā': 'PRO_p-1', 'neḥenā': 'PRO_p-1', 'kābezi': 'PRO_sm3',
            'bati': 'PRO_sm3', 'nesexi': 'PRO_sf2', 'nebayenaye': 'PRO_s-1', 'gazāıe-reıesexā': 'PRO_sm2', 'mesāxā': 'PRO_sm2',
            'kamezi': 'PRO_sm3', 'newayo': 'PRO_---', 'nābeıu': 'PRO_sm3', 'natane': 'PRO_pf3', 'mesezi': 'PRO_sm3',
            'bāüelayewene': 'PRO_s-1', 'bāüelexume': 'PRO_pm2', 'nātekume': 'PRO_pm2', 'nesexume': 'PRO_pm2',
            'nesexāne': 'PRO_sm2', 'ıekala': 'PRO_sm3', 'neüāıā': 'PRO_sf3', 'ıetane': 'PRO_pf3', 'negala': 's-3',
            'kābeziıātome': 'PRO_pm3', 'kābetane': 'PRO_pf3', 'meseti': 'PRO_sm3', 'nafesi-wakafenā': 'PRO_p-1',
            'kābetā': 'PRO_sf3',  'manegonā': 'PRO_p-1', 'negoxāne': 'PRO_sm2', 'manegoxume': 'PRO_pm2', 'nazome': 'PRO_pm3',
            'kāleıene': 'PRO_sm3', 'neüeıome': 'PRO_pm3', 'ḥedeḥede': 'PRO_s-3', 'nesātome': 'PRO_pm3', 
            'nātenā': 'PRO_p-1', 'ıābāıu': 'PRO_sm3', 'nābāıu': 'PRO_sm3', 'bāüelu': 'PRO_sm3', 'neüāıu': 'PRO_sm3',
            'nāteki': 'PRO_sf2', 'bāüelexi': 'PRO_sf2', 'deḥeriıu': 'PRO_sm3', 'kābeıā': 'PRO_sf3', 'kābeıome': 'PRO_pm3',
            'bāüelexā': 'PRO_sm2', 'bexamezi': 'PRO_sm3', 'neḥādeḥedome': 'PRO_sm3', 'batā': 'PRO_sf3',
            'mesānā': 'PRO_p-1', 'natome': 'PRO_pm3', 'mesetome': 'PRO_pm3', 'nesome': 'PRO_pm3',
            'meseıu': 'PRO_sm3', 'meseıome': 'PRO_pm3', 'bayenu': 'PRO_sm3', 'qedemiıu': 'sm3', 
            'nesexātekene': 'PRO_pf2', 'nesexene': 'PRO_pf2', 'nesexātekume': 'PRO_pm2', 'nesā': 'PRO_sf3', 
            'nesātane': 'PRO_pf3', 'nesane': 'PRO_pf3', 'nebāüelu': 'PRO_sm3', 'nesomeka': 'PRO_pm3',
            'bāüelome': 'PRO_pm3', 'bāüelenā': 'PRO_p-1', 'negazāıe-reıesenā': 'PRO_p-1', 'kābeıātome': 'PRO_pm3', 
            'kābāxi': 'PRO_sf2', 'beıāxi': 'PRO_sf2', 'nebāüelā': 'PRO_sf3', 'ıābezā': 'PRO_sf3', 'nābāxā': 'PRO_sm2',
            'gazāıe-zégātātāne': 'PRO_Ssf3_Op-3', 'kamānā': 'PRO_s-3', 'nāyetome': 'PRO_pm3', 'meseıane': 'PRO_---',
            'nābeıane': 'PRO_---', 'nebāüelane': 'PRO_pf3', 'neüāye': 'PRO_s-1', 'nebayenu': 'PRO_sm3',
            'gazāıe-nabesu': 'PRO_sm3', 'nexulome': 'PRO_pm3', 'benātome': 'PRO_---', 'neüāxi': 'PRO_sf2',
            'ıābeıu': 'PRO_sm3', 'neüuıu': 'PRO_sm3', 'nafese-wakafenā': 'PRO_p-1', 'ıeziıātomesi': 'PRO_pm3',
            'newayā': 'PRO_---', 'nābeıome': 'PRO_pm3', 'ıātā': 'PRO_sm2', 'ıeziıāse': 'PRO_sf3', 'nābānā': 'PRO_---',
            'nesune': 'PRO_sm3', 'bezāüebāıu': 'PRO_---', 'galane': 'PRO_--3', 'benafesi-wakafe': 'PRO_s--', 
            'ḥādeḥedome': 'PRO_pm3', 'naḥādeḥedome': 'PRO_pm3', 'beıeıu': 'PRO_sm3', 'nātu': 'PRO_sm3',
            'bexameıu': 'PRO_sm3', 'bazene': 'PRO_sm3', 'batene': 'PRO_sm3', 'ıābānā': 'PRO_---',
            'nexamezi': 'PRO_sm3', 'nātātekume': 'PRO_---', 'kenedezi': 'PRO_sm3', 'ıābetome': 'PRO_pm3',
            'nanebayenane': 'PRO_sf3', 'ḥādeḥedanene': 'PRO_sf3', 'nazitāte': 'PRO_sm3', 'benātekā': 'PRO_sm3',
            'kābezene': 'PRO_sm3', 'kābetene': 'PRO_sm3', 'nābezi': 'PRO_sm3', 'kābāxā': 'PRO_sm2',
            'begazāıe-reıesu': 'PRO_sm3', 'meseıā': 'PRO_---', 'gazāıe-reıesā': 'PRO_sf3', 'galiıane': 'PRO_pf3',
            'nātā': 'PRO_---', 'negazāıenabesā': 'PRO_sf3', 'ıeziıātomene': 'PRO_pm3', 'kameıātome': 'PRO_---',
            'beıāıātome': 'PRO_---', 'nafesi-wakafome': 'PRO_pm3', 'nanātome': 'PRO_pm3', 'nātayene': 's-1', 
            'mesāxi': 'PRO_---', 'bayenaye': 'PRO_s-1', 'ḥādeḥedenā': 'PRO_p-1', 'bāüelaye': 'PRO_s-1', 
            'kametā': 'PRO_sf2', 'beıāxā': 'PRO_---', 'naüaıane': 'PRO_pf3', 'naziıome': 'PRO_pm3', 
            'ḥādeḥedu': 'PRO_sm3', 'mesāxume': 'PRO_---', 'nazene': 'PRO_sm3', 'ıābeıā': 'PRO_---', 
            'kameıā': 'PRO_sf3', 'bāüelātome': 'PRO_pm3', 'neüāıātome': 'PRO_pm3', 'gazāıe-üāöemenā': 'PRO_p-1',
            'neüeıune': 'PRO_sm3', 'nafese-wakafe': 'PRO_sm3', 'naneḥedeḥedome': 'PRO_pm3', 'ıezese': 'sm3',
            'nābāye': 'PRO_---', 'kābāxume': 'PRO_sm3', 'ıezitāte': 'PRO_s-3', 'ıetiıomesi': 'PRO_pm3',
            'neḥādeḥedane': 'PRO_sf3', 'neüeıane': 'PRO_pf3', 'newayome': 'PRO_---', 'neüāresu': 'PRO_sm3',
            'neüāxume': 'PRO_pm3', 'beıāıu': 'PRO_sm3', 'kābāıu': 'PRO_sm3', 'neḥādeḥedu': 'PRO_sm3', 
            'nesexumeka': 'PRO_sm2', 'negazāıereıesome': 'PRO_pm3', 'negazāıe-reıesexā': 'PRO_sm2',
            'wayane': 'PRO_---', 'bezayekāıu': 'PRO_---', 'bezāüebeıu': 'PRO_sm3', 'neüeüu': 'PRO_sm3',
            'nātekene': 'PRO_sf2', 'ıānase': 'PRO_s-1', 'bāüelā': 'PRO_sf3', 'baziıā': 'PRO_sf3',
            'neüāxene': 'PRO_pf2', 'nebétasabekene': 'PRO_p-3', 'neüāxāne': 'PRO_pf2', 'kamezane': 'PRO_pf3',
            'zayenātekā': 'PRO_sm3', 'negazāıe-nabesu': 'PRO_sm3', 'ıenetane': 'PRO_---', 'leüelaye': 'PRO_s-2', 
            'nanāye': 'PRO_---', 'bezayekāzi': 'PRO_sm3', 'bezayekātome': 'PRO_pm3', 'nenafesiwakafe': 'PRO_sm3',
            'beıāxume': 'PRO_pm3', 'kābāye': 'PRO_---', 'ıenaha': 'PRO_---', 'kābatane': 'PRO_---', 
            'babeweleqome': 'PRO_sm3', 'negazāıe-reıesu': 'PRO_sm3', 'nātekāne': 'PRO_sm2', 'zayenātekāne': 'PRO_sm3',
            'nenafesi-wakafekume': 'PRO_pm2', 'bāüelātekume': 'PRO_pm2', 'Kilu': 'pm3', 'nātune': 'PRO_---', 
            'babenātu': 'PRO_---', 'nenafese-wakafe': 'PRO_sm3', 'kulātane': 'PRO_pf3', 'mesāye': 'PRO_---',
            'nexeletiıome': 'PRO_pm3', 'ıābeziıā': 'PRO_---', 'ıezi': 'PRO_sm3', 'ıeziıā': 'PRO_sf3', 
            'ıeziıome': 'PRO_pm3', 'ıeziıane': 'PRO_pf3', 'ıetiıā': 'PRO_sf3', 'ıetiıome': 'PRO_pm3',
            'ıetiıane': 'PRO_pf3', 'ıeziıātome': 'PRO_pm3', 'ıeziıātane': 'PRO_pf3', 'ıetiıātome': 'PRO_pm3',
            'ıetiıātane': 'PRO_pf3', 'Kelu': 'PRO_-p-3', 'ḥāda': 'PRO_sm3', 'ḥidate': 'PRO_p-3', 
            'tawasāxi': 'PRO_sm3', 'zexona': 'PRO_sm3', 'zexonate': 'PRO_sf3', 'zexonā': 'PRO_pf3',
            'zexonu': 'PRO_pm3', 'galiıu': 'PRO_sm3', 'kāleıe': 'PRO_sm3', 'nafesewakafe': 'PRO_sm3'
            }

def pronoun(verb):
    return pron_dict[verb]


#print(pronoun('ıetane'))













