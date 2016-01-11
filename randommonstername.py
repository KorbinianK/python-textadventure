import textwrap, random

# To use this class:
# from randommonstername import RandomMonsterName
#
# monstername = RandomMonsterName()
# print monstername.getName()
#


class RandomMonsterName(object):

    def __init__(self):
        with open('txt/namegenerator/name.txt', 'r') as f:
            self.names = f.read().splitlines()
        with open('txt/namegenerator/pre.txt', 'r') as f:
            self.pre = f.read().splitlines()
        with open('txt/namegenerator/adjective.txt', 'r') as f:
            self.adjectives = f.read().splitlines()
        with open('txt/namegenerator/type.txt', 'r') as f:
            self.types = f.read().splitlines()
        with open('txt/namegenerator/objective.txt', 'r') as f:
            self.tobject = f.read().splitlines()

        self.shuffName = sorted(self.names, key=lambda k: random.random())[0]
        self.shuffAdj = sorted(self.adjectives, key=lambda k: random.random())[0]
        self.shuffType = sorted(self.types, key=lambda k: random.random())[0]
        self.shuffObj =  sorted(self.tobject, key=lambda k: random.random())[0]


#
# Returns the full name incl. type etc.
#
    def getFullName(self):
        monstername = self.shuffName +", "+self.pre[0]+" "+self.shuffAdj +" "+ self.shuffType+" "+self.shuffObj
        return monstername

#
# Returns only the first name
#
    def getShortName(self):
        return  self.shuffName
