from random import randint, choice
from time import sleep


class Team():
    def __init__(self, team_name, player_names=list()):
        self.team_name = team_name
        self.player_names = player_names
        self.total_team_run = {self.team_name: 0}

    def view_players(self):
        for name in self.player_names:
            print(name)

    def team_score(self, score):
        self.total_team_run[self.team_name] += score


class Player():
    def __init__(self, name):
        self.name = name
        self.player_info_dict = {self.name: 0}

    def run(self, score):
        self.player_info_dict[self.name] += score


user_team = Team(input("Enter your team name: "), player_names=input(
    "Enter your players, seperated by commas: ").title().split(", "))

sleep(0.3)
oppo_team = input("Do you have any specific team you want to play against?: ")
oppo_team = input("Enter the team name: ") if oppo_team in ["y", "yes", "yeah", "okay", "sure", "yeah sure", "kay", "oh yeah"] else "Opposing Team"
opposing_team = Team(oppo_team)

# setting up opposing team players
# this will reflect the number of players the user has on their team
count = 1
for player in range(len(user_team.player_names)):
    opposing_team.player_names.append("Player " + str(count))
    count += 1

sleep(0.5)
# Getting the number of balls from the user
overs = int(input("How many over(s)?: "))
game_balls = overs * 6

# Creating a Toss simulation

def toss():
    heads_tails = ["heads", "tails"]
    return choice(heads_tails)

# Assigning Heads or Tails to both teams
sleep(0.75)
user_team.toss_choice = input("[h/t] Heads or Tails: ").lower()
user_team.toss_choice = "heads" if user_team.toss_choice in ["h", "heads"] else "tails"
opposing_team.toss_choice = "heads" if user_team.toss_choice == "tails" else "tails"

print()
sleep(1)
# Let's check who won and who'll play what
if user_team.toss_choice == toss():
    print("You have won the toss")
    user_choice = input("Bat or Ball: ").lower()
    user_team.playing = 'Batting' if user_choice == "bat" else "Balling"
    opposing_team.playing = "Balling" if user_team.playing == "Batting" else "Batting"
else:
    print("You have lost")
    bat_or_ball = ["Bat", "Ball"]
    opponent_choice = bat_or_ball[randint(0, 1)]
    opposing_team.playing = "Batting" if opponent_choice == "Bat" else "Balling"
    user_team.playing = "Balling" if opposing_team.playing == "Batting" else "Batting"

print()
sleep(0.4)
print(f"You are {user_team.playing}")
sleep(0.4)
print(f"{opposing_team.team_name} is {opposing_team.playing}")

# Beginning game
# Creating players for both teams
# Number of players in opponent team depends on how many players your team has
user_player_dict = dict()
opposing_player_dict = dict()

for player in range(1, len(user_team.player_names)+1):
    user_player_dict[f"user_player{player}"] = Player(
        user_team.player_names[player-1])
    opposing_player_dict[f"Player {player}"] = Player(
        opposing_team.player_names[player-1])

# Creating wickets
user_wickets = opponent_wickets = len(user_team.player_names) - 1

