import math
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def set_width(self,value):
        self.width = value
        return self.width
    
    def set_height(self,value):
        self.height = value
        return self.height
    
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = math.sqrt(self.width ** 2 + self.height ** 2)
        return diagonal
    def __str__(self):
        return(f'Rectangle(width={self.width}, height={self.height})')

    def get_picture(self):
        lines = "*" * self.width
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        return(f'{lines}\n') * self.height
        
    def get_amount_inside(self,shape):
        x = self.width // shape.width
        y = self.height // shape.height
        return x * y

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        
    def set_width(self,side):
        self.width = side
        self.height = side
    
    def set_height(self,side):
        self.width = side
        self.height = side

    def set_side(self,side):
        self.width = side
        self.height = side

    def __str__(self):
        return(f'Square(side={self.width})')

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
rect.set_height(8)
rect.set_width(16)
print(rect.get_area())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
