9/06/2018
Created By: Angelo Zhu
This game is not my original idea. 

Intructions:
	Press the arrow keys to move the numbers.
	Match the same number to create bigger numbers.
	The goal is to reach 2048!

Development:
	The game id split into three Python modules:
	game_mechanics.py: Controls all the functionality of the 
		game logic including movement, losing, matching,
		making new numbers, etc.
	game_visual.py: Uses the pygame library to make a gui for
		the game. Allows the game to be played on a 
		resizable window. Color codes the different numbers.
		Only functionality that is related to visual aspects
		of the game like centering a number in a cell is
		included in this module.
	2048_game.py: Receives user input on board size to play
		the game and uses the other two modules to run
		the game.
		