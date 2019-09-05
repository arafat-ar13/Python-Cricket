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
* Finally added support for custom player choosing when deploying them. During the starting of the user's batting session, they will be asked to say which two players they want to send first. Then if someone gets out, the user will again have an option to choose which player to send next.
* Worked really hard on Lookout Parameters, which will cancel any abuse to the Custom Selection feature. Such include: you cannot send a player who have played before and neither can you enter a player's name who isn't in your team.
* For both teams during batting, view which player has been out. And for your (the user's) batting innings, when a player gets out, a list of all available players are displayed for better selection view. The list keeps decreasing as your players get out.


# Future plans
* After each over, get an option to do a number of things:
  * Continue with your usual bowling/batting.
  * If batting:
    * View a list of your remaining players
    * View your total team score
    * View your players' scores
    * View balls left
    * See how many wickets you have left
    * If second innings batting:
      * View your target
      * Surrender (vastly different from autoplay)
  * If bowling:
    * An option to autoplay the remaining balls
    * View opponent's total current run
    * View opponent's wickets left
    * View opponent's current batsmen
* No one really quite likes or gets impressed by a text-based game (or any program for that matter) and I am sorry but I just don't know much GUI programming yet. So, in the future, I will include an option to autoplay the whole bowling innings. Happy now?
* Now, when any team wins, the basic text that gets displayed is "Team A won by [run] runs". I wish to change that someday to reflect the real Cricket game where they say "Team A won by [wicket] wickets" or "Team B won by [run] runs". That's a complex thing to implement and so will take a while. (This feature is minor and will get less attention)


# Happy playing!
