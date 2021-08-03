def morphImperfec(word):

    #Imperfective verbs with Subject no object, ህሉው ጊዜ
    #This function will be applied to the words after ohter prefixes are removed from the main imperfective verb
    #the arrangement is going to be organised in decreasing number of letter size
    
    if word[:2] == 'ıe' and word[-1] == 'e':
        return 'V_IMF_Ss-1_'
    elif word[:2] == 'ne' and word[-1] == 'e':
        return 'V_IMF_Sp-1_'
    elif word[:2] == 'te' and word[-1] == 'e':
        return 'V_IMF_Ssm2_'  #2nd person masculine
    elif word[:2] == 'te' and word[-1] == 'i':
        return 'V_IMF_Ssf2_'
    elif word[:2] == 'te' and word[-1] == 'u':
        return 'V_IMF_Spm2_'
    elif word[:2] == 'te' and word[-1] == 'ā':
        return 'V_IMF_Spf2_'
    elif word[:2] == 'ye' and word[-1] == 'e':
        return 'V_IMF_Ssm3_'
    elif word[:2] == 'te' and word[-1] == 'e':
        return 'V_IMF_Ssf3_'  #3rd person feminine
    elif word[:2] == 'ye' and word[-1] == 'u':
        return 'V_IMF_Spm3_'  
    elif word[:2] == 'ye' and word[-1] == 'ā':
        return 'V_IMF_Spf3_'
    
    #object1stPersonSingular
    elif word[:2] == 'te' and word[-3:] == 'ani':
        return 'V_IMF_Ssm2_Os-1'#2nd person masculine
    elif word[:2] == 'te' and word[-3:] == 'eni':
        return 'V_IMF_Ssf2_Os-1'
    elif word[:2] == 'te' and word[-1:] == 'uni':
        return 'V_IMF_Spm2_Os-1'  
    elif word[:2] == 'te' and word[-3:] == 'āni':
        return 'V_IMF_Spf2_Os-1'
    elif word[:2] == 'ye' and word[-3:] == 'ani':
        return 'V_IMF_Ssm3_Os-1'
    elif word[:2] == 'te' and word[-3:] == 'ani':
        return 'V_IMF_Ssf3_Os-1'  #3rd person feminine
    elif word[:2] == 'ye' and word[-3:] == 'uni':
        return 'V_IMF_Spm3_Os-1'
    elif word[:2] == 'ye' and word[-3:] == 'āni':
        return 'V_IMF_Spf3_Os-1'
    
    #object1stPersonPlural
    elif word[:2] == 'te' and word[-3:] == 'anā':
        return 'V_IMF_Ssm2_Op-1'#2nd person masculine
    elif word[:2] == 'te' and word[-3:] == 'enā':
        return 'V_IMF_Ssf2_Op-1'
    elif word[:2] == 'te' and word[-3:] == 'unā':
        return 'V_IMF_Spm2_Op-1'  
    elif word[:2] == 'te' and word[-3:] == 'ānā':
        return 'V_IMF_Spf2_Op-1'
    elif word[:2] == 'ye' and word[-3:] == 'anā':
        return 'V_IMF_Ssm3_Op-1'
    elif word[:2] == 'te' and word[-3:] == 'anā':
        return 'V_IMF_Ssf3_Op-1'  #3rd person feminine
    elif word[:2] == 'ye' and word[-3:] == 'unā':
        return 'V_IMF_Spm3_Op-1'
    elif word[:2] == 'ye' and word[-3:] == 'ānā':
        return 'V_IMF_Spf3_Op-1'
    
    #object2ndPersonSingularMascu
    elif word[:2] == 'ıe' and word[-3:] == 'akā':
        return 'V_IMF_Ss-1_Osm2'
    elif word[:2] == 'ne' and word[-3:] == 'akā':
        return 'V_IMF_Sp-1_Osm2'
    elif word[:2] == 'ye' and word[-3:] == 'akā':
        return 'V_IMF_Ssm3_Osm2' 
    elif word[:2] == 'te' and word[-3:] == 'akā':
        return 'V_IMF_Ssf3_Osm2'  #3rd person feminine 
    elif word[:2] == 'ye' and word[-3:] == 'uxā':
        return 'V_IMF_Spm3_Osm2'
    elif word[:2] == 'ye' and word[-3:] == 'āxā':
        return 'V_IMF_Spf3_Osm2'
    
    #object2ndPersonSingularFemini
    elif word[:2] == 'ıe' and word[-3:] == 'aki':
        return 'V_IMF_Ss-1_Osf2'
    elif word[:2] == 'ne' and word[-3:] == 'aki':
        return 'V_IMF_Sp-1_Osf2'
    elif word[:2] == 'ye' and word[-3:] == 'aki':
        return 'V_IMF_Ssm3_Osf2' 
    elif word[:2] == 'te' and word[-3:] == 'aki':
        return 'V_IMF_Ssf3_Osf2'   
    elif word[:2] == 'ye' and word[-3:] == 'uxi':
        return 'V_IMF_Spm3_Osf2'
    elif word[:2] == 'ye' and word[-3:] == 'āxi':
        return 'V_IMF_Spf3_Osf2'
    
    #object2ndPersonPluralMascu
    elif word[:2] == 'ıe' and word[-5:] == 'akume':
        return 'V_IMF_Ss-1_Opm2'
    elif word[:2] == 'ne' and word[-5:] == 'akume':
        return 'V_IMF_Sp-1_Opm2'
    elif word[:2] == 'ye' and word[-5:] == 'akume':
        return 'V_IMF_Ssm3_Opm2' 
    elif word[:2] == 'te' and word[-5:] == 'akume':
        return 'V_IMF_Ssf3_Opm2'  #3rd person feminine 
    elif word[:2] == 'ye' and word[-5:] == 'uxume':
        return 'V_IMF_Spm3_Opm2'
    elif word[:2] == 'ye' and word[-5:] == 'āxume':
        return 'V_IMF_Spf3_Opm2'
    
    #object2ndPersonPluralFemini
    elif word[:2] == 'ıe' and word[-3:] == 'akene':
        return 'V_IMF_Ss-1_Opf2'
    elif word[:2] == 'ne' and word[-3:] == 'akene':
        return 'V_IMF_Sp-1_Opf2'
    elif word[:2] == 'ye' and word[-3:] == 'akene':
        return 'V_IMF_Ssm3_Opf2' 
    elif word[:2] == 'te' and word[-3:] == 'akene':
        return 'V_IMF_Ssf3_Opf2'   
    elif word[:2] == 'ye' and word[-3:] == 'uxene':
        return 'V_IMF_Spm3_Opf2'
    elif word[:2] == 'ye' and word[-3:] == 'āxene':
        return 'V_IMF_Spf3_Opf2'
    
    #object3rdPersonSingularMascul
    elif word[:2] == 'ıe' and word[-1:] == 'o':
        return 'V_IMF_Ss-1_Osm3'
    elif word[:2] == 'ne' and word[-1:] == 'o':
        return 'V_IMF_Sp-1_Osm3'
    elif word[:2] == 'te' and word[-1:] == 'o':
        return 'V_IMF_Ssm2_Osm3' #
    elif word[:2] == 'te' and word[-3:] == 'eyo':
        return 'V_IMF_Ssf2_Osm3'   
    elif word[:2] == 'te' and word[-3:] == 'uwo':
        return 'V_IMF_Spm2_Osm3'
    elif word[:2] == 'te' and word[-3:] == 'aıo':
        return 'V_IMF_Spf2_Osm3'
    elif word[:2] == 'ye' and word[-1:] == 'o':
        return 'V_IMF_Ssm3_Osm3' 
    elif word[:2] == 'te' and word[-1:] == 'o':
        return 'V_IMF_Ssf3_Osm3' #Feminine3rdPerson
    elif word[:2] == 'ye' and word[-3:] == 'uwo':
        return 'V_IMF_Spm3_Osm3'
    elif word[:2] == 'ye' and word[-3:] == 'aıo':
        return 'V_IMF_Spf3_Osm3'
    
    #object3rdPersonSingularFemini
    elif word[:2] == 'ıe' and word[-1:] == 'ā':
        return 'V_IMF_Ss-1_Osf3'
    elif word[:2] == 'ne' and word[-3:] == 'ā':
        return 'V_IMF_Sp-1_Osf3'
    elif word[:2] == 'te' and word[-3:] == 'ā':
        return 'V_IMF_Ssm2_Osf3' #
    elif word[:2] == 'te' and word[-3:] == 'eyā':
        return 'V_IMF_Ssf2_Osf3'   
    elif word[:2] == 'te' and word[-3:] == 'uwā':
        return 'V_IMF_Spm2_Osf3'
    elif word[:2] == 'te' and word[-3:] == 'āıā':
        return 'V_IMF_Spf2_Osf3'
    elif word[:2] == 'ye' and word[-1:] == 'ā':
        return 'V_IMF_Ssm3_Osf3' 
    elif word[:2] == 'te' and word[-1:] == 'ā':
        return 'V_IMF_Ssf3_Osf3' 
    elif word[:2] == 'ye' and word[-3:] == 'uwā':
        return 'V_IMF_Spm3_Osf3'
    elif word[:2] == 'ye' and word[-3:] == 'āıā':
        return 'V_IMF_Spf3_Osf3'
    
    #object3rdPersonPluralMascul
    elif word[:2] == 'ıe' and word[-3:] == 'ome':
        return 'V_IMF_Ss-1_Opm3'
    elif word[:2] == 'ne' and word[-3:] == 'ome':
        return 'V_IMF_Sp-1_Opm3'
    elif word[:2] == 'te' and word[-3:] == 'ome':
        return 'V_IMF_Ssm2_Opm3' #
    elif word[:2] == 'te' and word[-5:] == 'eyome':
        return 'V_IMF_Ssf2_Opm3'   
    elif word[:2] == 'te' and word[-5:] == 'uwome':
        return 'V_IMF_Spm2_Opm3'
    elif word[:2] == 'te' and word[-5:] == 'aıome':
        return 'V_IMF_Spf2_Opm3'
    elif word[:2] == 'ye' and word[-3:] == 'ome':
        return 'V_IMF_Ssm3_Opm3' 
    elif word[:2] == 'te' and word[-3:] == 'ome':
        return 'V_IMF_Ssf3_Opm3' 
    elif word[:2] == 'ye' and word[-5:] == 'uwome':
        return 'V_IMF_Spm3_Opm3'
    elif word[:2] == 'ye' and word[-5:] == 'aıome':
        return 'V_IMF_Spf3_Opm3'
    
    #object3rdPersonPluralFemini
    elif word[:2] == 'ıe' and word[-1:] == 'ane':
        return 'V_IMF_Ss-1_Opf3'
    elif word[:2] == 'ne' and word[-3:] == 'ane':
        return 'V_IMF_Sp-1_Opf3'
    elif word[:2] == 'te' and word[-3:] == 'ane':
        return 'V_IMF_Ssm2_Opf3' #
    elif word[:2] == 'te' and word[-3:] == 'eyane':
        return 'V_IMF_Ssf2_Opf3'   
    elif word[:2] == 'te' and word[-3:] == 'uwane':
        return 'V_IMF_Spm2_Opf3'
    elif word[:2] == 'te' and word[-3:] == 'aıane':
        return 'V_IMF_Spf2_Opf3'
    elif word[:2] == 'ye' and word[-1:] == 'ane':
        return 'V_IMF_Ssm3_Opf3' 
    elif word[:2] == 'te' and word[-1:] == 'ane':
        return 'V_IMF_Ssf3_Opf3' 
    elif word[:2] == 'ye' and word[-3:] == 'uwane':
        return 'V_IMF_Spm3_Opf3'
    elif word[:2] == 'ye' and word[-3:] == 'aıane':
        return 'V_IMF_Spf3_Opf3'
    else:
        return 'Not Available'

 
"""
import json

with open('v_imf.json') as f:
    v_imf = json.load(f)

v_imf_morh = {}
for verb in v_imf:
    v_imf_morh[verb] = morphImperfec(verb)

not_avai = []
for a in v_imf_morh.keys():
    if v_imf_morh[a] == 'Not Available':
        not_avai.append(a)
              
from translitration import*

print(revers_translit('keneıāleyone'))
print(not_avai)
"""








