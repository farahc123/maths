class Rectangle:
  def __init__(self, width, height):
    self.width=float(width)
    self.height=float(height)

  def area(self):
    return self.width*self.height

  def perimeter(self):
      return 2* (self.width+self.height)

  def is_square(self):
      return self.width==self.height

my_rect=Rectangle(4,5)
print(my_rect.area())
