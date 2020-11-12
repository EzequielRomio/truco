import random
import sys

import cards

import pygame


def get_hands():
	p1 = random.choices([k for k in cards.cards_dict.keys()], k=6)
	
	p1 = [cards.Card(p1[ix]) for ix in range(6)]
	
	p2 = [p1.pop(1) for _ in range(3)]
	
	return p1, p2



def calculate_envido_score(hand):
	
	if hand[0].symbol == hand[1].symbol and hand[0].symbol == hand[2].symbol:
		scores = []
		for card in hand:
			if card.number in (10, 11, 12):
				scores.append(0)
			else:
				scores.append(card.number)
		
		return (sum(scores) - min(scores)) + 20
	
	cards_scores = {}
	for card in hand:
		if not card.symbol in cards_scores:
			cards_scores[card.symbol] = card.number
		else:
			cards_scores[card.symbol] += card.number + 20
		if card.number in (10, 11, 12):
			cards_scores[card.symbol] -= card.number
			
	return max(cards_scores.values())
		
first_round_menu = """
Elige una carta:
1 - {}
2 - {}
3 - {}
"""
	
class Player:
	def __init__(self):
		self.name = None
		self.score = 0
		self.hand = None
		self.envido_score = 0
		self.first_round_won = False
	
	def set_hand(self, hand):
		self.hand = hand
		
	def drop_card(self, card_ix):
		return self.hand.pop(card_ix)
		
	def show_cards(self):
		for card in self.hand:
			print(card.name)
	
	def set_envido_score(self):
		self.envido_score = calculate_envido_score(self.hand)
		
	def set_name(self, name):
		self.name = name



def main():
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption("Truco!")
	
	player_1 = Player()
	player_2 = Player()
	
	player_1.set_name('p1')
	player_2.set_name('p2')
	
	first_round = True
	
	while True:
		if first_round:
			p1, p2 = get_hands()	
			player_1.set_hand(p1)
			player_1.set_envido_score()
			player_2.set_hand(p2)
			player_2.set_envido_score()
		
			player_1.show_cards()
			print(player_1.envido_score)
			player_2.show_cards()
			print(player_2.envido_score)
			
			move = input('Cantar envido?\ny = si, n = no\n')
			if move != 'y':
				move = input(first_round_menu.format(player_1.hand[0].name, player_1.hand[1].name, player_1.hand[2].name))
				move = int(move) - 1
				
				cards_on_board = []
				cards_on_board.append(player_1.drop_card(move))
				
				cards_on_board.append(player_2.drop_card(move))
				
				
			
			
		
		break

if __name__ == '__main__':
	pygame.init()
	main()
