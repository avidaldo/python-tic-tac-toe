class GameMessages:
    ENTER_MOVE = "Enter your move (1-9): "
    INVALID_NUMBER = "You must enter a number between 1 and 9."
    CELL_TAKEN = "That cell is already taken."
    INVALID_INPUT = "Invalid input. Please enter a number."
    
    HUMAN_WIN = "Congratulations! You won!"
    MACHINE_WIN = "I won! Better luck next time."
    DRAW = "It's a draw!"
    
    DIFFICULTY_PROMPT = (
        "Select difficulty level:\n"
        "1. Easy (Random moves)\n"
        "2. Hard (Minimax algorithm)\n"
        "Choose 1/(2): "
    )
    
    FIRST_PLAYER_PROMPT = (
        "Who wants to start?\n"
        "1. Human\n"
        "2. Machine\n"
        "Choose 1/(2): "
    )