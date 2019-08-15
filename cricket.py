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
        total_score = sum(score)
        self.total_team_run[self.team_name] += total_score


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
balls = 15
wickets = len(user_team.player_names) - 1

if user_team.playing == "Batting":
    position = 0
    playing_batsmen = [user_player_dict["user_player1"], user_player_dict["user_player2"]]
    current_batsman = playing_batsmen[position]
    while balls != 0:
        user_team_run = int(input("Enter your run number: "))
        run = randint(0, 6)
        if run != user_team_run:
            if user_team_run % 2 == 0:
                print(
                    f"Wow! {current_batsman.name} scored {user_team_run} runs")
                current_batsman.run(user_team_run)
            else:
                print(f"Wow! {current_batsman.name} scored {user_team_run} runs")
                position += 1
                if position > 1:
                    position = 0
                current_batsman.run(user_team_run)
                current_batsman = playing_batsmen[position] if current_batsman == playing_batsmen[position-1] else playing_batsmen[position-1]
        else:
            sleep(0.5)
            print("Shoot! Your number matched! Your player scored 0 runs!!")
            current_batsman.run(0)

        sleep(1)
        balls -= 1

    print()
    sleep(1)
    print(user_player_dict["user_player1"].player_info_dict)
    print(user_player_dict["user_player2"].player_info_dict)

else:
    current_batsman = opposing_player_dict["Player 1"]
    while balls != 0:
        user_team_ball = int(input("Enter your ball number: "))
        run = randint(0, 6)
        if run != user_team_ball:
            if run % 2 == 0:
                print("You missed!")
                sleep(0.5)
                print(f"Wow! {current_batsman.name} scored {run} runs")
                current_batsman.run(run)
            else:
                print("You missed!")
                sleep(0.5)
                print(f"Wow! {current_batsman.name} scored {run} runs")
                current_batsman.run(run)
                current_batsman = opposing_player_dict["Player 2"] if current_batsman == opposing_player_dict[
                    "Player 1"] else opposing_player_dict["Player 1"]
        else:
            sleep(0.5)
            print("You hit him! The opposing playing didn't score anything!!")
            current_batsman.run(0)

        sleep(1)
        balls -= 1

    print()
    sleep(1)
    print(opposing_player_dict["Player 1"].player_info_dict)
    print(opposing_player_dict["Player 2"].player_info_dict)

first_innings_done = True


# Second innings
print()
sleep(1)
print("The first session was done. We will now proceed to the next session")


balls = 15
wickets = len(user_team.player_names) - 1

if first_innings_done:
    user_team.playing = "Balling" if user_team.playing == "Batting" else "Batting"
    opposing_team.playing = "Batting" if opposing_team.playing == "Balling" else "Balling"

    # Staring innings
    if user_team.playing == "Balling":
        current_batsman = opposing_player_dict["Player 1"]
        while balls != 0:
            user_team_ball = int(input("Enter your ball number: "))
            run = randint(0, 6)
            if run != user_team_ball:
                sleep(0.5)
                print("You missed!")
                if run % 2 == 0:
                    print(f"Wow! {current_batsman.name} scored {run} runs")
                    current_batsman.run(run)
                else:
                    print(f"Wow! {current_batsman.name} scored {run} runs")
                    current_batsman.run(run)
                    current_batsman = opposing_player_dict["Player 2"] if current_batsman == opposing_player_dict[
                        "Player 1"] else opposing_player_dict["Player 1"]
            else:
                sleep(0.5)
                print("You hit him!")
                current_batsman.run(0)

            balls -= 1

        print()
        sleep(1)
        print(opposing_player_dict["Player 1"].player_info_dict)
        print(opposing_player_dict["Player 2"].player_info_dict)

    else:
        current_batsman = user_player_dict["user_player1"]
        while balls != 0:
            user_team_run = int(input("Enter your run number: "))
            run = randint(0, 6)
            if run != user_team_run:
                if user_team_run % 2 == 0:
                    print(
                        f"Wow! {current_batsman.name} scored {user_team_run} runs")
                    current_batsman.run(user_team_run)
                else:
                    print(
                        f"Wow! {current_batsman.name} scored {user_team_run} runs")
                    current_batsman.run(user_team_run)
                    current_batsman = user_player_dict["user_player2"] if current_batsman == user_player_dict[
                        "user_player1"] else user_player_dict["user_player1"]
            else:
                sleep(0.5)
                print("Shoot! You got hit!!")
                current_batsman.run(0)

            sleep(1)
            balls -= 1

        print()
        sleep(1)
        print(user_player_dict["user_player1"].player_info_dict)
        print(user_player_dict["user_player2"].player_info_dict)


user_team.team_score([user_player_dict["user_player1"].player_info_dict[user_player_dict["user_player1"].name],
                      user_player_dict["user_player2"].player_info_dict[user_player_dict["user_player2"].name]])
opposing_team.team_score([opposing_player_dict["Player 1"].player_info_dict[opposing_player_dict["Player 1"].name],
                          opposing_player_dict["Player 2"].player_info_dict[opposing_player_dict["Player 2"].name]])

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
