### prompt-01 : 
> create a GameLgic class with python 

- result : 
```python
class GameLogic:
    def __init__(self):
        self.players = []
        self.current_player = None
        self.game_over = False
    
    def add_player(self, player_name):
        self.players.append(player_name)
    
    def start_game(self):
        if len(self.players) < 2:
            print("At least 2 players are required to start the game.")
            return
        
        self.current_player = self.players[0]
        self.game_over = False
        print("Game started. Current player: ", self.current_player)
    
    def next_turn(self):
        if self.game_over:
            print("The game is already over.")
            return
        
        current_player_index = self.players.index(self.current_player)
        next_player_index = (current_player_index + 1) % len(self.players)
        self.current_player = self.players[next_player_index]
        print("Next turn. Current player: ", self.current_player)
    
    def end_game(self):
        self.game_over = True
        print("Game over.")
In this example, the GameLogic class represents the logic and functionality of a game. It maintains a list of players, tracks the current player, and determines if the game is over or not.

You can create an instance of the GameLogic class and interact with its methods like this:

python
Copy code
game = GameLogic()
game.add_player("Player 1")
game.add_player("Player 2")
game.add_player("Player 3")

game.start_game()
game.next_turn()
game.next_turn()
game.end_game()
This will output:

sql
Copy code
Game started. Current player:  Player 1
Next turn. Current player:  Player 2
Next turn. Current player:  Player 3
Game over.
Note that this is a basic example, and you can expand upon it by adding more game-specific functionality and rules to the GameLogic class as per your requirements.


```

### prompt-02 :
> create  empty Gamelogic class python 

- result : 
```python 
class GameLogic:
    def __init__(self):
        pass
    
    def start_game(self):
        pass
    
    def next_turn(self):
        pass
    
    def end_game(self):
        pass
This empty GameLogic class serves as a template that you can fill in with the specific logic and functionality of your game. You can add additional methods and attributes based on the requirements of your game.

For example, if your game involves tracking scores, you can add a score attribute to the class and methods to update and retrieve the scores. Similarly, if your game has specific rules for winning or determining the next player, you can define methods to handle those rules.

Remember to replace the pass statements with the actual implementation code for each method.





```

### prompt-03 :
>create roll_dice method inside GameLogic class 

- result : 
```python 
import random

class GameLogic:
    def __init__(self):
        pass
    
    def start_game(self):
        pass
    
    def next_turn(self):
        pass
    
    def end_game(self):
        pass
    
    def roll_dice(self):
        return random.randint(1, 6)
In this example, the roll_dice method uses the random module in Python to simulate rolling a six-sided die. It generates a random number between 1 and 6, representing the result of the dice roll.

You can then use the roll_dice method within your game logic to simulate dice rolls or implement specific game mechanics based on dice outcomes.

Remember to replace the pass statements with the actual implementation code for other methods in the GameLogic class based on your game's requirements.
```