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

# Recent updates
I want to congratulate myself for all the implementations I have made to this game recently. Those include:
* You can now play with as many players as you intend. Bring in a thousand people and my game will also create a thousand players of its own to show you who's the boss :) 
* I have implemented a system that takes control when all your players are out and you still have balls left. You will cease to bat and the next innings will start.
* After each innings, the program will show a list of the players who have scored. For example, if you bat first and your players have scored well, after your batting is done, the program will show which players have scored. If you have any player who hasn't scored anything, he/she will not be shown. This also works for when the opposing team is batting.
* Made the game fully fledged and playable.

# Future upgrades
* Make an update for when both the teams score the same run. In which case, a special session will begin with only 6 balls.
* For now, suppose you are batting after the opposing team and you surpass your target, you still have to wait for the balls to finish. After the second innings is done, then you can see that you have won. This is same for when the opponent is batting after you. In a future update, I will fix this and make sure that the game ends and the winner is declared whenever a team surpasses their target.

# Happy playing!
