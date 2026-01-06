# Ten-Pin-Bowling-Game-score-calculation

## Problem Statement
This project calculates the total score of a single ten-pin bowling game based on standard bowling rules.

## Features
- Calculate scores for a **10-frame bowling game**.
- Handles:
  - **Strike** (`X`): 10 points plus the next two rolls.
  - **Spare** (`/`): 10 points for the frame plus the next roll.
  - **Open frame** (`0-9` and `-` for miss).
- Validate input:
  - Detect invalid bowling score strings.
  - Reject incorrect formats (like too many rolls or invalid characters).
- Unit tests to check:
  - All open frames
  - All strikes
  - Spares
  - Invalid inputs

## Files in the Repository
- `Ten_Pin_Bowling_score.py` – Main Python program with validation and scoring logic
- `test_cases.py` – Unit test cases using Python `unittest`
- `Presentation.pptx` – Short presentation 
- `README.md` – Project documentation
  
## Tech Stack
- Python 3

## How the Program Works
1. **Input Validation**
   - The `validate_input(game: str)` function ensures the input string is a valid bowling game.
   - Returns a list of integer scores if valid, or `None` if invalid.
2. **Score Calculation**
   - The `calculate_score(rolls: list)` function calculates the total score frame by frame:
     - Strike: Add next two rolls as bonus.
     - Spare: Add next roll as bonus.
     - Open frame: Add the two rolls.


## Running the Program
1.Open a terminal in the project folder.   
2.Run the main program:    
    ` python bowling.py `      
3.The program will prompt you for input and display the total bowling score.  

## Running Unit Tests
1.Unit tests are written in test_cases.py using Python’s unittest module.      
2.To run the tests:          
    ` python -m unittest test_cases.py `  
3.Each . represents a passed test. Failed tests will show details.        
