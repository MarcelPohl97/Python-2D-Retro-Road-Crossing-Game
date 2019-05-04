from tkinter import *
import random
import pygame
import time



WIDTH = 700
HEIGHT = 700
game_window = Tk()
game_window.title("Golden Treasure Hunter 2D Run Dodge Game")
game_root = Canvas(game_window, width=WIDTH, height=HEIGHT)
background = PhotoImage(file="jungletileset.png")
game_root.create_image(350, 300, image=background)
game_root.pack()



player_front = PhotoImage(file="npc4_bk22.png")
player_right = PhotoImage(file="npc4_rt2.png")
player_down = PhotoImage(file="npc4_fr2.png")
player_right_stop = PhotoImage(file="npc4_rt1.png")
player_left = PhotoImage(file="npc4_lf2.png")
player_left_stop = PhotoImage(file="npc4_lf1.png")
enemy_1_left = PhotoImage(file="enemyleft.png")
enemy_1_right = PhotoImage(file="enemyright.png")
enemy_1_up = PhotoImage(file="enemyup.png")
enemy_1_down = PhotoImage(file="enemydown.png")
treasure = PhotoImage(file="treasure.png")
sword_ = PhotoImage(file="sword1.png")
score = 0


class Enemy:
    def __init__(self):
        self.enemy_id = game_root.create_image(50, 100, image=enemy_1_down)

        self.speedx = random.randint(1,3)
        self.speedy = random.randint(1,3)

    def update(self):
        global game_loop
        game_root.move(self.enemy_id, self.speedx, self.speedy)
        pos = game_root.bbox(self.enemy_id)

        if pos[0] <= 0:
            self.speedx *= -1
            game_root.itemconfig(self.enemy_id, image=enemy_1_right)
        if pos[2] >= WIDTH:
            self.speedx *= -1
            game_root.itemconfig(self.enemy_id, image=enemy_1_left)
        if pos[1] <= 0:
            self.speedy *= -1
            game_root.itemconfig(self.enemy_id, image=enemy_1_down)
        if pos[3] >= HEIGHT:
            self.speedy *= -1
            game_root.itemconfig(self.enemy_id, image=enemy_1_up)

        x1, y1, x2, y2 = game_root.bbox(self.enemy_id)
        collision = game_root.find_overlapping(x1, y1, x2, y2)
        if player.player_id in collision:
            pass


class Player:
    def __init__(self):
        self.player_id = game_root.create_image(350, 650, image=player_down)
        self.speedx = 0
        self.speedy = 0
        game_root.bind_all("<KeyPress-Right>", self.move_right)
        game_root.bind_all("<KeyRelease-Right>", self.move_right_stop)
        game_root.bind_all("<KeyPress-Left>", self.move_left)
        game_root.bind_all("<KeyRelease-Left>", self.move_left_stop)
        game_root.bind_all("<KeyPress-Up>", self.move_up)
        game_root.bind_all("<KeyRelease-Up>", self.move_up_stop)
        game_root.bind_all("<KeyPress-Down>", self.move_down)
        game_root.bind_all("<KeyRelease-Down>", self.move_down_stop)


    def move(self):
        global pos
        pos = game_root.bbox(self.player_id)
        game_root.move(self.player_id, self.speedx, self.speedy)
        if pos[0] <= 0:
            game_root.move(self.player_id, 3, 0)
            game_root.itemconfig(self.player_id, image=player_right)
        if pos[2] >= WIDTH:
            game_root.move(self.player_id, -3, 0)
            game_root.itemconfig(self.player_id, image=player_left)
        if pos[1] <= 0:
            game_root.move(self.player_id, 0, 3)
            game_root.itemconfig(self.player_id, image=player_down)
        if pos[3] >= HEIGHT:
            game_root.move(self.player_id, 0, -3)
            game_root.itemconfig(self.player_id, image=player_front)


    def move_right(self, evt):

        self.speedx = 3
        game_root.itemconfig(self.player_id, image=player_right)

    def move_right_stop(self, evt):
        self.speedx = 0
        game_root.itemconfig(self.player_id, image=player_right_stop)

    def move_left(self, evt):
        self.speedx = -3
        game_root.itemconfig(self.player_id, image=player_left)

    def move_left_stop(self, evt):
        self.speedx = 0
        game_root.itemconfig(self.player_id, image=player_left_stop)

    def move_down(self, evt):
        self.speedy = 3
        game_root.itemconfig(self.player_id, image=player_down)

    def move_down_stop(self, evt):
        self.speedy = 0

    def move_up(self, evt):
        self.speedy = -3
        game_root.itemconfig(self.player_id, image=player_front)

    def move_up_stop(self, evt):
        self.speedy = 0


class Treasure:
    def __init__(self):
        self.treasure_id = game_root.create_image(350, 100, image=treasure)

    def treasure_collision(self):
        x1, y1, x2, y2 = game_root.bbox(self.treasure_id)
        collision = game_root.find_overlapping(x1, y1, x2, y2)
        if player.player_id in collision:
            game_root.delete(self.treasure_id)
            self.treasure_id = game_root.create_image(random.randint(100, 600), random.randint(100, 600), image=treasure)
            enemy_list.pop()



game_loop = True
enemy_list = []
for i in range(5):
    enemy_list.append(Enemy())

player = Player()
treasure_ = Treasure()

while game_loop:
    for enemy in enemy_list:
        enemy.update()
    player.move()
    treasure_.treasure_collision()
    game_window.update()
    game_window.after(6)




