fpath = "C:\Users\YJ\OneDrive\Documents\Project Euler\Grids\Project Euler Q54 Poker.txt"
fhand = open(fpath)

suits = {"D":1,"C":2,"H":3,"S":4}
cards =dict()
for i in xrange(2,11):
    cards.update({i:i})
cards.update({"J":11})
cards.update({"Q":12})
cards.update({"K":13})
cards.update({"A":14})


for line in fhand:
    line.rstrip("\n")
    player1=[]
    player2=[]
    for card in line.split(" "):
        for type in str(card):
            if len(player1)<10:
                player1.append(type)
            else:
                if type!="\n":
                    player2.append(type)
        for i in xrange(len(player1)):
            if i%2==0:
                1card
#.split(" ")
