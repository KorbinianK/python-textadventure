
class Room(object):

  def __init__(self,difficulty,player):
    self.hasMonster = True
    self.hasChest = False
    self.isDone = False
    self.difficulty = difficulty
    self.player = player

    def newRoom(self):
        print "You enter a dark room."

    def inspectRoom(self):
        
        return
