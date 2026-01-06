def validate_input(game: str):
    """
    This function checks whether the input is correct or not.
    """

    scores = []
    frame=1
    roll=1
    prev_roll=None
    bonus=False

    for i in game:
        if i.isdigit():
            value=int(i)
        elif i=='-':
            value=0
        elif i=='X':
            if frame<10 and roll!=1:
                return None
            value=10
        elif i=='/':
            if roll!=2 or prev_roll is None or prev_roll==10:
                return None
            value=10-prev_roll
        else:
            return None
    
        if frame<10 and roll==2 and prev_roll is not None:
            if prev_roll+value== 10 and i!='/': 
                return None
            
        scores.append(value)

        
        if frame==10:
            if roll==1 and value==10:
                bonus=True
            elif roll==2 and prev_roll+value==10:
                bonus=True
            
        prev_roll=value   

        
        if frame<10:
            if value==10 and roll==1:
                frame+=1
                roll=1
                prev_roll=None
            elif roll==2:
                frame+=1
                roll=1
                prev_roll=None
            else:
                roll=2
        else:
            roll+=1
            if not bonus and roll>3:
                return None
            if bonus and roll >4:
                return None
            
    if frame !=10:
        return None
    if bonus and roll != 4:
        return None
    if not bonus and roll != 3:
        return None
            
    return scores

    
def calculate_score(rolls:list) -> int:
    """
    This function calculate the total score of a single ten-pin bowling game.
    """
    scores=rolls
    total = 0
    index = 0
    
    for frames in range(10):
           if scores[index]==10:
                  total+=scores[index]+scores[index+1]+scores[index+2]
                  index+=1
           elif scores[index]+scores[index+1]==10:
                  total+=10+scores[index+2]
                  index+=2
           else:
                 total+=scores[index]+scores[index+1]
                 index+=2
                  

    return total


def main():
    game=input("Enter the score table in the correct format:")
    valid_input=validate_input(game)
    if valid_input is None:
        print("Invalid input")
        return
    total_point = calculate_score(valid_input)
    if total_point is not None:
        print("Total points:", total_point)
if __name__ == "__main__":
    main()
