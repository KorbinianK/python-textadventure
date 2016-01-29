

import random, time,sys
from random import uniform
from stringhandler import Stringhandler

class ByteBoss(object):

    def __init__(self):
        self.name = "The Megabyte"
        self.shortname = "Megabyte"
        self.isBoss = True
        self.hp = 64
        self.strength = 8
        self.killed = False
        self.handler = Stringhandler()

    def getShortName(self):
        return self.shortname

class HipsterBoss(object):

    def __init__(self):
        self.name = "the Hipster"
        self.shortname = "Hipster"
        self.isBoss = True
        self.hp = 60
        self.strength = 8
        self.killed = False
        self.handler = Stringhandler()

    def getShortName(self):
        return self.shortname
