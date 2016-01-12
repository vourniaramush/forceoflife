"""
This module contains the races relating to the world.
Its use is mainly during the character creation process.


Selectable Races:

Human:
Werewolves: subject to unlock
Veela: subject to unlock
Centaurs: subject to unlock
Giants: subject to unlock
goblins: subject to unlock
house-elves: subject to unlock

sub-races of human/half-vampire/half-werewolf/half-giants

pure-blood:
half-blood:
muggle-born:
non-magical(muggle):
squib: subject to unlock
"""

from world.archetypes import Archetype

class RaceException(Exception):
	"""Base exception class for races module"""
	def __init__(self, msg):
		self.msg = msg

ALL_RACES = ('Human', 
		     'Werewolf', 'half-werewolf',
		     'Veela', 'half-vampire',
		     'Giants', 'half-giants',
		     'goblins', 'half-goblin',
		     'Centaurs', 'house-elves')

ALL_SUB_RACES = ('pure-blood', 'half-blood', 'muggle-born', 'squib', 'non-magical')
