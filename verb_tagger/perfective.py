#//
from translitration import*

def morphPerfec(word):

    #perfective verbs with Subject no object, ኣጕል ሕሉፍ
    #the arrangement is going to be organised in decreasing number of letter size
    
    if 0 < -1:
        pass
    elif word[-9:] == 'ekumewome':
        return 'V_PRF_Spm2_Opm3'
    elif word[-9:] == 'ekenaıome':
        return 'V_PRF_Spf2_Opm3'
    elif word[-9:] == 'ekumewane':
        return 'V_PRF_Spm2_Opf3'
    elif word[-9:] == 'ekenaıane':
        return 'V_PRF_Spf2_Opf3'
    elif word[-7:] == 'enāyane':
        return 'V_PRF_Sp-1_Opf3'
    elif word[-7:] == 'ekāyane':
        return 'V_PRF_Ssm2_Opf3'
    elif word[-7:] == 'ekeyane':
        return 'V_PRF_Ssf2_Opf3'
    elif word[-7:] == 'ekuwane':
        return 'V_PRF_Ss-1_Opf3'
    elif word[-7:] == 'enāyome':
        return 'V_PRF_Sp-1_Opm3'
    elif word[-7:] == 'ekāyome':
        return 'V_PRF_Ssm2_Opm3'
    elif word[-7:] == 'ekeyome':
        return 'V_PRF_Ssf2_Opm3'
    elif  word[-7:] == 'ekumeni':
        return 'V_PRF_Spm2_Os-1'
    elif word[-7:] == 'ekenāni':
        return 'V_PRF_Spf2_Os-1'
    elif word[-7:] == 'ekumewā':
        return 'V_PRF_Spm2_Osf2'
    elif word[-7:] == 'ekenaıā':
        return 'V_PRF_Spf2_Osf2'
    elif  word[-7:] == 'ekumenā':
        return 'V_PRF_Spm2_Op-1'
    elif  word[-7:] == 'ekenānā':
        return 'V_PRF_Spf2_Op-1'
    elif  word[-7:] == 'ekuxume':
        return 'V_PRF_Ss-1_Opm2'
    elif word[-7:] == 'ekumewo':
        return 'V_PRF_Spm2_Osm2'
    elif word[-7:] == 'ekenaıo':
        return 'V_PRF_Spf2_Osm2'
    elif  word[-7:] == 'ekuxene':
        return 'V_PRF_Ss-1_Opf2'
    elif word[-7:] == 'enākene':
        return 'V_PRF_Sp-1_Opf2'
    elif  word[-7:] == 'atekume':
        return 'V_PRF_Ssf3_Opm2'
    elif  word[-7:] == 'atekene':
        return 'V_PRF_Ssf3_Opf2'
    elif word[-7:] == 'enākume':
        return 'V_PRF_Sp-1_Opm2' 
    elif word[-5:] == 'ekume': 
        return 'V_PRF_Spm2_'
    elif word[-5:] == 'atome':
        return 'V_PRF_Ssf3_Opm3'
    elif word[-5:] == 'uwome':
        return 'V_PRF_Spm3_Opm3'
    elif word[-5:] == 'aıome':
        return 'V_PRF_Spf3_Opm3'
    elif word[-5:] == 'atane':
        return 'V_PRF_Ssf3_Opf3'
    elif word[-5:] == 'uwane':
        return 'V_PRF_Spm3_Opf3'
    elif word[-5:] == 'aıane':
        return 'V_PRF_Spf3_Opf3'
    elif word[-5:] == 'ekume': 
        return 'V_PRF_Spm2_'
    elif word[-5:] == 'ekene':
        return 'V_PRF_Spf2'
    elif  word[-5:] == 'ekāni':
        return 'V_PRF_Ssm2_Os-1'
    elif word[-5:] == 'ekeni':
        return 'V_PRF_Ssf2_Os-1'
    elif word[-5:] == 'ateni':
        return 'V_PRF_Ssf3_Os-1'
    elif  word[-5:] == 'ekānā':
        return 'V_PRF_Ssm2_Op-1'
    elif word[-5:] == 'ekenā':
        return 'V_PRF_Ssf2_Op-1'
    if word[-5:] == 'ekuwā':
        return 'V_PRF_Ss-1_Osf2'
    elif word[-5:] == 'enāyā':
        return 'V_PRF_Sp-1_Osf2'
    elif word[-5:] == 'ekuwome':
        return 'V_PRF_Ss-1_Opm3'
    elif word[-5:] == 'ekāyā':
        return 'V_PRF_Ssm2_Osf2'
    elif word[-5:] == 'ekeyā':
        return 'V_PRF_Ssf2_Osf2'
    elif  word[-5:] == 'atenā':
        return 'V_PRF_Ssf3_Op-1'
    elif  word[-5:] == 'akume': 
        return 'V_PRF_Ssm3_Opm2'
    elif word[-5:] == 'uxume':
        return 'V_PRF_Spm3_Opm2'
    elif  word[-5:] == 'āxume':
        return 'V_PRF_Spf3_Opm2'
    elif word[-5:] == 'uxene':
        return 'V_PRF_Spm3_Opf2'
    elif  word[-5:] == 'āxene':
        return 'V_PRF_Spf3_Opf2'
    elif  word[-5:] == 'akene':
        return 'V_PRF_Ssm3_Opf2'
    elif word[-5:] == 'ekuwo':
        return 'V_PRF_Ss-1_Osm2'
    elif word[-5:] == 'enāyo':
        return 'V_PRF_Sp-1_Osm2'
    elif word[-5:] == 'ekāyo':
        return 'V_PRF_Ssm2_Osm2'
    elif word[-5:] == 'ekeyo':
        return 'V_PRF_Ssf2_Osm2'
    elif  word[-5:] == 'ekuxā':
        return 'V_PRF_Ss-1_Osm2'
    elif word[-5:] == 'enākā':
        return 'V_PRF_Sp-1_Osm2'
    elif  word[-5:] == 'ateki':
        return 'V_PRF_Ssf3_Osf2'
    elif  word[-5:] == 'atekā':
        return 'V_PRF_Ssf3_Osm2'    
    elif  word[-5:] == 'ekuxi':
        return 'V_PRF_Ss-1_Osf2'    
    elif word[-3:] == 'anā':
        return 'V_PRF_Ssm3_O-1'
    elif word[-3:] == 'unā':
        return 'V_PRF_Spm3_Op-1'
    elif word[-3:] == 'ānā':
        return 'V_PRF_Spf3_Op-1'
    elif word[-3:] == 'uxā':
        return 'V_PRF_Spm3_Osm2'
    elif  word[-3:] == 'āxā':
        return 'V_PRF_Spf3_Osm2'
    elif  word[-3:] == 'akā':
        return 'V_PRF_Ssm3_Osm2'
    elif word[-3:] == 'aki':
        return 'V_PRF_Sp-1_Osf2'
    elif  word[-3:] == 'akā':
        return 'V_PRF_Ssm3_Osf2'
    elif word[-3:] == 'uxi':
        return 'V_PRF_Spm3_Osf2'
    elif  word[-3:] == 'āxi':
        return 'V_PRF_Spf3_Osf2'
    elif word[-3:] == 'atā':
        return 'V_PRF_Ssf3_Osf2'
    elif word[-3:] == 'uwā':
        return 'V_PRF_Spm3_Osf2'
    elif word[-3:] == 'aıā':
        return 'V_PRF_Spf3_Osf2'
    elif word[-3:] == 'ome':
        return 'V_PRF_Ssm3_Opm3'
    elif word[-3:] == 'ane':
        return 'V_PRF_Ssm3_Opf3'
    elif  word[-3:] == 'ani':
        return 'V_PRF_Ssm3_Os-1'
    elif  word[-3:] == 'uni':
        return 'V_PRF_Spm3_Os-1'
    elif word[-3:] == 'āni':
        return 'V_PRF_Spf3_Os-1'
    elif word[-3:] == 'ato':
        return 'V_PRF_Ssf3_Osm2'
    elif word[-3:] == 'uwo':
        return 'V_PRF_Spm3_Osm2'
    elif word[-3:] == 'aıo':
        return 'V_PRF_Spf3_Osm2'
    elif word[-3:] == 'ekā':
        return 'V_PRF_Ssm2'
    elif word[-3:] == 'eki':
        return 'V_PRF_Ssf2'
    elif word[-3:] == 'enā':
        return 'V_PRF_Sp-1'
    elif word[-3:] == 'eku':
        return 'V_PRF_Ssm3_'
    elif word[-3:] == 'ate':
        return 'V_PRF_Ssf3'
    elif word[-1:] == 'u':
        return 'V_PRF_Spm3'
    elif word[-1:] == 'a':
        return 'V_PRF_Ss-3'
    elif word[-1:] == 'ā':
        return 'V_PRF_Ssm3_Osf2'
    elif word[-1:] == 'o':
        return 'V_PRF_Ssm3_Osm2'
    elif word[-1:] == 'ā':
        return 'V_PRF_Spf3'
    else:
        return 'Not Avail'

"""
import json

with open('v_prf.json') as f:
    v_prf = json.load(f)

v_prf_morh = {}
for verb in v_prf:
    v_prf_morh[verb] = morphPerfec(verb)

not_avai = []
for a in v_prf_morh.keys():
    if v_prf_morh[a] == 'Not Avail':
        not_avai.append(a)

print(revers_translit('faṭirukume'))
print(not_avai)
"""



