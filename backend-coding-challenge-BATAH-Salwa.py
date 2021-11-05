import pandas
import requests

repositories=[]

# Get data and store in variable
req=requests.get("https://api.github.com/search/repositories?q=created:>2021-08-01&sort=stars&order=desc")
data=pandas.read_json(req.content)

# loop over items, for every item get its language and name, store it as dictionary in a list if it doesn't exist, or add it to an already existing dic
for item in data['items']:
    # varible to check if it is already added or not
    added=0
    for dic in repositories:
        if dic['language'] == item['language']:
            dic['number']+=1
            dic['repos'].append(item['name'])
            added=1
            break
    #if not added, create a new dic        
    if(added==0):
        dic={'language':item['language'] , 'number': 1 , 'repos':[item['name']]}
        repositories.append(dic)

# print answer:
for dic in repositories:
    print( "- " , dic['number'] , " repositories of {{ " , dic['language'] , " }} which are: ")
    for l in dic['repos']:
        print("         --- " , l)

