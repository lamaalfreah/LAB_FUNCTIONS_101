def print_countdown_pattern(x:int):
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
    print(pattern)

# Call the function
print_countdown_pattern(5) 
# Print the documentation 
print("\nFunction documentation:"+print_countdown_pattern.__doc__)
# or we can use help(print_countdown_pattern)
