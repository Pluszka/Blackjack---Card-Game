from random import choice

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal(amount_player, amount_computer):
  player=[choice(cards) for card in range(amount_player)]
  computer=[choice(cards) for card in range(amount_computer)]
  return player, computer

deal_step=True

dealt_cards=deal(2,2)
player_cards=dealt_cards[0]
computer_cards=dealt_cards[1]
card_to_show=computer_cards[1],'?'
player_score=(sum(player_cards))
computer_score=(sum(computer_cards))

print(f'Here you are your cards: {player_cards}\nThat\'s a single card which belong to your opponent: {card_to_show}')
if player_score>=21:
  print(f'Your score is equal to {player_score}, you lose.')
else:
  while deal_step:
    next_cards=input(f'Your score is equal to {player_score}.\nWill you continue?(Y/N)').upper()
    if next_cards=='Y':
      card=deal(1,0)[0][0]
      player_cards.append(card)
      player_score+=card
      print(f'Now you have these cards: {player_cards}')
    else:
      deal_step=False
