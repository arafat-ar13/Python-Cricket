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
8) When batting, you are asked to enter an integer number. If your number matches the random number that the opposing bowler creates when bowling, your current batsman gets out and is permanently removed from the playing field and your next batsman will come to play. If they don't match, then your current batsman will score the number you have given.
9) During batting, for either teams, if the current batsman scores an odd number, the player gets switched and the next player becomes the current batsman.
10) After an over, the player gets changed.
11) When batting, in the second innings, if a team surpasses their target, they are immediately declared winners and the game will stop.

# Bowling rules
12) When bowling, you are again asked to enter an integer number. If your number matches the random number that the opposing batsman scores, the current opposing batsman gets out and is permanently replaced by another player. But if they don't match, the opposing batsman will score the run that he/she random-created.

# Recent updates
I want to congratulate myself for all the implementations I have made to this game recently. Those include:
* Introducing Score Comments! Now, if the user scores different runs, different messages will be displayed. For example, if you score 4 runs, an appropriate message will be displayed!
* Fixed the bug regarding the "Surrender" feature. Now, during batting the "Surrender" feature will stop your batting innings and start the opponent's batting or if you are batting in the second innings then your batting will cease. But during bowling, the case is different. Whichever innings you are bowling in, if you surrender, you will most definitely lose the match.
* Made internal changes to match the real game of Cricket. Now, after the game and appropriate "win" message will be displayed that will completely match the real Cricket game's messages.
* When someone from the opponent team gets out during their batting innings, the next batsman will always be the current batsman.

# Future plans
## Updates
* Introduce "Wicket Comments" as well.


# Happy playing!
