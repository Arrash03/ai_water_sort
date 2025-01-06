import copy
from typing import Dict, List, Set, Tuple

from pq import PQ



class GameSolution:
    MAX_DEPTH: int = 10
    Tube = List[int]
    MotherTube = List[Tube]
    Move = List[List[int]]
    NodeState = Tuple[MotherTube, Tuple[int, int], Move]
    NColorInTube=2
    NEmptyTubes=1
    NColor=3
    """
        A class for solving the Water Sort game and finding solutions(normal, optimal).

        Attributes:
            ws_game (Game): An instance of the Water Sort game which implemented in game.py file.
            moves (List[Tuple[int, int]]): A list of tuples representing moves between source and destination tubes.
            solution_found (bool): True if a solution is found, False otherwise.

        Methods:
            solve(self, current_state):
                Find a solution to the Water Sort game from the current state.
                After finding solution, please set (self.solution_found) to True and fill (self.moves) list.

            optimal_solve(self, current_state):
                Find an optimal solution to the Water Sort game from the current state.
                After finding solution, please set (self.solution_found) to True and fill (self.moves) list.
    """
    def __init__(self):
        """
            Initialize a GameSolution instance.
            Args:
                game (Game): An instance of the Water Sort game.
        """
        # self.ws_game = game  # An instance of the Water Sort game.
        self.moves = []  # A list of tuples representing moves between source and destination tubes.
        self.tube_numbers = GameSolution.NEmptyTubes + GameSolution.NColor  # Number of tubes in the game.
        self.solution_found = False  # True if a solution is found, False otherwise.
        self.visited_tubes = set()  # A set of visited tubes.
        self.own_state = []

    def __is_tube_completed(self, tube: Tube) -> bool:
        result = False
        if len(tube) == GameSolution.NColorInTube:
            tmp_set = set(tube)
            if len(tmp_set) == 1:
                result = True
        return result

    def __find_sources(self, tubes: MotherTube) -> List[int]:
        MIN_TUBE_LEN: int = 0
        sources: List[int] = []
        for i in range(len(tubes)):
            if len(tubes[i]) != MIN_TUBE_LEN and not self.__is_tube_completed(tubes[i]):
                sources.append(i)
        return sources

    def __find_destinations(self, tubes: MotherTube) -> List[int]:
        destinations: List[int] = []
        for i in range(len(tubes)):
            if len(tubes[i]) != GameSolution.NColorInTube:
                destinations.append(i)
        return destinations

    @staticmethod
    def __move_from_src_to_dst(tubes: MotherTube, src: int, dst: int) -> None:
        tubes[dst].append(tubes[src][-1])
        tubes[src].pop()

    def __check_win(self, tubes: MotherTube) -> bool:
        result = True
        if len(tubes) == 0:
            result = False
        else:
            for tube in tubes:
                if len(tube) != 0 and len(tube) != GameSolution.NColorInTube:
                    result = False
                    break
                tmp_set = set(tube)
                if len(tmp_set) > 1:
                    result = False
                    break
        return result

    def solve(self, current_state: MotherTube, moves: List[List[int]] = [], depth: int = MAX_DEPTH) -> bool:
        """
            Find a solution to the Water Sort game from the current state.

            Args:
                current_state (List[List[int]]): A list of lists representing the colors in each tube.

            This method attempts to find a solution to the Water Sort game by iteratively exploring
            different moves and configurations starting from the current state.
        """
        if depth == 0:
            return False
        
        while True:
            sources = self.__find_sources(current_state)
            destinations = self.__find_destinations(current_state)
            for src in sources:
                for dst in destinations:
                    if src == dst:
                        continue
                    own_current_state = copy.deepcopy(current_state)
                    GameSolution.__move_from_src_to_dst(own_current_state, src, dst)
                    own_moves = copy.deepcopy(moves)
                    own_moves.append([src, dst])
                    if self.__check_win(own_current_state):
                        self.solution_found = True
                        self.moves = own_moves
                        self.own_state = own_current_state
                        return True 
                    result = self.solve(own_current_state, own_moves, depth - 1)
                    if result:
                        return True

            if depth == GameSolution.MAX_DEPTH:
                depth += 4
            else:
                break

    @staticmethod
    def __f_compare(prev: NodeState, next: NodeState) -> bool:
        prev_f = prev[1][0] + prev[1][1]
        next_f = next[1][0] + next[1][1]
        return prev_f < next_f

    def __count_completed_tubes(self, tubes) -> int:
        count = 0
        for tube in tubes:
            if self.__is_tube_completed(tube):
                count += 1

        return count

    def __h(self, tubes: MotherTube):
        # if ncolor is alwas 2
        completed_tubes = self.__count_completed_tubes(tubes)
        return len(tubes) - completed_tubes - 1
        
    def optimal_solve(self, current_state: MotherTube):
        """
            Find an optimal solution to the Water Sort game from the current state.

            Args:
                current_state (List[List[int]]): A list of lists representing the colors in each tube.

            This method attempts to find an optimal solution to the Water Sort game by minimizing
            the number of moves required to complete the game, starting from the current state.
        """
        frontier: PQ = PQ(GameSolution.__f_compare)
        own_current_state = copy.deepcopy(current_state)
        current_h = self.__h(own_current_state)
        if current_h == 0:
            self.solution_found = True
            return
        tmp_node: GameSolution.NodeState = [own_current_state, [0, current_h], []]
        frontier.push_back(tmp_node)

        while not frontier.is_empty():
            closest: GameSolution.NodeState = frontier.pop_back()
            sources: List[int] = self.__find_sources(closest[0])
            destinations: List[int] = self.__find_destinations(closest[0])

            for src in sources:
                for dst in destinations:
                    if src == dst:
                        continue
                    own_state: GameSolution.MotherTube = copy.deepcopy(closest[0])
                    GameSolution.__move_from_src_to_dst(own_state, src, dst)
                    h_value = self.__h(own_state)
                    tmp_moves: GameSolution.Move = copy.deepcopy(closest[2])
                    tmp_moves.append([src, dst])
                    if h_value == 0:
                        self.solution_found = True
                        self.moves = tmp_moves
                        self.own_state = own_state
                        return
                    tmp_node: GameSolution.NodeState = [own_state, [closest[1][0] + 1, h_value], tmp_moves]
                    node_i = frontier.find(tmp_node)
                    if node_i != -1:
                        tmp_node_f = tmp_node[1][0] + tmp_node[1][1]
                        existed_node = frontier[node_i]
                        f_of_node_i = existed_node[1][0] + existed_node[1][1]
                        if tmp_node_f < f_of_node_i:
                            frontier.pop_back(node_i)

                    frontier.push_back(tmp_node)
