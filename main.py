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


typing_speed = 300
x = 1
playgame = 1
A = "A,"
J = "J,"
Q = "Q,"
K = "K,"
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11]
money = round(200 * random.random(), 2)
while playgame == 1:

  D1 = random.choice(cards)
  D2 = random.choice(cards)
  Y1 = random.choice(cards)
  Y2 = random.choice(cards)
  Dhand = D1 + D2
  yourhand = Y1 + Y2

  if money == 0:
    playgame = 0
    break

  print_slow("You have $ " + str(money))
  print_slow("How much do you want to bet?")
  bet = float(input("> "))

  if Dhand > 21:
    print_slow("Dealers first hand was over 21, so...")
    print_slow("You win!\n Next game begins now")
    money += 5

  if yourhand > 21:
    print_slow("Your first hand was over 21, so...")
    print_slow("You lose!\n Next game begins now")
    money -= 5
  print_slow(yourhand)
  choice = 1
  while choice == 1:

    print_slow("Hit (1) Or Stand (2)")
    choice = int(input("> "))

    if choice == 1:

      yourhand = yourhand + random.choice(cards)
      if yourhand > 21:
        print_slow("You lose!\n Next game begins now")
        money -= bet
        break
      else:
        print_slow(yourhand)
    else:
      if yourhand > 21:
        print_slow("You lose!\n Next game begins now")
        money -= bet
        break
      if yourhand == 21:
        print_slow("YOU WIN!\n Next game begins now")
        money += bet
        break
      else:
        if yourhand > Dhand:
          print_slow("You Win!\n Next game begins now")
          money += bet
          break
        else:
          print_slow("You lose\n Next game begins now")
          money -= bet
          break

print_slow("Wow. You spent all your money. Now get out.")
