import copy
from typing import List


Tube = List[int]
MotherTube = List[Tube]

class GameSolution:
    MAX_DEPTH: int = 10
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
    def __init__(self, game):
        """
            Initialize a GameSolution instance.
            Args:
                game (Game): An instance of the Water Sort game.
        """
        self.ws_game = game  # An instance of the Water Sort game.
        self.moves = []  # A list of tuples representing moves between source and destination tubes.
        self.tube_numbers = game.NEmptyTubes + game.NColor  # Number of tubes in the game.
        self.solution_found = False  # True if a solution is found, False otherwise.
        self.visited_tubes = set()  # A set of visited tubes.

    def __is_tube_completed(self, tube: Tube) -> bool:
        result = False
        if len(tube) == self.ws_game.NColorInTube:
            tmp_set = set(tube)
            if len(tmp_set) == 1:
                result = True
        return result

    def __choose_source(self, tubes: MotherTube) -> List[int]:
        MIN_TUBE_LEN: int = 0
        sources: List[int] = []
        for i in range(len(tubes)):
            if len(tubes[i]) != MIN_TUBE_LEN and not self.__is_tube_completed(tubes[i]):
                sources.append(i)
        return sources

    def __choose_destination(self, tubes: MotherTube) -> List[int]:
        destinations: List[int] = []
        for i in range(len(tubes)):
            if len(tubes[i]) != self.ws_game.NColorInTube:
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
                if len(tube) != 0 and len(tube) != self.ws_game.NColorInTube:
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
            sources = self.__choose_source(current_state)
            destinations = self.__choose_destination(current_state)
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
                        return True 
                    result = self.solve(own_current_state, own_moves, depth - 1)
                    if result:
                        return True

            if depth == GameSolution.MAX_DEPTH:
                depth *= 2
            else:
                break

    def optimal_solve(self, current_state):
        """
            Find an optimal solution to the Water Sort game from the current state.

            Args:
                current_state (List[List[int]]): A list of lists representing the colors in each tube.

            This method attempts to find an optimal solution to the Water Sort game by minimizing
            the number of moves required to complete the game, starting from the current state.
        """
        pass
