import math
import config

class SpaceObject:

    def __init__(self, x, y, radius, angle, obj_type, id):
        self.x = x
        self.y = y
        self.radius = radius 
        self.angle = angle
        self.obj_type = obj_type
        self.id = id 

    def turn_left(self):
        if self.obj_type == "":
            self.x -= 10
        elif self.obj_type == "asteroid":
            pass 

    def turn_right(self):
        
        # Enter your code here

        pass

    def move_forward(self):
        
        # Enter your code here

        # 3 truong hop 

        pass

    def get_xy(self):
        
        # Enter your code here

        return (self.x, self.y)

    def collide_with(self, other):
        
        # Enter your code here
        pass
    
    def __repr__(self):
        
        # Enter your code here
        # khong can phai viet 
        return "TODO"

    # You can add additional methods if required
