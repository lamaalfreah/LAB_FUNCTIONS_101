def countdown_pattern(x:int)->str:
    '''     
    Prints a countdown pattern starting from x down to 1.
    Each line starts from the current value of x and counts down to 1,
    and the starting value decreases by 1 on each new line.
    '''
    pattern:str=""
    while x>=1:
        for number in range(x,0,-1):
            pattern+=str(number)+" "
        pattern+='\n'
        x-=1
    return pattern

# print countdown_pattern(5) 
print(countdown_pattern(5))

