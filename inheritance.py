class Animal(object):
	def __init__(self, name):
		self.name = name;
		self.species = species;

	def speak(self):
		print self.name + " is making a noise.";

	def run(self):
		print self.name + " is running!";

animal1 = Animal("Mitze", "Alien");
animal1.speak();
animal1.run();


# Make a new class, instead of passing "object" or nothing, we pass the name of the parent clas.
# Class Dog is now a child class of Animal
class Dog(Animal): 
	def __init__(self, dogName):
		# to use parent properties, send something up to it. in this case, we sent up self and dogName to the parent class Animal to use the properties of the Animal class.
		# it's like when we send up this.props in a JS constructor
		Animal.__init__(self, dogName, "Dog");
		print self.name;
	def bark(self):
		print self.name + " is barking!";

dog = Dog("Fido");
dog.speak()
print dog.species