class Hero(object):
	def __init__(self):
		self.name = "Connie"

# must pass self for self.name to be accessible
def cheer_hero(self):
	print "Fight hard, " + self.name;


