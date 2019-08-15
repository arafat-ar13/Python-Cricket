# Python-Cricket
A text-based cricket game with some sick features 

Run cricket.py on any text editor to get started

# How to play
1) Tell the game your team name and your player name. NOTE: For now the game only supports two players
2) Based on your player names, the game will auto-create two opposing players called "Player 1" and "Player 2"
3) You enter your toss preference
4) If you win, you get to choose to bat or ball
5) If you lose, the opponent will randomly choose bat or ball.
6) In any case, whatever you get, the opponent will always get the opposite of that. For e.g, if you get to bat, the opponent will be balling.

# Batting rules
7) When batting, you are asked to enter an integer number. If your number matches the random number that the opposing baller creates when balling, your current batsman gets no run. If they don't match, then your current batsman will score the number you have given.
8) During batting, for either teams, if the current batsman scores an odd number, the player gets switched and the next player becomes the current batsman.

# Balling rules
9) When balling, you are again asked to enter an integer number. If your number matches the random number that the opposing batsman scores, the current opposing batsman gets no run at all. But if they don't match, the opposing batsman will score the run that he/she random-created.

# Future upgrades
* Include as many players as the user intends and the opposing team will change to match the user team players.
* When including more players, a system has to be created for "out". Unlike a player switch during odd scores, the out will permanently remove the current batsman from the playing field and bring the next player.
* If all the players of a team gets out before the balls are completed, the team will cease to bat.

# Cheat sheet
When batting you can enter any integer number you want like 13 or 35 or even over a thousand. This is valid for this game because the baller will only generate random numbers from 0 to 6. So if you enter any number above that, they just won't match! (Will be fixing this real soon. Life ain't that easy!)
