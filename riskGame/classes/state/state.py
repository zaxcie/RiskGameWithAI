class State:

    def __init__(self, number_nodes, partitions, players, player_turn_number):
        self.__number_nodes = number_nodes
        self.__partitions = partitions
        self.__players = players
        self.__player_turn_number = player_turn_number

    @property
    def set_players(self, players):
        self.__players = players

    @property
    def set_number_nodes(self, number_nodes):
        self.__number_nodes = number_nodes

    @property
    def set_partitions(self, partitions):
        self.__partitions = partitions

    @property
    def set_player_turn_number(self, player_turn_number):
        self.__player_turn_number = player_turn_number

    @property
    def get_players(self):
        return self.__players

    @property
    def get_number_nodes(self):
        return self.__number_nodes

    @property
    def get_partitions(self):
        return self.__partitions

    @property
    def get_player_turn_number(self):
        return self.__player_turn_number

    def get_current_player(self):
        return self.__players[self.__player_turn_number]

    def get_winner(self):
        for player in self.__players:
            if len(player.get_hold_nodes()) == self.__number_nodes:
                return player
        return None

    def expand_bonus(self):
