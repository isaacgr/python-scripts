# Can change the meaning of an operator depending on the operands used
# ex. the + can add numbers, concatenate strings and merge lists

class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

#p1 = Point(2,3)
#p2 = Point(-1,2)

# now doing p1+p2 wont work, since python doesnt know how to add two Point objects together
# Can teach this to python using operator overloading

# The __init__ function gets called everytim we create a new object of that class
# If we define the __str__ function in our class we can control how it gets printed

	def __str__(self):
		return "({0}, {1})".format(self.x, self.y)

#p1 = Point(2,3)
#p2 = Point(-1,2)

#print(p1)	# now we can print p1, since the str method is invoked when this function is used

# Python is internally doing p1.__str__()

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Point(x,y)

p1 = Point(2,3)
p2 = Point(-1,2)

print(p1+p2)	# this calls p1.__add__(p2), which is Point.__add__(p1,p2)
