from tkinter import *
import random
import pygame


class Game:
    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Golden Treasure Hunter")
        self.WIDTH = 700
        self.HEIGHT = 700
        self.pygame = pygame.init()
        self.images()
        self.score = 0
        self.window_size()
        self.x = 0
        self.y = 0
        self.loop = True
        self.pause = False
        self.enemy_coords()
        self.game_objects()
        self.gameroot.bind_all("<KeyPress-Right>", self.move_right)
        self.gameroot.bind_all("<KeyRelease-Right>", self.move_right_stop)
        self.gameroot.bind_all("<KeyPress-Left>", self.move_left)
        self.gameroot.bind_all("<KeyRelease-Left>", self.move_left_stop)
        self.gameroot.bind_all("<KeyPress-Up>", self.move_up)
        self.gameroot.bind_all("<KeyRelease-Up>", self.move_up_stop)
        self.gameroot.bind_all("<KeyPress-Down>", self.move_down)
        self.gameroot.bind_all("<KeyRelease-Down>", self.move_down_stop)
        self.play_gameloop_sound()
        self.gameloop()

    def play_gameloop_sound(self):
        pygame.mixer.music.load("game_loop_sound.mp3")
        pygame.mixer.music.play()

    def play_treasure_sound(self):
        pygame.mixer.music.load("treasure_sound.mp3")
        pygame.mixer.music.play()

    def play_loose_sound(self):
        pygame.mixer.music.load("loose_sound.mp3")
        pygame.mixer.music.play()

    def game_objects(self):
        self.enemy_dict = {}
        self.player = self.gameroot.create_image(350, 680, image=self.player_down)
        self.enemy_1 = self.gameroot.create_image(680, 350, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_1"] = self.enemy_1
        self.enemy_2 = self.gameroot.create_image(680, 450, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_2"] = self.enemy_2
        self.enemy_3 = self.gameroot.create_image(680, 550, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_3"] = self.enemy_3
        self.enemy_4 = self.gameroot.create_image(680, 650, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_4"] = self.enemy_4
        self.enemy_5 = self.gameroot.create_image(680, 250, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_5"] = self.enemy_5
        self.enemy_6 = self.gameroot.create_image(680, 150, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_6"] = self.enemy_6
        self.enemy_7 = self.gameroot.create_image(680, 50, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_7"] = self.enemy_7
        self.enemy_8 = self.gameroot.create_image(20, 350, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_8"] = self.enemy_8
        self.enemy_9 = self.gameroot.create_image(20, 450, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_9"] = self.enemy_9
        self.enemy_10 = self.gameroot.create_image(20, 550, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_10"] = self.enemy_10
        self.enemy_11 = self.gameroot.create_image(20, 650, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_11"] = self.enemy_11
        self.enemy_12 = self.gameroot.create_image(20, 250, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_12"] = self.enemy_12
        self.enemy_13 = self.gameroot.create_image(20, 150, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_13"] = self.enemy_13
        self.enemy_14 = self.gameroot.create_image(20, 50, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_14"] = self.enemy_14
        self.treasure = self.gameroot.create_image(350, 300, image=self.treasure_)

    def enemy_coords(self):
        self.enemy_x = -2
        self.enemy_x2 = -2
        self.enemy_x3 = -2
        self.enemy_x4 = -2
        self.enemy_x5 = -2
        self.enemy_x6 = -2
        self.enemy_x7 = -2
        self.enemy_x8 = 2
        self.enemy_x9 = 2
        self.enemy_x10 = 2
        self.enemy_x11 = 2
        self.enemy_x12 = 2
        self.enemy_x13 = 2
        self.enemy_x14 = 2

        self.enemy_y = 0
        self.enemy_y2 = 0
        self.enemy_y3 = 0
        self.enemy_y4 = 0
        self.enemy_y5 = 0
        self.enemy_y6 = 0
        self.enemy_y7 = 0
        self.enemy_y8 = 0
        self.enemy_y9 = 0
        self.enemy_y10 = 0
        self.enemy_y11 = 0
        self.enemy_y12 = 0
        self.enemy_y13 = 0
        self.enemy_y14 = 0

    def images(self):
        self.background = PhotoImage(file="jungletileset.png")
        self.player_front = PhotoImage(file="npc4_bk22.png")
        self.player_right = PhotoImage(file="npc4_rt2.png")
        self.player_down = PhotoImage(file="npc4_fr2.png")
        self.player_right_stop = PhotoImage(file="npc4_rt1.png")
        self.player_left = PhotoImage(file="npc4_lf2.png")
        self.player_left_stop = PhotoImage(file="npc4_lf1.png")
        self.enemy_1_left = PhotoImage(file="enemyleft.png")
        self.enemy_1_right = PhotoImage(file="enemyright.png")
        self.enemy_1_up = PhotoImage(file="enemyup.png")
        self.enemy_1_down = PhotoImage(file="enemydown.png")
        self.treasure_ = PhotoImage(file="treasure.png")

    def window_size(self):
        self.frame = Frame(self.root, relief="ridge", bd=10, bg="black")
        self.frame.pack()
        self.gameroot = Canvas(self.frame, width=self.WIDTH, height=self.HEIGHT)
        self.gameroot.create_image(350, 300, image=self.background)
        self.gameroot.pack()
        self.frame2 = Frame(self.root, relief="ridge", bd=10, bg="black")
        self.frame2.pack()
        self.gameroot_window = Canvas(self.frame2, width=self.WIDTH, height=50, bg="lightgrey")
        self.gameroot_window.pack()
        self.pause = Button(self.frame2, text="Pause", bg="lightgrey", bd=3, relief="ridge", command= lambda: self.pause_())
        self.pause.place(relx=0.02, rely=0.22, relwidth=0.15)
        self.unpause = Button(self.frame2, text="Unpause", bg="lightgrey", bd=3, relief="ridge", command=lambda: self.unpause_())
        self.unpause.place(relx=0.18, rely=0.22, relwidth=0.15)
        self.restart = Button(self.frame2, text="Restart", bg="lightgrey", bd=3, relief="ridge", command = lambda: self.restart_())
        self.restart.place(relx=0.34, rely=0.22, relwidth=0.15)
        self.exit = Button(self.frame2, text="Exit Game", bg="lightgrey", bd=3, relief="ridge", command= lambda: self.exit_())
        self.exit.place(relx=0.75, rely=0.22, relwidth=0.15)
        self.score_label = Label(self.frame2, text="Hunted Treasures : " + str(self.score), bd=3, relief="ridge", bg="lightgrey")
        self.score_label.place(relx=0.5, rely=0.215, relwidth=0.2, relheight=0.53)

    def overlaps(self, x1, y1, x2, y2):
        self.enemy_list = []
        self.e_object = self.gameroot.find_overlapping(x1, y1, x2, y2)
        for k,v in self.enemy_dict.items():
            if v in self.e_object:
                self.enemy_list.append(k)
        return self.enemy_list

    def enemy_collision1(self):
        self.gameroot.move(self.enemy_1, self.enemy_x, self.enemy_y)
        self.gameroot.move(self.enemy_2, self.enemy_x2, self.enemy_y2)
        self.gameroot.move(self.enemy_3, self.enemy_x3, self.enemy_y3)
        self.gameroot.move(self.enemy_4, self.enemy_x4, self.enemy_y4)
        self.gameroot.move(self.enemy_5, self.enemy_x5, self.enemy_y5)
        self.gameroot.move(self.enemy_6, self.enemy_x6, self.enemy_y6)
        self.gameroot.move(self.enemy_7, self.enemy_x7, self.enemy_y7)
        self.gameroot.move(self.enemy_8, self.enemy_x8, self.enemy_y8)
        self.gameroot.move(self.enemy_9, self.enemy_x9, self.enemy_y9)
        self.gameroot.move(self.enemy_10, self.enemy_x10, self.enemy_y10)
        self.gameroot.move(self.enemy_11, self.enemy_x11, self.enemy_y11)
        self.gameroot.move(self.enemy_12, self.enemy_x12, self.enemy_y12)
        self.gameroot.move(self.enemy_13, self.enemy_x13, self.enemy_y13)
        self.gameroot.move(self.enemy_14, self.enemy_x14, self.enemy_y14)

        self.enemy_1_pos = self.gameroot.bbox(self.enemy_1)
        self.enemy_2_pos = self.gameroot.bbox(self.enemy_2)
        self.enemy_3_pos = self.gameroot.bbox(self.enemy_3)
        self.enemy_4_pos = self.gameroot.bbox(self.enemy_4)
        self.enemy_5_pos = self.gameroot.bbox(self.enemy_5)
        self.enemy_6_pos = self.gameroot.bbox(self.enemy_6)
        self.enemy_7_pos = self.gameroot.bbox(self.enemy_7)
        self.enemy_8_pos = self.gameroot.bbox(self.enemy_8)
        self.enemy_9_pos = self.gameroot.bbox(self.enemy_9)
        self.enemy_10_pos = self.gameroot.bbox(self.enemy_10)
        self.enemy_11_pos = self.gameroot.bbox(self.enemy_11)
        self.enemy_12_pos = self.gameroot.bbox(self.enemy_12)
        self.enemy_13_pos = self.gameroot.bbox(self.enemy_13)
        self.enemy_14_pos = self.gameroot.bbox(self.enemy_14)

        self.x1, self.y1, self.x2, self.y2 = self.gameroot.bbox(self.player)

        if self.overlaps(self.x1, self.y1, self.x2, self.y2):
            self.pause = True
            self.loose_info = self.gameroot.create_text(350, 300, text="You Lost! Hunted Treasure points : " + str(self.score), font="Arial 20 bold", fill="White")
            self.loose_info2 = self.gameroot.create_text(350, 400, text="If u want to play again press Restart!", font="Arial 20 bold", fill="White")
            self.play_loose_sound()
        #Enemy_1
        if self.enemy_1_pos[0] <= 0:
                self.gameroot.move(self.enemy_1, 2, 0)
                self.enemy_x = 2
                self.enemy_y = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_1, image=self.enemy_1_right)

        if self.enemy_1_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_1, -2, 0)
            self.enemy_x = -2
            self.enemy_y = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_1, image=self.enemy_1_left)

        if self.enemy_1_pos[1] <= 0:
            self.gameroot.move(self.enemy_1, 0, 2)
            self.enemy_y = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_1, image=self.enemy_1_down)

        if self.enemy_1_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_1, 0, -2)
            self.enemy_y = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_1, image=self.enemy_1_up)

        #Enemy_2
        if self.enemy_2_pos[0] <= 0:
                self.gameroot.move(self.enemy_2, 2, 0)
                self.enemy_x2 = 2
                self.enemy_y2 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_2, image=self.enemy_1_right)

        if self.enemy_2_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_2, -2, 0)
            self.enemy_x2 = -2
            self.enemy_y2 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_2, image=self.enemy_1_left)

        if self.enemy_2_pos[1] <= 0:
            self.gameroot.move(self.enemy_2, 0, 2)
            self.enemy_y2 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_2, image=self.enemy_1_down)

        if self.enemy_2_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_2, 0, -2)
            self.enemy_y2 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_2, image=self.enemy_1_up)

        #Enemy_3
        if self.enemy_3_pos[0] <= 0:
                self.gameroot.move(self.enemy_3, 2, 0)
                self.enemy_x3 = 2
                self.enemy_y3 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_3, image=self.enemy_1_right)

        if self.enemy_3_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_3, -2, 0)
            self.enemy_x3 = -2
            self.enemy_y3 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_3, image=self.enemy_1_left)

        if self.enemy_3_pos[1] <= 0:
            self.gameroot.move(self.enemy_3, 0, 2)
            self.enemy_y3 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_3, image=self.enemy_1_down)

        if self.enemy_3_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_3, 0, -2)
            self.enemy_y3 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_3, image=self.enemy_1_up)

        #Enemy_4
        if self.enemy_4_pos[0] <= 0:
                self.gameroot.move(self.enemy_4, 2, 0)
                self.enemy_x4 = 2
                self.enemy_y4 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_4, image=self.enemy_1_right)

        if self.enemy_4_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_4, -2, 0)
            self.enemy_x4 = -2
            self.enemy_y4 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_4, image=self.enemy_1_left)

        if self.enemy_4_pos[1] <= 0:
            self.gameroot.move(self.enemy_4, 0, 2)
            self.enemy_y4 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_4, image=self.enemy_1_down)

        if self.enemy_4_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_4, 0, -2)
            self.enemy_y4 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_4, image=self.enemy_1_up)

        #Enemy_5
        if self.enemy_5_pos[0] <= 0:
                self.gameroot.move(self.enemy_5, 2, 0)
                self.enemy_x5 = 2
                self.enemy_y5 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_5, image=self.enemy_1_right)

        if self.enemy_5_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_5, -2, 0)
            self.enemy_x5 = -2
            self.enemy_y5 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_5, image=self.enemy_1_left)

        if self.enemy_5_pos[1] <= 0:
            self.gameroot.move(self.enemy_5, 0, 2)
            self.enemy_y5 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_5, image=self.enemy_1_down)

        if self.enemy_5_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_5, 0, -2)
            self.enemy_y5 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_5, image=self.enemy_1_up)

        #Enemy_6
        if self.enemy_6_pos[0] <= 0:
                self.gameroot.move(self.enemy_6, 2, 0)
                self.enemy_x6 = 2
                self.enemy_y6 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_6, image=self.enemy_1_right)

        if self.enemy_6_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_6, -2, 0)
            self.enemy_x6 = -2
            self.enemy_y6 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_6, image=self.enemy_1_left)

        if self.enemy_6_pos[1] <= 0:
            self.gameroot.move(self.enemy_6, 0, 2)
            self.enemy_y6 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_6, image=self.enemy_1_down)

        if self.enemy_6_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_6, 0, -2)
            self.enemy_y6 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_6, image=self.enemy_1_up)

        #Enemy_7
        if self.enemy_7_pos[0] <= 0:
                self.gameroot.move(self.enemy_7, 2, 0)
                self.enemy_x7 = 2
                self.enemy_y7 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_7, image=self.enemy_1_right)

        if self.enemy_7_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_7, -2, 0)
            self.enemy_x7 = -2
            self.enemy_y7 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_7, image=self.enemy_1_left)

        if self.enemy_7_pos[1] <= 0:
            self.gameroot.move(self.enemy_7, 0, 2)
            self.enemy_y7 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_7, image=self.enemy_1_down)

        if self.enemy_7_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_7, 0, -2)
            self.enemy_y7 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_7, image=self.enemy_1_up)

        #Enemy_8
        if self.enemy_8_pos[0] <= 0:
                self.gameroot.move(self.enemy_8, 2, 0)
                self.enemy_x8 = 2
                self.enemy_y8 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_8, image=self.enemy_1_right)

        if self.enemy_8_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_8, -2, 0)
            self.enemy_x8 = -2
            self.enemy_y8 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_8, image=self.enemy_1_left)

        if self.enemy_8_pos[1] <= 0:
            self.gameroot.move(self.enemy_8, 0, 2)
            self.enemy_y8 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_8, image=self.enemy_1_down)

        if self.enemy_8_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_8, 0, -2)
            self.enemy_y8 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_8, image=self.enemy_1_up)

        #Enemy_9
        if self.enemy_9_pos[0] <= 0:
                self.gameroot.move(self.enemy_9, 2, 0)
                self.enemy_x9 = 2
                self.enemy_y9 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_9, image=self.enemy_1_right)

        if self.enemy_9_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_9, -2, 0)
            self.enemy_x9 = -2
            self.enemy_y9 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_9, image=self.enemy_1_left)

        if self.enemy_9_pos[1] <= 0:
            self.gameroot.move(self.enemy_9, 0, 2)
            self.enemy_y9 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_9, image=self.enemy_1_down)

        if self.enemy_9_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_9, 0, -2)
            self.enemy_y9 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_9, image=self.enemy_1_up)

        #Enemy_10
        if self.enemy_10_pos[0] <= 0:
                self.gameroot.move(self.enemy_10, 2, 0)
                self.enemy_x10 = 2
                self.enemy_y10 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_10, image=self.enemy_1_right)

        if self.enemy_10_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_10, -2, 0)
            self.enemy_x10 = -2
            self.enemy_y10 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_10, image=self.enemy_1_left)

        if self.enemy_10_pos[1] <= 0:
            self.gameroot.move(self.enemy_10, 0, 2)
            self.enemy_y10 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_10, image=self.enemy_1_down)

        if self.enemy_10_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_10, 0, -2)
            self.enemy_y10 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_10, image=self.enemy_1_up)

        #Enemy_11
        if self.enemy_11_pos[0] <= 0:
                self.gameroot.move(self.enemy_11, 2, 0)
                self.enemy_x11 = 2
                self.enemy_y11 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_11, image=self.enemy_1_right)

        if self.enemy_11_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_11, -2, 0)
            self.enemy_x11 = -2
            self.enemy_y11 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_11, image=self.enemy_1_left)

        if self.enemy_11_pos[1] <= 0:
            self.gameroot.move(self.enemy_11, 0, 2)
            self.enemy_y11 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_11, image=self.enemy_1_down)

        if self.enemy_11_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_11, 0, -2)
            self.enemy_y11 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_11, image=self.enemy_1_up)

        #Enemy_12
        if self.enemy_12_pos[0] <= 0:
                self.gameroot.move(self.enemy_12, 2, 0)
                self.enemy_x12 = 2
                self.enemy_y12 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_12, image=self.enemy_1_right)

        if self.enemy_12_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_12, -2, 0)
            self.enemy_x12 = -2
            self.enemy_y12 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_12, image=self.enemy_1_left)

        if self.enemy_12_pos[1] <= 0:
            self.gameroot.move(self.enemy_12, 0, 2)
            self.enemy_y12 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_12, image=self.enemy_1_down)

        if self.enemy_12_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_12, 0, -2)
            self.enemy_y12 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_12, image=self.enemy_1_up)

        #Enemy_13
        if self.enemy_13_pos[0] <= 0:
                self.gameroot.move(self.enemy_13, 2, 0)
                self.enemy_x13 = 2
                self.enemy_y13 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_13, image=self.enemy_1_right)

        if self.enemy_13_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_13, -2, 0)
            self.enemy_x13 = -2
            self.enemy_y13 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_13, image=self.enemy_1_left)

        if self.enemy_13_pos[1] <= 0:
            self.gameroot.move(self.enemy_13, 0, 2)
            self.enemy_y13 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_13, image=self.enemy_1_down)

        if self.enemy_13_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_13, 0, -2)
            self.enemy_y13 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_13, image=self.enemy_1_up)

        #Enemy_14
        if self.enemy_14_pos[0] <= 0:
                self.gameroot.move(self.enemy_14, 2, 0)
                self.enemy_x14 = 2
                self.enemy_y14 = random.randint(-2, 2)
                self.gameroot.itemconfig(self.enemy_14, image=self.enemy_1_right)

        if self.enemy_14_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.enemy_14, -2, 0)
            self.enemy_x14 = -2
            self.enemy_y14 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_14, image=self.enemy_1_left)

        if self.enemy_14_pos[1] <= 0:
            self.gameroot.move(self.enemy_14, 0, 2)
            self.enemy_y14 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_14, image=self.enemy_1_down)

        if self.enemy_14_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.enemy_14, 0, -2)
            self.enemy_y14 = random.randint(-2, 2)
            self.gameroot.itemconfig(self.enemy_14, image=self.enemy_1_up)

    def treasure_collision(self):
        self.x1, self.y1, self.x2, self.y2 = self.gameroot.bbox(self.player)
        self.collision = self.gameroot.find_overlapping(self.x1, self.y1, self.x2, self.y2)
        self.treasure_coords = self.gameroot.bbox(self.treasure)

        if self.treasure in self.collision:
            print("Found the Treasure")
            self.play_treasure_sound()
            self.score += 1
            self.score_label.configure(text="Hunted Treasures : " + str(self.score))
            print(self.score)
            self.gameroot.delete(self.treasure)
            self.loop = False

            self.treasure = self.gameroot.create_image(random.randint(50,600), random.randint(50,600), image=self.treasure_)
            self.loop = True

    def move_player(self):
        self.gameroot.move(self.player, self.x, self.y)

        self.player_pos = self.gameroot.bbox(self.player)
        if self.player_pos[0] <= 0:
            self.gameroot.move(self.player, 2, 0)

        if self.player_pos[2] >= self.gameroot.winfo_width():
            self.gameroot.move(self.player, -2, 0)

        if self.player_pos[1] <= 0:
            self.gameroot.move(self.player, 0, 2)

        if self.player_pos[3] >= self.gameroot.winfo_height():
            self.gameroot.move(self.player, 0, -2)

    def gameloop(self):

        while self.loop == True:
            if self.pause == False:

                self.treasure_collision()
                self.enemy_collision1()
                self.move_player()
                self.root.update_idletasks()
                self.root.update()
                self.root.after(6)
            elif self.pause == True:

                self.treasure_collision()
                self.root.update_idletasks()
                self.root.update()
                self.root.after(6)

    def exit_(self):
        self.root.destroy()

    def pause_(self):
        self.pause = True

    def unpause_(self):
        self.pause = False

    def restart_(self):
        self.score = 0
        self.gameroot.delete(self.player)
        self.gameroot.delete(self.treasure)
        self.gameroot.delete(self.enemy_1)
        self.gameroot.delete(self.enemy_2)
        self.gameroot.delete(self.enemy_3)
        self.gameroot.delete(self.enemy_4)
        self.gameroot.delete(self.enemy_5)
        self.gameroot.delete(self.enemy_6)
        self.gameroot.delete(self.enemy_7)
        self.gameroot.delete(self.enemy_8)
        self.gameroot.delete(self.enemy_9)
        self.gameroot.delete(self.enemy_10)
        self.gameroot.delete(self.enemy_11)
        self.gameroot.delete(self.enemy_12)
        self.gameroot.delete(self.enemy_13)
        self.gameroot.delete(self.enemy_14)
        self.gameroot.delete(self.loose_info)
        self.gameroot.delete(self.loose_info2)

        self.loop = False
        self.enemy_1 = self.gameroot.create_image(680, 350, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_1"] = self.enemy_1
        self.enemy_2 = self.gameroot.create_image(680, 450, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_2"] = self.enemy_2
        self.enemy_3 = self.gameroot.create_image(680, 550, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_3"] = self.enemy_3
        self.enemy_4 = self.gameroot.create_image(680, 650, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_4"] = self.enemy_4
        self.enemy_5 = self.gameroot.create_image(680, 250, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_5"] = self.enemy_5
        self.enemy_6 = self.gameroot.create_image(680, 150, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_6"] = self.enemy_6
        self.enemy_7 = self.gameroot.create_image(680, 50, image=self.enemy_1_left)
        self.enemy_dict["self.enemy_7"] = self.enemy_7
        self.enemy_8 = self.gameroot.create_image(20, 350, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_8"] = self.enemy_8
        self.enemy_9 = self.gameroot.create_image(20, 450, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_9"] = self.enemy_9
        self.enemy_10 = self.gameroot.create_image(20, 550, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_10"] = self.enemy_10
        self.enemy_11 = self.gameroot.create_image(20, 650, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_11"] = self.enemy_11
        self.enemy_12 = self.gameroot.create_image(20, 250, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_12"] = self.enemy_12
        self.enemy_13 = self.gameroot.create_image(20, 150, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_13"] = self.enemy_13
        self.enemy_14 = self.gameroot.create_image(20, 50, image=self.enemy_1_right)
        self.enemy_dict["self.enemy_14"] = self.enemy_14
        self.treasure = self.gameroot.create_image(random.randint(50, 600), random.randint(50, 600), image=self.treasure_)
        self.player = self.gameroot.create_image(350, 680, image=self.player_down)
        self.score_label.config(text="Hunted Treasures : " + str(self.score))
        self.loop = True
        self.pause = False
        self.play_gameloop_sound()

    def move_right(self, evt):
        self.x = 2
        self.gameroot.itemconfig(self.player, image=self.player_right)

    def move_right_stop(self, evt):
        self.x = 0
        self.gameroot.itemconfig(self.player, image=self.player_right_stop)

    def move_left(self, evt):
        self.x = -2
        self.gameroot.itemconfig(self.player, image=self.player_left)

    def move_left_stop(self, evt):
        self.x = 0
        self.gameroot.itemconfig(self.player, image=self.player_left_stop)

    def move_down(self, evt):
        self.y = 2
        self.gameroot.itemconfig(self.player, image=self.player_down)

    def move_down_stop(self, evt):
        self.y = 0

    def move_up(self, evt):
        self.y = -2
        self.gameroot.itemconfig(self.player, image=self.player_front)

    def move_up_stop(self, evt):
        self.y = 0

Game()
