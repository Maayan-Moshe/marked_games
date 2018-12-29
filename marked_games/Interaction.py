import numpy as np

class Player:

    def __init__(self, params):

        self.marker = params['marker']
        self.strategy = params['strategy']
        self.wealth = params.get('wealth', 0)

    def get_response(self, other_player):

        res = self.strategy[other_player.marker]
        return res

    def get_positive_wealth(self):

        return max(self.wealth, 0)

    def multiply(self, factor):

        f_copies = self.get_positive_wealth() * factor
        new_copies = int(f_copies)
        new_copies+=(np.random.rand()<(np.remainder(f_copies,1)))
        new_players = [self.__get_new() for index in range(new_copies)]
        return new_players

    def get_name(self):

        res = '{}, {}'.format(self.marker, self.strategy)
        return res

    def __get_new(self):

        return Player({'marker': self.marker, 'strategy': self.strategy})

class Interaction:

    def __init__(self, table):

        self.table = table

    def interact(self, player_a, player_b):

        res_a = player_a.get_response(player_b)
        res_b = player_b.get_response(player_a)


        player_a.wealth += self.table[res_a,res_b]
        player_b.wealth += self.table[res_b,res_a]
    
class Universe:

    def __init__(self, players, interaction):

        self.players = players
        self.interaction = interaction

    def update(self):

        self.__do_interactions()
        
        sum = 0
        for player in self.players:
            sum += player.get_positive_wealth()
        
        factor = len(self.players)/sum

        self.__multiply(factor)

    def get_stats(self):

        stats=dict() 
        for player in self.players:
            stats[player.get_name()] = stats.get(player.get_name(), 0) + 1 

        return stats   

    def __multiply(self, factor):

        new_players = list()
        for player in self.players:
            new_players += player.multiply(factor) 

        self.players = new_players

    def __do_interactions(self):

        indices = list(range(len(self.players)))
        while len(indices) > 1:
            player_a = self.__get_player(indices)
            player_b = self.__get_player(indices)
            self.interaction.interact(player_a, player_b)

    def __get_player(self, indices):

        pre_a = np.random.randint(len(indices))
        index_a = indices[pre_a]
        del indices[pre_a]
        return self.players[index_a]
