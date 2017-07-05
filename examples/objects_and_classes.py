# An object is simply a collection of data (variables) and methods (functions) that act on those data
# A class is a blueprint for the object

# An object is an instance of a class and the process of creating the object is called instantiation

# A class creates a new local namespace where all its attributes are defined (can be data or funcitons)

# As soon as we define a class, a new class object of the same name is created
# This allows us to access different attributes of the class as well as to instantiate new objects

class MyClass:
	"This is a docstring. I have created a new class"
	a = 10
	def func(self):
		print('Hello')

print(MyClass.a)

print(MyClass.func)	#MyClass.func is a function object (an attribute of a class)

print(MyClass.__doc__) #__doc__ is the docstring method

ob = MyClass()	#Instatiate a new object (create new object instance of that class)
print(ob)
print(ob.func)
ob.func()	#This should actually print 'Hello' since we are calling the function func() (method object)

# Whenever an object calls its method, the object itself is passed as the first argument (in this case 'self')
# So ob.func() translates to MyClass.func(ob)
# This is why the first argument of a function in a class must be self, otherwise you wont be able to instantiate a new object and then call a function of that class

print('\n')

# Class functions that begin with a __ are called special functions
# The __init__ function gets called whenever a new object of that class is instantiated
# These functions are also known as constructors, they are used to initialize all the variables

class ComplexNumber:
	def __init__(self, r=0, i=0):
		self.real = r
		self.imag = i

	def getData(self):
		print("{0}+{1}j".format(self.real, self.imag))

c1 = ComplexNumber(2,3)
c1.getData()

c2 = ComplexNumber(5)
c2.attr = 10	#Create a new attribute attr for c2

print((c2.real, c2.imag, c2.attr))
c2.getData()

# c1 does not have this attribute

# Any attribute of an object ca n be delted anytime, using the del statement

print('\n')

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
