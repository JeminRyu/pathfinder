from random import randint

class Graph:

    def __init__(self, length = 20, start = [0, 0], end = -1):
        self.start = start
        if(end == -1):
            self.end = [length - 1, length - 1]
        else:
            self.end = end
        self.length = length
        self.graph = self.createGraph(length)


    def createGraph(self, length = 20):
        graph = [[0 for _ in range(length)] for _ in range(length)]
        obstacles = self.createObstacles(length)
        for x, y in obstacles:
            graph[x][y] = "+"
        return graph

    def createObstacles(self, length):
        userInput = input("random or custom or no obstacles? (c/r/n): ")
        obstacles = []
        if(userInput == "n"):
            return []
        elif(userInput == "c"):
            return []
        else:
            for _ in range(randint(length//10, length//5)):
                obstacleLength = randint(length//5, length//3)
                row = randint(0, length - 1)
                col = randint(0, length - 1)
                for _ in range(obstacleLength):
                    while(0 <= row < length and 0 <= col < length):
                        dir = randint(0, 7)
                        if not ((row == self.start[0] and col == self.start[1]) or (row == self.end[0] and col == self.end[1])):
                            obstacles.append([row, col])
                        if(dir == 0):
                            row += 1
                        elif(dir == 1):
                            row += 1
                            col += 1
                        elif(dir == 2):
                            col += 1
                        elif(dir == 3):
                            col += 1
                            row -= 1
                        elif(dir == 4):
                            row -= 1
                        elif(dir == 5):
                            row -= 1
                            col -= 1
                        elif(dir == 6):
                            col -= 1
                        elif(dir == 7):
                            col -= 1
                            row += 1
        return obstacles
    
    def getAdj(self, row, col):
        adj = []
        if(row < self.length - 1 and not self.seen(row + 1, col)):
            adj.append([row + 1, col])
        if(col > 0 and not self.seen(row, col - 1)):
            adj.append([row, col - 1])
        if(row > 0 and not self.seen(row - 1, col)):
            adj.append([row - 1, col])
        if(col < self.length - 1 and not self.seen(row, col + 1)):
            adj.append([row, col + 1])
        return adj

    def print(self):
        print("\n")
        start = self.graph[self.start[0]][self.start[1]]
        end = self.graph[self.end[0]][self.end[1]]

        self.graph[self.start[0]][self.start[1]] = "S"
        self.graph[self.end[0]][self.end[1]] = "E"
        for row in self.graph:
            print(" ".join(str(x) for x in row))

        self.graph[self.start[0]][self.start[1]] = start
        self.graph[self.end[0]][self.end[1]] = end
        
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end
    
    def getLength(self):
        return self.length
    
    def setSeen(self, row, col):
        self.graph[row][col] = 1
    
    def seen(self, row, col):
        num = self.graph[row][col]
        return num == 1 or num == "+"