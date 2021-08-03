import json

#copula and Verb of Existence, present tense, 
aux_list = {'ıeya': 'V_AUX_Ss-1', 'ıexā': 'V_AUX_Ssm2', 'ıixā': 'V_AUX_Ssm2', 'ıexi': 'V_AUX_Ssf2', 'ıixi': 'V_AUX_Ssf2',
 'ıeyu': 'V_AUX_Ssm3', 'ıeyā': 'V_AUX_Ssf3', 'ıinā': 'V_AUX_Sp-1', 'ıexume': 'V_AUX_Spm2',
 'ıixume': 'V_AUX_Spm2', 'ıexene': 'V_AUX_Spf2', 'ıixene': 'V_AUX_Spf2', 'ıeyome': 'V_AUX_Spm3',
 'ıeyane': 'V_AUX_Spf3', 'ıāyekonekune': 'V_AUX_Ss-1_Neg', 'ıāyekonekāne': 'V_AUX_Ssm2_Neg', 
 'ıāyekonekene': 'V_AUX_Ssf2_Neg', 'ıāyekonane': 'V_AUX_Ssm3_Neg', 'ıāyekonatene': 'V_AUX_Ssf3_Neg',
 'ıāyekonenāne': 'V_AUX_Sp-1_Neg', 'ıāyekonekumene': 'V_AUX_Spm2_Neg', 'ıāyekonekenene': 'V_AUX_Spf2_Neg',
 'ıāyekonune': 'V_AUX_Spm3_Neg', 'ıāyekonāne': 'V_AUX_Spf3_Neg', 'ıāloxu': 'V_AUX_Ss-1',
 'ıāloxā': 'V_AUX_Ssm2', 'ıāloxi': 'V_AUX_Ssf2', 'ıālo': 'V_AUX_Ssm3', 'ıālā': 'V_AUX_Ssf3',
 'ıālonā': 'V_AUX_Sp-1', 'ıāloxume': 'V_AUX_Spm2', 'ıāloxene': 'V_AUX_Spf2', 'ıālawu': 'V_AUX_Spm3',
 'ıālawā': 'V_AUX_Spf3','ıāloni': 'V_AUX_Ss-1', 'ıālokā': 'V_AUX_Ssm2', 'ıāloki': 'V_AUX_Ssf2',
 'ıālowo': 'V_AUX_Ssm3', 'ıālowā': 'V_AUX_Ssf3', 'ıālonā': 'V_AUX_Sp-1', 'ıālokume': 'V_AUX_Spm2',
 'ıālokene': 'V_AUX_Spf2', 'ıālawome': 'V_AUX_Spm3', 'ıālawone': 'V_AUX_Spf3',
 'yaloxune': 'V_AUX_Ss-1_Neg', 'yaloxāne': 'V_AUX_Ssm2_Neg', 'yaloxene': 'V_AUX_Ssf2_Neg',
 'yalone': 'V_AUX_Ssm3_Neg', 'yalebone': 'V_AUX_Ssm3_Neg', 'yalāne': 'V_AUX_Ssf3_Neg', 
 'yalonāne': 'V_AUX_Sp-1_Neg', 'yaloxumene': 'V_AUX_Spm2_Neg', 'yaloxenene': 'V_AUX_Spf2_Neg',
 'yalawene': 'V_AUX_Spm3_Neg', 'yalawāne': 'V_AUX_Spf3_Neg', 'yabelayene': 'V_AUX_Ss-1', 
 'yabelekāne': 'V_AUX_Ssm2', 'yabelekene': 'V_AUX_Ssf2', 'yabelune': 'V_AUX_Ssm3', 
 'yabelāne': 'V_AUX_Ssf3', 'yabelenāne': 'V_AUX_Sp-1', 'yabelekumene': 'V_AUX_Spm2',
 'yabelekenene': 'V_AUX_Spf2', 'yabelomene': 'V_AUX_Spm3', 'yabelanene': 'V_AUX_Spf3',
 'ıiyu': 'V_AUX_Ssm2', 'nayeru': 'V_AUX_Ssm3', 'nayerome': 'V_AUX_Spm3', 'ıeyome': 'V_AUX_Spm3', 'yabelune': 'V_AUX_Ssm2_Neg', 'ıiyome': 'V_AUX_Spm3',
 'yegebāıe': 'V_AUX_Spm3', 'ıālawo': 'V_AUX_Ssm2', 'yegebaıānā': 'V_AUX_Sp-1', 'yadeli': 'V_AUX_Ssm3', 'ıālaxu': 'V_AUX_Ss-1', 'ıixā': 'V_AUX_Ssm2', 'xalo': 'V_AUX_Ssm3', 'ıāyereıane': 'V_AUX_Ssm3_Neg', 'kenesu': 'V_AUX_Ssm3', 'dixā': 'V_AUX_Ssm2',
 'ıālaxā': 'V_AUX_Ssm2', 'kalā': 'V_AUX_Ssf3', 'nexeıele': 'V_AUX_Sp-1', 'do': 'V_AUX_S---', 'ıenekalo': 'V_AUX_Ssm3', 'deyu': 'V_AUX_Ssm3', 'ıālani': 'V_AUX_Ss-1', 'kafeıāni': 'V_AUX_Ss-1', 'ıāleyomo': 'V_AUX_Spm3', 'ıenekalaxā': 'V_AUX_Ssm2',
 'yebahāle': 'V_AUX_Ssm3', 'yabelekāne': 'V_AUX_Ssm2_Neg', 'yaxeıelā': 'V_AUX_Spf3', 'fatana': 'V_AUX_Ssm3', 'ıāzaxāxirome': 'V_AUX_Spm3', 'nataḥāsāsebe': 'V_AUX_Sp-1', 'nazaxāxere': 'V_AUX_Sp-1', 'ıālakā': 'V_AUX_Ssm2', 
 'kalaxu': 'V_AUX_Ss-1', 'ıālanā': 'V_AUX_Sp-1', 'yexeıelu': 'V_AUX_Spm3', 'yeṭeüeme': 'V_AUX_Ssm3', 'yabelome': 'V_AUX_Spm3', 'ıālawane': 'V_AUX_Spm3', 'diyome': 'V_AUX_Spm3', 'ıālaxi': 'V_AUX_Ssf2', 'ıenekalā': 'V_AUX_Ssf3', 
 'tejemere': 'V_AUX_Ssf3', 'nayerā': 'V_AUX_Ssf3', 'jamira': 'V_AUX_Ssf3', 'tasameüa': 'V_AUX_Ssm3', 'taGāyaya': 'V_AUX_Ssm3', 'tawasana': 'V_AUX_Ssm3', 'tanagero': 'V_AUX_Ssm3', 'ıāyekaıālune': 'V_AUX_Ssm3_Neg', 'tarāıeya': 'V_AUX_Ssf3', 
 'ıāyetaṣagamane': 'V_AUX_Ssm3_Neg', 'tahāneṭayu': 'V_AUX_Ssm3', 'ḥātato': 'V_AUX_Ssm3_Osm3', 'yalanāne': 'V_AUX_Sp-1', 'tamadibu': 'V_AUX_Ssm3', 'ıālaxume': 'V_AUX_Spm2', 'ṣaniḥenā': 'V_AUX_Sp-1', 'ıāloni': 'V_AUX_Ss-1', 'ḥāsaba': 'V_AUX_Ssm3', 
 'ḥābara': 'V_AUX_Ssm3', 'yedela': 'V_AUX_Ssm3', 'ıāyenabarane': 'V_AUX_Ssm3_Neg', 'ıāyekeıālune': 'V_AUX_Ssm3_Neg', 'nabarate': 'V_AUX_Ssf3', 'ıāzazo': 'V_AUX_Ssm3_Osm3', 'yalane': 'V_AUX_Ssm3_Neg', 'yenebabe': 'V_AUX_Ssm3', 'nayiru': 'V_AUX_Ssm3', 
 'deyome': 'V_AUX_Spm3', 'ıi': 'V_AUX_S---', 'ıālā': 'V_AUX_Ssf3', 'ıenekalawu': 'V_AUX_Spm3', 'ıāwafeyewo': 'V_AUX_Ssm3_Osm3', 'ıātabābiüu': 'V_AUX_Ssm3', 'ıiyane': 'V_AUX_Spf3', 'ıāyekaıālene': 'V_AUX_Ssm3_Neg', 'ıāyetegebare': 'V_AUX_Ssm3_Neg', 
 'yefetenā': 'V_AUX_Spf3', 'yedelayu': 'V_AUX_Spm3', 'ıālanālekā': 'V_AUX_Sp-1_Osm2', 'keıilome': 'V_AUX_Spm3', 'ıenekalaxu': 'V_AUX_Ss-1', 'yeöalani': 'V_AUX_Ssm3_Os-1', 'weüilome': 'V_AUX_Spm3', 'tawakasekuwā': 'V_AUX_Ss-1_Osf3', 
 'nayerane': 'V_AUX_Spf3', 'ıālone': 'V_AUX_Ssm3', 'ıāseḥiöunā': 'V_AUX_Ssm3_Op-1', 'ıenekalawā': 'V_AUX_Spf3', 'ıiyā': 'V_AUX_Ssf3', 'kalawe': 'V_AUX_Spm3', 'yeṭemetā': 'V_AUX_Ssm3', 'talābeyu': 'V_AUX_Ssm3', 'ıātaḥāsāsibu': 'V_AUX_Ssm3', 
 'baöiüā': 'V_AUX_Ssm3', 'ıālāne': 'V_AUX_Spf3', 'wasanu': 'V_AUX_Ssm3', 'taüāzabuwo': 'V_AUX_Ssm3_Osm3', 'ıāyedalayane': 'V_AUX_Ssm3_Neg', 'ıāyedaneGayane': 'V_AUX_Ssm3_Neg', 'ıāyenabaromene': 'V_AUX_Spm3', 'dinā': 'V_AUX_Sp-1', 
 'fatanu': 'V_AUX_Ssm3', 'kono': 'V_AUX_Ssm3', 'kalawā': 'V_AUX_Spf3', 'ıenedeyu': 'V_AUX_Ssm3', 'ıālawune': 'V_AUX_Ss-1', 'nayerenā': 'V_AUX_Sp-1', 'diyu': 'V_AUX_Ssm3', 'yeXanā': 'V_AUX_Spf3', 'yeXanu': 'V_AUX_Spm3', 'ıālakume': 'V_AUX_Spm2', 
 'kalaxā': 'V_AUX_Ssm2', 'deya': 'V_AUX_Ssf3', 'ıāyenedalene': 'V_AUX_Sp-1', 'ıeyuxa': 'V_AUX_Ssm2', 'fatanate': 'V_AUX_Ssf3', 'nayerewā': 'V_AUX_Ssf3', 'ıāyenabaratene': 'V_AUX_Ssf3_Neg', 'kaıālate': 'V_AUX_Ssf3', 'ıālawe': 'V_AUX_Spm3', 
 'ıenekalawe': 'V_AUX_Spm3', 'tamaneyome': 'V_AUX_Spm3', 'nexawene': 'V_AUX_Sp-1', 'baöeüa': 'V_AUX_Ssm3', 'talābeyome': 'V_AUX_Spm3', 'kalaxāse': 'V_AUX_Ssm2', 'yefaöedalu': 'V_AUX_Spf3', 'yeḥešani': 'V_AUX_Ss-1', 'nérenā': 'V_AUX_Ssf3', 
 'ıenehāla': 'V_AUX_Ssf3', 'ıenedixi': 'V_AUX_Ssf2', 'ıenekalanā': 'V_AUX_Sp-1', 'ıāyetafatawanine': 'V_AUX_Ssf3__Os-1_Neg', 'daleyu': 'V_AUX_Ssm3', 'ıāyenabarekune': 'V_AUX_Ss-1_Neg', 'ıābāxā': 'V_AUX_Ssm3', 'ıālawuwo': 'V_AUX_Ssm3_Opm3', 
 'ıāyetaxāıelane': 'V_AUX_Ssm3_Neg', 'ıāyaüebayewone': 'V_AUX_Spm3_Osm3', 'qaneyu': 'V_AUX_Ssm3', 'ıālowome': 'V_AUX_Spm3', 'tamāḥeṣinekumeni': 'V_AUX_Spm2_Os-1', 'dixume': 'V_AUX_Spm2', 'fataneku': 'V_AUX_Ss-1', 'teüezabe': 'V_AUX_Ssf3', 
 'ıālāteni': 'V_AUX_Ssf3', 'ıāyetegebaro': 'V_AUX_Ssm2', 'nayerekā': 'V_AUX_Ssm2', 'yeöeneyā': 'V_AUX_Spf3', 'yeṣebayu': 'V_AUX_Spm3', 'ıāyewaḥāṭalune': 'V_AUX_Ssm3_Osm3_Neg', 'deyuse': 'V_AUX_Ssm3', 'ıāyetemaselene': 'V_AUX_Ssm3_Osf3_Neg', 
 'nazaxāxerakā': 'V_AUX_Sp-1_Osm2', 'üādamani': 'V_AUX_Ssm2_Os-1', 'jamareku': 'V_AUX_Ss-1', 'tagadadeku': 'V_AUX_Ss-1', 'jamarenā': 'V_AUX_Sp-1', 'kaıāla': 'V_AUX_Spf3', 'ıemenayalane': 'V_AUX_Ss-1_Opf3', 'wasaneku': 'V_AUX_Ss-1', 
 'lamanato': 'V_AUX_Ssf3_Osm2', 'ıenedeya': 'V_AUX_Ssf3', 'yegebare': 'V_AUX_Ssm2', 'dixi': 'V_AUX_Ssf3', 'yehelu': 'V_AUX_Ssm3', 'ıenedixā': 'V_AUX_Ssm2', 'ıenedeyā': 'V_AUX_Ssf3', 'yeheqenu': 'V_AUX_Spm3', 'baöiüenā': 'V_AUX_Sp-1', 
 'yegaberunā': 'V_AUX_Spm3_Op-1', 'ıāyemaraṣekune': 'V_AUX_Ss-1_Neg', 'ıāyebalatene': 'V_AUX_Ssf3_Neg', 'deyane': 'V_AUX_Spf3', 'ıenekalonā': 'V_AUX_Sp-1', 'yeḥetatā': 'V_AUX_Spf3', 'ıāyetarāıeyāne': 'V_AUX_Ssm3_Neg', 
 'netesefo': 'V_AUX_Sp-1"', 'ıālawuni': 'V_AUX_Ss-1', 'yegedadu': 'V_AUX_Spm3', 'yegebeıome': 'V_AUX_Spm3', 'yemenayu': 'V_AUX_Spm3', 'yeḥālemu': 'V_AUX_Spm3', 'ṣiḥifu': 'V_AUX_Ssm3', 'ıāyekaıālane': 'V_AUX_Ssm3_Neg', 
 'tamariṣome': 'V_AUX_Spm3', 'ıāyeraıāyāne': 'V_AUX_Ssm3_Osf3_Neg', 'ıewekasā': 'V_AUX_Ss-1_Opf3', 'ıāyegebeıākāne': 'V_AUX_Ssm2_Neg', 'ıāyetarāıeyane': 'V_AUX_Ssm3_Neg', 'ıāyekeıelāne': 'V_AUX_Ssm3_Neg', 'yeḥādereıo': 'V_AUX_Spm3', 
 'ıeḥādere': 'V_AUX_Ss-1', 'yenabere': 'V_AUX_Ss-1', 'yaṣageme': 'V_AUX_Ssm3', 'ıālawomene': 'V_AUX_Spm3', 'nabaro': 'V_AUX_Ssm3', 'tawadeıa': 'V_AUX_Spf3', 'ṣaniḥewo': 'V_AUX_Ssm3_Osm3', 'yalawune': 'V_AUX_Spm3_Neg', 'ıāyemaraṣatene': 'V_AUX_Ssf3_Neg', 
 'dixene': 'V_AUX_Spf2', 'ıālaki': 'V_AUX_Ssf2', 'neṭeneqaöe': 'V_AUX_Sp-1', 'ıāyekaıālatene': 'V_AUX_Ssf3_Neg', 'ıāyenabarakene': 'V_AUX_Ssf2', 'ıenekalaxi': 'V_AUX_Ssf2', 'deyā': 'V_AUX_Ssf3', 'ıāyememaṣāıekune': 'V_AUX_Ss-1_Neg', 
 'ıāyekeıālene': 'V_AUX_Ssm3_Neg', 'kenefetene': 'V_AUX_Sp-1'}

from translitration import*


def morphAuxil(verb):
		return aux_list[verb]
















