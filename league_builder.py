import csv

sharks = []
dragons = []
raptors = []
advanced = []
recruits = []

def unpacker(pre_rosters):
    """Unpack one player at a time into final team lists."""
    return pre_rosters.pop(0)

def string_list(team):
    """Prepare team strings for final roster."""
    player_string = ''
    for player in team:        
        del player["Height (inches)"]
        player_string += str(player)
        player_string = player_string.replace("OrderedDict", "")
        player_string = player_string.replace(')', '')
        player_string = player_string.replace('(', '')
        player_string = player_string.replace('[', '')
        player_string = player_string.replace(']', '')
        player_string = player_string.replace("'", "")
        player_string = player_string.replace('Guardian Names, ', '')
        player_string = player_string.replace('Name, ', '')
        player_string = player_string.replace('Soccer Experience, ',
                                              '')

        player_string += '\n'        
    player_string += '\n'
    return player_string
        
def acceptance_letters(team, team_string):
    """Write acceptance letters to parents."""
    with open('letter.txt') as letter_temp:
        for player in team:
            file_name = str(player['Name'].replace(' ', '_'))
            file_name = file_name.lower()
            file_name += '.txt'
            letter_temp.seek(0)
            letter_string = letter_temp.read().format(player['Guardian Name(s)'], 
                                                      player['Name'], 
                                                      team_string)
            with open(file_name, 'w') as welcome_letter:
                welcome_letter.write(letter_string)
        print("{} acceptance letters written.".format(team_string))
    
if __name__ == "__main__":
    with open('soccer_players.csv', newline='') as csvroster:
        roster = list(csv.DictReader(csvroster, delimiter=','))
        
    for player in roster:
        # Seperate experienced players from beginners.
        if player['Soccer Experience'] == 'YES':
            advanced.append(player)            
        else:
            recruits.append(player)            
            
    while advanced or recruits:
        # Distribute players to teams.        
        if advanced != []:
            # Seperate advanced players to each team until we run out.
            sharks.append(unpacker(advanced))
            dragons.append(unpacker(advanced))
            raptors.append(unpacker(advanced))
        elif recruits != []:
            # After we run out of advanced players,
            # seperate novice players to each team until we run out.
            sharks.append(unpacker(recruits))
            dragons.append(unpacker(recruits))
            raptors.append(unpacker(recruits))

    if len(sharks) == len(raptors) and len(raptors) == len(dragons):
        # If all teams have equal number of players, write letters.
        acceptance_letters(sharks, 'Sharks')
        acceptance_letters(raptors, 'Raptors')
        acceptance_letters(dragons, 'Dragons')        
        with open('teams.txt', 'w') as teamrosters:
            # Write final roster.
            teamrosters.write("Sharks \n")
            teamrosters.write(string_list(sharks))
            teamrosters.write("Dragons \n")
            teamrosters.write(string_list(dragons))
            teamrosters.write("Raptors \n")
            teamrosters.write(string_list(raptors))
            print("Final roster file written.")
    else:
        print("Error: Uneven teams.")

else:
    # Explicitly announce that code will not run as imported module.
    print("Due to tariffs, this file cannot be imported.")