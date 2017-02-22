from rpg_hero import Hero;
from rpg_monsters import Goblin;


hero = Hero();
enemies = [Goblin()];

for enemy in enemies:
	# Loop through all the bad guys in the enemies list
	print vars(enemy);
	# while hero.health > 0 and enemy.health > 0:
	while hero.alive() and enemy.alive():

		# Print off content
		print "What will you do?";
		print "1. Fight %s" % enemy.name
		print "2. Run away";
		# comma will keep input on the same line
		# get input from user
		print "> ",
		input = int(raw_input());
		if input == 1:
			# user chose to fight
			# subtract health from enemy = hero power
			# enemy.health -= hero.power;
			hero.attack(enemy);
		elif input == 2:
			# user chose to run away. break out of while loop
			break;
		else:
			# user made invalid choice
			print "Invalid choice. You're terrible. %r" % input
		if enemy.alive():
			# user has made their choice and now it's enemy's
			# if enemy has health. subtract his power from hero's health
			# hero.health -= enemy.power;
			enemy.attack(hero);
	if hero.alive():
		# we know they won because someone's health is less than 0
		print "You won! The %s is defeated" % enemy.name;
	else:
		# We know the hero lost because someone won and it's not him/her
		print "You were defeated by the ferocious %s" % enemy.name;
		 