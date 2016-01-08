"""
Archetypes

Human:
Werewolves: subject to unlock
Veela: subject to unlock
Centaurs: subject to unlock
Giants: subject to unlock
goblins: subject to unlock
house-elves: subject to unlock
"""

from world.rulebook import roll_max


class ArchetypeException(Exception):
	def __init__(self, msg):
		self.msg = msg

VALID_ARCHETYPES = ('Human', 'Werewolves', 'Veela', 'Centaurs', 
					'Giants', 'Goblins', 'House-elves')

PRIMARY_TRAITS = ('Strength', 'Perception', 'Intelligence',
				  'Dexterity', 'Charisma', 'Vitality', 'Magic')

SECONDARY_TRAITS = ('Health', 'Stamina Points', 'Movment Points', )