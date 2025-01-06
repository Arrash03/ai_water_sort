import random
from ai_solution import GameSolution

def create_tubes() -> GameSolution.MotherTube:
    tubes: GameSolution.MotherTube = []
    numbers = [0, 0, 1, 1, 2, 2]
    for _ in range(3):
        tube: GameSolution.Tube = []
        for _ in range(2):
            index = random.randint(0, len(numbers) - 1)
            tube.append(numbers[index])
            numbers.pop(index)
        tubes.append(tube)
    tubes.append([])
    return tubes


if __name__ == "__main__":
    tubes = create_tubes()
    solver = GameSolution()
    print(tubes)
    solver.solve(tubes)
    optimal_solver = GameSolution()
    optimal_solver.optimal_solve(tubes)
    print("*"*10, "water sort sovled", "*"*10)
    print("normal solve:")
    print(f"\tmoves_count: {len(solver.moves)}")
    print(f"\tmoves: {solver.moves}")
    print(f"\tlast_state: {solver.own_state}")
    print("#"*30)
    print("optimal solve:")
    print(f"\tmoves_count: {len(optimal_solver.moves)}")
    print(f"\tmoves: {optimal_solver.moves}")
    print(f"\tlast_state: {optimal_solver.own_state}")
    print("*"*30)
    
    
