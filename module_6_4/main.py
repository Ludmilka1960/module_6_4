import math


class Figure:
    sides_count = 0
    def __init__(self,color:tuple[int,int,int],*sides,filled=False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color
    @staticmethod
    def __is_valid_color(r,g,b):
        valid_values = 0 <= r <= 255 and 0<= g <= 255 and 0 <= b <=255
        valid_types = isinstance(r,int) and isinstance(g,int) and isinstance(b,int)
        return valid_values,valid_types
    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color = r,g,b

    @staticmethod

    def __is_valid_sides(*sides):
        for side in sides :
            if not isinstance(side,int) or side<=0:
             return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self,*sides):
        if len(sides) == len(self.__sides):
            valid_sides = []
            for side in sides:
                if self.__is_valid_sides(side):
                    valid_sides.append(side)

            self.__sides = valid_sides


class Circle(Figure):
    sides_count = 1
    def __init__(self,color:tuple[int,int,int],length,filled=False):

        super().__init__(color,length,filled=filled)
        self.__radius = length/(2* math.pi)
    def __radius(self):
        return f'__radius{self_sides_count}'
    def get_square(self):
        return len(self) ** 2/(4*math.pi)


class Triangle(Figure):
    sides_count = 3
    def __init__(self,color:tuple[int,int,int],height,*side,filled=False):

        super().__init__(color, height, filled=filled)
        self.height = height

    def get_square(self):
        p = (len(self)/2)
        sides = self.get_sides()
        return (math.sqrt(p - sides[0]) * (p - sides[1]) * (p - sides[2]))



class Cube(Figure):
    sides_count = 12


    def __init__(self,color:tuple[int,int,int],side,filled=False):
        cube_sides = [side] * 12
        super().__init__(color, *cube_sides, filled=filled)

    def get_volume(self):
        return self.get_sides()[0]**3




circle1 = Circle((200,200,150),10)
cube1 = Cube((230,180,50),8)
triangle1 = Triangle((230,200,200),10,5)
cube2 = Cube((220,220,100),6,12)


circle1.set_color(60,165,60)
print(circle1.get_color())
cube1.set_color(330,13,200)
print(cube1.get_color())

cube1.set_sides(4,3,5,4,6)
print(cube1.get_sides())
print(cube2.get_sides())
circle1.set_sides(10)
print(circle1.get_sides())

print(len(triangle1))
print(len(circle1))

print(cube1.get_volume())
print(cube2.get_volume())






