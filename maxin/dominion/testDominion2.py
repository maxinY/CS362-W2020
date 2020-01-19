# -*- coding: utf-8 -*-
"""
Created on Thur January 16 2020

@author: Xinyu Ma
"""
import testUtility
import Dominion
import random
from collections import defaultdict

#Get player names
#for this test scenario, i am changing the number of player to 5
player_names = ["Annie","*Ben","*Carla","*Duke","*Emily"]

#number of curses and victory cards
nV = testUtility.num_victory(player_names)
nC = testUtility.num_curse(player_names)

#define box
box = testUtility.box_data(nV)
#define supply
supply = testUtility.supply_data(nV, nC,box,player_names)

players = testUtility.get_players(player_names)
#Play the game
testUtility.play_game(supply,players)
#final score
testUtility.score(players)