def batting(balls, first_innings=False):
    sleep(1)
    global user_wickets
    position = 0
    players_left = user_team.player_names
    print(f"You have {user_team.player_names}")
    played_batsmen = list()
    initial_batsmen = input("Which two players are you willing to send first?: ").split(",")
    initial_batsmen = [player.strip().title() for player in initial_batsmen]
    while set(initial_batsmen).issubset(user_team.player_names) == False or len(initial_batsmen) > 2:
        if len(initial_batsmen) > 2:
            initial_batsmen = input("You can't send more than two people to bat ").split(",")
            initial_batsmen = [player.strip().title() for player in initial_batsmen]
        else:
            initial_batsmen = input("The player you entered must be in your initial player list: ").split(",")
            initial_batsmen = [player.strip().title() for player in initial_batsmen]
    playing_batsmen = list()
    for player in initial_batsmen:
        for dev_player_name, player_name in user_player_dict.items():
            if player_name.name == player:
                playing_batsmen.append(user_player_dict[dev_player_name])

    for player in initial_batsmen:
        players_left.remove(player)
    for player in initial_batsmen:
        played_batsmen.append(player)

    current_batsman = playing_batsmen[position]
    def over_options(user_choice):
        if user_choice == "b":
            print(players_left)
        elif user_choice == "c":
            print(user_team.total_team_run)
        elif user_choice == "d":
            for player_name in user_player_dict:
                for value in user_player_dict[player_name].player_info_dict.values():
                    if value > 0:
                        print(user_player_dict[player_name].player_info_dict)
        elif user_choice == "e":
            print(f"Balls left: {balls}\nWickets left: {user_wickets}")
        elif user_choice == "g":
            print(f"Your target is {opposing_team.total_team_run[opposing_team.team_name]+1}")
            
    while balls > 0:
        if current_batsman.name not in played_batsmen:
            played_batsmen.append(current_batsman.name)
        if user_wickets > 0:
            if balls != game_balls:
                if balls % 6 == 0:
                    print()
                    print("A over is done")
                    print()
                    current_batsman = playing_batsmen[position] if current_batsman == playing_batsmen[position-1] else playing_batsmen[position-1]
                    print()
                    sleep(1)
                    if first_innings:
                        extra_options = "g) View target"
                        extra_option_suffix = ["/g"]
                    else:
                        extra_options = str()
                        extra_option_suffix = [""]
                    print(f"Options: a) Continue b) Remaining players\nc) Current team run d) Players' scores\ne) Balls & wickets left f) Surrender {extra_options}")
                    user_option_choice = input(f"[a/b/c/d/e/f{extra_option_suffix[0]}]: ").lower()
                    while user_option_choice not in ["a", "b", "c", "d", "e", "f", "g"]:
                        user_option_choice = input(f"You cannot enter anyting other than: [a/b/c/d/e/f/{extra_option_suffix[0]}] ").lower()
                    while user_option_choice != "a":
                        if user_option_choice == "f":
                            balls = 0
                            print("Surrendering...")
                            break
                        if user_option_choice not in ["a", "f"]:
                            over_options(user_option_choice)
                            user_option_choice = input(f"[a/b/c/d/e/f{extra_option_suffix[0]}]: ").lower()
                            sleep(0.85)
            if balls > 0:
                user_team_run = int(input(f"Playing: {current_batsman.name}. Enter your run number: "))
                print()
                if user_team_run > 6:
                    while user_team_run > 6:
                        user_team_run = int(input("You cannot enter number larger than 6 "))
                run = randint(0, 6)
                if run != user_team_run:
                    user_team.team_score(user_team_run)
                    if user_team_run % 2 == 0:
                        sleep(0.5)
                        print(f"Wow! {current_batsman.name} scored {user_team_run} runs")
                        current_batsman.run(user_team_run)
                    else:
                        print(f"Wow! {current_batsman.name} scored {user_team_run} runs")
                        position += 1
                        if position > 1:
                            position = 0
                        current_batsman.run(user_team_run)
                        current_batsman = playing_batsmen[position] if current_batsman == playing_batsmen[position-1] else playing_batsmen[position-1]
                else:
                    user_wickets -= 1
                    if user_wickets > 0:
                        if current_batsman.name not in initial_batsmen and current_batsman.name in players_left:
                            players_left.remove(current_batsman.name)

                        sleep(0.5)
                        print(f"Shoot! {current_batsman.name} is out!!") 
                        next_player = input(f"Players left: {players_left}. Which player do you want to send next?: ").strip().title()

                        while next_player not in user_team.player_names or next_player in played_batsmen:
                            if next_player == current_batsman.name:
                                while next_player == current_batsman.name:
                                    next_player = input("He just got out dude, wth? Enter again!: ").strip().title()
                            elif next_player in played_batsmen:
                                next_player = input("He already played. Try again: ").strip().title()
                            elif next_player not in user_team.player_names:
                                next_player = input("That player was not in your team. Enter again: ").strip().title()

                        if next_player in players_left:
                            players_left.remove(next_player)

                        playing_batsmen.remove(current_batsman)
                        for dev_player_name, player_name in user_player_dict.items():
                            if player_name.name == next_player:
                                playing_batsmen.append(user_player_dict[dev_player_name]) 
                                
                        current_batsman = playing_batsmen[1]
                        position += 1
                        if position > 1:
                            position = 0
            
            if first_innings:
                if user_team.total_team_run[user_team.team_name] > opposing_team.total_team_run[opposing_team.team_name]:
                    print()
                    sleep(1)
                    print(f"You have won the match with {balls} balls left!!")
                    balls = 0

        else:
            print(f"Damn! Your players have all been out with {balls} balls left")
            balls = 0

        sleep(1)
        balls -= 1

    print()
    sleep(1)

    
    # Shows the scores of the players who got to play and score anything above zero in the innings.
    if first_innings in [False, True]:
        for player_name in user_player_dict:
            for value in user_player_dict[player_name].player_info_dict.values():
                if value > 0:
                    print(user_player_dict[player_name].player_info_dict)

    print()
    sleep(0.5)
    # Displaying team total run
    print(user_team.total_team_run)

    print()
    sleep(0.5)
    if first_innings == False:
        print(f"You have scored {user_team.total_team_run[user_team.team_name]} runs. {opposing_team.team_name}'s target is {user_team.total_team_run[user_team.team_name]+1}")


