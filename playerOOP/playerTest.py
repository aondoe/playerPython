import ast; #Module to convert string to dictionary.

class Player:
    playerData=[];
    def __init__(self, playerName,position,teamName, nature):   #4 parameters to initialize the Player object.
        self.penalties=0;   #penalties
        self.salary=100;    #The salary of the player not yet used yet.
        self.teamName=teamName;
        self.playerName=playerName;     #Name of the player
        self.position=str(position); #   Position of the player
        self.nature=nature;     #   Play Offense or Defense
        rush_attack=[];
        
    def setPenalty(self,penalty):   #set Penalty counts for one player.
        self.penalties=penalty;
    def getPenalty(self):   #Get penalties for one player
        return self.penalties;

class Team:
    def __init__(self, teamName):
        self.teamName=teamName;

    def teamRushYards(self):
        with open("players.txt","r") as file:
            data = file.readlines();

        count=0;
        accum=0;
        newData=[];
        ##### For loop to Convert string elements of list into dictionary elements in a new list #######
        for x in data:
            adDict=ast.literal_eval(data[count]);#Use the ast module to go into the list and convert each element into the dictionary from file.
            newData.append(adDict); #Put the new dictionary element inside of a new list
            count=count+1;  #Iterates count variable to move across the list.

#newData list now has a list of the player stats in a dictionary.
        for x in newData:
            if self.teamName==x["Team"]:    #If the teamName from the parameter is equal to the dictiionary value in the 'Team' key proceed.
                accum+=x["RushYards"];      #Using the accumulator variable to capture data within the value from the key: 'RushYards'
        print(self.teamName+" had ",accum," ruhsing yards this year.");

class QuarterBack(Player):
    qb_player={};
    rush_attack={};
        
    def getYards(self):     #getyards() method is defined will return the number of yards for a quarterback for a year.
        return self.value;  #This will return the value after a setYards() has been captured

    def setYards(self, value):  #setTouch() method is defined will set the number of touchdowns for a quarterback in the year.
        self.value=value;       #sets the integer value for Yards in a year for a quarterback


    def getTouch(self):         #getTouch() method is defined will return the number of touchdowns for a quarterback in the year.
        return self.points;     #return the value from setTouch().
    
    def setTouch(self, points): #setTouch() method to capture the number of touchdowns for a quarterback in the year.
        self.points=points;     #programmer/user can set value

    def setRushTouch(self,rushTouch):   #set rushing touchdowns
        self.rushTouch=rushTouch;       #rushing touchdowns
    def getRushTouch(self):     #get rushing touchdowns
        return self.rushTouch;  #returns the value from the method declaration
    
    def setRushYardGame(self,rushGame): #Set the rushing yards per game
        self.rushGame=rushGame;     #return yards per game
    def getRushYardGame(self): #Set the rushing yards per game
        return int(self.rushGame);     #return yards per game

    def setRushTouch(self,rushTouch):   #set rushing touchdowns
        self.rushTouch=rushTouch;       #rushing touchdowns
    def getRushTouch(self):     #get rushing touchdowns
        return self.rushTouch;  #returns the value from the method declaration
        
    def rushStats(self):
        if self.nature.casefold()=="offense".casefold():
            rush_attack={"Player":self.playerName, "Position":self.position, "Team":self.teamName, "RushYards":self.getRushYardGame(), "RushTDs":self.getRushTouch()};
        return rush_attack;

    def qbGetStats(self):
        if self.position.casefold()=="quarterback":
            qb_player={"Player":self.playerName, "Position":self.position, "Team":self.teamName, "Nature":self.nature, "ThrowTds":self.getTouch(), "ThrowYards":self.getYards()};
            return qb_player;


