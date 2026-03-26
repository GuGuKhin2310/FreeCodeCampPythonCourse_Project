from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self):
        random_moves = random.choice(self.moves)
        new_position = (
        self.position[0] + random_moves[0],
        self.position[1] + random_moves[1]
        )
        self.position = new_position
        self.path.append(new_position)

        return new_position
    
    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(1,0),(0,1),(-1,0),(0,-1)]
    
    def level_up(self):
        diagonal_moves = [
        (1,1),
        (1,-1),
        (-1,1),
        (-1,-1)]
        self.moves.extend(diagonal_moves)
        print('Pawn leveled up')
