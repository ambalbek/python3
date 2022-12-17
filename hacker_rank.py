import logging
logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)
if __name__ == '__main__':
    newlist = []
    temp={}
    reallist = [['Harry',37.21],['Berry',37.21],['Tina',37.2], ['Akriti',41], ['Harsh',39]]
    #dictlist = sorted(reallist)
    newdict = dict(reallist)
    # for k,v in dictlist.items():
    #     if v in newdict.values():
    #         newdict[k]=v
    for k,v in newdict.items():
        if v not in temp:
            temp[v]=[k]
        else:
            temp[v].append(k)
    for i in temp.values():
        if len(i)>1:
            for a in i:
                logger.info(a)
                print(a)


# if __name__ == '__main__':    
#     newlist = []
#     for _ in range(int(input())):
#         zp=[]
#         name = input()
#         score = float(input())
#         zp.append(name) 
#         zp.append(score)     
#         newlist.append(zp)
#     print(newlist)
#     newdict= dict(newlist)
#     temp={}
#     for k,v in sorted(newdict.items()):
#         if v not in temp:
#             temp[v]=[k]
#         else:
#             temp[v].append(k)
#     for i in temp.values():
#         if len(i)>1:
#             for a in i:
#                 print(a)


