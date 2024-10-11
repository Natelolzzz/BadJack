import random
import sys
import time


def print_slow(string):
  string = str(string)
  string += "\n"
  for letter in string:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(random.random() * 10.0 / typing_speed)


def draw():
  global cards, deck_of_cards
  random.shuffle(cards)
  if len(cards) <= 0:
    cards = deck_of_cards
  return cards.pop()
  
def count_high_low_cards():
  global cards
  high_cards = len([card for card in cards if card >= 10])
  low_cards = len([card for card in cards if card < 10])
  return high_cards, low_cards


def dealer_hit_or_stand():
  global Dhand, yourhand, cards

  high_cards, low_cards = count_high_low_cards()

  bust_threshold = 21 - Dhand
  bust_cards = len([card for card in cards if card > bust_threshold])
  bust_probability = bust_cards / len(cards) if len(cards) > 0 else 1

  high_card_factor = high_cards / len(cards) if len(cards) > 0 else 0

  if yourhand < 15 and Dhand < 18:
      return 1  

  if bust_probability > 0.5 and Dhand >= 17:
      return 2  

  if yourhand > 18 and Dhand >= 17:
      return 2  
    
  if high_card_factor > 0.4 and Dhand >= 17:
      return 2  

  if Dhand < 17:
      return 1  

  return 2  

def dealer_draw():
  global Dhand, money, bet
  while dealer_hit_or_stand() == 1:
      print_slow("Dealer Hit")
      Dhand += draw()
      if Dhand > 21:
          print_slow("Dealer drew over 21! YOU WIN!\n")
          money += bet
          return 1
  print_slow("Dealer Stood")



typing_speed = 300
x = 1
playgame = 1
A = "A,"
J = "J,"
Q = "Q,"
K = "K,"
deck_of_cards = [
    11,
    11,
    11,
    11,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
    10,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
    10,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
    10,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
    10
]  # DONT FIDDLE WITH THIS, ONLY CHANGE cards INSTEAD
money = 200 * random.random()
while playgame == 1:
  money = round(money, 2)
  cards = deck_of_cards

  D1 = draw()
  D2 = draw()
  Y1 = draw()
  Y2 = draw()
  Dhand = D1 + D2
  yourhand = Y1 + Y2
  cards = deck_of_cards

  if money == 0:
    playgame = 0
    break

  print_slow("You have $" + str(money))
  print_slow("How much do you want to bet?")
  bet = float(input("> "))
  if bet > money:
    print_slow(
        "Thats more money than you have, assume you want to bet the max")
    bet = money

  if Dhand > 21:
    print_slow("Dealers first hand was over 21, so...")
    print_slow("You win!\n")
    money += 5

  if yourhand > 21:
    print_slow("Your first hand was over 21, so...")
    print_slow("You lose!\n")
    money -= 5
  print_slow(yourhand)
  choice = 1
  while choice == 1:

    print_slow("Hit (1) Or Stand (2)")
    choice = int(input("> "))

    if choice == 1:
      if dealer_draw() == 1:
        money += bet
        break

      yourhand = yourhand + draw()
      if yourhand > 21:
        print_slow("Over 21! You lose!\n")
        money -= bet
        break
      else:
        print_slow(yourhand)

    else:
      if dealer_draw() == 1:
        money += bet
        break

      if yourhand > 21:
        print_slow("Over 21! You lose!\n")
        money -= bet
        break

      if yourhand == 21:
        print_slow("YOU WIN!\n")
        money += bet
        break

      else:
        if yourhand > Dhand:
          print_slow("Bigger than dealers! You Win!\n")
          money += bet
          break

        else:
          print_slow("Less than dealers! You lose\n")
          money -= bet
          break

print_slow("Wow. You spent all your money. U lose :(.")
