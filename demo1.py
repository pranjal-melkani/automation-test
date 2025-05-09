dict1 = {
    "1" : "A",
    "2" : "B",
    "3" : "C",
    "4" : "D",
    "5" : "E"
}


def pattern(n):
    # upper part 
    spaces = n - 1
    chars = 1
        
    for i in range(n):
        # space 
        for j in range(spaces):
            print(" ", end="")
        # chars 
        
        for j in range(chars):
            ch = dict1[str(j+1)]
            print(ch, end=" ")
            
        # space 
        for j in range(spaces):
            print(" ", end="")

        print()
        chars += 1
        spaces -= 1
        
    
    # lower part 
    spaces = 1
    chars -= 2
    
    for i in range(n-1):
        # space 
        for j in range(spaces):
            print(" ", end="")
        
        # chars 
        for j in range(chars):
            ch = dict1[str(j+1)]
            print(ch, end=" ")
        
        # space 
        for j in range(spaces):
            print(" ", end="")
        
        print()
        spaces += 1
        chars -= 1

pattern(4)