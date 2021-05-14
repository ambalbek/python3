import json
from difflib import get_close_matches
data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    for i in data:
        pass

    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input('Did you mean %s? enter Y for yes or N for no:' % get_close_matches(w, data.keys())[0])
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        if yn =='n':
            return 'please double check it.'
        else:
            return 'I didnt understand your request. BYE'
    else:
        return 'please double check it.'
word = input('Enter word: ')
output = (translate(word))
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)