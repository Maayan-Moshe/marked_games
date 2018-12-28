import numpy as np
import Interaction
print ("Loaded Testing file")

### Testing the Interaction code.
n=100 # number of games.

#creating players
strat1=[0,0]
strat2=[0,1]
params1={'marker':0, 'strategy':strat1}
params2={'marker':0, 'strategy':strat2}
       
        
pl1=Interaction.Player(params1)
pl2=Interaction.Player(params2)

# creating universe
players=[pl1,pl2]
print (pl1.marker)

table_a=[[1,0],[0,2]]
table_b=[[2,4],[4,2]]
tables={'a':table_a,'b':table_b}
interact=Interaction.Interaction(tables)
print (interact)

Uni=Interaction.Universe(players,interact)
print (Uni.players[0].strategy)
print (Uni.interaction.tables)

for i in range(n):
	Uni.update()
	#print (Uni.players)





exit

