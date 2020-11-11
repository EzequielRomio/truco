cards_dict = {
	'1 espada': 14,
	'1 basto': 13,
	'7 espada': 12,
	'7 oro': 11,
	'3 espada': 10,
	'3 oro': 10,
	'3 basto': 10,
	'3 copa': 10,
	'2 espada': 9,
	'2 oro': 9,
	'2 basto': 9,
	'2 copa': 9,
	'1 oro': 8,
	'1 copa': 8,
	'12 espada': 7,
	'12 oro': 7,
	'12 basto': 7,
	'12 copa': 7,
	'11 espada': 6,
	'11 oro': 6,
	'11 basto': 6,
	'11 copa': 6,
	'10 espada': 5,
	'10 oro': 5,
	'10 basto': 5,
	'10 copa': 5,
	'7 basto': 4,
	'7 copa': 4,
	'6 espada': 3,
	'6 oro': 3,
	'6 basto': 3,
	'6 copa': 3,
	'5 espada': 2,
	'5 oro': 2,
	'5 basto': 2,
	'5 copa': 2,
	'4 espada': 1,
	'4 oro': 1,
	'4 basto': 1,
	'4 copa': 1
}



class Card:
	def __init__(self, name):
		self.name = name
		self.score = cards_dict[name]
		self.number = None
		self.symbol = None
		
		self.set_number_and_symbol()
		
	def set_number_and_symbol(self):
		aux = self.name.split(' ')
		self.number = int(aux[0])
		self.symbol = aux[1]
