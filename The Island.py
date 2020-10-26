'''Connecting to db'''
#opening database connection
import mysql.connector
import time
import random
db = mysql.connector.connect(host="localhost",
                             user="dbuser06",
                             passwd="islandpass",
                             db="island",
                             buffered=True)

'''-------------------------------
ENGINE & movement
----------------------------------'''
def myprint(jono):
    rivin_pituus = 80
    lista = jono.split()
    käytetty = 0
    for sana in lista:
        if käytetty + len(sana) <= rivin_pituus:
            if käytetty>0:
                print(" ",end='')
                käytetty = käytetty + 1
            print (sana, end='')
        else:
            print ("")
            käytetty = 0
            print(sana, end='')
        käytetty = käytetty + len(sana)
    print ("")


#timesleep 0.3
def sleep03():
    time.sleep(0.3)
    return

#timesleep 0.1
def sleep01():
    time.sleep(0.1)
    return

#intro
def introfunc():
    print("-------------------------------------------------------------------")
    sleep03()
    print(" #######                  ###                                    ")
    sleep03()
    print("    #    #    # ######     #   ####  #        ##   #    # #####  ")
    sleep03()
    print("    #    #    # #          #  #      #       #  #  ##   # #    # ")
    sleep03()
    print("    #    ###### #####      #   ####  #      #    # # #  # #    # ")
    sleep03()
    print("    #    #    # #          #       # #      ###### #  # # #    # ")
    sleep03()
    print("    #    #    # #          #  #    # #      #    # #   ## #    # ")
    sleep03()
    print("    #    #    # ######    ###  ####  ###### #    # #    # #####  ")
    sleep03()
    print("-------------------------------------------------------------------")
    sleep03()
    myprint("Game designed by: Juho Huhtanen, Nina Räsänen and Tommi Volotinen at Metropolia, University of Applied Sciences.")
    time.sleep(5)
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()
    sleep01()
    print()

#victory
def victory():
    print("-------------------------------------------------------------------")
    sleep03()
    print("          _______             _______  _______  _______  _______  _______  _______  ______  ")
    sleep03()
    print("|\     /|(  ___  )|\     /|  (  ____ \(  ____ \(  ____ \(  ___  )(  ____ )(  ____ \(  __  \ ")
    sleep03()
    print("( \   / )| (   ) || )   ( |  | (    \/| (    \/| (    \/| (   ) || (    )|| (    \/| (  \  )")
    sleep03()
    print(" \ (_) / | |   | || |   | |  | (__    | (_____ | |      | (___) || (____)|| (__    | |   ) |")
    sleep03()
    print("  \   /  | |   | || |   | |  |  __)   (_____  )| |      |  ___  ||  _____)|  __)   | |   | |")
    sleep03()
    print("   ) (   | |   | || |   | |  | (            ) || |      | (   ) || (      | (      | |   ) |")
    sleep03()
    print("   | |   | (___) || (___) |  | (____/\/\____) || (____/\| )   ( || )      | (____/\| (__/  )")
    sleep03()
    print("   \_/   (_______)(_______)  (_______/\_______)(_______/|/     \||/       (_______/(______/ ")
    sleep03()
    print("-------------------------------------------------------------------")
    sleep03()
    myprint("Game designed by: Juho Huhtanen, Nina Räsänen and Tommi Volotinen at Metropolia, University of Applied Sciences.")
    input( "Press <Enter> to quit the game." )

#current place
def current():
    cur = db.cursor()
    cur.execute("SELECT location.Tekstit FROM location, player WHERE location.ID=player.location_ID")
    place = ([row[0] for row in cur.fetchall()])
    placestr = (str(place[0]))
    myprint(placestr)

