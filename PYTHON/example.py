#!/usr/bin/env python3
with open('requirements.txt', 'w+') as newfile:
    newfile.write('aziz\nakmanai\nemir')
with open('requirements.txt', 'r') as f:
    print(f.read())