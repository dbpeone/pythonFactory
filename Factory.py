class ShapeInterface:
  def draw(self):
    pass

class Circle(ShapeInterface):
  def Draw(self):
    print "Circle.draw"

class Square(ShapeInterface):
  def Square(self):
    print "Square.draw"

class ShapeFactory:
  @staticmethod
  def getShape(type):
    print type