#movement
def movement():
    cur = db.cursor()
    if userinput.lower() in ("north", "n", "go north", "go n"):
        value = cur.execute("SELECT siirtymä.To_ID FROM siirtymä INNER JOIN player ON siirtymä.From_ID = player.location_ID AND siirtymä.Direction = 'north';")
    elif userinput.lower() in ("south", "s", "go south", "go s"):
        value = cur.execute("SELECT siirtymä.To_ID FROM siirtymä INNER JOIN player ON siirtymä.From_ID = player.location_ID AND siirtymä.Direction = 'south';")
    elif userinput.lower() in ("west", "w", "go west", "go w"):
        value = cur.execute("SELECT siirtymä.To_ID FROM siirtymä INNER JOIN player ON siirtymä.From_ID = player.location_ID AND siirtymä.Direction = 'west';")
    elif userinput.lower() in ("east", "e", "go east", "go e"):
        value = cur.execute("SELECT siirtymä.To_ID FROM siirtymä INNER JOIN player ON siirtymä.From_ID = player.location_ID AND siirtymä.Direction = 'east';")
    value = [row[0] for row in cur.fetchall()]
    if value:
        valuestr = (str(value[0]))
        cur.execute("SELECT Available FROM siirtymä WHERE To_ID='" + valuestr + "'")
        doorkey = [row[0] for row in cur.fetchall()]
        doorkeystr = (str(doorkey[0]))
        #print("doorketstr " + doorkeystr)
        #print("playerlocstr " + playerlocstr)
        if doorkeystr == '0':
            if playerlocstr == '6':
                print()
                myprint("The bar door won't budge, but it seems to be fairly loose. Maybe I could pry it open with some tools...")
                return
            elif playerlocstr == '5':
                print()
                myprint("The town hall's door looks sturdy. I'm going to need a key to open this one.")
                return
            elif playerlocstr == '4':
                print()
                myprint("The house looks really old and abandoned.. I wonder if there's a key around in this isle.")
                return
            elif playerlocstr == '12':
                if userinput.lower() in ("north", "n", "go north", "go n"):
                    print()
                    myprint("The church door is locked for good. There's got to be a key around...")
                    return
                else:
                    print()
                    haunted = cur.execute("SELECT Extratekstit FROM location WHERE ID = 11")
                    haunted = ([row[0] for row in cur.fetchall()])
                    hauntedstr = (str(haunted[0]))
                    print(hauntedstr)
                    return
        elif doorkeystr == '1':
            sql = "UPDATE player SET location_ID='" + valuestr + "'"
            cur.execute(sql)
            print("\n" * 20)
            current()
            return
    else:
        print("I can't go that way!")
        return


'''----------------------------
ENGINE OVER. CONTENT AND COMMANDS BELOW
-------------------------------'''

