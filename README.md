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
* Introducing Over Options! 
* Over Options are available for both batting and bowling sessions. The options are slightly different depending upon is it batting or bowling
innings or is it the first or second innings.
* Firstly during batting, after each over, you get the following options:
 * Continue with your usual bowling/batting.
 * View a list of your remaining players
 * View your total team score
 * View your players' scores
 * View balls left and wickets left
 * Surrender
 * If second innings batting:
   * View your target
* During balling the options are tweaked:
  * An option to autoplay the following over. Worked really hard on this feature. If you select autoplay, the following over will be played automatically and in the next Over Options you will get an option of "Manual play"! You can select that if you want to play manually again but if you don't then "Continue" will just let the game go on regardless of it's on autoplay or manual.
  * Surrender
  * View opponent's total current run
  * View opponent's wickets left
  * View opponent's current batsmen
* [INFO] Autoplay and surrender: Autoplay is only available when the user is bowling. This feature works by neglecting the user's ability to enter different ball numbers and rather random-generates a number from 0 to 6 and uses that number for the next ball. Whereas surrender will just straight-up finish the innings by making the balls zero while still retaining your or the opponent's current scores and other info.

# Future plans
* Now, when any team wins, the basic text that gets displayed is "Team A won by [run] runs". I wish to change that someday to reflect the real Cricket game where they say "Team A won by [wicket] wickets" or "Team B won by [run] runs". That's a complex thing to implement and so will take a while. (This feature is minor and will get less attention)


# Happy playing!
