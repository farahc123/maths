import math

class Circle:
  def __init__(self, radius):
    self.radius=float(radius)

  def area(self):
    area= (self.radius**2)*math.pi
    return round(area, 2)

  def perimeter(self):
      return round(2*self.radius*math.pi, 2)

my_circle=Circle(4)
print(my_circle.area())
print(my_circle.perimeter())
