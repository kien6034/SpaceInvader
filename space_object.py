import math

from pygame import constants
import config
import gui

class SpaceObject:
    def __init__(self, x, y, radius, angle, obj_type, id):
        self.x = x
        self.y = y
        self.radius = radius 
        self.angle = angle
        self.obj_type = obj_type
        self.id = id 

        self.range = 0 # for bullet 
        

    def move_forward(self):
        obj_speed = config.speed[self.obj_type]
            
        dx = math.cos(math.radians(self.angle))
        dy = math.sin(math.radians(self.angle))

        self.x += dx * obj_speed
        self.y -= dy * obj_speed


    def turn_left(self):    
       self.angle +=config.angle_increment
        
            
    def turn_right(self):
        self.angle -= config.angle_increment
            
       
    def get_xy(self):
        return (self.x, self.y)

    def collide_with(self,other):
        offset_x = self.x - other.x
        offset_y = self.y - other.y
        
        d = math.sqrt(offset_x**2 + offset_y ** 2)
        return d <= (self.radius + other.radius)
       
        
    def __repr__(self):
        
        # Enter your code here
        # khong can phai viet 
        return "TODO"
    
    # You can add additional methods if required
