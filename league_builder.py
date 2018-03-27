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

def string_list(team):
    """ Prepare team strings."""
    player_string = ''
    for player in team:        
        del player[1]
        player_string += str(player)
        player_string = player_string.replace('[', '')
        player_string = player_string.replace(']', '')
        player_string = player_string.replace("'", "")
        player_string += '\n'        
    player_string += '\n'
    return player_string
        

if __name__ == "__main__":


    with open('soccer_players.csv', newline='') as csvroster: 
        # Get players from csv file and put into roster list.
        roster = list(csv.DictReader(csvroster, delimiter=','))
        # We should be done with the csv file.  Deindenting steps below.
        
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


    if len(sharks) == len(raptors) and len(raptors) == len(dragons):
        with open('teams.txt', 'a') as teamrosters:
            
            teamrosters.write("Sharks \n")
            teamrosters.write(string_list(sharks))
            teamrosters.write("Dragons \n")
            teamrosters.write(string_list(dragons))
            teamrosters.write("Raptors \n")
            teamrosters.write(string_list(raptors))
            print("File(s) written.")

    else:
        print("Error: Uneven teams.")

    # Extra credit goals: Write welcome letter text for each player.

    # For my own idea of what would make this software IRL useful:    
    # Include functionality that can:
    #     1. Divide players into larger teams for different league types.
    #     2. Allow coordinators to insert number of teams to divide players into.
    #     3. Take player heights into account to keep teams evenly matched.
    #     4. Return error message or something if teams cannot be evenly matched. 

else:
    print("Due to tariffs, this file cannot be imported.")