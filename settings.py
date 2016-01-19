from ConfigParser import ConfigParser

class Settings(object):

    def __init__(self):
        config = ConfigParser()
        config.read('settings/settings.ini')
        self.difficulty = config.get("Game","difficulty")
        self.name = config.get("PlayerDefaults","name")
        self.goal = config.get("Game","rooms")

    def getGameDiff(self):
        return self.difficulty

    def getGoal(self):
        return self.goal

    def closeFile(file):
        with open('settings/settings.ini', 'w') as configfile:
            file.write(configfile)
