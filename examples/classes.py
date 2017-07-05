#Example of using classes
#Commented since I need to learn

class Song(object): #A class tells python to make a new type of thing, the object is any instance of something (an instance is what you get when you tell python to create a class)

	def __init__(self, lyrics):	#The __init__ method represents a constructor, when an object is created it gets passed to this method
		self.lyrics = lyrics	#The self variable represents the instance of the object being accessed

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(['Happy birthday to you',	#Set happy_bday to an instance of class Song
				   'I dont want to get sued',
				   'So I\'ll stop right there'])

bulls_on_parade = Song(['This is another song',
						'I should have typed out'])

happy_bday.sing_me_a_song()	#From happy_bday get the sing_me_a_song funciton and call it with parameters self
bulls_on_parade.sing_me_a_song()
