import numpy as np
import Interaction
import manager
print ("Loaded Testing file")


import unittest

class TestManager(unittest.TestCase):

	table = np.array([[1,0],[0,2]])

	def test_manager(self):

		pl1, pl2 = get_two_players({'red':0,'blue':1}, {'red':1,'blue':1})
		interact=Interaction.Interaction(self.table)
		interact.interact(pl1,pl2)

		players=[pl1,pl2]
		Uni=Interaction.Universe(players,interact)
		manag=manager.Manager(Uni)
		manag.plot_and_update()

def get_two_players(strat1,strat2):

    params1={'marker':'red', 'strategy':strat1}
    params2={'marker':'blue', 'strategy':strat2}
    pl1=Interaction.Player(params1)
    pl2=Interaction.Player(params2)


    return pl1, pl2

if __name__ == '__main__':
    unittest.main()


# ### Testing the Interaction code.
# n=100 # number of games.

# #creating players
# strat1={'red':0,'blue':1}
# strat2={'red':1,'blue':1}
# params1={'marker':'red', 'strategy':strat1}
# params2={'marker':'blue', 'strategy':strat2}
       
        
# pl1=Interaction.Player(params1)
# pl2=Interaction.Player(params2)

# # creating universe
# players=[pl1,pl2]
# print (pl1.marker)



# Uni=Interaction.Universe(players,interact)
# print (Uni.players[0].strategy)
# print (Uni.interaction.tables)

# for i in range(n):
# 	Uni.update()
# 	#print (Uni.players)





exit

