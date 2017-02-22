# import the entire file with a .py extension
import zombie
# from zombie import Zombie
import hero

# Make a zombie object from the class
zombie_object = zombie.Zombie (6,8,19,'bat',15); 

# ugly version of print all
# print dir(zombie_object);

# print vars(zombie_object);

# make a hero object from the hero class
heroObject = hero.Hero();
# print vars(hero);
hero.cheer_hero(heroObject);
