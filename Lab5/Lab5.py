from turtle import Turtle,colormode
import random
class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.size = size
		self.shape=shape
		
	def random_color(self):
		r=self.random.randint(0,256)
		g=self.random.randint(0,256)
		b=self.random.randint(0,256)
		self.color(r,g,b)

Square1=Square(30)
Square.random_color()

		
class Hexagon (turtle):
	def __init__(self, size,shape):
		Turtle.__init__(self)
		self.shapesize(size)
		turtle.shape("Hexagon",(50,50),(70,50),(90,25),(70,0),(50,0),(30,25))
class color(Hexagon):
	def __init__(self, color):
		turtle(color, self).__init__()
		self.color = color

class speed(Hexagon):
	def __init__(self, speed):
		turtle(speed, self).__init__()
		self.speed = speed

class speed(Hexagon):
	def __init__(self, speed):
		turtle(speed, self).__init__()
		self.speed = speed



		


			
			