def balling(balls, first_innings=False):
    global opponent_wickets
    position = 0
    playing_batsmen = [opposing_player_dict["Player 1"], opposing_player_dict["Player 2"]]
    current_batsman = playing_batsmen[position]
    next_player_position = 0
    def over_options(user_choice):
        if user_choice == "c":
            if first_innings:
                extra = f"They still need {(user_team.total_team_run[user_team.team_name]-opposing_team.total_team_run[opposing_team.team_name])+1} runs to win."
            else:
                extra = str()
            print(f"{opposing_team.team_name}'s current score is {opposing_team.total_team_run[opposing_team.team_name]}. {extra}")
        elif user_choice == "d":
            print(f"{opposing_team.team_name} has {opponent_wickets} wickets left")
        elif user_choice == "e":
            print(f"{[player.name for player in playing_batsmen]}")  

    autoplay = [False]        
    while balls > 0:
        if opponent_wickets > 0:
            if balls != game_balls:
                if balls % 6 == 0:
                    print()
                    print("A over is done")
                    print()
                    current_batsman = playing_batsmen[position] if current_batsman == playing_batsmen[position-1] else playing_batsmen[position-1]
                    extra_option = "Manual play" if autoplay[0] == True else "Autoplay"
                    print(f"Options: a) Continue b) {extra_option} c) {opposing_team.team_name}'s current score\nd) {opposing_team.team_name}'s renaming wickets e) {opposing_team.team_name}'s current batsmen\nf) Surrender")
                    user_option_choice = input(f"[a/b/c/d/e/f]: ").lower()
                    while user_option_choice not in ["a", "b", "c", "d", "e", "f"]:
                        user_option_choice = input(f"You cannot enter anything other than these [a/b/c/d/e/f]: ").lower()
                    while user_option_choice != "a":
                        if user_option_choice == "b" and extra_option == "Manual play":
                            autoplay.clear()
                            autoplay.append(False)
                            break
                        if user_option_choice == "b":
                            autoplay.clear()
                            autoplay.append(True)
                            break
                        if user_option_choice == "f":
                            balls = 0
                            print("Surrendering...")
                            break
                        if user_option_choice not in ["a", "b", "f"]:
                            over_options(user_option_choice)
                            user_option_choice = input(f"[a/b/c/d/e/f: ").lower()
                            while user_option_choice not in ["a", "b", "c", "d", "e", "f"]:
                                user_option_choice = input(f"You cannot enter anything other than these [a/b/c/d/e/f]: ").lower()
                            sleep(0.85)
            if balls > 0:
                if autoplay[0] == False:
                    user_team_ball = int(input(f"Playing: {current_batsman.name}. Enter your ball number: "))
                    print()
                    while user_team_ball > 6:
                        user_team_ball = int(input("Unless you don't want the opponent to get out, keep doin' your shitty stuff "))
                if autoplay[0]:
                    user_team_ball = randint(0, 6)
                    print(f"You bowled {user_team_ball}")
                    sleep(0.5)
                run = randint(0, 6)
                if run != user_team_ball:
                    opposing_team.team_score(run)
                    if run % 2 == 0:
                        print("You missed!")
                        sleep(0.5)
                        print(f"{current_batsman.name} scored {run} runs")
                        current_batsman.run(run)
                    else:
                        print("You missed!")
                        sleep(0.5)
                        print(f"{current_batsman.name} scored {run} runs")
                        position += 1
                        if position > 1:
                            position = 0
                        current_batsman.run(run)
                        current_batsman = playing_batsmen[position] if current_batsman == playing_batsmen[position-1] else playing_batsmen[position-1]
                else:
                    opponent_wickets -= 1
                    if opponent_wickets > 0:
                        next_player = ["Player " + str(x) for x in range(3, len(opposing_team.player_names)+1)] 
                        sleep(0.5)
                        print(f"Damn! You took out {current_batsman.name}!!")
                        playing_batsmen.remove(current_batsman)
                        playing_batsmen.append(opposing_player_dict[next_player[next_player_position]])
                        next_player_position += 1
                        current_batsman = playing_batsmen[position] if current_batsman == playing_batsmen[position-1] else playing_batsmen[position-1]
                        position += 1
                        if position > 1:
                            position = 0

            if first_innings:
                if opposing_team.total_team_run[opposing_team.team_name] > user_team.total_team_run[user_team.team_name]:
                    print()
                    sleep(1)
                    print(f"You have lost the match. {opposing_team.team_name} won with {balls} balls remaining")
                    balls = 0


        else:
            print(f"{opposing_team.team_name} is all out with {balls} balls left")
            balls = 0


        sleep(1)
        balls -= 1

    print()
    sleep(1)
    
    if first_innings in [False, True]:
        for player_name in opposing_player_dict:
            for value in opposing_player_dict[player_name].player_info_dict.values():
                if value > 0:
                    print(opposing_player_dict[player_name].player_info_dict)

    print()
    sleep(0.5)
    print(opposing_team.total_team_run)

    if first_innings == False:
        print(f"{opposing_team.team_name} scored {opposing_team.total_team_run[opposing_team.team_name]}. Your target is {opposing_team.total_team_run[opposing_team.team_name]+1}")