###################################          Rushing       #################################
class Rushing(Player):
    
    def attGame(self, att):     #Set the rushing attempts per game
        self.att=att;           #returnt the attempts per game
        
    def getAttGame(self):       #get attempts per game
        return self.att;

    def setRushYards(self,rush):        #Set Rushing yards
        self.rush=rush;         #return the rushing yards
    def getRushYards(self):             #Get Rushing yards
        return self.rush;       #Set rushing yards

    def setRushYardGame(self,rushGame): #Set the rushing yards per game
        self.rushGame=rushGame;     #return yards per game
    def getRushYardGame(self): #Set the rushing yards per game
        return self.rushGame;     #return yards per game

    def setRushTouch(self,rushTouch):   #set rushing touchdowns
        self.rushTouch=rushTouch;       #rushing touchdowns
    def getRushTouch(self):     #get rushing touchdowns
        return self.rushTouch;  #returns the value from the method declaration

    def rushStats(self):
        if self.position.casefold()=="running back".casefold():
            rush_attack={"Player":self.playerName, "Position":self.position, "Team":self.teamName, "Nature":self.nature, "AttemptsPerGame":self.getAttGame(), "RushYards":self.getRushYards(), "RushTDs":self.getRushTouch()};
        else:
            return self.playerName," is not a running back.";
        return rush_attack;

"""
This program will use the .setTouch() method to set touchdowns for a player object. And it will also display 
"""

def footballStats():  #define new QuarterBack object
    mahomes=QuarterBack("Mahomes","Quarterback", "Chiefs", "offense");
    mahomes.setTouch(28);    #Set the number of touchdowns for the player.
    mahomes.setYards(5000);  #Set the number of yards for a player.
    mahomes.setRushYardGame(500);
    mahomes.setRushTouch(5);

############        New Rushing Object   |  Running Back        ########################
    dWill=Rushing("Damien Williams", "running Back", "Chiefs", "Offense"); #Initialize new Player object
    dWill.position="Running Back";
    dWill.attGame(10);    #Set Rush yards for dHenry
    dWill.setRushYards(873);   #Set rushing yards for dHenry
    dWill.setRushTouch(16);    #How many touchdowns did dHenry run for in the regular season?
    dWill.setPenalty(3);       #Set penalties for the year for a player

############        New Rushing Object   |  Running Back        ########################
    sMccoy=Rushing("Lesean Mccoy", "running Back", "Chiefs", "Offense"); #Initialize new Player object
    sMccoy.attGame(10);    #Set Rush yards for dHenry
    sMccoy.setRushYards(573);   #Set rushing yards for dHenry
    sMccoy.setRushTouch(8);    #How many touchdowns did dHenry run for in the regular season?
    sMccoy.setPenalty(0);       #Set penalties for the year for a player

###############     New QuarterBack object       #########
    brady=QuarterBack("Brady", "quarterback", "Buccaneers", "offense"); #Initialize new QuarterBack object
    brady.playerName="Tom Brady";   #Tom Brady is the name of the new quarterback.
    bradyPoint=brady.setTouch(25);    #Set Touchdowns for Tom Brady
    bradyYards=brady.setYards(4135);   #Set throwing yards for Tom Brady

###############     New Rushing Object   |  Running Back             #######################
    dHenry=Rushing("Derick Henry", "running Back", "Tennesee Titans", "Offense"); #Initialize new Player object
    dHenry.position="Running Back";     #Set position
    dHenry.teamName="Tennessee Titans"; #Set team name
    dHenry.attGame(25);    #Set Rush yards for dHenry
    dHenry.setRushYards(1573);   #Set rushing yards for dHenry
    dHenry.setRushTouch(16);    #How many touchdowns did dHenry run for in the regular season?
    dHenry.setPenalty(3);       #Set penalties for the year for a player

    def addtoData(*args):   #Take unlimited arguments
        newList=list(args); #Turn the arguments parameter into a list object
        playerFile=open("players.txt","w");    #initialize IO object and set it in "append" mode
        count=0;    #count the records in your text file
        
        for x in newList:   #For each element created by the args paramter put into the 'newList' object write it into the file: 'players.txt'
            print(x,  file=playerFile);
            count=count+1;
        playerFile.close(); #close file after use
    addtoData(dHenry.rushStats(), mahomes.rushStats(), dWill.rushStats(), sMccoy.rushStats())   #add these objects to the text file.
    
##########      New Team Object     ##########
    chiefs=Team(sMccoy.teamName);      #New Team object, with Chiefs set to teamName.
    chiefs.teamRushYards();   #Return all the total touchdowns for any player on the Chiefs team

footballStats();    #Call the function which will execute above.
