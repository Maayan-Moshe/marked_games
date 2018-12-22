import numpy as np

class Player:

    def __init__(self, params):

        self.marker = params['marker']
        self.strategy = params['strategy']
        self.wealth = get(params, 'wealth', 0)

    def get_response(self, other_player):

        res = self.strategy[other_player.marker]
        return res

    def get_positive_wealth(self):

        return max(self.wealth, 0)

    def multiply(self, factor):

        f_copies = self.get_positive_wealth() * factor
        new_copies = int(np.round(f_copies))
        new_players = [self.__get_new() for index in range(new_copies)]

    def __get_new(self):

        return Player({'marker': self.marker, 'strategy': self.strategy})

class Interaction:

    def __init__(self, tables):

        self.tables = tables

    def interact(self, player_a, player_b):

        res_a = player_a.get_response(player_b)
        res_b = player_b.get_response(player_a)
        player_a.wealth += self.tables['a'][res_a, res_b]
        player_b.wealth += self.tables['b'][res_b, res_a]
    
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

    def __multiply(self, factor):

        new_players = list()
        for player in self.players:
            new_players += player.multiply(factor) 

        self.players = new_players

    def __do_interations(self):

        indexes = range(len(self.players))
        while len(indexes) > 1:
            player_a = self.__get_player(indexes)
            player_b = self.__get_player(indexes)
            self.interaction.interact(player_a, player_b)

    def __get_player(self, indexes):

        pre_a = np.random.randrange(len(indexes))
        index_a = indexes[pre_a]
        del indexes[pre_a]
        return self.players[index_a]
