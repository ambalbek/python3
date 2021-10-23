import os.path,sys
import pandas as pd

def logs_from_file(logs):
    fileName = os.path.join(directory,'../logs.txt')
    test_file = open(fileName,'r')  
    for line in test_file.readlines():
        if '*030240928' in line:
            logs['Availity'].append(line)
        if '*030240122' in line:
            logs['RealMed'].append(line)
        if '*030550127' in line:
            logs['Hews'].append(line)
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
    av_il_270 = []
    av_mt_270 = []
    av_nm_270 = []
    av_ok_270 = []
    av_tx_270 = []
    av_il_271 = []
    av_mt_271 = []
    av_nm_271 = []
    av_ok_271 = []
    av_tx_271 = []
    av_il_276 = []
    av_mt_276 = []
    av_nm_276 = []
    av_ok_276 = []
    av_tx_276 = []
    av_il_277 = []
    av_mt_277 = []
    av_nm_277 = []
    av_ok_277 = []
    av_tx_277 = []
    rm_il_270 = []
    rm_mt_270 = []
    rm_nm_270 = []
    rm_ok_270 = []
    rm_tx_270 = []
    rm_il_271 = []
    rm_mt_271 = []
    rm_nm_271 = []
    rm_ok_271 = []
    rm_tx_271 = []
    rm_il_276 = []
    rm_mt_276 = []
    rm_nm_276 = []
    rm_ok_276 = []
    rm_tx_276 = []
    rm_il_277 = []
    rm_mt_277 = []
    rm_nm_277 = []
    rm_ok_277 = []
    rm_tx_277 = []
    he_il_270 = []
    he_mt_270 = []
    he_nm_270 = []
    he_ok_270 = []
    he_tx_270 = []
    he_il_271 = []
    he_mt_271 = []
    he_nm_271 = []
    he_ok_271 = []
    he_tx_271 = []
    he_il_276 = []
    he_mt_276 = []
    he_nm_276 = []
    he_ok_276 = []
    he_tx_276 = []
    he_il_277 = []
    he_mt_277 = []
    he_nm_277 = []
    he_ok_277 = []
    he_tx_277 = []
    
    av_type_270 = [i for i in avility if '*1030223*' in i]  
    for i in av_type_270:
        if "*621*" in i:
            av_il_270.append(i)
           
        if "*751*" in i:
            av_mt_270.append(i)
        if "*290*" in i:
            av_nm_270.append(i)
        if "*340*" in i:
            av_ok_270.append(i)
        if "*400*" in i:
            av_tx_270.append(i)


    #####################################
    av_type_271 = [i for i in avility if '*191703*' in i]
    for i in av_type_271:
        if "*621*" in i:
            av_il_271.append(i)
        if "*751*" in i:
            av_mt_271.append(i)
        if "*290*" in i:
            av_nm_271.append(i)
        if "*340*" in i:
            av_ok_271.append(i)
        if "*400*" in i:
            av_tx_271.append(i)

    ######################################
    av_type_276 = [i for i in avility if '*085707*' in i]
    for i in av_type_276:
        if "*621*" in i:
            av_il_276.append(i)
        if "*751*" in i:
            av_mt_276.append(i)
        if "*290*" in i:
            av_nm_276.append(i)
        if "*340*" in i:
            av_ok_276.append(i)
        if "*400*" in i:
            av_tx_276.append(i)

    #####################################
    av_type_277 = [i for i in avility if '*0877077*' in i]
    for i in av_type_277:
        if "*621*" in i:
            av_il_277.append(i)
        if "*751*" in i:
            av_mt_277.append(i)
        if "*290*" in i:
            av_nm_277.append(i)
        if "*340*" in i:
            av_ok_277.append(i)
        if "*400*" in i:
            av_tx_277.append(i)


    
    ######################################### RealMed ##################################################
    rm_type_270 = [i for i in realmed if '*1030223*' in i]  
    
    for i in rm_type_270:
        if "*621*" in i:
            rm_il_270.append(i)
        if "*751*" in i:
            rm_mt_270.append(i)
        if "*290*" in i:
            rm_nm_270.append(i)
        if "*340*" in i:
            rm_ok_270.append(i)
        if "*400*" in i:
            rm_tx_270.append(i)

    #####################################
    rm_type_271 = [i for i in realmed if '*191703*' in i]
    for i in rm_type_271:
        if "*621*" in i:
            rm_il_271.append(i)
        if "*751*" in i:
            rm_mt_271.append(i)
        if "*290*" in i:
            rm_nm_271.append(i)
        if "*340*" in i:
            rm_ok_271.append(i)
        if "*400*" in i:
            rm_tx_271.append(i)


    ######################################
    rm_type_276 = [i for i in realmed if '*085707*' in i]
    for i in rm_type_276:
        if "*621*" in i:
            rm_il_276.append(i)
        if "*751*" in i:
            rm_mt_276.append(i)
        if "*290*" in i:
            rm_nm_276.append(i)
        if "*340*" in i:
            rm_ok_276.append(i)
        if "*400*" in i:
            rm_tx_276.append(i)

    #####################################
    rm_type_277  = [i for i in realmed if '*0877077*' in i]
    for i in rm_type_277:
        if "*621*" in i:
            rm_il_277.append(i)
        if "*751*" in i:
            rm_mt_277.append(i)
        if "*290*" in i:
            rm_nm_277.append(i)
        if "*340*" in i:
            rm_ok_277.append(i)
        if "*400*" in i:
            rm_tx_277.append(i)

       
    ########################################## Hews ##################################
    he_type_270  = [i for i in hews if '*1030223*' in i]  
    for i in he_type_270:
        if "*621*" in i:
            he_il_270.append(i)
        if "*751*" in i:
            he_mt_270.append(i)
        if "*290*" in i:
            he_nm_270.append(i)
        if "*340*" in i:
            he_ok_270.append(i)
        if "*400*" in i:
            he_tx_270.append(i)

    #####################################
    he_type_271 = [i for i in hews if '*191703*' in i]
    for i in he_type_271:
        if "*621*" in i:
            he_il_271.append(i)
        if "*751*" in i:
            he_mt_271.append(i)
        if "*290*" in i:
            he_nm_271.append(i)
        if "*340*" in i:
            he_ok_271.append(i)
        if "*400*" in i:
            he_tx_271.append(i)

    ######################################
    he_type_276 = [i for i in hews if '*085707*' in i]
    for i in he_type_276:
        if "*621*" in i:
            he_il_276.append(i)
        if "*751*" in i:
            he_mt_276.append(i)
        if "*290*" in i:
            he_nm_276.append(i)
        if "*340*" in i:
            he_ok_276.append(i)
        if "*400*" in i:
            he_tx_276.append(i)

    #####################################
    he_type_277  = [i for i in hews if '*0877077*' in i]
    for i in he_type_277:
        if "*621*" in i:
            he_il_277.append(i)
        if "*751*" in i:
            he_mt_277.append(i)
        if "*290*" in i:
            he_nm_277.append(i)
        if "*340*" in i:
            he_ok_277.append(i)
        if "*400*" in i:
            he_tx_277.append(i)

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
    import time
    start = time.time() * 1
    directory = os.path.realpath(sys.argv[0])
    
    converter()
    end = time.time() * 1
    print(end - start)
    