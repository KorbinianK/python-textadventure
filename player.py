class Player(object):

    def __init__(self):
    	self.name = "a"
        self.hp = 100
        self.facesMonster = False
        self.victory = False
        self.condition = "normal"
        self.strength = 1
        self.armor = 1
        self.level = 1
        self.inventory =[]
        self.hasItems=False

    def is_alive(self):
        return self.hp > 0

    def takeDamage(self, damage):
        self.hp -= damage

    def getHP(self):
        return self.hp

    def setCondition(self, condition):
    	self.condition = condition

    def is_facing_Monster(self):
        return self.facesMonster

    def facing_Monster(self, status):
        self.facesMonster = status

    def addItem(self, item):

        self.inventory.append(item)
        self.hasItems = True
        #print "added"+item.name
        print self.inventory[0].name + str(len(self.inventory))

    def printInventory(self):
        string = ""
        print len(self.inventory)
        if len(self.inventory) > 1:
            for index,item in enumerate(self.inventory, start=1):
                string = string+ str(index) +" "+item.name+", "
            return string
        else:
            return self.inventory[0].name
    #    return self.inventory[0].name + self.inventory[1].name
