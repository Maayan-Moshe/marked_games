import numpy as np
import Interaction
import manager
print ("Loaded Testing file")





import unittest

class TestInteraction(unittest.TestCase):

	table = np.array([[1,0],[0,2]])

	def test_wealth_growth_diag(self):

		pl1, pl2 = get_two_players({'red':0,'blue':1}, {'red':1,'blue':1})

		print (pl1.get_name())
		interact=Interaction.Interaction(self.table)
		interact.interact(pl1,pl2)
		new_wealth_pl1=pl1.wealth
		new_wealth_pl2=pl2.wealth
		self.assertEqual(new_wealth_pl1,self.table[1,1])
		self.assertEqual(new_wealth_pl2,self.table[1,1])

	def test_wealth_growth_nd(self):

		pl1, pl2 = get_two_players({'red':0,'blue':0}, {'red':1,'blue':1})
		interact=Interaction.Interaction(self.table)
		interact.interact(pl1,pl2)
		new_wealth_pl1=pl1.wealth
		new_wealth_pl2=pl2.wealth
		self.assertEqual(new_wealth_pl1,self.table[0,1])
		self.assertEqual(new_wealth_pl2,self.table[1,0])





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

