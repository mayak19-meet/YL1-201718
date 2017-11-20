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

		

			