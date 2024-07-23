from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

def highest_bid(bidder,bidamt):
    winner=[]
    highest_bidder={"current": 0}
    
    for person in recorded_bids:
        current= int(recorded_bids[person])
        if current > highest_bidder["current"]:
            highest_bidder={}
            highest_bidder["current"]=current
            highest_bidder["winner"]=person
           
    winner.append(highest_bidder)
    print(f"The winner is {winner[0]['winner']} with a bid of ${winner[0]['current']}")

#START
recorded_bids={}
addbidder=True
while addbidder==True:
    bidder=input("What is your name? ")
    bidamt=input("What is your bid? $")
    recorded_bids[bidder]=bidamt
    
    nextbidder=input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if nextbidder=="yes":
        clear()
    else:
        addbidder=False

highest_bid(bidder,bidamt)



