envido_scores = {
	'envido': 2,
	'real envido': 3,
}

envido_order = (
	'envido',
	'real envido',
	'falta envido'
)


truco_scores = {
	'truco': 2,
	'retruco': 3,
	'vale cuatro': 4
}

def falta_envido_result(looser_score):
	if looser_score < 15:
		return 30
	else:
		return 30 - looser_score
	
def truco_result(p1_card, p2_card):
	winner = None
	if p1_card.score > p2_card.score:
		winner = p1_card
	elif p1_card.score < p2_card.score:
		winner = p2_card
	else: #if ==
		winner = 'tie'
		
	return winner
	
def envido_scene(p1_score, p2_score, player_strikes_up, envido_type):
	
	aux = envido_order.index(envido_type)
	score = envido_scores[envido_type]
	while len(aux) < 3:
		response = input("""
1 - quiero
2 - no quiero

3 - envido
4 - real envido
5 - falta envido
""")

		if response in ('1', '2'):
			break
		else:
			response = int(response) - 3
			if response < aux:
				print('no se puede bajar el envido!\n')
				continue
			envido = envido_order[response]
			score += envido_scores[envido]
			if response == aux:
				aux += 1
			else:
				aux = envido_order.index(envido)
		

			
		
		