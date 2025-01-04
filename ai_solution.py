class GameSolution:
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

    def solve(self, current_state):
        """
            Find a solution to the Water Sort game from the current state.

            Args:
                current_state (List[List[int]]): A list of lists representing the colors in each tube.

            This method attempts to find a solution to the Water Sort game by iteratively exploring
            different moves and configurations starting from the current state.
        """
        pass

    def optimal_solve(self, current_state):
        """
            Find an optimal solution to the Water Sort game from the current state.

            Args:
                current_state (List[List[int]]): A list of lists representing the colors in each tube.

            This method attempts to find an optimal solution to the Water Sort game by minimizing
            the number of moves required to complete the game, starting from the current state.
        """
        pass
