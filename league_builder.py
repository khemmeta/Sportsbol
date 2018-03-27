import csv

sharks = []
dragons = []
raptors = []
advanced = []
recruits = []

def unpacker(pre_rosters):
    """Unpack one player at a time into final team lists."""
    row_list = []
    while len(row_list) < 4:
        row_list.append(pre_rosters[0]["Name"])        
        row_list.append(pre_rosters[0]["Height (inches)"])        
        row_list.append(pre_rosters[0]["Soccer Experience"])        
        row_list.append(pre_rosters[0]["Guardian Name(s)"])
    else:
        pre_rosters.pop(0)
        return row_list

def string_list(team):
    """Prepare team strings for final roster."""
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
        
def acceptance_letters(team, team_string):
    """Write acceptance letters to parents."""
    for player in team:
        file_name = str(player[0].replace(' ', '_'))
        file_name += '.txt'
        letter_string = """Dear {}, \n
    Congratulations!  {} has been accepted into the {} family! 
First practice session is on Friday at 5pm.  We recommend you arrive 15 minutes early.
We look forward to seeing you on our fields.  Enjoy your year! \n
    Sincerely,
        Khem Myrick, League Coordinator""".format(player[3], player[0], team_string)
        with open(file_name, 'w') as welcome_letter:
            welcome_letter.write(letter_string)
    print("{} acceptance letters written.".format(team_string))
    
if __name__ == "__main__":
    # Nothing below will run when file is imported.
    with open('soccer_players.csv', newline='') as csvroster:
        roster = list(csv.DictReader(csvroster, delimiter=','))
        
    for player in roster:
        # Seperate experienced players from beginners.
        if player['Soccer Experience'] == 'YES':
            advanced.append(player)
        else:
            recruits.append(player)
            # The above block of code was an early success in this process.

    while advanced or recruits:
        # Distribute players to actual teams.
        if advanced != []:
            # Seperate advanced players 1 by 1 to each team until we run out.
            sharks.append(unpacker(advanced))
            dragons.append(unpacker(advanced))
            raptors.append(unpacker(advanced))
        elif recruits != []:
            # After we run out of advanced players,
            # seperate novice players 1 by 1 to each team until we run out.
            sharks.append(unpacker(recruits))
            dragons.append(unpacker(recruits))
            raptors.append(unpacker(recruits))

    if len(sharks) == len(raptors) and len(raptors) == len(dragons):
        # If all teams have equal number of players, write acceptance letters.
        acceptance_letters(sharks, 'Sharks')
        acceptance_letters(raptors, 'Raptors')
        acceptance_letters(dragons, 'Dragons')        
        with open('teams.txt', 'a') as teamrosters:
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