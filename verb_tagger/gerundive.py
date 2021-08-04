#//
from transliteration import*

def morphGerund(word):
    #gerundive verbs with Subject no obje ct, ውዱእ ሕሉፍ
    #the arrangement is going to be organised in decreasing number of letter size
    
    if 0 > 1:
        pass
    elif  word[-9:] == 'ekumewane':
        return 'V_GER_Spm2_Opf3'
    elif  word[-9:] == 'ekenaıane':
        return 'V_GER_Spf2_Opf3'
    elif  word[-9:] == 'ekumewome':
        return 'V_GER_Spm2_Opm3'
    elif  word[-9:] == 'ekenaıome':
        return 'V_GER_Spf2_Opm3'
    elif  word[-7:] == 'enākene':
        return 'V_GER_Sp-1_Opf2'
    elif  word[-5:] == 'ukene':
        return 'V_GER_Ssm2_Opf2'
    elif  word[-7:] == 'ātekene':
        return 'V_GER_Ssf1_Opf2'
    elif  word[-7:] == 'omexene':
        return 'V_GER_Spm3_Opf2'
    elif  word[-7:] == 'anāxene':
        return 'V_GER_Spf3_Opf2'
    elif  word[-7:] == 'ātekume':
        return 'V_GER_Ssf3_Opm2'
    elif  word[-7:] == 'omexume':
        return 'V_GER_Spm3_Opf2'
    elif  word[-7:] == 'anāxume':
        return 'V_GER_Spf3_Opf2'
    elif  word[-7:] == 'omewane':
        return 'V_GER_Spm3_Opf3'
    elif  word[-7:] == 'anaıane':
        return 'V_GER_Spf3_Opf3'
    elif  word[-7:] == 'enāyane':
        return 'V_GER_Sp-1_Opf3'
    elif  word[-7:] == 'ekāyane':
        return 'V_GER_Ssm2_Opf3'
    elif  word[-7:] == 'ekeyane':
        return 'V_GER_Ssf2_Opf3'
    elif  word[-7:] == 'omewome':
        return 'V_GER_Spm3_Opm3'
    elif  word[-7:] == 'anaıome':
        return 'V_GER_Spf3_Opm3'
    elif  word[-7:] == 'enāyome':
        return 'V_GER_Sp-1_Opm3'
    elif  word[-7:] == 'ekāyome':
        return 'V_GER_Ssm2_Opm3'
    elif  word[-7:] == 'ekeyome':
        return 'V_GER_Ssf2_Opm3'
    elif  word[-7:] == 'ekumewā':
        return 'V_GER_Spm2_Osf3'
    elif  word[-7:] == 'ekenaıā':
        return 'V_GER_Spf2_Osf3'
    elif  word[-7:] == 'ekumewo' or word[-5:] == 'ekumo': ###################3
        return 'V_GER_Spm2_Osm3'
    elif  word[-7:] == 'ekenaıo':
        return 'V_GER_Spf2_Osm3'
    elif  word[-7:] == 'enākume':
        return 'V_GER_Sp-1_Opm2'
    elif  word[-7:] == 'ekumenā':
        return 'V_GER_Spm2_Op-1'
    elif  word[-7:] == 'ekenānā':
        return 'V_GER_Spf2_Op-1'
    elif  word[-7:] == 'ekumeni':
        return 'V_GER_Spm2_Os-1'
    elif word[-7:] == 'ekenāni':
        return 'V_GER_Spf2_Os-1'
    elif word[-5:] == 'ekume' or word[-5:] == 'ixume':
        return 'V_GER_Spm2'
    elif word[-5:] == 'exene':
        return 'V_GER_Spf2'
    elif  word[-5:] == 'ekāni':
        return 'V_GER_Ssm2_Os-1'
    elif word[-5:] == 'ekeni':
        return 'V_GER_Ssf2_Os-1'
    elif word[-5:] == 'āteni':
        return 'V_GER_Ssf3_Os-1'
    elif  word[-5:] == 'omeni':
        return 'V_GER_Spm3_Os-1'
    elif word[-5:] == 'anāni':
        return 'V_GER_Spf3_Os-1'
    elif  word[-5:] == 'ekānā':
        return 'V_GER_Ssm2_Op-1'
    elif word[-5:] == 'ekenā':
        return 'V_GER_Ssf2_Op-1'
    elif  word[-5:] == 'ātenā':
        return 'V_GER_Ssf3_Op-1'
    elif  word[-5:] == 'omenā':
        return 'V_GER_Spm3_Op-1'
    elif  word[-5:] == 'anānā':
        return 'V_GER_Spf3_Op-1'
    elif  word[-5:] == 'enākā':
        return 'V_GER_Spm1_Osm2'
    elif  word[-5:] == 'ātekā':
        return 'V_GER_Ssf3_Osm2'
    elif  word[-5:] == 'omexā':
        return 'V_GER_Spm3_Osm2'
    elif  word[-5:] == 'anāxā':
        return 'V_GER_Spf3_Osm2'
    elif  word[-5:] == 'enāki':
        return 'V_GER_Sp-1_Osf2'
    elif  word[-5:] == 'āteki':
        return 'V_GER_Ssf3_Osf2'
    elif  word[-5:] == 'omexi':
        return 'V_GER_Spm3_Osf2'
    elif  word[-5:] == 'anāxi':
        return 'V_GER_Spf3_Osf2'
    elif  word[-5:] == 'akume':
        return 'V_GER_Ss-1_Opm2'
    elif  word[-5:] == 'ukume':
        return 'V_GER_Ssm3_Opm2'
    elif  word[-5:] == 'akene':
        return 'V_GER_Ss-1_Opf2'
    elif  word[-5:] == 'enāyo':
        return 'V_GER_Sp-1_Osm3'
    elif  word[-5:] == 'ekāyo':
        return 'V_GER_Ssm2_Osm3'
    elif  word[-5:] == 'ekeyo' or word[-5:] == 'ixeyo' or word[-5:] == 'ekiyo':
        return 'V_GER_Ssf2_Osm3'
    elif  word[-5:] == 'omewo' or word[-3:] == 'omo' or word[-3:] == 'amo':
        return 'V_GER_Spm3_Osm3'
    elif  word[-5:] == 'anaıo' or word[-5:] == 'anāıo' or word[-5:] == 'aneıo':
        return 'V_GER_Spf3_Osm3'
    elif  word[-5:] == 'enāyā':
        return 'V_GER_Sp-1_Osf3'
    elif  word[-5:] == 'ekāyā':
        return 'V_GER_Ssm2_Osf3'
    elif  word[-5:] == 'ekeyā':
        return 'V_GER_Ssf2_Osf3'
    elif  word[-5:] == 'omewā':
        return 'V_GER_Spm3_Osf3'
    elif  word[-5:] == 'anaıā':
        return 'V_GER_Spf3_Osf3'
    elif  word[-5:] == 'ayome':
        return 'V_GER_Ss-1_Opm3'
    elif  word[-5:] == 'uwome':
        return 'V_GER_Ssm3_Opm3'
    elif  word[-5:] == 'ātome':
        return 'V_GER_Ssf3_Opm3'
    elif  word[-5:] == 'ayane':
        return 'V_GER_Ss-1_Opf3'
    elif  word[-5:] == 'uwane':
        return 'V_GER_Ssm3_Opf3'
    elif  word[-5:] == 'ātane':
        return 'V_GER_Ssf3_Opf3'
    elif  word[-3:] == 'akā':
        return 'V_GER_Ssm1_Osm2'
    elif  word[-3:] == 'ukā':
        return 'V_GER_Ssm3_Osm2'
    elif  word[-3:] == 'aki':
        return 'V_GER_Ss-1_Osf2'
    elif  word[-3:] == 'uki':
        return 'V_GER_Ssm3_Osf2'
    elif  word[-3:] == 'ayo':
        return 'V_GER_Ss-1_Osm3'
    elif  word[-3:] == 'ayā':
        return 'V_GER_Ss-1_Osf3'
    elif  word[-3:] == 'uwo' or word[-3:] == 'ewo' or word[-3:] == 'iwo' or word[-3:] == 'awo':
        return 'V_GER_Ssm3_Osm3'
    elif  word[-3:] == 'āto':
        return 'V_GER_Ssf3_Osm3'
    elif  word[-3:] == 'uwā' or word[-3:] == 'iwā' or word[-3:] == 'ewā':
        return 'V_GER_Ssm3_Osf3'
    elif  word[-3:] == 'ātā':
        return 'V_GER_Ssf3_Osf3'
    elif  word[-3:] == 'uni':
        return 'V_GER_Ssm3_Os-1'
    elif  word[-3:] == 'unā':
        return 'V_GER_Ssm3_Op-1'
    elif word[-3:] == 'ome':
        return 'V_GER_Spm3'
    elif word[-3:] == 'ane':
        return 'V_GER_Spf3'
    elif word[-3:] == 'ekā':
        return 'V_GER_Ssm2'
    elif word[-3:] == 'eki':
        return 'V_GER_Ssf2'
    elif word[-3:] == 'enā':
        return 'V_GER_Sp-1'
    elif word[-1:] == 'u':
        return 'V_GER_Ssm3'
    elif word[-1:] == 'a':
        return 'V_GER_Ss-1'
    elif word[-1:] == 'ā':
        return 'V_GER_Ssf3'
    
    else:
        return 'Not Available'
  
