class GenMaze:
    def __init__(self, movesrequired):
        self.rawmoves = []
        self.refinedmoves = []
        self.solution = []
        self.movesrequired = int(movesrequired)
        self.correctmove = []

#I'm assigning up, down, left, and right an int value of 1 through 4, making the odds and evens incompatible values later on
#like 1 being up and 3 being down. (you wouldnt want those next to eachother as a solution). Genrawmap determines how often each direction
#occurs and often removes one direction to keep all solutions from looking square. I'm looking for a shorter, more pythonic way to do this.

    def genrawmap(self):
        percentoptions = [.4, .45, .5, .55, .6, .65, .7]
        percentevens = random.choice(percentoptions)
        numevens = int(self.movesrequired*percentevens)
        numodds = self.movesrequired - numevens
        pathstyle = random.randint(1,5)
        if pathstyle == 1:
            for i in range(numevens):
                num = 2
                self.rawmoves.append(num)
            for x in range(numodds):
                num = random.choice((1, 3))
                self.rawmoves.append(num)
        elif pathstyle == 2:
            for i in range(numevens):
                num = 4
                self.rawmoves.append(num)
            for x in range(numodds):
                num = random.choice((1, 3))
                self.rawmoves.append(num)
        elif pathstyle == 3:
            for i in range(numevens):
                num = random.choice((2, 4))
                self.rawmoves.append(num)
            for x in range(numodds):
                num = 1
                self.rawmoves.append(num)
        elif pathstyle == 4:
            for i in range(numevens):
                num = random.choice((2, 4))
                self.rawmoves.append(num)
            for x in range(numodds):
                num = 3
                self.rawmoves.append(num)
        elif pathstyle == 5:
            for i in range(numevens):
                num = random.choice((2, 4))
                self.rawmoves.append(num)
            for x in range(numodds):
                num = random.choice((1, 3))
                self.rawmoves.append(num)
        random.shuffle(self.rawmoves)
        return self.rawmoves
        
#This takes the solution list and compares each move to it's next one. If the move wouldn't make sense (ex: go up, then go down)
#it takes the second direction and adds it to the end.

    def refine_map(self):
        try:
            i = 0
            j = 1
            for _ in range(len(self.rawmoves)*2):
                x = self.rawmoves[i]
                y = self.rawmoves[j]
                if x == y:
                    pass
                elif x != y:
                    if (x % 2 == 0) and (y % 2 == 0):
                        self.rawmoves.remove(y)
                        self.rawmoves.append(y)
                        i -= 2
                        j -= 2
                    elif (x % 2 == 1) and (y % 2 == 1):
                        self.rawmoves.remove(y)
                        self.rawmoves.append(y)
                        i -= 2
                        j -= 2
                    else:
                        pass
                i += 1
                j += 1
        except IndexError:
            pass
        return self.rawmoves
        
#the initial refine ran into an issue where sometimes, incompatible numbers would still be stuck together at the end.
#so in response this does the opposite. It compares the direction to the next one, and if it's incompatible, moves it to the back.
#with both in place, we get a consistently usable solution.

    def refinetwice(self):
        try:
            i = 0
            j = 1
            for _ in range(len(self.rawmoves)*2):
                x = self.rawmoves[i]
                y = self.rawmoves[j]
                if x == y:
                    pass
                elif x != y:
                    if (x % 2 == 0) and (y % 2 == 0):
                        self.rawmoves.remove(y)
                        self.refinedmoves.append(y)
                        i -= 2
                        j -= 2
                    elif (x % 2 == 1) and (y % 2 == 1):
                        self.rawmoves.remove(y)
                        self.refinedmoves.append(y)
                        i -= 2
                        j -= 2
                    else:
                        pass
                i += 1
                j += 1
        except IndexError:
            pass
        self.refinedmoves.extend(self.rawmoves)
        return self.refinedmoves
       
   #This takes those numerical values and actually makes them directions.

    def transposesolution(self):
        for i in self.refinedmoves:
            if i == 1:
                self.solution.append("go up")
            elif i == 2:
                self.solution.append("go right")
            elif i == 3:
                self.solution.append("go down")
            elif i == 4:
                self.solution.append("go left")
        return self.solution

if __name__ == '__main__':
    moves_needed = int(input("How many moves should this maze take? (minimum 4): "))
    x = GenMaze(moves_needed)
    print(x.genrawmap())
    print(x.refine_map())
    print(x.refinetwice())
    print(x.transposesolution())
