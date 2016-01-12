"""
Archetypes


"""

from world.rulebook import roll_max


class ArchetypeException(Exception):
	def __init__(self, msg):
		self.msg = msg

VALID_ARCHETYPES = ()

PRIMARY_TRAITS = ('Strength', 'Perception', 'Intelligence',
				  'Dexterity', 'Charisma', 'Vitality', 'Magic')

SECONDARY_TRAITS = ('Health', 'Stamina Points', 'Movment Points', )