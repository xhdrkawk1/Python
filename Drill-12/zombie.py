import random

import math

import game_framework

from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

from pico2d import *

import main_state



# zombie Run Speed

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm

RUN_SPEED_KMPH = 10.0  # Km / Hour

RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)

RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)

RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



# zombie Action Speed

TIME_PER_ACTION = 0.5

ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

FRAMES_PER_ACTION = 10





animation_names = ['Attack', 'Dead', 'Idle', 'Walk']





class Zombie:

    images = None



    def load_images(self):

        if Zombie.images == None:

            Zombie.images = {}

            for name in animation_names:

                Zombie.images[name] = [load_image("./zombiefiles/female/"+ name + " (%d)" % i + ".png") for i in range(1, 11)]



    def __init__(self):

        positions = [(43, 750), (1118, 750), (1050, 530), (575, 220), (235, 33), (575, 220), (1050, 530), (1118, 750)]

        self.patrol_positions = []

        for p in positions:

            self.patrol_positions.append((p[0], 1024 - p[1]))  # convert for origin at bottom, left

        self.patrol_order = 1

        self.target_x, self.target_y = None, None

        self.x, self.y = self.patrol_positions[0]

        self.load_images()

        self.dir = random.random() * 2 * math.pi  # random moving direction

        self.speed = 0

        self.timer = 1.0  # change direction every 1 sec when wandering

        self.frame = 0

        self.build_behavior_tree()

        self.ZombieHp =0

        self.font = load_font('ENCR10B.TTF', 16)



    def get_bb(self):

        # fill here

        return self.x - 50, self.y - 50, self.x + 50, self.y + 50



    def calculate_current_position(self):

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time

        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time





    def calculate_current_position2(self):

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        distance = (main_state.boy.x - self.x) ** 2 + (main_state.boy.y - self.y) ** 2

        if self.ZombieHp<main_state.boy.BoyHp and distance <=(PIXEL_PER_METER *8)**2:

            self.x -= self.speed * math.cos(self.dir) * game_framework.frame_time

            self.y -= self.speed * math.sin(self.dir) * game_framework.frame_time

        else:

            self.x += self.speed * math.cos(self.dir) * game_framework.frame_time

            self.y += self.speed * math.sin(self.dir) * game_framework.frame_time



    def wander(self):

        # fill here

        self.speed = RUN_SPEED_PPS

        self.calculate_current_position()

        self.timer -= game_framework.frame_time

        if self.timer < 0:

            self.timer += 1.0

            self.dir = random.random() * 2 * math.pi

        return BehaviorTree.SUCCESS



    def find_player(self):

        # fill here

        boy =main_state.get_boy()

        distance = (boy.x -self.x)**2 + (boy.y -self.y)**2

        if distance < (PIXEL_PER_METER *8)**2:

            self.dir = math.atan2(boy.y-self.y,boy.x-self.x)

            return  BehaviorTree.SUCCESS

        pass



    def move_to_player(self):

        # fill here

        self.speed = RUN_SPEED_PPS

        self.calculate_current_position2()

        return BehaviorTree.SUCCESS

        pass



    def get_next_position(self):

        # fill here

        self.target_x, self.target_y =self.patrol_positions[self.patrol_order % len(self.patrol_positions)]

        self.patrol_order += 1

        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)

        return BehaviorTree.SUCCESS

        pass



    def move_to_target(self):

        # fill here

        self.speed = RUN_SPEED_PPS

        self.calculate_current_position()

        distance = (self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2

        if distance < PIXEL_PER_METER * 8:

            return BehaviorTree.SUCCESS

        else:

            return BehaviorTree.RUNNING

        pass

    def Find_Ball(self):

        # fill here

        for Ball in main_state.balls:

            distance = (Ball.x - self.x) ** 2 + (Ball.y - self.y) ** 2
            self.dir = math.atan2(Ball.y - self.y, Ball.x - self.x)
            main_state.Section = 0
            return BehaviorTree.SUCCESS

        for BigBall in main_state.Bigballs:
            distance = (BigBall.x - self.x) ** 2 + (BigBall.y - self.y) ** 2
            self.dir = math.atan2(BigBall.y - self.y, BigBall.x - self.x)
            main_state.Section = 1
            return BehaviorTree.SUCCESS

        distance = ( main_state.boy.x - self.x) ** 2 + ( main_state.boy.y - self.y) ** 2
        self.dir = math.atan2( main_state.boy.y - self.y,  main_state.boy.x - self.x)
        main_state.Section = 2
        return BehaviorTree.SUCCESS



    def move_to_Ball(self):

        # fill here

        self.speed = RUN_SPEED_PPS

        self.calculate_current_position()

        return BehaviorTree.SUCCESS




    def build_behavior_tree(self):

        wander_node = LeafNode("Wander", self.wander)

        find_player_node = LeafNode("Find Player", self.find_player)

        move_to_player_node = LeafNode("Move to Player", self.move_to_player)

        chase_node = SequenceNode("Chase")



        find_ball_node= LeafNode("Find Ball",self.Find_Ball)

        move_to_ball_node = LeafNode("Move to Ball",self.move_to_Ball)

        Find_node = SequenceNode("FindBall")

        Find_node.add_children(find_ball_node,move_to_ball_node,find_player_node)

        self.bt = BehaviorTree(Find_node)











    def get_bb(self):

        return self.x - 50, self.y - 50, self.x + 50, self.y + 50



    def update(self):

        # fill here


        self.bt.run()





    def draw(self):

        self.font.draw(self.x - 60, self.y + 70, 'Zombie_HP: %d' % self.ZombieHp, (255, 255, 0))

        draw_rectangle(*self.get_bb())

        if math.cos(self.dir) < 0:

            if self.speed == 0:

                Zombie.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)

            else:

                Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)

        else:

            if self.speed == 0:

                Zombie.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)

            else:

                Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, 100, 100)



    def handle_event(self, event):

        pass