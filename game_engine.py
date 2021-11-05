import config
from space_object import SpaceObject
import pygame
import sys
import config
import time

class Engine:
    def __init__(self, game_state_filename, player_class, gui_class):
        self.import_state(game_state_filename)
        self.player = player_class()
        self.GUI = gui_class(self.width, self.height)

    def import_state(self, game_state_filename):
        # Enter your code here
        ## Read game state here 
        file1 = open(game_state_filename, "r")
        
        self.asteroids_ls = []

        while True:
            line = file1.readline()

            if not line:
                break

            fields = line.split()
            
            if fields[0] == "width":
                self.width = int(fields[1])
            elif fields[0] == "height":
                self.height = int(fields[1])
            elif fields[0] == "score":
                self.score = int(fields[1])
            elif fields[0] == "fuel":
                self.fuel = int(fields[1])
            elif fields[0] == "asteroids_count":
                self.asteroids_count = int(fields[1])
            elif fields[0] == "bullets_count":
                self.bullets_count = int(fields[1])
            elif fields[0] == "upcoming_asteroids_count":
                self.upcoming_asteroids_count = int(fields[1])
            elif fields[0] == "asteroid_large":
                object_attributes = fields[1].split(",")
                obj = SpaceObject(float(object_attributes[0]), float(object_attributes[1]), config.radius[fields[0]], float(object_attributes[2]), fields[0], int(object_attributes[3]))
                self.asteroids_ls.append(obj)
            elif fields[0] == "asteroid_small":
                object_attributes = fields[1].split(",")
                obj = SpaceObject(float(object_attributes[0]), float(object_attributes[1]), config.radius[fields[0]], float(object_attributes[2]), fields[0], int(object_attributes[3]))
                self.asteroids_ls.append(obj)
            elif fields[0] == "upcoming_asteroid_small":
                object_attributes = fields[1].split(",")
                #TODO
                obj = SpaceObject(float(object_attributes[0]), float(object_attributes[1]),20, float(object_attributes[2]), fields[0], int(object_attributes[3]))
            elif fields[0] == "upcoming_asteroid_large":
                object_attributes = fields[1].split(",")
                #TODO
                obj = SpaceObject(float(object_attributes[0]), float(object_attributes[1]),20, float(object_attributes[2]), fields[0], int(object_attributes[3]))
            elif fields[0] == "spaceship":
                object_attributes = fields[1].split(",")
                self.spaceship = SpaceObject(float(object_attributes[0]), float(object_attributes[1]),config.radius[fields[0]], float(object_attributes[2]), fields[0], int(object_attributes[3]))

    def export_state(self, game_state_filename):
        
        # Enter your code here
        
        pass

    def run_game(self):
        self.GUI.set_background(5, 100)
        pygame.display.update()

        while True: 
            pygame.time.delay(config.frame_delay)
            # 1. Receive player input
            thrust, left, right, bullet = self.player.action(self.spaceship, [], [], self.fuel, self.score)
            
            # 2. Process game logic
            if thrust:
                self.spaceship.move_forward()
            elif left:
                self.spaceship.turn_left()
            elif right:
                self.spaceship.turn_right()
            elif bullet:
                #Tạo bullet object vị trí tại vị trí của máy bay
                #
                pass 
        
            # 3. Draw the game state on screen using the GUI class
            self.GUI.update_frame(self.spaceship, self.asteroids_ls, [], self.score, self.fuel)

            # Game loop should stop when:
            # - the spaceship runs out of fuel, or
            # - no more asteroids are available
            pass
            

        # Display final score
        # self.GUI.finish(???)

    # You can add additional methods if required
