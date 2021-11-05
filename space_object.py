import math
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

    def turn_left(self):
        if self.obj_type == "space_ship" & self.x >=0 :
            self.x -= 10
        elif self.obj_type == "bullet" :
            pass
        elif self.obj_type == "asteroid_small" :
            pass
        elif self.obj_type == "asteroid_large" :
            pass
            
    def turn_right(self):
        
        # Enter your code here
        if self.obj_type == "space_ship" & self.x <= gui.width :
            self.x += 10
        elif self.obj_type == "bullet" :
            pass
        elif self.obj_type == "asteroid_small" :
            pass
        elif self.obj_type == "asteroid_large" :
            pass
    def move_forward(self):
        
        # Enter your code here
        if self.obj_type == "space_ship" & self.y >0 :
            self.y -= 10
        elif self.obj_type == "bullet" & self.y <= self.spaceship.y & self.y >= 0 :
            self.y -= 10
        elif self.obj_type == "asteroid_small" :
            pass
        elif self.obj_type == "asteroid_large" : 
            pass
        # 3 truong hop s

        pass

    def get_xy(self):
        
        # Enter your code here

        return (self.x, self.y)

    def collide_with(self,other):
        offset_x = self.x - other.x
        offset_y = self.y - other.y
        return self.mask.overlap(other.mask, (offset_x, offset_y)) !=None
        # Enter your code here
        d = math.sqrt ((self.x-other.x)**2 + (self.y - other.y)**2)
         
    def bullet_move (self, speed ) :
        pass
    def __repr__(self):
        
        # Enter your code here
        # khong can phai viet 
        return "TODO"
    
    # You can add additional methods if required
