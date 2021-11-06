from pygame import constants
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
        self.bullets_ls = []
        self.upcoming_asteroids = []

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
                self.maxFuel = self.fuel
            elif fields[0] == "asteroids_count":
                self.asteroids_count = int(fields[1])
            elif fields[0] == "bullets_count":
                self.bullets_count = int(fields[1])
            elif fields[0] == "upcoming_asteroids_count":
                self.upcoming_asteroids_count = int(fields[1])
            elif fields[0] == "asteroid_large":
                object_attributes = fields[1].split(",")
                obj = SpaceObject(float(object_attributes[0]), float(object_attributes[1]), config.radius[fields[0]], config.radius[fields[0]], float(object_attributes[2]), fields[0], int(object_attributes[3]))
                self.asteroids_ls.append(obj)
            elif fields[0] == "asteroid_small":
                object_attributes = fields[1].split(",")
                obj = SpaceObject(float(object_attributes[0]), float(object_attributes[1]), config.radius[fields[0]], config.radius[fields[0]], float(object_attributes[2]), fields[0], int(object_attributes[3]))
                self.asteroids_ls.append(obj)
            elif fields[0] == "upcoming_asteroid_small":
                object_attributes = fields[1].split(",")
                #TODO
                obj = SpaceObject(float(object_attributes[0]), float(object_attributes[1]), config.radius["asteroid_small"], config.radius["asteroid_small"], float(object_attributes[2]), "asteroid_small", int(object_attributes[3]))
                self.upcoming_asteroids.append(obj)
            elif fields[0] == "upcoming_asteroid_large":
                object_attributes = fields[1].split(",")
                #TODO
                obj = SpaceObject(float(object_attributes[0]), float(object_attributes[1]),config.radius["asteroid_large"], config.radius["asteroid_large"], float(object_attributes[2]), "asteroid_large", int(object_attributes[3]))
                self.upcoming_asteroids.append(obj)
            elif fields[0] == "spaceship":
                object_attributes = fields[1].split(",")
                self.spaceship = SpaceObject(float(object_attributes[0]), float(object_attributes[1]),config.radius[fields[0]],config.radius[fields[0]], float(object_attributes[2]), fields[0], int(object_attributes[3]))

    def export_state(self, game_state_filename):
        
        # Enter your code here
        
        pass

    def offscreen_handler(self, obj):
        #Handle offscreen cases of spaceship
        if obj.y <= 0:
            obj.y = self.height
            obj.x = self.width - obj.x
        elif obj.y >= self.height:
            obj.y = 0
            obj.x = self.width - obj.x
        
        
        if obj.x <= 0: 
            obj.x = self.width
            obj.y = self.height - obj.y
        
        elif obj.x >= self.width:
            obj.x = 0
            obj.y = self.height - obj.y

    def run_game(self):
        self.GUI.set_background(5, 100)
        pygame.display.update()
        
        while True: 
            pygame.time.delay(int(config.frame_delay * 1000))
            # 1. Receive player input
            thrust, left, right, bullet_event = self.player.action(self.spaceship, self.asteroids_ls, self.bullets_ls, self.fuel, self.score)
            
            # 2. Game Logic 
            # 2.1 Manoeuvre the spaceship as per the Player's input
            if left:
                self.spaceship.turn_left()
        
            if right:
                self.spaceship.turn_right()

            if thrust:
                self.spaceship.move_forward()
            
            self.fuel -= config.spaceship_fuel_consumption # Spaceship fuel consumption
        

            # 2.2 Update positions of asteroids
            for asteroid in self.asteroids_ls:
                asteroid.move_forward()
                self.offscreen_handler(asteroid)
            
            
            # 2.3 Update positions of bullet  
            # 2.3.1: launch a new bullet if instructed by Player
            if bullet_event:
                if self.fuel < config.shoot_fuel_threshold:
                    print("Cannot shoot due to low fuel")
                else:
                    bullet = SpaceObject(self.spaceship.x, self.spaceship.y, config.radius['bullet'], config.radius['bullet'] , self.spaceship.angle, "bullet",  len(self.bullets_ls))
                    self.bullets_ls.append(bullet)
                    self.fuel -= config.bullet_fuel_consumption

            for bullet in self.bullets_ls:
                #2.3.2: Remove expire bullet 
                if bullet.range == 150:
                    self.bullets_ls.remove(bullet)
                    continue

                #2.3.3: Update positon of bullets  
                bullet.move_forward()
                bullet.range += config.speed['bullet']
                self.offscreen_handler(bullet)

            # 2.4 Detect collisions 
            for asteroid in self.asteroids_ls:
                isCollide = False
                # 2.4.1: If a bullet collides with an asteroid 
                for bullet in self.bullets_ls:
                    if asteroid.collide_with(bullet):         
                        if asteroid.obj_type == "asteroid_small":
                            self.score += config.shoot_small_ast_score
                        elif asteroid.obj_type == "asteroid_large":
                            self.score += config.shoot_large_ast_score

                        print(f"Score: {self.score} \t [Bullet {bullet.id} has shot asteroid  {asteroid.id}]")
                        #remove the bullet 

                        isCollide = True 
                        self.bullets_ls.remove(bullet)

                        #remove the asteroid 
                        self.asteroids_ls.remove(asteroid) 

                #2.4.2: If the spaceship collides with an asteroid    
                if asteroid.collide_with(self.spaceship):
                    self.score += config.collide_score
                    print(f"Score: {self.score} \t [Spaceship collided with asteroid {asteroid.id}]")
                    self.asteroids_ls.remove(asteroid)
                    isCollide = True 
                    
                #2.4.3: Replenish asteroids
                if isCollide:
                    if len(self.upcoming_asteroids) == 0:
                        print("Error: no more asteroids available ")
                    else:
                        new_asteroid = self.upcoming_asteroids[0]
                        self.asteroids_ls.append(new_asteroid)
                        self.upcoming_asteroids.remove(new_asteroid)
                        self.upcoming_asteroids_count -= 1
                        print(f"Added asteroid {new_asteroid.id}")
            

            
            # 2.5 Deduct fuel for spaceship and bullets
            if self.fuel <= self.maxFuel * 0.75 and self.fuel > self.maxFuel * 0.5:
                print(f"75% fuel warning: {self.fuel} remaining")
            elif self.fuel <= self.maxFuel * 0.5 and self.fuel > self.maxFuel * 0.25:
                print(f"50% fuel warning: {self.fuel} remaining")
            elif self.fuel <= self.maxFuel * 0.25:
                print(f"25% fuel warning: {self.fuel} remaining")

            # 3. Draw the game state on screen using the GUI class
            self.GUI.update_frame(self.spaceship, self.asteroids_ls, self.bullets_ls, self.score, self.fuel)

            # Game loop should stop when:
            # - the spaceship runs out of fuel, or
            # - no more asteroids are available
            if self.fuel <= 0 or len(self.asteroids_ls) == 0:
                break
            

        # Display final score
        self.GUI.finish(self.score)

    # You can add additional methods if required
