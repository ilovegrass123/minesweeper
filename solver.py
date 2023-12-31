class Solver:
    def __init__(self, board):
        self.bored = board
        self.dug = {}
        self.flag = set()
    
    """
    Strategy:
    Scan all dug squares. If it is blank, skip over it. Otherwise, check the number of undug squares adjacent to that 
    location. If that number is equal to the number on on the square, then we deduce that all adjacent squares are bombs 
    Repeat this process taking into account all the flags we set earlier to solve the board.
    """
    def solve(self, flags, dug):
        while len(self.dug) + len(flags) < len(self.bored)**2:
            for key in self.dug:
                if self.dug[key] == 0:
                    continue
                
                vacant = set()
                for x in range(-1,2):
                    for y in range(-1,2):
                        if (x,y) in self.dug:
                            continue
                        vacant.add((x,y))
                
                if len(vacant) == self.dug[key]:
                    flags.update(vacant) # put all the flags in
            
    def dig(self, dug, flags):
        pass
        

def main():
    pass
if __name__ == "__main__":
    main()