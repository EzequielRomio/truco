import random
import sys
import time

import cards

import pygame
from pygame.locals import *


def get_hands():
	cards_list = [k for k in cards.cards_dict.keys()]

	p1 = [cards.Card(cards_list.pop(random.randint(0, len(cards_list)-1))) for _ in range(6)]
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

def load_image(filename, transparent=False):
	try: 
		image = pygame.image.load(filename)
	except pygame.error:
		raise SystemExit('No se pudo cargar la imagen')
  	
	image = image.convert()
	#convierte la imagen al tipo interno de Pygame 
	#que hace que sea mucho más eficiente
	if transparent:
		color = image.get_at((0,0)) # obtiene el color a transparentar en el pixel x=0,y=0 (sup, izquierda)
		image.set_colorkey(color, RLEACCEL) #lo hace transparente
	return image



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

class Board:
	def __init__(self):
		self.bg = None
		self.cards = []

	def set_cards_images(self, card_image):
		self.cards.append(card_image)



def main():
	game_over = False
	screen = pygame.display.set_mode((1920, 1080))
	pygame.display.set_caption("Truco!")
	pygame.mixer.music.load('music_01.mp3')
	pygame.mixer.music.play(-1) # -1 hace que sea loop infinito
	#solo un sonido => x = pygame.mixer.Sound('sonido.mp3') 


	player_1 = Player()
	player_2 = Player()
	
	player_1.set_name('p1')
	player_2.set_name('p2')
	
	first_round = True
	
	while not game_over:
		if first_round:
			p1, p2 = get_hands()	
			player_1.set_hand(p1)
			player_1.set_envido_score()
			player_2.set_hand(p2)
			player_2.set_envido_score()
			
			cards_imges = [load_image(c.image) for c in player_1.hand]
			card_back = [load_image('images/back.png') for _ in range(len(player_2.hand))]

			x_coord = 0
			for img in cards_imges:
				x_coord += 220
				screen.blit(img, (x_coord, 540))
			
			x_coord = 0
			for img in card_back:
				x_coord += 220
				screen.blit(img, (x_coord, 40))
			
			
			pygame.display.flip()
			
				
			player_1.show_cards()
			print(player_1.envido_score)
			player_2.show_cards()
			print(player_2.envido_score)
			"""
			move = input('Cantar envido?\ny = si, n = no\n')
			if move != 'y':
				move = input(first_round_menu.format(player_1.hand[0].name, player_1.hand[1].name, player_1.hand[2].name))
				move = int(move) - 1
				
				cards_on_board = []
				cards_on_board.append(player_1.drop_card(move))
				
				cards_on_board.append(player_2.drop_card(move))
			"""	
			first_round = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

			elif event.type == pygame.MOUSEMOTION:
				mouse_pos = pygame.mouse.get_pos()
				if mouse_pos[0] in list(range(220, 410)) and mouse_pos[1] in list(range(540, 1000)):			
					# player1.hand[0]
					print('card 1')
					time.sleep(1)
					#img = pygame.transform.smoothscale(cards_imges[0], (2*100, 2*200))
					#screen.blit(img, (220, 540))
					#time.sleep(1)

				elif mouse_pos[0] in list(range(440, 640)) and mouse_pos[1] in list(range(540, 1000)):
					# player1.hand[1]
					print('card 2')
					time.sleep(1)
				
				elif mouse_pos[0] in list(range(660, 780)) and mouse_pos[1] in list(range(540, 1000)):
					# player1.hand[2]
					print('card 3')
					time.sleep(1)
		
			pygame.display.flip()
					

if __name__ == '__main__':
	pygame.init()
	main()
