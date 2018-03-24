import csv

if __name__ == "__main__":
    sharks = []
    dragons = []
    raptors = []
    advanced = []
    recruits = []
    with open('soccer_players.csv', newline='') as csvroster, open('example.txt', 'w') as teamrosters:
        # Get players from csv file.
        rows = list(csv.DictReader(csvroster, delimiter=','))
        # These ordered maps / lists / etc are a pain in my brain.
        headings = rows[0]
        roster = rows[1:]
        for row in rows:
            # Seperate experienced players from beginners.
            if row['Soccer Experience'] == 'YES':
                advanced.append(row)
            else:
                recruits.append(row)
                # This part of my code does what I want it to do!
        
        
        while advanced or recruits:
            """ Distribute players to actual teams. """
            if advanced != []:
                for row in advanced:
                    for key, val in row:
                        # This was my first attmept to turn ODs into plain lists.
                        rowlist = []
                        val[0], val[2], val[3] = advanced.pop()
                        rowlist.append(val[0])
                        rowlist.append(val[2])
                        rowlist.append(val[3])
                        sharks.append(rowlist)
                        
                        rowlist = []
                        val[0], val[2], val[3] = advanced.pop()
                        rowlist.append(val[0])
                        rowlist.append(val[2])
                        rowlist.append(val[3])
                        dragonss.append(rowlist)
                        
                        rowlist = []
                        val[0], val[2], val[3] = advanced.pop()
                        rowlist.append(val[0])
                        rowlist.append(val[2])
                        rowlist.append(val[3])
                        raptors.append(rowlist)
                        
            elif recruits != []:
                for row in recruits:
                    for key, val in row:
                        rowlist = []
                        val[0], val[2], val[3] = recruits.pop()
                        rowlist.append(val[0])
                        rowlist.append(val[2])
                        rowlist.append(val[3])
                        sharks.append(rowlist)
                        
                        rowlist = []
                        val[0], val[2], val[3] = recruits.pop()
                        rowlist.append(val[0])
                        rowlist.append(val[2])
                        rowlist.append(val[3])
                        dragonss.append(rowlist)
                        
                        rowlist = []
                        val[0], val[2], val[3] = recruits.pop()
                        rowlist.append(val[0])
                        rowlist.append(val[2])
                        rowlist.append(val[3])
                        raptors.append(rowlist)
                                            
            print(sharks)
            # **Babylon 5 Narration voice**: It failed.
        # name, height, exp, rents = sharks

        

        # teamrosters.write("Sharks: \n {}".format(sharks))
        # Unpack ordered maps, tuples/lists/etc to get to strings.
        # Write ", "joined strings to our file.
        # print(sharks)
        # print("\n \n")
        # print("Number of Raptors: {}".format(len(raptors)))
        # print(raptors)
        # print("\n \n")
        # print("Number of Dragons: {}".format(len(dragons)))
        # print(dragons)
        # if len(sharks) == len(raptors) and len(raptors) == len(dragons):
        #    print("Next time, I can write these teams to teams.text!")
        # else:
        #    print("Error: Uneven teams.")
    # 1. TRYHARD MODE:
    # Set league_type, U6, U8, U10, U12 or U13.
    # Set default value of league_type to U8 for this project.
    # For a U8 class league_type, have lbp calc how many experienced players can be distributed to the available number of teams of the specific size.
    # Also, try to evenly distribute shorter players to each team as well.

    # 2. ACTUAL ASSIGNMENT:
    # In the list of teams include the team name on one line, followed by a separate line for each player. Include the player's name, whether the player has experience playing soccer, and the player's guardian names. Separate each bit of player information by a comma. For example, the text file might start something like this:
     
# Sharks
# Frank Jones, YES, Jim and Jan Jones
# Sarah Palmer, YES, Robin and Sari Washington
# Joe Smith, NO, Bob and Jamie Smith 



    # Generate lists of experienced vs inexperienced players.
    # Use loop to evenly pop experienced players into 3 team lists.
    # Use another loop to pop remainder of players into same 3 teams.
    
    # with open('teams.txt', 'a') as teamrosters ( now included in line opening csv file):
        # fieldnames = ['get_these_from_roster']
        # teamrosters.write(csvfile, fieldnames=fieldnames)
else:
    print("Due to tariffs, this file cannot be imported.")