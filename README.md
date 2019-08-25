# Python-Cricket
A text-based cricket game with some sick features 

Run cricket.py on any text editor to get started

# How to play
1) Tell the game your team name and your player name.
2) [OPTIONAL] Tell the game the name of the opponent team. If you deny this option, opponent team will simply be named "Opposing Team"
3) Based on your number of players, the game will auto-create the EXACT same number of players to match your team. So, it's quite scalable.
4) You enter your toss preference.
5) If you win, you get to choose to bat or ball.
6) If you lose, the opponent will randomly choose bat or ball.
7) In any case, whatever you get, the opponent will always get the opposite of that. For e.g, if you get to bat, the opponent will be bowling.

# Batting rules
7) When batting, you are asked to enter an integer number. If your number matches the random number that the opposing bowler creates when bowling, your current batsman gets out and is permanently removed from the playing field and your next batsman will come to play. If they don't match, then your current batsman will score the number you have given.
8) During batting, for either teams, if the current batsman scores an odd number, the player gets switched and the next player becomes the current batsman.
9) After an over, the player gets changed.
10) When batting, in the second innings, if a team surpasses their target, they are immediately declared winners and the game will stop.

# Bowling rules
11) When bowling, you are again asked to enter an integer number. If your number matches the random number that the opposing batsman scores, the current opposing batsman gets out and is permanently replaced by another player. But if they don't match, the opposing batsman will score the run that he/she random-created.

# Recent updates
I want to congratulate myself for all the implementations I have made to this game recently. Those include:
* Reduced lines of code by over 30% and still produce same results but even better as this allowed fewer tweaks to get more job done.
* Early cessation of game when a team surpasses their target is now live! Whenever any team (you or the computer) bats in the second innings and chases and surpasses their target with balls and wickets left, the game will stop and the winner will be declared immediately.
* Implemented a "over" system. Now overs have replaced balls. Each over consists of 6 balls and unlike before, the user gets to choose how many overs they wish to play. And after each over, the player gets changed. But player remains same if he/she scored odd run (just like in real Cricket game)
* Added an optional option for users to name the opponent team to their liking. If they wish to not play against any specific team, my game will automatically name the oppoent team "Opposing Team". (So creative, right?)


# Future plans
* The order of your players is what you have fed my game when setting up your players and that is unchangable, for now. In the future, I will include options for you (the user) to choose which two players to send to bat first and when someone gets out, you will again get to choose which batsman to send next. This will be the next big update. (It'll be quite not-so-easy tbh!)
* No one really quite likes or gets impressed by a text-based game (or any program for that matter) and I am sorry but I just don't know much GUI programming yet. So, in the future, I will include an option to autoplay when the user is batting or bowling. Happy now?
* Now, when any team wins, the basic text that gets displayed is "Team A won by [run] runs". I wish to change that someday to reflect the real Cricket game where they say "Team A won by [wicket] wickets" or "Team B won by [run] runs". That's a complex thing to implement and so will take a while. (This feature is minor and will get less attention)


# Happy playing!
