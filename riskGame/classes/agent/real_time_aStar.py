from sys import maxsize
from riskGame.classes.evaluations.sigmoidEval import SigmoidEval
from riskGame.classes.agent.passive_agent import Passive


class RTAStar:

    def __init__(self, evaluation_heuristic=SigmoidEval()):
        self.__hash_table = {}
        self.__evaluate = evaluation_heuristic
        self.__passive_agent = Passive()
        self.__memo = {}

    def dfs(self, curr_state, distance_from_root, limit):
        if limit == 0 or curr_state.get_winner():
            # end of limit
            return SigmoidEval().score(curr_state) + distance_from_root

        if curr_state.__hash__() in self.__memo:
            return self.__memo[curr_state.__hash__()]

        my_turn_state = self.__passive_agent.play(curr_state)
        child_states = my_turn_state.expand()
        child_states = child_states[: min(5 * limit, len(child_states))]
        min_cost = maxsize
        for child in child_states:
            if child.get_winner():
                return distance_from_root
            child_cost = self.dfs(child, distance_from_root + 1, limit - 1)
            min_cost = min(min_cost, child_cost)
        self.__memo[curr_state.__hash__()] = min_cost
        return min_cost

    def play(self, state):
        # Plan phase
        limit = 3
        print("At the RTA*\n")
        child_states = state.expand()
        min_cost = maxsize
        second_min_cost = -1
        next_state = None
        for child in child_states:
            if child in self.__hash_table:
                child_cost = self.__hash_table[child]
            else:
                child_cost = self.dfs(child, 1, limit - 1)

            if child_cost < min_cost:
                second_min_cost = min_cost
                min_cost = child_cost
                next_state = child

        # Execute phase
        self.__hash_table[state] = second_min_cost if second_min_cost != maxsize else min_cost
        print('RTA* choose the best state to be: ')
        next_state.print_state()
        return next_state


