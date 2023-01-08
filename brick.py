#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import gameConfig


class Brick(object):
    # This class is making bricks randomly.

    def __init__(self, Game_obj):
        self.level = Game_obj.level
        self.Wallmade = True
        self.Enemymade = False
    ''' return level value '''

    def get_level(self):
        return self.level

    '''set level game value'''

    def set_level(self):
        self.level += 1

    ''' Made bricks amd enemy '''

    def entity_build(self):
        if (self.Wallmade):
            # print("gulshan")
            for x in range(4, gameConfig.Length - 4, 2):
                for y in range(6, gameConfig.Width - 6, 4):
                    m = random.randint(0, 1)
                    n = random.randint(0, 1)
                    o = random.randint(0, 1)
                    if (m and n and o and gameConfig.global_arr[x][y] == ' '):
                        gameConfig.setbrick.append([x, y])
            self.Wallmade = False

            # making enemy randomly
            if (self.Enemymade):
                del gameConfig.enemybin2[:]
                p = self.set_level()
                q = self.get_level()
                # print(q)
                for i in range(0, q + 3, 1):
                    gameConfig.enemybin2.append(
                        random.choice(gameConfig.setbrick))
                    gameConfig.setbrick.remove(
                        random.choice(gameConfig.setbrick))
                self.Enemymade = False
                # gameConfig.Enemymade = False
                # print(len(gameConfig.enemybin2))....

        for x in gameConfig.setbrick:
            for y in range(0, 4, 1):
                gameConfig.global_arr[x[0] + 1][y + x[1]] = '%'
                gameConfig.global_arr[x[0]][y + x[1]] = '%'
