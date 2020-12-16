import requests
from datetime import datetime
now = datetime.now()
curr = now.strftime("%Y-%m-%d") # current data in format year-month(number)-day(number)
langs = set() # Store unique names of language
repos = [] # store repositories data
repos_by_lang = {} # store repositories in a dictionary as language: (repos using this language ,number of repos using this language)
"""
        1- Send GET Request to Github API by parameters (created date,sort method,sort order,page i want)
        2- Jsonify the response
        3- Append the repos in list  break at 100 (I wanna first 100 trending)
        4- Stroe langs in lang set to prevent redunadant results
        5- filter the repos by the langyage attribute and store the results in list reps
        6- Add reps list and its length (number of repos used the language) as values coressponding to language as a key
"""
try:
    for i in range(1,5):

        URL = "https://api.github.com/search/repositories?q=created:<" + curr+ "&sort=stars&order=desc&page="+str(i)
        res = requests.get(URL).json()
        for j in res['items']:
            repos.append(j)
        if len(repos) == 100: 
            break
except KeyError:
    print("finished")
for repo in repos:
    if repo['language'] != None :
        langs.add(repo['language'])
for lang in langs:
    reps =  list(filter(lambda x: x['language'] == lang,repos))
    repos_by_lang[lang] = (reps,len(reps))
    print("{} :  numebr of repos : {}".format(lang,len(reps)))