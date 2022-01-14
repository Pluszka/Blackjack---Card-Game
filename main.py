from random import choice
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal():
  player=choice(cards),choice(cards)
  computer=choice(cards),choice(cards)
  return player, computer

dealt_cards=deal()
player_cards=dealt_cards[0]
computer_cards=dealt_cards[1]
card_to_show=computer_cards[1],'?'
print(f'Here you are your cards: {player_cards}\nThat\'s a single card belong to your opponent: {card_to_show}')
