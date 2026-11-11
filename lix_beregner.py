from unittest import case

import requests

def tæl_ord(t:str):
    return t.count(' ')

def tæl_sætninger(t:str):
    return t.count('.')

def tæl_lange_ord(t:str):
    words = t.split(' ')
    count = 0
    for word in words:
        if len(word) > 6:
            count += 1
    return count

def bestem_sværhedsgrad(index:int):
    match index:
        case x if x <= 24:
            return 'Let for alle'
        case x if 24 <= x < 35:
            return 'Let for øvede'
        case x if 35 <= x < 45:
            return 'Middel'
        case x if 45 <= x < 55:
            return 'Svær'
        case x if x >= 55:
            return 'Meget svær'


# Hent data
req = requests.get('https://lorem.place/api/generate?format=text&paragraphs=50&words=100&random=true&start=false')

# Behandl data
raw = req.json()

# Læs rå tekst
text = raw['data']['text']

antal_ord = tæl_ord(text)
antal_sætninger = tæl_sætninger(text)
antal_lange_ord = tæl_lange_ord(text)

print(f'Ord: {antal_ord}\t\t(faktisk: {raw['meta']['totalWords']})')
print(f'Sætninger: {antal_sætninger}\t(faktisk: {raw['meta']['paragraphs']})')
print(f'Lange ord: {antal_lange_ord}')

lix = (antal_ord / antal_sætninger) + ((antal_lange_ord * 100) / antal_ord)
print(f'LIX-tal: {round(lix)}\t({bestem_sværhedsgrad(lix)})')
