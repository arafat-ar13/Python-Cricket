from random import randint
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
    "Enter your players, seperated by commas: ").split(", "))

sleep(0.3)
oppo_team = input("Do you have any specific team you want to play against?: ")
oppo_team = input("Enter the team name: ") if oppo_team in ["y", "yes", "yeah", "okay", "sure"] else "Opposing Team"
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
    choice = ["heads", "tails"]
    return choice[randint(0, 1)]

# Assigning Heads or Tails to both teams
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
    global user_wickets
    position = 0
    playing_batsmen = [user_player_dict["user_player1"], user_player_dict["user_player2"]]
    current_batsman = playing_batsmen[position]
    next_player_position = 0
    while balls > 0:
        if user_wickets > 0:
            if balls != game_balls:
                if balls % 6 == 0:
                    print()
                    print("A over is done")
                    print()
                    current_batsman = playing_batsmen[position] if current_batsman == playing_batsmen[position-1] else playing_batsmen[position-1]
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
                    next_player = ["user_player" + str(x) for x in range(3, len(user_team.player_names)+1)]
                    sleep(0.5)
                    print("Shoot! Your player is out!!")
                    playing_batsmen.remove(playing_batsmen[position])
                    playing_batsmen.append(user_player_dict[next_player[next_player_position]]) 
                    next_player_position += 1
                    current_batsman = playing_batsmen[position] if current_batsman == playing_batsmen[position-1] else playing_batsmen[position-1]
                    position += 1
                    if position > 1:
                        position = 0
            
            if first_innings:
                if user_team.total_team_run[user_team.team_name] > opposing_team.total_team_run[opposing_team.team_name]:
                    print()
                    sleep(1)
                    print("You have won the match!!")
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
    while balls > 0:
        if opponent_wickets > 0:
            user_team_ball = int(input("Enter your ball number: "))
            print()
            while user_team_ball > 6:
                user_team_ball = int(input("Unless you don't want the opponent to get out, keep doin' your shitty stuff "))
            run = randint(0, 6)
            if run != user_team_ball:
                if balls != game_balls:
                    if balls % 6 == 0:
                        print()
                        print("A over is done")
                        print()
                        current_batsman = playing_batsmen[position] if current_batsman == playing_batsmen[position-1] else playing_batsmen[position-1]
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
                    print("Damn! You took a wicket!!")
                    playing_batsmen.remove(playing_batsmen[position])
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
                    print("You have lost the match")
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