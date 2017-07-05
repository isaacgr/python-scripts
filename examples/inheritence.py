# Inheritence enables us to define a class that takes all the functionality from a parent class and allows us to add more

#Define a new class with little or no modification to an existing class
#The new class is called the derived (or child) class and the one which it inherits attributes is called the base (or parent) class

# class BaseClass:
#	...
# class DerivedClass(BaseClass):
#	...

class Polygon:
	def __init__(self, no_of_sides):
		self.n = no_of_sides
		self.sides = [0 for i in range(no_of_sides)]

	def inputSides(self):
		self.sides = [float(input("Enter side " +str(i+1) +" : ")) for i in range(self.n)]

	def dispSides(self):
		for i in range(self.n):
			print("Side", i+1, "is", self.sides[i])

# The above class has data attributes to store the number of sides, n, and the magnitude of each side as a list, sides

# Can create a new class which inherits from polygon
# This makes all the attributes available in polygon available to the new class

class Triangle(Polygon):
	def __init__(self):
		Polygon.__init__(self,3)
	
	def findArea(self):
		a, b, c = self.sides
		s = (a + b + c)/2
		area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
		print('The area of the triangle is %0.2f' %area)
