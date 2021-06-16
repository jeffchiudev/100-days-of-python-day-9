from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")

repeat = True
auction_bids = {}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  #('name': number, 'name2': number2)
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while repeat == True:

  name = input("What is your name?\n")
  price = int(input("What is your bid?\n"))
  auction_bids[name] = price
  again = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if again == "no":
    repeat = False
    find_highest_bidder(auction_bids)
  elif again == "yes":
    clear()