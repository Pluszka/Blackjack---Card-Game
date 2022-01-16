from random import choice
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
win='Well played, you win.'
lose='You lose, so sad.'
draw='Draw!'

def deal(amount_player, amount_computer):
  player=[choice(cards) for card in range(amount_player)]
  computer=[choice(cards) for card in range(amount_computer)]
  return player, computer

def next_card(person_score, person_cards, capton):
  card=deal(1,0)[0][0]
  person_cards.append(card)
  person_score+=card
  if capton:
    print(f'Now you have these cards: {person_cards}')
  return person_score, person_cards

def who_won(player, computer):
  if player>=21:
    print(lose)
  elif computer>=21:
    print(win)
  elif player>computer:
    print(win)
  elif player<computer:
    print(lose)
  else:
    print(draw)



def game():
  clearConsole()

  deal_step=True
  comp_step=True

  dealt_cards=deal(2,2)
  player_cards=dealt_cards[0]
  computer_cards=dealt_cards[1]
  card_to_show=computer_cards[1],'?'
  player_score=(sum(player_cards))
  computer_score=(sum(computer_cards))

  print(f'Here you are your cards: {player_cards}\nThat\'s a single card which belong to your opponent: {card_to_show}')
  if player_score==21:
    player_score=0
  if player_score>21:
    print(f'Your score is equal to {player_score}, you lose.')
  else:
    while deal_step:
      next_cards=input(f'Your score is equal to {player_score}.\nWill you continue?(Y/N)').upper()
      
      if next_cards=='Y':
        result=next_card(player_score, player_cards, True)
        player_score=result[0]
        player_cards=result[1]
        if player_score>=21:
          deal_step=False
      else:
        deal_step=False

  if computer_score==21:
    computer_score=0
  while comp_step:      
    if computer_score>=19:
      new_card=choice(['Y','N'])
      if new_card=='Y':
        compresult=next_card(computer_score, computer_cards, False)
        player_score=compresult[0]
        if player_score>=21:
            comp_step=False
    else:
      comp_step=False

  print(f'Your final score is equal to: {player_score}\nComputer final score is equal to: {computer_score}')

  who_won(player_score, computer_score)
  again=input('Will you play again?(Y/N)').upper()
  if again=='Y':
    game()

game()

print('GG, see you next time.')