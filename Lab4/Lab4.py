Class Animal (object):
	def_init_(self,sound,name,favorit_color)
		self.sound=sound
		self.name=name
		self.age=age
		self.favorite_color=favorite_color
		self.favorit_food=favorit_food

	def eat(self,food):
		print("Yummy!!" + self.name + "is eating" + favorit_food)

	def description(self,color):
		print(self.name + "is" + self.age +"years old an loves the color"+self.favorite_color)

	def make_sound(self,sound):
		print(self.sound*3)

	def make_soundx(self,x):
		print(self.sound*x)

	c=animal("meaw","cat",4,"red")
	c.eat("fish")
	c.description()

	class person(object):
		"""docstring for person"""
		def __init__(self, name,age,city,gender):
			super(person, self).__init__()
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender

		def favorit_breakfast(self,breakfast):
			print(self.name + "is eating" + favorit_breakfast +"yummy:*")

		def favorit_song (self,song):
			print(self.name +"is listening to " + favorit_song)


	m=person("maya",15,"judayda","female")
	m.favorit_breakfast("cornflex")
	m.favorit_song("allofme")
	
