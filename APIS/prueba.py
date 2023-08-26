import requests
import json 

url= 'https://rickandmortyapi.com/api/character/{}'

#print(j)
i=1
while i < 5:
    url='https://rickandmortyapi.com/api/character/{}'.format(i)
    r = requests.get(url)
    j = r.json()
    I=j['name']
    II=j['status']
    print('{} esta {}'.format(I,II))
    i+=1