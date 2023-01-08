import sys
from board import *
from gameConfig import *
import gameConfig
from bomberman import *
from getch import *
import bomb
from bomb import bomb_plant1
#from bomb import bomb_plant2
#from bomb import bomb_plant3
from bomb import bomb_plant4
import brick
import os
import time
import random
#from enemy import Enemy
from termcolor import colored

import time


#import algorithms
from algorithms import bfs
from algorithms import dfs
from algorithms import random_move
from IPython.display import clear_output

# This is the main game file where game is running &print game score & lives of bomberman
# Update bomb, enemies etc.
# print board and bricks in board

class Game:
    def __init__(self, level):
        self.level = level

Game_obj = Game(gameConfig.level)
#count_game_running = 1 #check if the game is working
tr = 0
brick_obj = brick.Brick(Game_obj)





#return the 'lose' player
def launch_the_game():

    global Game_obj, count_game_running, tr, brick_obj, bomb_bin1, bomb_bin4, obj1, obj4, bomb_plant1, bomb_plant4
    
    Game_obj = Game(gameConfig.level)
    count_game_running = 1 #check if the game is working
    tr = 0
    brick_obj = brick.Brick(Game_obj)
    
    while count_game_running != 0:
        
        if(obj1.lives <= 0):
            #print('player 1 lose')
            count_game_running = 0
            return 'player1'
        
        if(obj4.lives <= 0):
            #print('player 4 lose')
            count_game_running = 0
            return 'player4'
        
        print_board()
        
        def update_status(ch, obj):
            if(ch == 'up'):
                obj.remove()
                obj.up_Move()
                obj.curr()

            elif(ch == 'down'):
                obj.remove()
                obj.down_Move()
                obj.curr()

            elif(ch == 'left'):
                obj.remove()
                obj.left_Move()
                obj.curr()

            elif(ch == 'right'):
                obj.remove()
                obj.right_Move()
                obj.curr()
        
        #-----player1-----
        #ch = random_move.random_move()

        ch = random_move.random_move()
        #ch = input('please input player1 move\n')
        update_status(ch, obj1)
        
        if(ch == 'put'):
            if(len(bomb_bin1) == 0):
                bomb_bin1.append(bomb_plant1)
                bomb_bin1[0].set_coordinate()
                tr = int(time.time())
        #-----player1-----
        
        #-----player4-----
        ch = random_move.random_move()
        #ch = input('please input player4 move\n')
        update_status(ch, obj4)
        
        if(ch == 'put'):
            if(len(bomb_bin4) == 0):
                bomb_bin4.append(bomb_plant4)
                bomb_bin4[0].set_coordinate()
                tr = int(time.time())
        #-----player4-----
        
        time.sleep(0.5)

        #os.system('clear') # for linux
        #os.system('cls') # for windows powershell


def print_board():
    global obj1, obj4, brick_obj, tr, bp, bomb_bin1, bomb_bin4, global_arr
    #clear the terminal before printing new infos
    #os.system('clear') # for linux
    #os.system('cls') # for windows powershell
    clear_output(wait=True)
    
    #global flag1
    if(obj1.lives <= 0):
        #print('player 1 lose')
        return
        #loose()
        
    if(obj4.lives <= 0):
        #print('player 4 lose')
        return
        #loose()
        
    # os.system('tput reset')
    # if(len(enemybin)==0):
    # 	youwin()
    #print(colored("\t\t\t\t    BOMBERMAN \t\t\t\t\t", "green", attrs=["bold"]))
    bp.make_board()
    brick_obj.entity_build()
    
    #set the position here
    obj1.curr()
    obj4.curr()
    
    #setup_bomb_bin
    def setup_bomb_bin(bomb_bin):
        for i in bomb_bin:
            i.set_bomb()
    setup_bomb_bin(bomb_bin1)
    setup_bomb_bin(bomb_bin4)

    # bricks.Bricks()
    check_Game_Score()
    
    #print the maze
    print(len(global_arr), len(global_arr[0]), Length, Width)
    
    for i in range(Length):
        for j in range(Width):
            print(global_arr[i][j], end='')
        print()
    print(f'player1 live {obj1.lives}')
    print(f'player4 live {obj4.lives}')


def check_Game_Score():
    global bomb_plant1, bomb_plant4
    def search_bomb_bin(bomb_bin, bomb_plant, obj, reset_x, reset_y):    
        for entity in bomb_bin:
            explode_time = 3 + tr - int(time.time())
            if(explode_time >= 0):
                bomb_plant.start_counter(explode_time - 1)
                #bomb_plant2.start_counter(explode_time - 1)
                if(explode_time < 1):
                    bomb_plant.start_counter('B')
                    bomb_plant.explosion()
            elif(explode_time < 0):
                bomb_plant.explode()
                if(obj.hanged_bomber(entity.present_Coordiate_Bomb())):
                    obj.set_Pos(reset_x, reset_y)
                    obj.curr()
                del bomb_bin[:]
    
    search_bomb_bin(bomb_bin1, bomb_plant1, obj1, 2, 2)
    search_bomb_bin(bomb_bin4, bomb_plant4, obj4, 38, 74)

def reset_game():
    
    #for variables in gameConfig.py
    global bomb_bin1, bomb_bin4, dynamite_arr, setbomb, Wallmade, Enemymade, setbrick, score, bp, global_arr
    bomb_bin1.clear()
    bomb_bin4.clear()
    dynamite_arr = [['e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e']]
    setbomb = 0
    Wallmade = True
    Enemymade = True
    setbrick = []
    score = 0
    
    #for variables in bomberman.py
    global obj1, obj4
    obj1 = Bomberman(2, 2, 0, 3)
    obj4 = Bomberman(38, 74, 0, 3)
    
    #default bomb_plant
    global bomb_plant1, bomb_plant4
    bomb_plant1 = bomb.Bomb(obj1.x, obj1.y, obj1)
    #bomb_plant2 = Bomb(obj2.x, obj2.y, obj2)
    #bomb_plant3 = Bomb(obj3.x, obj3.y, obj3)
    bomb_plant4 = bomb.Bomb(obj4.x, obj4.y, obj4)
    
    #for variables in board.py
    bp = Board(Length, Width)
    
    #global count_game_running
    #count_game_running = 1
    
    #global arr
    #global_arr = []    

#os.system('cls')
#print(player_1_win)
#print(player_4_win)