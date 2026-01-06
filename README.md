# Ten-Pin-Bowling-Game-score-calculation

## Problem Overview
This project implements a Python module to calculate the total score of a single ten-pin bowling game based on standard bowling rules.
A bowling game consists of 10 frames, where each frame can have:
 .Open frame
 .Spare
 .Strike
The program validates the input game string, converts it into numerical rolls, and computes the final score accurately.

## Tech Stack
- Python 3
  
## Rules in Game
Frames 1–9
  -Maximum 2 rolls per frame
  -Total pins per frame ≤ 10
  -Strike (X) ends the frame immediately
Frame 10
  -Always at least 2 rolls
  -If strike or spare, one bonus roll is allowed
  -Maximum 3 rolls in the 10th frame
Scoring Rules
  -Open frame: Sum of pins knocked down in the frame
  -Spare (/): 10 + next roll
  -Strike (X): 10 + next two rolls
  
## Input format
he game is represented as a string using standard bowling notation:

| Symbol | Meaning           |
| ------ | ----------------- |
| `0–9`  | Pins knocked down |
| `X`    | Strike (10 pins)  |
| `/`    | Spare             |
| `-`    | Miss (0 pins)     |

## Approach
1️.Input Validation (validate_input)

.Parses the input roll by roll
.Converts symbols (X, /, -, digits) into numeric pin values
.Tracks:
   -> Current frame
   -> Roll number within frame
   -> Previous roll value
   -> Bonus eligibility in 10th frame
.Ensures:
   -> No invalid characters
   -> No frame exceeds 10 pins
   -> Proper strike and spare usage
   -> Correct number of rolls in the 10th frame

If validation fails, the function returns None.

2️.Score Calculation (calculate_score)
.Iterates through 10 frames
.Uses an index over the rolls list
.Applies:
   -> Strike bonus (next two rolls)
   -> Spare bonus (next roll)
   -> Open frame sum

.Accumulates the total score and returns to main function

## Files in the Repository
- `Ten_Pin_Bowling_score.py` – Main Python program with validation and scoring logic
- `test_cases.py` – Unit test cases using Python `unittest`
- `Presentation.pptx` – Short presentation 
- `README.md` – Project documentation

## Running the Program
1.Open a terminal in the project folder.   
2.Run the main program:    
    ` python bowling.py `      
3.The program will prompt you for input and display the total bowling score.  

## Running Unit Tests
1.Unit tests are written in test_cases.py using Python’s unittest module.      
2.To run the tests:          
    ` python test_cases.py `  
3.Each . represents a passed test. Failed tests will show details.        
