# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:06:13 2016

@author: Arthur
"""

from kmeansAlgo import Model

X = np.genfromtxt("C:\\Users\\Arthur\\Documents\\GitHub\\codejam\\Data Fetcher\\forAlgo.csv",delimiter=',')
mod = Model()
testsamp = X[1,:].reshape(1, -1)
print(mod.predict(testsamp))
print(mod.model)


        #Pull Data
        query = "http://www.omdbapi.com/?t=" + movTitle + "&y=&plot=long&tomatoes=true&r=json&type=series"
        r = requests.get(query)
        
        show = json.loads(r.content.decode("utf-8"))
        #print(json.dumps(showimdb, sort_keys=False,indent=4, separators=(',', ': ')))
        
        print("Getting Metacritic Data")
        metacriticData = scraper.getMetaCriticData(movTitle)
        print("Got Meta Data")
        
        if(not(isValid(show))):
            continue
        if(type(metacriticData) is int):
            metacriticData = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
            print("Bad Meta for Show: " + movTitle)
        
        show["criticscore"] = metacriticData[0]
        show["criticcount"] = metacriticData[1]
        show["criticpos"] = metacriticData[2]
        show["criticmixed"] = metacriticData[3]
        show["criticneg"] = metacriticData[4]
        show["userscore"] = metacriticData[5]
        show["usercount"] = metacriticData[6]
        show["userpos"] = metacriticData[7]
        show["usermixed"] = metacriticData[8]
        show["userneg"] = metacriticData[9]
        
        exportHelper.cleanShow(show)
        
        genres = show["Genre"]
        
        to_pred = []
        to_pred.append(show["imdbVotes"])
        for i in range(3):
            if(len(genres)>i):
                temp = genres_constant.getGenreNum(genres[i])
                to_pred.append(temp)
            else :
                to_pred.append(temp)
        to_pred.append(show["imdbRating"])
        to_pred.append(show["criticscore"])
        to_pred.append(show["criticcount"])
        to_pred.append(show["criticpos"])
        to_pred.append(show["criticmixed"])
        to_pred.append(show["userscore"])
        to_pred.append(show["usercount"])
        to_pred.append(show["userpos"])
        to_pred.append(show["usermixed"])
        to_pred.append(show["userneg"])
        
        
        algoData = np.asarray(to_pred).reshape(1, -1)
        res = mod.predict(algoData)
            
        show["Kmeans"] = int(res[0])