import os.path,sys
import pandas as pd
import numpy as np
def converter():
    fileName = os.path.join(workingDirectory,'../test.txt')
    # print('MONTHLY  LOCAL')
    # print('Vendor       TYPE      IL     MT     NM     OK     TX')
    with open(fileName,'r') as test_file: 
        avility=[line for line in test_file if '*030240928' in line]
        test_file.close()
    with open(fileName,'r') as test_file:     
        realmed=[line for line in test_file if '*030240122' in line]
        test_file.close()
    with open(fileName,'r') as test_file: 
        hews=[line for line in test_file if '*030550127' in line]
        test_file.close()
        
    ############################ Availity ###############################
    type_270 = [i.split('        ')[3] for i in avility if '*1030223*' in i]   
    
    il_270 = [i for i in type_270 if "*621*" in i]
    mt_270 = [i for i in type_270 if "*751*" in i]
    nm_270 = [i for i in type_270 if "*290*" in i]
    ok_270 = [i for i in type_270 if "*340*" in i]
    tx_270 = [i for i in type_270 if "*400*" in i]
    #####################################
    type_271 = [i.split('        ')[3] for i in avility if '*191703*' in i]
    il_271 = [i for i in type_271 if "*621*" in i]
    mt_271 = [i for i in type_271 if "*751*" in i]
    nm_271 = [i for i in type_271 if "*290*" in i]
    ok_271 = [i for i in type_271 if "*340*" in i]
    tx_271 = [i for i in type_271 if "*400*" in i]
    ######################################
    type_276 = [i.split('        ')[3] for i in avility if '*085707*' in i]
    il_276 = [i for i in type_276 if "*621*" in i]
    mt_276 = [i for i in type_276 if "*751*" in i]
    nm_276 = [i for i in type_276 if "*290*" in i]
    ok_276 = [i for i in type_276 if "*340*" in i]
    tx_276 = [i for i in type_276 if "*400*" in i]
    #####################################
    type_277 = [i.split('        ')[3] for i in avility if '*0877077*' in i]
    il_277 = [i for i in type_277 if "*621*" in i]
    mt_277 = [i for i in type_277 if "*751*" in i]
    nm_277 = [i for i in type_277 if "*290*" in i]
    ok_277 = [i for i in type_277 if "*340*" in i]
    tx_277 = [i for i in type_277 if "*400*" in i]
    # print('Availity','270',len(il_270),len(mt_270),len(nm_270),len(ok_270),len(tx_270),'\nAvaility','271',len(il_271),len(mt_271),len(nm_271),len(ok_271),len(tx_271),'\nAvaility','276',len(il_276),len(mt_276),len(nm_276),len(ok_276),len(tx_276),'\nAvaility','277',len(il_277),len(mt_277),len(nm_277),len(ok_277),len(tx_277), sep= '      ')
    
    data = {'Vendor': ['Availity', 'Availity', 'Availity', 'Availity'],#, 'RealMed','RealMed','RealMed','RealMed','Hews','Hews','Hews','Hews'],
        'Type': [270,271,276,277],
        'IL':[len(il_270),len(il_271),len(il_276),len(il_277)],
        'MT':[len(mt_271),len(mt_271),len(mt_276),len(mt_277)], 
        'NM':[len(nm_270),len(nm_271),len(nm_276),len(nm_277)],
        'OK':[len(ok_270),len(ok_271),len(ok_276),len(ok_277)],
        'TX':[len(tx_270),len(tx_271),len(tx_276),len(tx_277)]

        }

    df = pd.DataFrame(data)
    
    print (df)
    
    
    
    
    
    
    ######################################### RealMed ##################################################
    type_270 = [i.split('        ')[3] for i in realmed if '*1030223*' in i]    
    il_270 = [i for i in type_270 if "*621*" in i]
    mt_270 = [i for i in type_270 if "*751*" in i]
    nm_270 = [i for i in type_270 if "*290*" in i]
    ok_270 = [i for i in type_270 if "*340*" in i]
    tx_270 = [i for i in type_270 if "*400*" in i]
    #####################################
    type_271 = [i.split('        ')[3] for i in realmed if '*191703*' in i]
    il_271 = [i for i in type_271 if "*621*" in i]
    mt_271 = [i for i in type_271 if "*751*" in i]
    nm_271 = [i for i in type_271 if "*290*" in i]
    ok_271 = [i for i in type_271 if "*340*" in i]
    tx_271 = [i for i in type_271 if "*400*" in i]
    ######################################
    type_276 = [i.split('        ')[3] for i in realmed if '*085707*' in i]
    il_276 = [i for i in type_276 if "*621*" in i]
    mt_276 = [i for i in type_276 if "*751*" in i]
    nm_276 = [i for i in type_276 if "*290*" in i]
    ok_276 = [i for i in type_276 if "*340*" in i]
    tx_276 = [i for i in type_276 if "*400*" in i]
    #####################################
    type_277 = [i.split('        ')[3] for i in realmed if '*0877077*' in i]
    il_277 = [i for i in type_277 if "*621*" in i]
    mt_277 = [i for i in type_277 if "*751*" in i]
    nm_277 = [i for i in type_277 if "*290*" in i]
    ok_277 = [i for i in type_277 if "*340*" in i]
    tx_277 = [i for i in type_277 if "*400*" in i]
    data = {'Vendor': ['RealMed', 'RealMed', 'RealMed', 'RealMed'],#, 'RealMed','RealMed','RealMed','RealMed','Hews','Hews','Hews','Hews'],
        'Type': [270,271,276,277],
        'IL':[len(il_270),len(il_271),len(il_276),len(il_277)],
        'MT':[len(mt_271),len(mt_271),len(mt_276),len(mt_277)], 
        'NM':[len(nm_270),len(nm_271),len(nm_276),len(nm_277)],
        'OK':[len(ok_270),len(ok_271),len(ok_276),len(ok_277)],
        'TX':[len(tx_270),len(tx_271),len(tx_276),len(tx_277)]

        }

    df = pd.DataFrame(data)
    print('==========*****==========')
    print (df)
    # print('RealMed ','270',len(il_270),len(mt_270),len(nm_270),len(ok_270),len(tx_270),'\nRealMed ','271',len(il_271),len(mt_271),len(nm_271),len(ok_271),len(tx_271),'\nRealMed ','276',len(il_276),len(mt_276),len(nm_276),len(ok_276),len(tx_276),'\nRealMed ','277',len(il_277),len(mt_277),len(nm_277),len(ok_277),len(tx_277), sep= '      ')
    ########################################## Hews ##################################
    type_270 = [i.split('        ')[3] for i in hews if '*1030223*' in i]    
    il_270 = [i for i in type_270 if "*621*" in i]
    mt_270 = [i for i in type_270 if "*751*" in i]
    nm_270 = [i for i in type_270 if "*290*" in i]
    ok_270 = [i for i in type_270 if "*340*" in i]
    tx_270 = [i for i in type_270 if "*400*" in i]
    #####################################
    type_271 = [i.split('        ')[3] for i in hews if '*191703*' in i]
    il_271 = [i for i in type_271 if "*621*" in i]
    mt_271 = [i for i in type_271 if "*751*" in i]
    nm_271 = [i for i in type_271 if "*290*" in i]
    ok_271 = [i for i in type_271 if "*340*" in i]
    tx_271 = [i for i in type_271 if "*400*" in i]
    ######################################
    type_276 = [i.split('        ')[3] for i in hews if '*085707*' in i]
    il_276 = [i for i in type_276 if "*621*" in i]
    mt_276 = [i for i in type_276 if "*751*" in i]
    nm_276 = [i for i in type_276 if "*290*" in i]
    ok_276 = [i for i in type_276 if "*340*" in i]
    tx_276 = [i for i in type_276 if "*400*" in i]
    #####################################
    type_277 = [i.split('        ')[3] for i in hews if '*0877077*' in i]
    il_277 = [i for i in type_277 if "*621*" in i]
    mt_277 = [i for i in type_277 if "*751*" in i]
    nm_277 = [i for i in type_277 if "*290*" in i]
    ok_277 = [i for i in type_277 if "*340*" in i]
    tx_277 = [i for i in type_277 if "*400*" in i]
    data = {'Vendor': ['Hews', 'Hews', 'Hews', 'Hews'],#, 'RealMed','RealMed','RealMed','RealMed','Hews','Hews','Hews','Hews'],
        'Type': [270,271,276,277],
        'IL':[len(il_270),len(il_271),len(il_276),len(il_277)],
        'MT':[len(mt_271),len(mt_271),len(mt_276),len(mt_277)], 
        'NM':[len(nm_270),len(nm_271),len(nm_276),len(nm_277)],
        'OK':[len(ok_270),len(ok_271),len(ok_276),len(ok_277)],
        'TX':[len(tx_270),len(tx_271),len(tx_276),len(tx_277)]
        }

    df = pd.DataFrame(data)
    print('==========*****==========')
    print(df)
    # print('Hews  ','  270',len(il_270),len(mt_270),len(nm_270),len(ok_270),len(tx_270),'\nHews  ','  271',len(il_271),len(mt_271),len(nm_271),len(ok_271),len(tx_271),'\nHews  ','  276',len(il_276),len(mt_276),len(nm_276),len(ok_276),len(tx_276),'\nHews  ','  277',len(il_277),len(mt_277),len(nm_277),len(ok_277),len(tx_277), sep= '      ')
    
if "__main__" == __name__:
    workingDirectory  = os.path.realpath(sys.argv[0])
    converter()
