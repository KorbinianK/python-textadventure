from colorama import init, Fore, Back, Style
import random,sys,re


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
        """
        Megabyte Boss
        """
        damage = Fore.RED + str(damage)+Fore.WHITE
        if type == "bHit":
            self.strlist.append("01101111 01110101 0110"+damage+Fore.GREEN+" 01110100 01100011 01101000")
            self.strlist.append("01100100 01101111 01101110 01110100 00100111 00100000 01101000 01110101 01110010 01110100 00100000 01101101 01100101")
            self.strlist.append("print: response(playerHit)")
            # self.strlist.append("")
            string = Fore.GREEN + random.choice(self.strlist) + Fore.WHITE

        if type == "bAttack":

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
            self.strlist.append("Oh shit... it's "+Fore.GREEN+"a MEGABYTE!!!!"+ Fore.WHITE)
            self.strlist.append("This almost sounds like R2D2... but no wait... this is..."+Fore.GREEN+"A MEGABYTE!"+ Fore.WHITE)
            # self.strlist.append("")
            # self.strlist.append("")
            string = random.choice(self.strlist)
        """
        Hipster Boss
        """
        if type == "hSpawn":
            self.strlist.append("You are not sure, but you think you heard someone mumbeling "+Fore.GREEN+ "'Yolo'"+Fore.WHITE+" in a shrill and strange voice")
            self.strlist.append("In front of you you see a man or more like a boy.\nThe lack of light you again has you unsure what exactly you are facing...\nCould it be? "+Fore.GREEN+"A Hipster"+Fore.WHITE+"?! No please, not "+Fore.GREEN+"the Hipster"+Fore.WHITE+".")
            self.strlist.append("As soon as you enter the next room you hear some strange voice:\n"+\
             Fore.GREEN+ "'Oh boy is this a classy vintage room'"+Fore.WHITE+" and"+Fore.GREEN+ " 'yolo who cares about light, don't let the negative vibes catch you'\n"+Fore.WHITE+\
             "Scared shitless you realize: it's the cursed lair of "+Fore.GREEN+"the Hipster"+Fore.WHITE+"!")
            self.strlist.append("You enter a room, in front of you a person, you would describe to others as weirdly dressed man.\n"+\
            "His face framed by an excellent long beard. He wears skinny jeans much closer to leggings than they should be... "+Fore.GREEN+"a Hipster"+Fore.WHITE+".")
            string = random.choice(self.strlist)
        if type == "hHit":
            damage = str(Fore.RED + str(damage) + Fore.WHITE)
            self.strlist.append("He softly and sensitives looks through his nerdy glasses. While catching his ultra positive vibes you take "+damage+" damage")
            self.strlist.append("Oh holy crap you looked him in the eye! He begins to tell you about an alternative life style and you take "+damage+" damage by only listening.")
            self.strlist.append("Not understanding how one can run so fast in such skinny jeans, he jumps forward to hand you a flyer- you take "+damage+" damage")
            self.strlist.append("Oh no, he throws his hessian bag towards you! You get XX damage!")
            self.strlist.append("Hearing a loud 'YOLO' the hipster jumps towards you, beating you with his skinny arms. You take "+damage+" damage.")
            string = random.choice(self.strlist)
        if type == "hDie":
            self.strlist.append("You got away from the hipster! Finally, you see ....a unicorn coming towards you?!. You jump on it and ride towards the rainbow on the horizon.")
            self.strlist.append("Surprisingly, well not really all that surprising, you win! The hipster allows you to shave his beard!\nYou rescued the princess... ehm..."+Fore.GREEN+" the Hipster"+Fore.WHITE+" and you won the game!")
            self.strlist.append("As the room starts to crumble a unicorn suddenly appears and runs across the room, you just manage to jump on it!\nTogether you are riding towards the glittery sunrise while the room around you collapses and buries "+Fore.GREEN+ "the Hipster"+Fore.WHITE+" for good.")
            self.strlist.append("You catch the moment while"+Fore.GREEN+" the Hipster "+Fore.WHITE+"is playing gameboy and ran out of the room into the freedom! Congratulation you won.")
            self.strlist.append(Fore.GREEN+"'Screw you! I played text adventures before it was cool!'"+Fore.WHITE+"\nhe shouted before exploding into a million, definitely cool, pieces.")
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
        self.strlist.append('Who are we looking at here?')
        self.strlist.append('Hail traveller! Would you mind introducing yourself?')
        string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)

    def strGreeting(self,player):
        """
        Greets the new player
        """
        playername = str(Fore.CYAN+player.name+ Fore.WHITE)
        self.strlist.append('Hello '+playername+'!\nWelcome to a world of pain and suffering! Or was it miracles and wonders??')
        self.strlist.append('MWAHAHAHAHAHAHA!\nNow you are trapped here, ' +playername+'!')
        self.strlist.append('Welcome to the DARKSIDE '+playername+'!\nHere take some cookies! *evillaugh*')
        self.strlist.append('Welcome to our little dungeon, '+playername+'!\nWe hope you enjoy your stay and survive so you can recommend us to your friends.')
        self.strlist.append('Welcome '+playername+'!\nAs they say: my house is your house! Or in this case, my cave is your cave. But beware of the shadows!')
        self.strlist.append("H-hello "+playername+"?!\nCan you hear me?? ... \nWell let's start then")
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
            self.strlist.append("At the first glimpse, the room seems empty. Wanna risk another?")
            self.strlist.append("Nothing to see here! Keep moving!")
            string = random.choice(self.strlist)

        if type == "moving":

            self.strlist.append("Moving towards the door")
            self.strlist.append("You are toddling slowly to the door")
            self.strlist.append("You decide to try your luck in another room")
            self.strlist.append("Eagerly you leave the room to find out, what this place still has to offer")
            string = random.choice(self.strlist)

        if type == "nextRoomMonster":

            self.strlist.append("You almost stumble over the carcass of "+monstershort+" as you walk through the door into the next room.")
            self.strlist.append("Finally, you overturned the foe. Weakend, but still breathing, you continue your journey.")
            self.strlist.append(monstershort+" is no more. Pumped with adrenaline, you head for the next room.")
            self.strlist.append("Legends and tales might be told about this moment. But this is not the time. More trials await!")
            string = random.choice(self.strlist)

        if type == "moveChest":

                self.strlist.append("Carefully you walk through the darkness. Then you hit your knee on something...\nMaybe you should "+look+" first?")
                self.strlist.append("You toddle very carefully through the darkness without a special direction.\nYou should "+look+" before continuing with your mission.")
                self.strlist.append("You notice a box-like shadow in the far corner of the room. Try to"+look+" and find out , what it is.")
                self.strlist.append("No monster this time. But you can't shake the feeling, that there is more to this room than it seems. Perhaps you could "+look+" and find out?")
                string = random.choice(self.strlist)

        if type == "nextRoom":

                self.strlist.append("You walk through the door into the next room")
                self.strlist.append("You just passed the door of darkness. You are in a new room now.")
                self.strlist.append("You enter the next room.")
                self.strlist.append("Creaking, the next door opens, granting you access to the next room.")
                string = random.choice(self.strlist)

        if type == "attackNoMonster":

                self.strlist.append("You shake your fists and try to attack your shadows")
                self.strlist.append("Save your breath! There is nothing in here!")
                self.strlist.append("You sure are funny to watch! What do you think you're doing??")
                self.strlist.append("You charge into the room and hit a rock.")
                string = random.choice(self.strlist)

        if type == "fleeNoMonster":

                self.strlist.append("'Coward! You stay exactly where you are!', shouts a voice and you tremble at its power over you.")
                self.strlist.append("'Leaving so soon?' a voice asked smugly, rooting you in place.")
                self.strlist.append("Who are you hiding from you coward?")
                self.strlist.append("Why leave?? You haven't met my special friends yet!")
                string = random.choice(self.strlist)

        if type == "fleeing":

                self.strlist.append("Trying to flee")
                self.strlist.append("Fly, you fool!")
                self.strlist.append("Run,for heaven's sake!!!")
                self.strlist.append("'Hell No!', you think, running for the exit")
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
                self.strlist.append("Nothing but spiderwebs and dust left in this chest!")
                self.strlist.append("You snooze, you loose! Someone has opened this chest already. Or was it you?")
                string = random.choice(self.strlist)

        if type == "lookNothing":

                self.strlist.append("You looked around. Good job")
                self.strlist.append("Look who's all nosy.")
                self.strlist.append("Someone wants to be an investigator, huh?")
                self.strlist.append("We'll done Sherlock Holmes!")
                string = random.choice(self.strlist)

        if type == "looking":

                self.strlist.append("Looking around")
                self.strlist.append("Inspecting the room")
                self.strlist.append("Paranoid as you are, you scan the room thoroughly.")
                self.strlist.append("Carefully you stride through the shadows, looking for something useful")
                string = random.choice(self.strlist)

        if type == "chestOpens":

                self.strlist.append("The chest opens with a loud squeaky noise.")
                self.strlist.append("A strong scent of blood is escaping the chest as you open it.")
                self.strlist.append("You just opened the chest.")
                self.strlist.append('What do we have here?')
                string = random.choice(self.strlist)

        if type == "chestOpenAgain":

                self.strlist.append("You found a flaw in this game, you are looting the chest again...NOT\nDid you really think you could cheat the system?! Think again...")
                self.strlist.append("Alzheimer is strong with this one, you just looted this chest.")
                self.strlist.append("Sure, always double check.")
                self.strlist.append("Didn't you like what you got the first time? No refunds here!")
                self.strlist.append("Nothing but lost hopes and dreams left in this chest!")
                string = random.choice(self.strlist)

        if type == "openChestNoLook":

                self.strlist.append("You seem to imagine things in the darkness. Maybe "+look+" first?")
                self.strlist.append("Even with your powerful imagination, you cannot make things appear in front of you.\nMaybe "+look+" first?")
                self.strlist.append("So, where is this chest you'd like to open? Carry one in your backpack, do you?")
                self.strlist.append("How about finding an actual chest for starters?? "+look+" and then try again")
                string = random.choice(self.strlist)

        if type == "tryOpenChest":

                self.strlist.append("You try to open the chest.")
                self.strlist.append("You want to open the chest, but it's harder than expected.")
                self.strlist.append("This chest is sealed. It takes your time opening it.")
                self.strlist.append("Hastily you try to rip the chest open.")
                self.strlist.append("Easy, easy ... you will break the lock!")
                string = random.choice(self.strlist)

        if type == "searchingInventory":

                self.strlist.append("You are searching your pockets")
                self.strlist.append("Checking your pockets")
                self.strlist.append("You are looking for something in your pockets")
                self.strlist.append('"I am sure I had something useful in there somewhere"')
                string = random.choice(self.strlist)



        del self.strlist[:]
        return self.modify(string,player)


    def strChest (self,type,item):
        player = None
        if type == "open":

            item = Fore.YELLOW + item +Fore.WHITE
            itemshort = Fore.YELLOW +item.replace("a ","",1) +Fore.WHITE

            self.strlist.append("You found "+item+"! It has been added to your inventory")
            self.strlist.append("Oooh. Shiny! You got "+item+"!" )
            self.strlist.append("*plop* Wow a new "+itemshort+"!")
            self.strlist.append("Hey, I wonder if this "+itemshort+" is part of a set...")
            self.strlist.append("This is now MINE! My "+itemshort+"! My PRECIOUS!")
            self.strlist.append("Oh yes, a "+item+"! Exactly what I needed!")
            self.strlist.append("Winner winner, chicken dinner! It's a "+item)
            string = random.choice(self.strlist)

        if type == "empty":

            self.strlist.append("It's empty.")
            self.strlist.append("Of course, there is nothing inside...")
            self.strlist.append("Alas, no luck.")
            self.strlist.append("As empty as your hops and dreams.")
            self.strlist.append("Well, at least there was no trap inside...")
            self.strlist.append("You find... nothing.")
            self.strlist.append("Sorry, only cobwebs, nothing of use.")
            self.strlist.append("These bugs are definitely no feature.")
            self.strlist.append("Only used scrolls an empty flasks...")
            self.strlist.append("Nothing ... really??")
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
            self.strlist.append("You've got my huge respect dude! You just beaten up "+name+" and it's dead. Congrats!")
            self.strlist.append("A farewell to one of the unique monsters. It died a very painful death by your hands.")
            self.strlist.append("You complete your mission."+name+" is dead finally! Congrats! Go get some cookies!")
            self.strlist.append("Hey man, this "+name+" was endangered! Might have been the last of its kind...")
            self.strlist.append("You killed "+ name+"!")
            self.strlist.append('You beat ' +name+ ' into oblivion.')
            self.strlist.append('The great ' +name+ ' is no more. Songs of this epic moment will be sung through all eternity ... \nbut not for you. Not now! There is still work to do!')
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
            self.strlist.append("You've got my huge respect dude! You just beaten up "+name+" and it's dead. Congrats!")
            self.strlist.append("A farewell to one of the unique monsters. It died a very painful death by your hands.")
            self.strlist.append("You complete your mission."+name+" is dead finally! Congrats! Go get some cookies!")
            self.strlist.append("Hey man, this "+name+" was endangered! Might have been the last of its kind...")
            self.strlist.append("You killed "+name+"!")
            self.strlist.append('You beat '+name+' into oblivion.')
            self.strlist.append('The great '+name+' is no more. Songs of this epic moment will be sung through all eternity ... \nbut not for you. Not now! There is still work to do!')
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
            self.strlist.append("Celebrating your victory, you almost forgot to take "+item+" with you.")
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
            self.strlist.append('Tell me '+playername+'. Do you fear death?')
            self.strlist.append('Why leave so soon?')
            self.strlist.append('How rude! Right as I started to like you!')
            self.strlist.append("The party ain't over yet!")
            string = random.choice(self.strlist)

        elif type == "fleeSuccess":
            """
            If the player flees without hurting himself
            """
            self.strlist.append('You barely manage, stumbling through the darkness ')
            self.strlist.append('Close call, mate. Try not to die, will you?')
            self.strlist.append('To be, or not to be?')
            self.strlist.append('Can you please watch out. You almost died.')
            self.strlist.append('Running for your life, you manage to reach a temporary safe spot.')
            self.strlist.append("With a desperate move, you head for the exit. Barely alive and all out of breath, you're safe at last ... for the moment")
            string = random.choice(self.strlist)

        elif type == "fleeFail":
            """
            The player tries to flee but hurts himself
            """
            self.strlist.append('As you run through the darkness you fall and hit your head on something.')
            self.strlist.append('You are tumbling through the darkness, trusting your reflexes to keep yourself on track.\nBut, alas, you have been betraid! You stuble, and your head crashes into a rock.')
            self.strlist.append('Can you please watch out. You almost died.')
            self.strlist.append('Hastily trying to flee you stumble over your own feet.')
            self.strlist.append('You try to run for good, but the angry stomps of '+name+' throws you off your feet and on your back.')
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
            self.strlist.append(name+ " is almost down! You've just dealt" + damage + "damage! You have my respect! Keep going!")
            self.strlist.append("I think you just broke "+name+ "'s arm. That was"+ damage +"damage.")
            self.strlist.append("A brutal kick in the gut! "+name+" suffers"+ damage +"damage.")
            self.strlist.append("You hit "+name+" right between the eyes and deal "+damage+" damage. Blinded by your hit, "+name+" gets furious and blindly swings at you.")
            self.strlist.append("A solid hit for "+damage+" damage. Well done champ!")
            string = random.choice(self.strlist)


        elif type == "returnHP":
            """
            Some strings to let the player know the monster lost health
            """
            self.strlist.append("The monster's health is now at"+hp )
            self.strlist.append('If it bleeds, you can kill it! '+hp+' life left!')
            self.strlist.append(name+" already took a good beating. Only "+hp+" life left. Keep going!")
            self.strlist.append('The defenses are weakened. Health now at '+hp+'.')
            self.strlist.append("The monster's healthpoints are at "+hp+"! Don't stop now!")
            string = random.choice(self.strlist)


        elif type == "spawn":
            """
            Notifies the player that a monster has spawned
            """
            self.strlist.append('A wild '+ namelong + ' appears! '+ name + ' attacks you.')
            self.strlist.append("What's this?! Oh no it's "+ namelong+ "!")
            self.strlist.append('Crap, not another one of those... \nThis one looks like '+ namelong+ "!")
            self.strlist.append("'Why hello there! I am " + namelong +"\nPleased to meet you. NOT!'")
            self.strlist.append("I'll be damned, the legends are true! It's "+namelong+"!")
            self.strlist.append("From the shadows, a mysterious figure emerges. As you draw closer, you recognize this figure as "+namelong+"!")
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
            self.strlist.append("As you enter a cold and unwelcoming room, you try to remember, \nwhy on earth you HAD to leave your couch tonight.")
            self.strlist.append("Wandering step by step into the mysterious darkness, \nstill wondering, how you even got here.")
            string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)


    def strPlayerDamage(self,type,player,monster,damage):
        """
        Handles the player strings that include damage values
        """
        damage =str(Fore.RED+""+str(damage)+" "+Fore.WHITE)
        hp = str(Fore.CYAN +" "+ str(player.getHP()) +" "+ Fore.WHITE)
        playerName = str(Fore.CYAN +" "+player.name +" "+Fore.WHITE)
        monster = str(Fore.GREEN +monster.getShortName()+Fore.WHITE)

        # print player.name
        # print player.getCondition()

        if type == "takeDamage":
            """
            The player took some damage from a monster
            """
            self.strlist.append(monster+' hits you hard. You take '+damage+'damage!')
            self.strlist.append(monster+" just whipped your ASS. "+damage+"damage for you.")
            self.strlist.append("You've got hit by "+monster+ " very badly. You take "+damage+"damage.")
            self.strlist.append(monster+" is out of control. It is attacking you non stop and you can't protect yourself. You suffer "+damage+"damage.")
            self.strlist.append("A brutal attack from "+monster+". You suffer "+damage+"damage.")
            self.strlist.append("The monster throws everything at you it has. What a hit ! "+damage+"damage!")
            self.strlist.append("It strikes back! "+damage+"damage! BRUTAL!")
            self.strlist.append("You try to dodge "+monster+"'s attack and fail. Ouch! That must have hurt... "+damage+"damage right to the face.")
            self.strlist.append("A strong hit from "+monster+" throws you hard on your back. You suffer "+damage+" damage!")
            self.strlist.append("FATALITY!!! "+damage+" damage!")
            self.strlist.append(monster+" gets at you for "+damage+" damage! You almost passed out!")
            self.strlist.append("Relentlessly, the monster unleashes blow after blow. In your despair, you seek for shelter or retreat, no chance! "+damage+"  damage dealt!")
            self.strlist.append("You took an arrow to the knee! "+damage+" damage!")
            string = random.choice(self.strlist)

        if type == "hp":
            """
            Informs the player about his health situation
            """
            self.strlist.append('Do you WANT to die? '+hp+' life left!')
            self.strlist.append('Only'+hp+'drops of blood left,'+playerName+'!')
            self.strlist.append("Tis but a scratch! "+hp+" life left!")
            self.strlist.append("It's only a fleshwound! "+hp+" life left.")
            self.strlist.append('Life is slowly slipping away... '+hp+' lifepoints left!')
            self.strlist.append('Tick, tock, tick, tock. '+hp+' hitpoints left.')
            string = random.choice(self.strlist)
        del self.strlist[:]
        return self.modify(string,player)

    def strPlayer(self,type,player):
        """
        Handles the player strings without damage values
        """
        hp = str(Fore.CYAN +" "+ str(player.getHP()) +" "+ Fore.WHITE)
        playerName = str(Fore.CYAN +" "+player.name +""+Fore.WHITE)

        if type == "condition":
            condition = Fore.MAGENTA+player.getCondition()+Fore.WHITE
            if player.getCondition() == "poisoned":
                self.strlist.append('\nYou feel a strange sting in your arm... you got '+condition+'.\n')
                self.strlist.append('\nYour head starts spinning and you want to throw up. You got '+condition+'.\n')
                self.strlist.append('\nThis new wound is leaking some blue liquid... It is '+Fore.MAGENTA+'Poison!'+Fore.WHITE+'\n')
                self.strlist.append('\nYou are '+condition+'.\n')
                return random.choice(self.strlist)
            elif player.previous == "poisoned":
                player.previous = "normal"
                self.strlist.append("This attack knocked you right back into reality.")
                self.strlist.append("The "+Fore.MAGENTA+"Poison"+Fore.WHITE+" seems to have faded.")
                # self.strlist.append("")
                # self.strlist.append("")
                return random.choice(self.strlist)
            else:
                return ""

        if type == "lvl":
            """
            Informs the player that he gained a level
            """
            self.strlist.append('\nCongratulations'+playerName+', you leveled up!\n')
            self.strlist.append('\n*ding* Level up!\n')
            self.strlist.append('\n*dong* Next level!\n')
            self.strlist.append('\nNext Level! Here you go!\n')
            self.strlist.append('\nKA-CHING! Next up!\n')
            self.strlist.append('\nFrom deep within your soul, you can feel it. Something has changed. You feel... harder...better...faster...stronger??\n')
            self.strlist.append('\nLevel up... but where are those damn cookies??\n')
            self.strlist.append('\nWelcome to the next level of greatness, hero!\n')
            string = random.choice(self.strlist)
        if type == "heal":
            """
            Informs the player that he healed
            """
            self.strlist.append('You healed some. Health now at '+hp)
            self.strlist.append('You feel refreshed. Health now at '+hp)
            self.strlist.append('Regaining strength. Health now at '+hp)
            self.strlist.append('That should help! Health now at '+hp)
            self.strlist.append('You think to hear a short curse after you heal, thus stepping away from the brink of death once more. Health now at '+hp)
            self.strlist.append('Comforting, the mysterious liquid trickles down your throat. You already feel renewed! Health now at '+hp)
            string = random.choice(self.strlist)

        if type == "healFull":
            """
            Informs the player that he is at full health
            """
            self.strlist.append('You are now at full health')
            self.strlist.append('All patched up and ready to go')
            self.strlist.append('Health maximized')
            self.strlist.append('Health levels over 9000')
            self.strlist.append("Alive and kickin'!")
            self.strlist.append("Dont't worry, you're fine!")
            string = random.choice(self.strlist)

        if type =="emptyPot":
            """
            Informs the player that his potion is empty
            """
            self.strlist.append("It's empty.")
            self.strlist.append('Nope.')
            self.strlist.append('A healthy sip of old, stinky air.')
            self.strlist.append('Awkwardly, you sip at the empty bootle. Better look first!')
            self.strlist.append('There is nothing in there...')
            self.strlist.append('All gone!')
            self.strlist.append('Someone drank it all up. Might have been you.')
            string = random.choice(self.strlist)

        if type =="drinkAir":
            """
            If the player tries to drink an empty potion
            """
            self.strlist.append("You can't drink air...")
            self.strlist.append("Some say you can live of love and air... you won't.")
            self.strlist.append("Just fyi: You can't drink air ;)")
            self.strlist.append('What an earth are you doing??')
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
        itemname =  Fore.YELLOW +item.name + Fore.WHITE
        itemshort = Fore.YELLOW+ item.nameshort + Fore.WHITE

        if type =="drinkItem":
            """
            If the player tries to drink items
            """
            self.strlist.append("You can't drink "+itemname)
            self.strlist.append("This is not a potion, fool!")
            self.strlist.append("Why on earth did you think you can drink "+itemname+"?! Are you drunk?")
            self.strlist.append("I would not drink that if I were you...")
            self.strlist.append("Sure! I mean you can try drinking "+itemname+". But you have to know, that's impossible!")
            string = random.choice(self.strlist)

        if type =="newItem":
            """
            Informs the player about a new item he found
            """
            self.strlist.append("You now have "+itemname+" in your hand.")
            self.strlist.append("Oh, ah shiny new "+itemshort+".")
            self.strlist.append("Wow the new "+itemshort+" feels nice.")
            self.strlist.append("What a nice "+itemshort+ "! Feels heavy.")
            self.strlist.append("You grasp the "+itemshort+" and swing it through the air for a testdrive! Nice!")
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
            # print player.getCondition()
            if player.getCondition() == "normal":
                return string
                #return self.killString(string)
            elif player.getCondition() == "poisoned":
                # print "poisoned"
                # return self.killString(string)
                return self.reverseString(string)
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

    def reverseString(self,string):
        """
        Modifier: Returns the entire string -> gnirts eritne eht snruteR
        """
        newString = re.sub(r'(\x1b[^m]*m)',"",string)[::-1]
        return newString
