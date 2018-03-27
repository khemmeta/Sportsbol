import csv

sharks = []
dragons = []
raptors = []
advanced = []
recruits = []

def unpacker(pre_rosters):
    row_list = []
    while len(row_list) < 4:
        """ Unpack one player at a time into final team lists. """
        row_list.append(pre_rosters[0]["Name"])        
        row_list.append(pre_rosters[0]["Height (inches)"])        
        row_list.append(pre_rosters[0]["Soccer Experience"])        
        row_list.append(pre_rosters[0]["Guardian Name(s)"])
    else:
        pre_rosters.pop(0)
        return row_list

if __name__ == "__main__":


    with open('soccer_players.csv', newline='') as csvroster, open('example.txt', 'w') as teamrosters:
        # Get players from csv file.
        roster = list(csv.DictReader(csvroster, delimiter=','))
        # These ordered maps are a pain in my brain.
        for player in roster:
            # Seperate experienced players from beginners.
            if player['Soccer Experience'] == 'YES':
                advanced.append(player)
            else:
                recruits.append(player)
                # This part of my code does what I want it to do!

        while advanced or recruits:
            """ Distribute players to actual teams. """
            if advanced != []:
                sharks.append(unpacker(advanced))
                dragons.append(unpacker(advanced))
                raptors.append(unpacker(advanced))
            elif recruits != []:
                sharks.append(unpacker(recruits))
                dragons.append(unpacker(recruits))
                raptors.append(unpacker(recruits))
            # Everything's lists now.  No dicts.  Almost there?

        
        
        if len(sharks) == len(raptors) and len(raptors) == len(dragons):
            print("Time to write txt files!")
            # write(this that and the other thing)
        else:
            print("Error: Uneven teams.")
    # 1. TRYHARD MODE: (let's just write the extra credit letters and ditch the league types and heights business.  Classes will likely come into play in project 2 anyway. 
    # EC: Create welcome letter text files to each of the 18 students indicating which team they're on etc.
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