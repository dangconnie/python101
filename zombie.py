# : in python is {} in JS
# think of self in Python as "this" in JS

class Zombie(object):
	# define this thing's setup (remember ES5 constructors in JS??)
	def __init__(self, speed, strength, hunger, weapon, health):
		self.speed = speed;
		self.strength = strength;
		self.hunger = hunger;
		self.weapon = weapon;
		self.health = health;
		self.type = "zombie";

# we've just created a zombie idea, we actually need to make this! RIght now, it does nothing.
# zombie_object = Zombie (6,8,19,'bat',15); 

# . notation is used for objects, so we do print zombie_object.speed; to see speed.
# print zombie_object.speed;

# in dicitonaries, you would use print zombie_object['speed']; to see speed

# displays all about this object!
# print dir(zombie_object);

# much nicer way to see all:
# print vars(zombie_object);
