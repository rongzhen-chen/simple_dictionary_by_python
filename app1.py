import json
from difflib import get_close_matches
'''
a simple English dictionary by python3
'''

def loadData():
    ''' load the data'''
    data = json.load(open("data.json",'r'))
    return data

def searchWord(str_search, data):
    '''find the definition of the word "str_search" from database "data"
    '''

    str = str_search.lower()

    ### find the similarity from str to some strings in database
    strSim = get_close_matches(str,list(data.keys()), n=3)

    if str_search in data:
        strDef = data[str_search]
        return strDef
    elif str in data:
            strDef = data[str]
            return strDef
    elif len(strSim) > 0:
        strDec = input("can you find the word from {}? enter 'Y or y', otherwise press any key to return: ".format(strSim))
        #strDec = input("do you mean {}? if so, enter 'Y or y', otherwise press any key to return: ".format(strSim[0]))
        if strDec == "Y" or strDec== "y":
            index_word = input("enter the index: ")
            strDef = data[strSim[int(index_word)]]
            return strDef
        else:
            return "can not find the word: {}".format(str)
    else:
            return "can not find the word: {}".format(str)


##### load data #####
data = loadData()

##### choose a word #####
strinput = input("input a word: ")

##### search for the definition of the word
strreturn = searchWord(strinput, data)

##### print output #####
if type(strreturn) == str:
    print(strreturn)
else:
    for item in strreturn:
        print(item)