#take
def take():
    cur = db.cursor()
    if userinput.lower() in ("pickup note", "pick-up note", "get note", "loot note", "take note", "take letter", "pickup letter", "take letter", "pick-up letter", "get letter", "loot letter"):
        value = cur.execute("SELECT `Player_ID` FROM `items` WHERE Item_Name='Note'")
        itemname = 'Note'
    elif userinput.lower() in ("pickup crowbar", "pick-up crowbar", "get crowbar", "loot crowbar", "take crowbar"):
        value = cur.execute("SELECT `Player_ID` FROM `items` WHERE Item_Name='Crowbar'")
        itemname = 'Crowbar'
    elif userinput.lower() in ("pickup gold", "pick-up gold", "get gold", "loot gold", "take gold", "pickup coins", "pick-up coins", "get coins", "loot coins", "take coins"):
        value = cur.execute("SELECT `Player_ID` FROM `items` WHERE Item_Name='Gold'")
        itemname = 'Gold'
    elif userinput.lower() in ("pickup town hall key", "pick-up town hall key", "get town hall key", "loot town hall key", "take town hall key", "pickup townhall key", "pick-up townhall key", "get townhall key", "loot townhall key", "take townhall key"):
        value = cur.execute("SELECT `Player_ID` FROM `items` WHERE Item_Name='Town Hall key'")
        itemname = 'Town Hall key'
    elif userinput.lower() in ("pickup shovel", "pick-up shovel", "get shovel", "loot shovel", "take shovel"):
        value = cur.execute("SELECT `Player_ID` FROM `items` WHERE Item_Name='Shovel'")
        itemname = 'Shovel'
    elif userinput.lower() in ("pickup house key", "pick-up house key", "get house key", "loot house key", "take house key"):
        value = cur.execute("SELECT `Player_ID` FROM `items` WHERE Item_Name='House key'")
        itemname = 'House key'
    elif userinput.lower() in ("pickup silver key", "pick-up silver key", "get silver key", "loot silver key", "take silver key"):
        value = cur.execute("SELECT `Player_ID` FROM `items` WHERE Item_Name='Silver key'")
        itemname = 'Silver key'
    elif userinput.lower() in ("pickup gasoline", "pick-up gasoline", "get gasoline", "loot gasoline", "take gasoline"):
        value = cur.execute("SELECT `Player_ID` FROM `items` WHERE Item_Name='Gasoline'")
        itemname = 'Gasoline'
    else:
        print()
        print("Command not recognized.")
        return
    value = [row[0] for row in cur.fetchall()]
    valuestr = (str(value[0]))
    sql = "SELECT location_ID FROM items WHERE Item_Name='"+itemname+"'"
    itemloc = cur.execute(sql)
    itemloc = [row[0] for row in cur.fetchall()]
    itemlocstr = (str(itemloc[0]))
    if valuestr == 'None':
        if playerlocstr == itemlocstr:
            sql2 = "UPDATE items SET Player_ID=1 WHERE Item_Name='"+itemname+"'"
            cur.execute(sql2)
            print()
            print("Picked up item: " + itemname.lower() + ".")
            if itemname == 'Gold':
                cur.execute("UPDATE `island`.`siirtymä` SET `Available`='1' WHERE  `From_ID`=12 AND `To_ID`=11;")
                return
            if itemname == 'Note':
                cur.execute("UPDATE `island`.`location` SET `Tekstit`='You get on the motorboat. There is water surrounding you everywhere but north.' WHERE  `ID`=1;")
                return
            if itemname == 'Crowbar':
                cur.execute("UPDATE `island`.`location` SET `Tekstit`='You step inside the old barn, the building is barely standing at this point...' WHERE  `ID`=15;")
                return
            if itemname == 'Shovel':
                cur.execute("UPDATE `island`.`location` SET `Tekstit`='You step inside the old office building. There’s paper and other useless looking office equipment laying everywhere...' WHERE  `ID`=9;")
                return
            if itemname == 'Silver key':
                cur.execute("UPDATE `island`.`location` SET `Tekstit`='You just stepped inside something ravaged and miserable. I guess you can still call it a house.' WHERE  `ID`=3;")
                return
            if itemname == 'Gasoline':
                cur.execute("UPDATE `island`.`location` SET `Tekstit`='You are inside a church that seems to be a thousand years old. The walls have been painted from floor to ceiling and covered with huge religious mosaic art.' WHERE  `ID`=16;")
                return
            else:
                return
        else:
            print()
            print("No such item located here.")
            return
    else:
        print()
        print("I already have that item.")
        return

