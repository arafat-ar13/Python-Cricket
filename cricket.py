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
opposing_team = Team("Opposing Team")

# setting up opposing team players
# this will reflect the number of players the user has on their team
count = 1
for player in range(len(user_team.player_names)):
    opposing_team.player_names.append("Player " + str(count))
    count += 1

# Creating a Toss simulation

def toss():
    choice = ["heads", "tails"]
    return choice[randint(0, 1)]


# Assigning Heads or Tails to both teams
user_team.toss_choice = input("Heads or Tails: ").lower()
opposing_team.toss_choice = "heads" if user_team.toss_choice == "tails" else "tails"

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

print(f"You are {user_team.playing}")
print(f"Opposing team is {opposing_team.playing}")

# Beginning game
user_player_dict = dict()
opposing_player_dict = dict()

for player in range(1, len(user_team.player_names)+1):
    user_player_dict[f"user_player{player}"] = Player(
        user_team.player_names[player-1])
    opposing_player_dict[f"Player {player}"] = Player(
        opposing_team.player_names[player-1])


# First innings
def batting():
    balls = 10
    wickets = len(user_team.player_names) - 1
    position = 0
    playing_batsmen = [user_player_dict["user_player1"], user_player_dict["user_player2"]]
    current_batsman = playing_batsmen[position]
    next_player_position = 0
    while balls > 0:
        if wickets > 0:
            user_team_run = int(input(f"Playing: {current_batsman.name}. Enter your run number: "))
            print()
            if user_team_run > 6:
                while user_team_run > 6:
                    user_team_run = int(input("You cannot enter number larger than 6"))
            run = randint(0, 6)
            if run != user_team_run:
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
                wickets -= 1
                if wickets > 0:
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
        else:
            print(f"Damn! Your players have all been out with {balls} balls left")
            balls = 0

        sleep(1)
        balls -= 1

    print()
    sleep(1)


    # Shows the scores of the players who got to play and score anything above zero in the innings.
    # And also calculating total team run
    for player_name in user_player_dict:
        for value in user_player_dict[player_name].player_info_dict.values():
            if value > 0:
                print(user_player_dict[player_name].player_info_dict)
                user_team.team_score(value)
    print()
    sleep(0.5)
    # Displaying team total run
    print(user_team.total_team_run)


def balling():
    balls = 12
    wickets = len(opposing_team.player_names) - 1
    position = 0
    playing_batsmen = [opposing_player_dict["Player 1"], opposing_player_dict["Player 2"]]
    current_batsman = playing_batsmen[position]
    next_player_position = 0
    while balls > 0:
        if wickets > 0:
            user_team_ball = int(input("Enter your ball number: "))
            print()
            while user_team_ball > 6:
                user_team_ball = int(input("Unless you don't want the opponent to get out, keep doin' your shitty stuff"))
            run = randint(0, 6)
            if run != user_team_ball:
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
                wickets -= 1
                if wickets > 0:
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
        else:
            print(f"The opponent is all out with {balls} balls left")
            balls = 0


        sleep(1)
        balls -= 1

    print()
    sleep(1)
    
    for player_name in opposing_player_dict:
        for value in opposing_player_dict[player_name].player_info_dict.values():
            if value > 0:
                print(opposing_player_dict[player_name].player_info_dict)
                opposing_team.team_score(value)

    print()
    sleep(0.5)
    print(opposing_team.total_team_run)


if user_team.playing == "Batting":
    batting()
else:
    balling()
    

first_innings_done = True


# Second innings
print()
sleep(1)
print("The first innings was done. We will now proceed to the next innings")


balls = 15

if first_innings_done:
    user_team.playing = "Balling" if user_team.playing == "Batting" else "Batting"
    opposing_team.playing = "Batting" if opposing_team.playing == "Balling" else "Balling"

    # Staring innings
    if user_team.playing == "Balling":
        balling()
    else:
        batting()


print()
sleep(1)
print(user_team.total_team_run)
sleep(1)
print(opposing_team.total_team_run)

# Let's see who won
user_team_won = True if user_team.total_team_run[
    user_team.team_name] > opposing_team.total_team_run[opposing_team.team_name] else False

sleep(1)
if user_team_won == True:
    print(
        f"Congrats! Your team won by {user_team.total_team_run[user_team.team_name] - opposing_team.total_team_run[opposing_team.team_name]} runs")
else:
    print(
        f"Better luck next time! You lost by {opposing_team.total_team_run[opposing_team.team_name] - user_team.total_team_run[user_team.team_name]} runs")
