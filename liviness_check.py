import os
inventory_dir = os.path.dirname(__file__)
file_name = 'inventory.txt'
real_path = os.path.join(inventory_dir,file_name)
hostfile = open(file_name, 'r')
hosts = hostfile.readlines()
for i in hosts:
    responce = os.system('nslookup ' + i)
    if responce == 0:
        status = i.rstrip()+ ' zelenniy'
    else:
        status = i + ' ne zelenniy'
    print(status)