#examine
def examine():
    cur = db.cursor()
    if userinput.lower() in ("examine note", "inspect note", "check note", "read note", "use note"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='Note'")
        itemname = 'Note'
    elif userinput.lower() in ("examine crowbar", "inspect crowbar", "check crowbar"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='Crowbar'")
        itemname = 'Crowbar'
    elif userinput.lower() in ("examine gold", "inspect gold", "check gold"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='Gold'")
        itemname = 'Gold'
    elif userinput.lower() in ("examine town hall key", "inspect town hall key", "check town hall key", "examine townhall key", "inspect townhall key", "check townhall key"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='Town hall Key'")
        itemname = 'Town hall key'
    elif userinput.lower() in ("examine shovel", "inspect shovel", "check shovel"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='Shovel'")
        itemname = 'Shovel'
    elif userinput.lower() in ("examine house key", "inspect house key", "check house key"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='House Key'")
        itemname = 'House Key'
    elif userinput.lower() in ("examine silver key", "inspect silver key", "check silver key"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='Silver Key'")
        itemname = 'Silver Key'
    elif userinput.lower() in ("examine gasoline", "inspect gasoline", "check gasoline"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='Gasoline'")
        itemname = 'Gasoline'
    else:
        print()
        print("Command not recognized.")
        return
    value = [row[0] for row in cur.fetchall()]
    valuestr = (str(value[0]))
    if valuestr == 'None':
        print()
        print("You do not have that item.")
        return
    else:
        print()
        sql = cur.execute("SELECT examine FROM items WHERE Item_Name='" + itemname + "'")
        sql = ([row[0] for row in cur.fetchall()])
        sqlstr = (str(sql[0]))
        myprint(sqlstr)
        return

#useitem
def use():
    cur = db.cursor()
    if userinput.lower() in ("use crowbar", "unlock bar door", "open baar door"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='Crowbar'")
        itemname = 'Crowbar'
    elif userinput.lower() in ("use town hall key", "use town hallkey", "use townhall key", "use townhallkey", "unlock townhall", "unlock town hall"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='Town Hall key'")
        itemname = 'Town Hall key'
    elif userinput.lower() in ("use shovel", "dig shovel", "dig with shovel", "dig spade", "dig with spade", "dig ground"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='Shovel'")
        itemname = 'Shovel'
    elif userinput.lower() in ("use house key", "use housekey", "unlock house", "unlock abandonedhouse", "unlock abandoned house"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='House key'")
        itemname = 'House key'
    elif userinput.lower() in ("use silver key", "use silverkey", "unlock church"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='Silver key'")
        itemname = 'Silver key'
    elif userinput.lower() in ("use gasoline", "pour gasoline", "use gas", "tank boat", "tank tanker", "tank the tanker"):
        value = cur.execute("SELECT Player_ID FROM items WHERE Item_Name='Gasoline'")
        itemname = 'Gasoline'
    elif userinput.lower() in ("use key", "use key on door"):
        print()
        print("You have to be more specific of which key to use!")
        return
    else:
        print()
        print("Command not recognized.")
        return
    value = [row[0] for row in cur.fetchall()]
    valuestr = (str(value[0]))
    if valuestr == 'None':
        print()
        print("You do not have that item.")
        return
    else:
        if itemname == 'Crowbar':
            if playerlocstr == '6':
                cur.execute("UPDATE `island`.`siirtymä` SET `Available`='1' WHERE  `From_ID`=6 AND `To_ID`=7;")
                print()
                print("You unlock the bar door with your crowbar.")
                return
            else:
                print()
                print("I can't use that here!")
                return
        elif itemname == 'Town Hall key':
            if playerlocstr == '5':
                cur.execute("UPDATE `island`.`siirtymä` SET `Available`='1' WHERE  `From_ID`=5 AND `To_ID`=9;")
                print()
                print("You unlock the town hall with the key.")
                return
            else:
                print()
                print("I can't use that here!")
                return
        if itemname == 'Shovel':
            if playerlocstr == '12':
                cur.execute("UPDATE `island`.`items` SET `Player_ID`='1' WHERE  `Item_ID`=6;")
                print()
                print("You dig the ground and find a 'House key'.")
                return
            else:
                print()
                print("I can't use that here!")
                return
        elif itemname == 'House key':
            if playerlocstr == '4':
                cur.execute("UPDATE `island`.`siirtymä` SET `Available`='1' WHERE  `From_ID`=4 AND `To_ID`=3;")
                print()
                print("You unlock the house with your key.")
                return
            else:
                print()
                print("I can't use that here!")
                return
        elif itemname == 'Silver key':
            if playerlocstr == '12':
                cur.execute("UPDATE `island`.`siirtymä` SET `Available`='1' WHERE  `From_ID`=12 AND `To_ID`=16;")
                print()
                print("You unlock the church with your Silver key.")
                return
            else:
                print()
                print("I can't use that here!")
                return
        elif itemname == 'Gasoline':
            if playerlocstr == '1':
                cur.execute("UPDATE `island`.`siirtymä` SET `Available`='1' WHERE  `From_ID`=1 AND `To_ID`=17;")
                print()
                print("You pour the gasoline into the tank.")
                return
            else:
                print()
                print("I can't use that here!")
                return

#check inventory
def inventory():
    cur = db.cursor()
    items = cur.execute("SELECT Item_Name FROM items WHERE Player_ID=1")
    items = cur.fetchall()
    if items:
        print()
        print("You have the following items:")
        for row in items:
            print(row[0], end=" ")
        print()
        return
    else:
        print()
        print("No items in inventory.")
        return

#drive boat to home
def boat():
    cur = db.cursor()
    if playerlocstr == '1':
        available = cur.execute("SELECT Available FROM siirtymä WHERE From_ID=1 AND To_ID=17")
        available = [row[0] for row in cur.fetchall()]
        availablestr = (str(available[0]))
        if availablestr == '1':
            cur.execute("UPDATE `island`.`player` SET `location_ID`='17' WHERE  `Player_ID`=1;")
            print()
            print("You start the boat and drive far far away, until you find civilization and safety.")
            return
        else:
            print()
            print("The boat doesn't have any gas in it!")
            return
    else:
        print()
        print("I'm not in the boat...")
        return

#help
def commands():
    print()
    print("Moving in the world: north, east, south, west.")
    print("Other commands: Use, examine, pickup, inventory, read.")
    return


'''----------------------------------------
MINIGAME STARTS HERE
----------------------------------------'''
def round():
    cur = db.cursor()
    input( "Press <Enter> to roll dice" )
    g_roll = random.randint(1, 6)
    p_roll = random.randint(1, 6)

    print()
    print("Ghost's roll is " + str(g_roll) + " and your roll is " + str(p_roll))

    if p_roll > g_roll:
        print("You win. You get the key.")
        sleep03()
        print()
        myprint("The ghost goes insane from you winning. He proceeds to give you the key, and tells you to never return. The key looks to be suitable for the town hall.")
        sleep03()
        print()
        myprint("You find yourself at the graveyard. There's path to your south and west. Theres also church to your north and a haunted house to your west.")
        cur.execute("UPDATE `island`.`items` SET `Player_ID`='1' WHERE  `Item_ID`=4;")
        cur.execute("UPDATE `island`.`player` SET `location_ID`='12' WHERE  `Player_ID`=1;")
        cur.execute("UPDATE `island`.`siirtymä` SET `Available`='0' WHERE  `From_ID`=12 AND `To_ID`=11;")
        cur.execute("UPDATE `island`.`location` SET `Extratekstit`='The ghost instantly rushes to you once you open the door and is threathening you.. Maybe it would be the best if I returned to the graveyard...' WHERE  `ID`=11;")

        return

    elif p_roll == g_roll:
        print()
        print("Draw. Try again!")
        return "Draw"
    else:
        print()
        print("Ghost wins. You lost your gold.")
        cur.execute("UPDATE `island`.`items` SET `Player_ID`= NULL WHERE  `Item_ID`=3;")
        cur.execute("UPDATE `island`.`siirtymä` SET `Available`='0' WHERE  `From_ID`=12 AND `To_ID`=11;")
        myprint("You find yourself at the graveyard. There's path to your south and west. Theres also church to your north and a haunted house to your west.")
        cur.execute("UPDATE `island`.`player` SET `location_ID`='12' WHERE  `Player_ID`=1;")
        return "Ghost"

def game():
    game_running = True
    while game_running:
        round_winner = round()
        if round_winner!="Draw":
            game_running = False

def ghost_encounter():
    cur = db.cursor()
    cur.execute("SELECT Player_ID FROM items WHERE Item_ID=4")
    value = [row[0] for row in cur.fetchall()]
    valuestr = (str(value[0]))
    if valuestr != 1:
        print()
        myprint("I'm willing to give you this key, if you are willing to risk all of your gold. We will both roll the dice. The one with the bigger number wins.")
        command = input("Do you want to play? ")
        if command in [ "roll", "yes", "ok" ]:
            game()
        else:
            print()
            myprint("Go away then... The ghost shoo's you away, you run for your life!")
            myprint("You find yourself at the graveyard. There's path to your south and west. Theres also church to your north and a haunted house to your west.")
            cur.execute("UPDATE `island`.`player` SET `location_ID`='12' WHERE  `Player_ID`=1;")
            return
    else:
        return

'''----------------------------------------'''

#INTRO
playerloc = 1
print("\n"*20)
introfunc()
print("\n"*20)
current()
cur = db.cursor()
cur.execute("UPDATE `island`.`location` SET `Tekstit`='You get on the motorboat. There is water surrounding you everywhere but north. There is also a note on the boat.' WHERE  `ID`=1;")
playerlocstr = 1

#Main
while playerlocstr != '17':
    cur = db.cursor()
    cur.execute("SELECT location_ID FROM Player")
    playerloc = [row[0] for row in cur.fetchall()]
    playerlocstr = (str(playerloc[0]))
    if playerlocstr == '11':
        ghost_encounter()
    else:
        sleep03()
        userinput = input("Give a command: ")

        #movement
        if userinput.lower() in ("north", "n", "go north", "go n", "south", "s", "go south", "go s", "west", "w", "go west", "go w", "east", "e", "go east", "go e"):
            movement()

        #1 word, not specific enough phrases
        elif userinput.lower() in ("pickup", "pick-up", "get", "loot", "take", "read", "examine", "inspect"):
            print()
            print("You have to be more specific!")

        #take
        elif userinput.lower() in ("pickup note", "pick-up note", "get note", "loot note", "take note", "take letter", "pickup letter", "take letter", "pick-up letter",
                                   "get letter", "loot letter", "pickup crowbar", "pick-up crowbar", "get crowbar", "loot crowbar", "take crowbar", "pickup gold", "pick-up gold",
                                   "get gold", "loot gold", "take gold", "pickup coins", "pick-up coins", "get coins", "loot coins", "take coins", "pickup town hall key", "pick-up town hall key",
                                   "get town hall key", "loot town hall key", "take town hall key", "pickup townhall key", "pick-up townhall key", "get townhall key", "loot townhall key",
                                   "take townhall key", "pickup shovel", "pick-up shovel", "get shovel", "loot shovel", "take shovel", "pickup house key", "pick-up house key", "get house key",
                                   "loot house key", "take house key", "pickup silver key", "pick-up silver key", "get silver key", "loot silver key", "take silver key", "pickup gasoline",
                                   "pick-up gasoline", "get gasoline", "loot gasoline", "take gasoline"):
            take()

        # examine/read/inspect
        elif userinput.lower() in ("read letter", "examine letter", "inspect letter", "read note", "inspect note", "check note", "read note", "examine note",
                                    "examine crowbar", "inspect crowbar", "check crowbar", "examine gold", "inspect gold", "check gold",
                                    "examine town hall key", "inspect town hall key", "check town hall key", "examine townhall key",
                                    "inspect townhall key", "check townhall key", "examine shovel", "inspect shovel", "check shovel",
                                    "examine house key", "inspect house key", "check house key", "examine silver key", "inspect silver key",
                                    "check silver key", "examine gasoline", "inspect gasoline", "check gasoline", "use note"):
            examine()

        #use item on something
        elif userinput.lower() in ("use crowbar", "use town hall key", "use town hallkey", "use shovel", "dig shovel", "use house key", "use housekey",
                                   "use silver key", "use silverkey", "use gasoline", "pour gasoline", "use townhall key", "use townhallkey",
                                   "unlock bar door", "open baar door", "unlock townhall", "unlock town hall", "dig with shovel",
                                   "dig spade", "dig with spade", "dig ground", "unlock house", "unlock abandonedhouse", "unlock abandoned house", "unlock church",
                                   "use gas", "tank boat", "tank tanker", "tank the tanker"):
            use()

        #checks inventory
        elif userinput.lower() in ("inventory", "i", "bag", "bags", "keys", "items"):
            inventory()

        #using boat/driving boat
        elif userinput.lower() in ("use boat", "drive boat", "launch boat", "start boat", "use motorboat", "drive motorboat", "launch motorboat", "start motorboat"):
            boat()
            cur.execute("SELECT location_ID FROM Player")
            playerloc = [row[0] for row in cur.fetchall()]
            playerlocstr = (str(playerloc[0]))
            if playerlocstr == '17':
                print()
                victory()

        #help
        elif userinput.lower() in ("help", "commands"):
            commands()

        #if command is not supported
        else:
            print()
            print("Command not recognized.")