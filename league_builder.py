import csv

if __name__ == "__main__":
    sharks = []
    dragons = []
    raptors = []
    advanced = []
    recruits = []
    with open('soccer_players.csv', newline='') as csvroster:
        # Get players from csv file.
        rows = list(csv.DictReader(csvroster, delimiter=','))
        headings = rows[0]
        roster = rows[1:]
        for row in rows:
            # Seperate experienced players from beginners.
            if row['Soccer Experience'] == 'YES':
                advanced.append(row)
            else:
                recruits.append(row)

        while advanced or recruits:
            """ Distribute players to actual teams. """
            if advanced != []:
                for row in advanced:
                    sharks.append(advanced.pop())
                    dragons.append(advanced.pop())
                    raptors.append(advanced.pop())
            elif recruits != []:
                for row in recruits:
                    sharks.append(recruits.pop())
                    dragons.append(recruits.pop())
                    raptors.append(recruits.pop())
        print("Number of Sharks: {}".format(len(sharks)))
    # 1. TRYHARD MODE:
    # Set league_type, U6, U8, U10, U12 or U13.
    # Set default value of league_type to U8 for this project.
    # For a U8 class league_type, have lbp calc how many experienced players can be distributed to the available number of teams of the specific size., 

    # 2. ACTUAL ASSIGNMENT:
    # In the list of teams include the team name on one line, followed by a separate line for each player. Include the player's name, whether the player has experience playing soccer, and the player's guardian names. Separate each bit of player information by a comma. For example, the text file might start something like this:
     
# Sharks
# Frank Jones, YES, Jim and Jan Jones
# Sarah Palmer, YES, Robin and Sari Washington
# Joe Smith, NO, Bob and Jamie Smith 



    # Generate lists of experienced vs inexperienced players.
    # Use loop to evenly pop experienced players into 3 team lists.
    # Use another loop to pop remainder of players into same 3 teams.
    
    # with open('teams.txt', 'a') as teamrosters:
        # fieldnames = ['get_these_from_roster']
        # teamrosters.write(csvfile, fieldnames=fieldnames)
# else:
    # print("Due to tariffs, this file cannot be imported.")