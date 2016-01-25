from colorama import init, Fore, Back, Style
import random


class Stringhandler(object):

    def __init__(self):

        self.strlist = []

    # Template:
    #
    # def  abc (self):
    #     if type == "":
    #
    #         self.strlist.append("")
    #         self.strlist.append("")
    #         self.strlist.append("")
    #         self.strlist.append("")
    #         string = random.choice(self.strlist)
    #     del self.strlist[:]
    #     return self.modify(string,player)

    def strBoss (self,type,player,damage):

        if type == "bHit":
            self.strlist.append("01101111 01110101 01110100 01100011 01101000")
            self.strlist.append("01100100 01101111 01101110 01110100 00100111 00100000 01101000 01110101 01110010 01110100 00100000 01101101 01100101")
            # self.strlist.append("")
            # self.strlist.append("")
            string = random.choice(self.strlist)

        if type == "bDie":
            self.strlist.append("59 6f 75 20 77 69 6c 6c 20 72 65 67 72 65 74 20 74 68 69 73 21 (dead)")
            self.strlist.append("4e 4f 4f 4f 4f (dead)")
            # self.strlist.append("")
            # self.strlist.append("")
            string = random.choice(self.strlist)

        if type == "bSpawn":
            self.strlist.append("Oh shit... it's a MEGABYTE!!!!")
            # self.strlist.append("4e 4f 4f 4f 4f")
            # self.strlist.append("")
            # self.strlist.append("")
            string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)

    def strIntro(self):
        """
        The intro text for the player, asking for his/her name
        """
        player = None
        self.strlist.append('Hello there!\nHow should we call you?')
        self.strlist.append("Oh, a new face.\nWhat's your name?")
        self.strlist.append('Hello there new fella!\nWould you mind telling us your name?')
        self.strlist.append('Ok, take a deep breath. This might be the most important decision of your life.\nHow will you name yourself? ')
        self.strlist.append('No no no, take your time.\nI understand that remembering your name might be hard.')
        string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)

    def strGreeting(self,player):
        """
        Greets the new player
        """
        playername = str(Fore.CYAN+player.name+ Fore.WHITE)
        self.strlist.append('Hello '+playername+'!\nWelcome to our world of pain and suffering!')
        self.strlist.append('MWAHAHAHAHAHAHA!\nNow you are trapped here, ' +playername+'!')
        self.strlist.append('Welcome to the DARKSIDE '+playername+'!\nHere take some cookies! *evillaugh*')
        self.strlist.append('Welcome to our little dungeon, '+playername+'!\nWe hope you enjoy your stay and survive so you can recommend us to your friends.')
        string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)



    def strActions(self,type,player,room):
        look = str(Fore.CYAN + "look around"+Fore.WHITE)
        cont = str(Fore.CYAN + "continue"+Fore.WHITE)
        monstershort =  str(Fore.GREEN + room.monster.getShortName()+Fore.WHITE)
        chest = str(Fore.YELLOW + "closed chest"+Fore.WHITE)

        if type == "roomEmpty":

            self.strlist.append("The room is empty... like your soul.\nDo you want to " + cont +" or " + look +"?")
            self.strlist.append("It seems like the room is all empty.\nDo you want to " + cont +" or " + look +"?")
            self.strlist.append("Wanna " + look +"? Something might be hidden in this room.")
            # self.strlist.append("")
            string = random.choice(self.strlist)

        if type == "moving":

            self.strlist.append("Moving towards the door")
            self.strlist.append("You are toddling slowly to the door")
            # self.strlist.append("")
            # self.strlist.append("")
            string = random.choice(self.strlist)

        if type == "nextRoomMonster":

            self.strlist.append("You almost stumble over the carcass of "+monstershort+" as you walk through the door into the next room.")
            self.strlist.append("Finally, you overturned the foe. Weakend, but still breating, you continue your journey.")
            # self.strlist.append("")
            # self.strlist.append("")
            string = random.choice(self.strlist)

        if type == "moveChest":

                self.strlist.append("Carefully you walk through the darkness. Then you hit your knee on something...\nMaybe you should " + look +" first?")
                self.strlist.append("You toddle very carefully through the darkness without a special direction.\nYou should " + look +" before continuing with your mission.")
                # self.strlist.append("")
                # self.strlist.append("")
                string = random.choice(self.strlist)

        if type == "nextRoom":

                self.strlist.append("You walk through the door into the next room")
                self.strlist.append("You just passed the door of darkness. You are in a new room now.")
                self.strlist.append("You enter the next room.")
                self.strlist.append("Creaking, the next door opens, granting you access to the next room.")
                string = random.choice(self.strlist)

        if type == "attackNoMonster":

                self.strlist.append("You shake your fists and try to attack your shadows")
                # self.strlist.append("")
                # self.strlist.append("")
                # self.strlist.append("")
                string = random.choice(self.strlist)

        if type == "fleeNoMonster":

                self.strlist.append("'Coward! You stay exactly where you are!', shouts a voice and you tremble at its power over you.")
                self.strlist.append("'Leaving so soon?' a voice asked smugly, rooting you in place.")
                # self.strlist.append("")
                # self.strlist.append("")
                string = random.choice(self.strlist)

        if type == "fleeing":

                self.strlist.append("Trying to flee")
                self.strlist.append("Fly, you fool!")
                self.strlist.append("Run,for heaven's sake!!!")
                # self.strlist.append("")
                string = random.choice(self.strlist)

        if type == "lookClosedChest":

                self.strlist.append("You see "+ chest +" in one corner of the room.")
                self.strlist.append("A pretty big "+ chest +" is on your left side and it's kinda sparkling. You should check it out!")
                self.strlist.append("After looking around you see a massive "+ chest +" in the middle of the room.")
                self.strlist.append("But wait, what is that? A "+ chest +"? You do some quick math, which confirms what you already thought: Chest = loot!")
                string = random.choice(self.strlist)

        if type == "lookOpenChest":

                self.strlist.append("There seems to be only an open chest in this room.")
                self.strlist.append("Oh cruel fate! The only chest in this room has already been looted.")
                # self.strlist.append("")
                # self.strlist.append("")
                string = random.choice(self.strlist)

        if type == "lookNothing":

                self.strlist.append("You looked around. Good job")
                self.strlist.append("Look who's all nosy.")
                self.strlist.append("Someone wants to be an investigator, huh?")
                # self.strlist.append("")
                string = random.choice(self.strlist)

        if type == "looking":

                self.strlist.append("Looking around")
                self.strlist.append("Inspecting the room")
                self.strlist.append("Paranoid as you are, you scan the room thoroughly.")
                # self.strlist.append("")
                string = random.choice(self.strlist)

        if type == "chestOpens":

                self.strlist.append("The chest opens with a loud squeaky noise.")
                self.strlist.append("A strong scent of blood is escaping the chest as you opening it.")
                self.strlist.append("You just opened the chest.")
                self.strlist.append('What do we have here?')
                string = random.choice(self.strlist)

        if type == "openChestNoLook":

                self.strlist.append("You seem to imagine things in the darkness. Maybe "+look+" first.")
                # self.strlist.append("")
                # self.strlist.append("")
                # self.strlist.append("")
                string = random.choice(self.strlist)

        if type == "tryOpenChest":

                self.strlist.append("You try to open the chest.")
                self.strlist.append("You want to open the chest, but it's harder than expected.")
                self.strlist.append("This chest is sealed. It takes your time opening it.")
                # self.strlist.append("")
                string = random.choice(self.strlist)

        if type == "searchingInventory":

                self.strlist.append("You are searching your pockets")
                self.strlist.append("Checking your pockets")
                self.strlist.append("You are looking for something in your pockets")
                self.strlist.append('"I am sure I had something useful in there somewhere"')
                string = random.choice(self.strlist)

        # if type == "":
        #
        #         self.strlist.append("")
        #         self.strlist.append("")
        #         self.strlist.append("")
        #         self.strlist.append("")
        #         string = random.choice(self.strlist)

        del self.strlist[:]
        return self.modify(string,player)


    def strChest (self,type,item):
        player = None
        if type == "open":

            item = Fore.YELLOW + item +Fore.WHITE
            itemshort = Fore.YELLOW +item.replace("a ","",1) +Fore.WHITE

            self.strlist.append("You found " + item +"! It has been added to your inventory")
            self.strlist.append("Oooh. Shiny! You got " + item+"!" )
            self.strlist.append("*plop* Wow a new " + itemshort+"!")
            self.strlist.append("Hey, I wonder if this " + itemshort+ " is part of a set...")
            self.strlist.append("This is now MINE! My " + itemshort+"! My PRECIOUS!")
            #         self.strlist.append("")
            #         self.strlist.append("")
            string = random.choice(self.strlist)

        if type == "empty":

            self.strlist.append("It's empty.")
            self.strlist.append("Of course, there is nothing inside...")
            self.strlist.append("Alas, no luck.")
            self.strlist.append("As empty as your hops and dreams.")
            self.strlist.append("Well, at least there was no trap inside...")
            self.strlist.append("You find... nothing.")
            self.strlist.append("Sorry, one cannot loot cobwebs.")
            self.strlist.append("These bugs are definitely no feature.")
            # self.strlist.append("")
            string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)


    def strMonster(self,type,monster,player):
        """
        Has most monster strings, that don't need damage values
        """
        name = str(Fore.GREEN+monster.getShortName()+ Fore.WHITE)
        item = str(Fore.YELLOW+monster.getLoot().name + Fore.WHITE)

        if type == "killedLoot":
            """
            Returns the string, when a monster with loot was killed
            """
            self.strlist.append("You killed "+ name  +" and it drops some Loot!")
            self.strlist.append(name+ ' is dead! Oh look something is on the ground.')
            self.strlist.append('The mighty oh glorious '+name+' left you something special after his death. Just take a moment and appreciate it.')
            self.strlist.append(name+" passed on! This monster is no more! It has ceased to be!\n"+\
            name+ "'s expired and gone to meet its maker! It's a stiff! Bereft of life, it rests in peace!\n"+\
            "If you hadn't nailed it to the perch it'd be pushing up the daisies! It's metabolic processes are now!\n"+\
            "It's off the twig! It's kicked the bucket, It's shuffled off its mortal coil, run down the curtain and joined the bleedin' choir invisible!!\n"+\
            "THIS IS AN EX-MONSTER!!")
            self.strlist.append("Oh Lord! You did it! The Monster is on his way to hell.")
            self.strlist.append("You've got my huge respect dude! You just beaten up MONSTER and it's dead. Congrats!")
            self.strlist.append("A farewell to one of the unique monsters. It died a very painful death by your hands.")
            self.strlist.append("You complete your mission."+name+" is dead finally! Congrats! Go get some cookies!")
            self.strlist.append("Hey man, this "+name+" was endangered! Might have been the last of its kind...")
            self.strlist.append("You killed "+ name+"!")
            self.strlist.append('You beat ' +name+ ' into oblivion.')
            self.strlist.append(name+ ' is dead!')
            string = random.choice(self.strlist)

        elif type == "killed":
            """
            Strings, when a monster without any items has been killed
            """
            self.strlist.append(name+" passed on! This monster is no more! It has ceased to be!\n"+\
            name+ "'s expired and gone to meet its maker! It's a stiff! Bereft of life, it rests in peace!\n"+\
            "If you hadn't nailed it to the perch it'd be pushing up the daisies! It's metabolic processes are now!\n"+\
            "It's off the twig! It's kicked the bucket, It's shuffled off its mortal coil, run down the curtain and joined the bleedin' choir invisible!!\n"+\
            "THIS IS AN EX-MONSTER!!")
            self.strlist.append("Oh Lord! You did it! The Monster is on his way to hell.")
            self.strlist.append("You've got my huge respect dude! You just beaten up MONSTER and it's dead. Congrats!")
            self.strlist.append("A farewell to one of the unique monsters. It died a very hurtfull death by your hands.")
            self.strlist.append("You complete your mission."+name+" is dead finally! Congrats! Go get some cookies!")
            self.strlist.append("Hey man, this "+name+" was endangered! Might have been the last of its kind...")
            self.strlist.append("You killed "+ name+"!")
            self.strlist.append('You beat ' +name+ ' into oblivion.')
            self.strlist.append(name+ ' is dead!')
            string = random.choice(self.strlist)

        elif type == "loot":
            """
            Some text explaining that the player found an item
            """
            self.strlist.append("Oh look, it's "+item+"!")
            self.strlist.append('Someone seems to favour you... A new '+item+'!')
            self.strlist.append('uuuuh, look what you found! You better keep that little precious '+item+", 'cause you will never know when you need it. *blink*")
            self.strlist.append("MY PRECIOUS! It's "+item)
            string = random.choice(self.strlist)

        elif type == "hit":
            """
            Response of the monster when it gets hit by a player attack
            """
            self.strlist.append('Ohhh myyyy')
            self.strlist.append('Well met, traveller!')
            self.strlist.append('Oh, who do we have here? Fancy a cuppa?')
            self.strlist.append('That tickled!!')
            self.strlist.append("Oh no you didn't. ")
            self.strlist.append('How dare you attacking me, you little punk! Come here and taste the blood.')
            self.strlist.append('HAHAHAHAHAH.. oops I mean.. URGH that hurts! ')
            self.strlist.append('Yessss I like it. Keep attacking me. *hrrrrrrrr*')
            self.strlist.append('Can you be more gentle please. I mean I have feelings too. I hate this monster stereotype. *hmpf*')
            string = random.choice(self.strlist)

        elif type == "flee":
            """
            If the player tries to flee
            """
            self.strlist.append(name+' laughs manically as you try to flee from it')
            self.strlist.append('"Your soul is mine!"')
            self.strlist.append("'Nope dude! You ain't going nowhere!'")
            self.strlist.append("'Where do you think you're going?!'")
            self.strlist.append('')
            string = random.choice(self.strlist)

        elif type == "fleeSuccess":
            """
            If the player flees without hurting himself
            """
            self.strlist.append('You barely manage, stumbling through the darkness ')
            self.strlist.append('Close call, mate. Try not to die, will you?')
            self.strlist.append('To be, or not to be?')
            self.strlist.append('Can you please watch out. You almost died.')
            string = random.choice(self.strlist)

        elif type == "fleeFail":
            """
            The player tries to flee but hurts himself
            """
            self.strlist.append('As you run through the darkness you fall and hit your head on something.')
            self.strlist.append('You are tumbling through the darkness, trusting your reflexes to keep yourself on track.\nBut, alas, you have been betraid! You stuble, and your head crashes into a rock.')

            self.strlist.append('Can you please watch out. You almost died.')
            string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)


    def strMonsterDamage(self,type,monster,damage,player):
        """
        The strings for Monster where some damage value is returned
        """
        name = str(Fore.GREEN+""+monster.getShortName()+""+ Fore.WHITE)
        namelong = str(Fore.GREEN+""+monster.getFullName()+""+ Fore.WHITE)
        damage =str(Fore.RED+" "+str(damage)+" "+Fore.WHITE)
        hp = str(Fore.GREEN +" "+ str(monster.getHP()) +" "+ Fore.WHITE)

        if type == "getAttacked":
            """
            The player hit the monster
            """
            self.strlist.append('Bam, right in the muzzle. That was' + damage + 'damage!')
            self.strlist.append('Boom. Right in his face! Keep going.' + damage + 'damage for the monster.')
            self.strlist.append('You attack ' +name+ ' and you deal' + damage + 'damage.')
            self.strlist.append(name+ " is down! You've just dealt" + damage + "damage! You have my respect! Keep going!")
            self.strlist.append("I think you just broke "+name+ "'s arm. That was"+ damage +"damage.")
            self.strlist.append("A brutal kick in the gut! "+name+" suffers"+ damage +"damage.")
            # self.strlist.append("")
            string = random.choice(self.strlist)


        elif type == "returnHP":
            """
            Some strings to let the player know the monster lost health
            """
            self.strlist.append("The monster's health is now at"+hp )
            self.strlist.append('If it bleeds, you can kill it!')
            string = random.choice(self.strlist)


        elif type == "spawn":
            """
            Notifies the player that a monster has spawned
            """
            self.strlist.append('A wild '+ namelong + ' appears! '+ name + ' attacks you.')
            self.strlist.append("What's this?! Oh no it's "+ namelong+ "!")
            self.strlist.append('Crap, not another one of those... \nThis one looks like '+ namelong+ "!")
            self.strlist.append("'Why hello there! I am " + namelong +"\nPleased to meet you. NOT!'")
            string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)

    def strRoom(self,type,room):
        """
        Displays some intro text when the player enters a new room
        """
        player = room.player
        if type == "intro":
            """
            Some fluff text as the player enters a new room
            """
            self.strlist.append("You blink once or twice as you enter the room, trying to adjust\nto the darkness surrounding you, failing miserably.\nA little light would be useful!")
            self.strlist.append("'Ahh this room looks just like my basement', you think while trying\nto ignore the foul smell of death.")
            self.strlist.append("You enter a very dark room and yet in the very far corner you see\na tiny little bit of light, that gives you hope.")
            self.strlist.append("You are going inside a room and it is so pitch black that you feel\nlike the darkness is going to swallow you up.\nYou hate the darkness, already.")
            self.strlist.append("A cold shiver ran down your spine as you enter a dark room.")
            self.strlist.append("You are entering a room full of the scent of fear, tears, torture and death.\nAnd you know right ahead, your journey will be a tough one.")
            string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)


    def strPlayerDamage(self,type,player,monster,damage):
        """
        Handles the player strings that include damage values
        """
        damage =str(Fore.RED+" "+str(damage)+" "+Fore.WHITE)
        hp = str(Fore.CYAN +" "+ str(player.getHP()) +" "+ Fore.WHITE)
        playerName = str(Fore.CYAN +" "+player.name +" "+Fore.WHITE)
        monster = str(Fore.GREEN +monster.getShortName()+Fore.WHITE)

        if type == "takeDamage":
            """
            The player took some damage from a monster
            """
            self.strlist.append(monster+' hits you hard. You take'+damage+'damage!')
            self.strlist.append(monster+" just whipped your ASS. "+damage+"damage for you.")
            self.strlist.append("You got hit by "+monster+ " very badly. You take"+damage+"damage.")
            self.strlist.append(monster+" is out of control. It is attacking you non stop and you can't protect yourself. You suffer" +damage+ "damage.")
            self.strlist.append("A brutal attack from "+monster+". You suffer"+damage+"damage.")
            self.strlist.append("What a hit!"+damage+"damage!")
            self.strlist.append(damage+"damage! BRUTAL!")
            self.strlist.append("Ouch! That must have hurt... "+damage+"damage right to the face.")

            string = random.choice(self.strlist)

        if type == "hp":
            """
            Informs the player about his health situation
            """
            self.strlist.append('Do you WANT to die?')
            self.strlist.append('Only'+ hp+ 'drops of blood left,'+playerName+'!')
            self.strlist.append("'Tis but a scratch!")
            self.strlist.append("It's only a fleshwound!"+hp+"life left.")
            self.strlist.append('Life is slowly slipping away... ')
            self.strlist.append('Tick, tock, tick, tock.'+hp+'hitpoints left.')
            string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)

    def strPlayer(self,type,player):
        """
        Handles the player strings without damage values
        """
        hp = str(Fore.CYAN +" "+ str(player.getHP()) +" "+ Fore.WHITE)
        playerName = str(Fore.CYAN +" "+player.name +""+Fore.WHITE)

        if type == "lvl":
            """
            Informs the player that he gained a level
            """
            self.strlist.append('\nCongratulations'+playerName+', you leveled up!\n')
            self.strlist.append('\nDing.\n')
            self.strlist.append('\nDong.\n')
            self.strlist.append('\nNext Level! Here you go!\n')
            string = random.choice(self.strlist)
        if type == "heal":
            """
            Informs the player that he healed
            """
            self.strlist.append('You healed some.')
            self.strlist.append('You feel refreshed.')
            self.strlist.append('You think to hear a short curse after you heal, thus stepping away from the brink of death once more.')
            string = random.choice(self.strlist)

        if type == "heal":
            """
            Informs the player that he is at full health
            """
            self.strlist.append('You are now at full health')
            self.strlist.append('All patched up and ready to go')
            self.strlist.append('Health maximized')
            self.strlist.append('Health levels over 9000')
            string = random.choice(self.strlist)

        if type =="emptyPot":
            """
            Informs the player that his potion is empty
            """
            self.strlist.append("It's empty.")
            self.strlist.append('Nope.')
            self.strlist.append('A healthy sip of old, stinky air.')
            string = random.choice(self.strlist)

        if type =="drinkAir":
            """
            If the player tries to drink an empty potion
            """
            self.strlist.append("You can't drink air...")
            self.strlist.append("Some say you can live of love and air... you won't.")
            self.strlist.append("Just fyi: You can't drink air ;)")
            # self.strlist.append('')
            string = random.choice(self.strlist)


        if type == "dies":
            self.strlist.append("FORGET The air escapes your lungs and a metallic taste fills your mouth.\n"+\
            "One last thought rushes into your mind, screaming and trying to escape your mouth: ")
            self.strlist.append("I hope you are listed as organ donor.")
            self.strlist.append("SHAKESPEAR To be, or not to be, that is the question:\n"+
            "Whether 'tis Nobler in the mind to suffer. The Slings and Arrows of outrageous Fortune,\n"
            "Or to take Arms against a Sea of troubles, And by opposing end them: ")
            self.strlist.append("FIREFLY Like a leaf on the wind you feel, trying to dodge the monster's attack.\n"+\
            "This time, though, your reflexes were not quick enough.\n"+\
            "With shock in your eyes you look down, where a long spike penetrates your body, pinning you to the wall behind you.\n"+\
            "You think of your loved ones, who you will never see again. Ah, death, I thought we had a deal...\n")
            self.strlist.append("Always look on the bright side of death, a-just before you draw your terminal breath.")
            string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)


    def strPlayerItem(self,type,player,item):
        """
        Strings for the player that involve items
        """
        print item
        item = str(Fore.YELLOW + item.name + Fore.WHITE)
        itemshort = str(Fore.YELLOW + item.nameshort + Fore.WHITE)
        if type =="drinkItem":
            """
            If the player tries to drink items
            """
            self.strlist.append("You can't drink "+item)
            self.strlist.append("This is not a potion, fool!")
            self.strlist.append("Why on earth did you think you can drink "+item+"?! Are you drunk?")
            self.strlist.append("I would not drink that if I were you...")
            self.strlist.append("Sure! I mean you can try drinking "+item+". But you have to know, that's impossible!")
            # self.strlist.append('')
            string = random.choice(self.strlist)

        if type =="newItem":
            """
            Informs the player about a new item he found
            """
            self.strlist.append("You now have "+item+" in your hand.")
            self.strlist.append("Oh, ah shiny new "+itemshort+".")
            self.strlist.append("Wow the new "+itemshort+" feels nice.")
            # self.strlist.append("")
            # self.strlist.append("")
            string = random.choice(self.strlist)

        del self.strlist[:]
        return self.modify(string,player)

    def strBasic(self,type):
        if type == "restart":
            string = str(Back.GREEN+"                  "+Fore.WHITE+"Game restarted"+ Back.GREEN+"                  "+Style.RESET_ALL)

        elif type == "exit":
            string = str(Back.RED+"                  "+Fore.WHITE+"Game exited"+ Back.RED +"                  "+Style.RESET_ALL)
        return string

    def modify(self,string,player):
        """
        Modifies the strings before returning, depending on his condition
        """
        if player is not None:
            if player.condition == "normal":
                return string
                #return self.killString(string)
            elif player.condition == "poisoned":
                print "poisoned"
                return self.killString(string)
        else:
            return string
            # print "else"
            # return self.killString(string)

    def killString(self,string):
        """
        Modifier: Swaps letters -> String = gtrinS
        """
        newString = ""
    	builder = ""
    	for i in range(len(string)):
    		letter = string[i]
    		if((letter == " ") or (letter == ".") or (letter == ",")):
    			newString += builder[-1] + builder[1: -1] + builder[0] + " "
    			builder = ""
    		else:
    			builder += letter
    	return newString