sleep(1)
print()
print(f"Line up: {user_team.team_name}: {user_team.player_names}")
sleep(0.5)
print(f"{opposing_team.team_name}: {opposing_team.player_names}")
print()

# Starting first innings
if user_team.playing == "Batting":
    batting(game_balls)
else:
    balling(game_balls)
    

first_innings_done = True


# Second innings
print()
sleep(1)
print("The first innings was done. We will now proceed to the next innings")


if first_innings_done:
    user_team.playing = "Balling" if user_team.playing == "Batting" else "Batting"
    opposing_team.playing = "Batting" if opposing_team.playing == "Balling" else "Balling"

    # Staring innings
    if user_team.playing == "Balling":
        balling(game_balls, first_innings_done)
    else:
        batting(game_balls, first_innings_done)


print()
sleep(1)
print(user_team.total_team_run)
sleep(1)
print(opposing_team.total_team_run)


# Let's see who won
def winner_decider(user_team_run, opposing_team_run):
    if user_team_run > opposing_team_run:
        print(f"Congrats! Your team won by {user_team.total_team_run[user_team.team_name] - opposing_team.total_team_run[opposing_team.team_name]} runs")
    else:
        print(f"Better luck next time! {opposing_team.team_name} won by {opposing_team.total_team_run[opposing_team.team_name] - user_team.total_team_run[user_team.team_name]} runs")

sleep(1)
winner_decider(user_team.total_team_run[user_team.team_name], opposing_team.total_team_run[opposing_team.team_name])