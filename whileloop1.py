#while True:
 #   x = input("please enter a number:")
  #  if x == "fuck off":
   #     print("get out!")
    #    break
    #else:
    #    print(x)

#number = 1
#while number <= 5:
 #     print(number)
  #    number += 1

#breakfast = ["shit", "orange", "apple", "watermelon"]
#number = 0
#while number < len(breakfast):
 #   if number == 4:
  #      break
   # print(breakfast[number])
    #number += 1

#price_of_product = 20
#player1 = input("please enter the name of player1")
#player2 = input("please enter the name of player2")
#attempt = 1
#while True:
 #  attempt_of_player1 = int(input(f"{player1} enter the price"))
  # attempt_of_player2 = int(input(f"{player2} enter the price"))
    #if attempt_of_player1 == price_of_product:
     #   print(f"{player1}correct!{player1} win!")
      #  break
    #elif attempt_of_player2 == price_of_product:
    #    print(f"{player2}correct!{player2} win!")
     #   break
    #elif abs(price_of_product-attempt_of_player1) < abs(price_of_product-attempt_of_player2):
     #   print(f"the answer of {player1} is close to the price")
    #else:
     #   print(f"the answer of {player2} is close to the price")


price_of_product = 20
player1 = input("please enter the name of player1")
player2 = input("please enter the name of player2")
attempt = 1
total_attempt = 3
while attempt <= total_attempt:
    attempt_of_player1 = int(input(f"{player1} enter the price"))
    attempt_of_player2 = int(input(f"{player2} enter the price"))
    if attempt_of_player1 == price_of_product or attempt_of_player2 == price_of_product:
          break
    elif abs(price_of_product-attempt_of_player1) < abs(price_of_product-attempt_of_player2):
        print(f"the answer of {player1} is close to the price")
    else:
        print(f"the answer of {player2} is close to the price")
    attempt += 1
if attempt_of_player1 == price_of_product:
        print(f"{player1}correct!{player1} win!")
elif attempt_of_player2 == price_of_product:
        print(f"{player2}correct!{player2} win!")
elif abs(price_of_product-attempt_of_player1) < abs(price_of_product-attempt_of_player2):
        print(f"game finish! the correct price is{price_of_product}, the answer of {player1} is close to the price, {player1}win!")
else:
     print(f"game finish! the correct price is{price_of_product}, the answer of {player2} is close to the price, {player2}win!")