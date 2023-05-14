import random

class GameLogic:
    
    def __init__(self):
        pass
    
    @staticmethod
    def roll_dice(dice_num):# this method with take 
        return tuple(random.randint(1, 6) for _ in range(dice_num))
        

if __name__ == "__main__":
    game_logic = GameLogic()
    print(game_logic.roll_dice(3))

    
        
    
    