import os.path,sys
import pandas as pd

def logs_from_file(logs):
    fileName = os.path.join(directory,'../logs.txt')
    test_file = open(fileName,'r')
    logs['Availity']=[i for i in test_file.readlines() if '*030240928' in i]
    logs['Availity']=[i for i in test_file.readlines() if '*030240122' in i]
    logs['Availity']=[i for i in test_file.readlines() if '*030550127' in i]
    test_file.close()

def init_logs():
    logs = {}
    logs['Availity']=[]
    logs['RealMed']=[]
    logs['Hews']=[]
    return logs
    
def converter():
    logs = init_logs()
    logs_from_file(logs)
    avility=logs['Availity']
    realmed=logs['RealMed']
    hews = logs['Hews']  
    
    ############################ Availity ###############################
    av_type_270 = [i for i in avility if '*1030223*' in i]    
    av_il_270 = [i for i in av_type_270 if "*621*" in i]
    av_mt_270 = [i for i in av_type_270 if "*751*" in i]
    av_nm_270 = [i for i in av_type_270 if "*290*" in i]
    av_ok_270 = [i for i in av_type_270 if "*340*" in i]
    av_tx_270 = [i for i in av_type_270 if "*400*" in i]
    #####################################
    av_type_271 = [i for i in avility if '*191703*' in i]
    av_il_271 = [i for i in av_type_271 if "*621*" in i]
    av_mt_271 = [i for i in av_type_271 if "*751*" in i]
    av_nm_271 = [i for i in av_type_271 if "*290*" in i]
    av_ok_271 = [i for i in av_type_271 if "*340*" in i]
    av_tx_271 = [i for i in av_type_271 if "*400*" in i]
    ######################################
    av_type_276 = [i for i in avility if '*085707*' in i]
    av_il_276 = [i for i in av_type_276 if "*621*" in i]
    av_mt_276 = [i for i in av_type_276 if "*751*" in i]
    av_nm_276 = [i for i in av_type_276 if "*290*" in i]
    av_ok_276 = [i for i in av_type_276 if "*340*" in i]
    av_tx_276 = [i for i in av_type_276 if "*400*" in i]
    #####################################
    av_type_277 = [i for i in avility if '*0877077*' in i]
    av_il_277 = [i for i in av_type_277  if "*621*" in i]
    av_mt_277 = [i for i in av_type_277  if "*751*" in i]
    av_nm_277 = [i for i in av_type_277  if "*290*" in i]
    av_ok_277 = [i for i in av_type_277  if "*340*" in i]
    av_tx_277 = [i for i in av_type_277  if "*400*" in i]
    
    ######################################### RealMed ##################################################
    rm_type_270 = [i for i in realmed if '*1030223*' in i]    
    rm_il_270 = [i for i in rm_type_270 if "*621*" in i]
    rm_mt_270 = [i for i in rm_type_270 if "*751*" in i]
    rm_nm_270 = [i for i in rm_type_270 if "*290*" in i]
    rm_ok_270 = [i for i in rm_type_270 if "*340*" in i]
    rm_tx_270 = [i for i in rm_type_270 if "*400*" in i]
    #####################################
    rm_type_271 = [i for i in realmed if '*191703*' in i]
    rm_il_271 = [i for i in rm_type_271 if "*621*" in i]
    rm_mt_271 = [i for i in rm_type_271 if "*751*" in i]
    rm_nm_271 = [i for i in rm_type_271 if "*290*" in i]
    rm_ok_271 = [i for i in rm_type_271 if "*340*" in i]
    rm_tx_271 = [i for i in rm_type_271 if "*400*" in i]
    ######################################
    rm_type_276 = [i for i in realmed if '*085707*' in i]
    rm_il_276 = [i for i in rm_type_276 if "*621*" in i]
    rm_mt_276 = [i for i in rm_type_276 if "*751*" in i]
    rm_nm_276 = [i for i in rm_type_276 if "*290*" in i]
    rm_ok_276 = [i for i in rm_type_276 if "*340*" in i]
    rm_tx_276 = [i for i in rm_type_276 if "*400*" in i]
    #####################################
    rm_type_277  = [i for i in realmed if '*0877077*' in i]
    rm_il_277 = [i for i in rm_type_277  if "*621*" in i]
    rm_mt_277 = [i for i in rm_type_277  if "*751*" in i]
    rm_nm_277 = [i for i in rm_type_277  if "*290*" in i]
    rm_ok_277 = [i for i in rm_type_277  if "*340*" in i]
    rm_tx_277 = [i for i in rm_type_277  if "*400*" in i] 
       
    ########################################## Hews ##################################
    he_type_270  = [i for i in hews if '*1030223*' in i]    
    he_il_270 = [i for i in  he_type_270  if "*621*" in i]
    he_mt_270 = [i for i in  he_type_270  if "*751*" in i]
    he_nm_270 = [i for i in  he_type_270  if "*290*" in i]
    he_ok_270 = [i for i in  he_type_270  if "*340*" in i]
    he_tx_270 = [i for i in  he_type_270  if "*400*" in i]
    #####################################
    av_type_271 = [i for i in hews if '*191703*' in i]
    he_il_271 = [i for i in av_type_271 if "*621*" in i]
    he_mt_271 = [i for i in av_type_271 if "*751*" in i]
    he_nm_271 = [i for i in av_type_271 if "*290*" in i]
    he_ok_271 = [i for i in av_type_271 if "*340*" in i]
    he_tx_271 = [i for i in av_type_271 if "*400*" in i]
    ######################################
    av_type_276 = [i for i in hews if '*085707*' in i]
    he_il_276 = [i for i in av_type_276 if "*621*" in i]
    he_mt_276 = [i for i in av_type_276 if "*751*" in i]
    he_nm_276 = [i for i in av_type_276 if "*290*" in i]
    he_ok_276 = [i for i in av_type_276 if "*340*" in i]
    he_tx_276 = [i for i in av_type_276 if "*400*" in i]
    #####################################
    av_type_277  = [i for i in hews if '*0877077*' in i]
    he_il_277 = [i for i in av_type_277  if "*621*" in i]
    he_mt_277 = [i for i in av_type_277  if "*751*" in i]
    he_nm_277 = [i for i in av_type_277  if "*290*" in i]
    he_ok_277 = [i for i in av_type_277  if "*340*" in i]
    he_tx_277 = [i for i in av_type_277  if "*400*" in i]

    #######################**Table Part**####################################################
    data = {'Vendor': ['Availity', 'Availity', 'Availity', 'Availity','RealMed','RealMed','RealMed','RealMed','Hews','Hews','Hews','Hews'],
        'Type': [270,271,276,277,270,271,276,277,270,271,276,277],
        'IL':[len(av_il_270),len(av_il_271),len(av_il_276),len(av_il_277),len(rm_il_270),len(rm_il_271),len(rm_il_276),len(rm_il_277),len(he_il_270),len(he_il_271),len(he_il_276),len(he_il_277)],
        'MT':[len(av_mt_270),len(av_mt_271),len(av_mt_276),len(av_mt_277),len(rm_mt_270),len(rm_mt_271),len(rm_mt_276),len(rm_mt_277),len(he_mt_270),len(he_mt_271),len(he_mt_276),len(he_mt_277)], 
        'NM':[len(av_nm_270),len(av_nm_271),len(av_nm_276),len(av_nm_277),len(rm_nm_270),len(rm_nm_271),len(rm_nm_276),len(rm_nm_277),len(he_nm_270),len(he_nm_271),len(he_nm_276),len(he_nm_277)],
        'OK':[len(av_ok_270),len(av_ok_271),len(av_ok_276),len(av_ok_277),len(rm_ok_270),len(rm_ok_271),len(rm_ok_276),len(rm_ok_277),len(he_ok_270),len(he_ok_271),len(he_ok_276),len(he_ok_277)],
        'TX':[len(av_tx_270),len(av_tx_271),len(av_tx_276),len(av_tx_277),len(rm_tx_270),len(rm_tx_271),len(rm_tx_276),len(rm_tx_277),len(he_tx_270),len(he_tx_271),len(he_tx_276),len(he_tx_277)]

        }

    df = pd.DataFrame(data)
    
    print(df)

if "__main__" == __name__:
    directory = os.path.realpath(sys.argv[0])
    converter()
    