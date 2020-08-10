from random import randint

class Graph:

    def __init__(self, length = 20, start = [0, 0], end = [ -1, -1]):
        self.graph = self.createGraph(length, start, end)
        self.start = start
        self.end = [length - 1, length - 1]
        self.length = length

    def createGraph(self, length = 20, start = [0, 0], end = [ -1, -1]):
        graph = [[0 for _ in range(length)] for _ in range(length)]
        obstacles = self.createObstacles(length)
        for x, y in obstacles:
            graph[x][y] = 1
        # graph[start[0]][start[1]] = 2
        # if(end[0] == -1):
        #     graph[length - 1][length - 1] = 2
        # else:
        #     graph[end[0]][end[1]] = 2
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
                        obstacles.append([row, col])
                        if(dir == 0):
                            row += 1
                        elif(dir == 1):
                            row += 1
                            col += 1
                        elif(dir == 2):
                            col += 1
                        elif(dir == 3):
                            row += 1
                            col -= 1
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
        if(row > 0 and not self.seen(row - 1, col)):
            adj.append([row - 1, col])
        if(row < self.length - 1 and not self.seen(row + 1, col)):
            adj.append([row + 1, col])
        if(col > 0 and not self.seen(row, col - 1)):
            adj.append([row, col - 1])
        if(col < self.length - 1 and not self.seen(row, col + 1)):
            adj.append([row, col + 1])
        return adj

    def print(self):
        for row in self.graph:
            print(" ".join(str(x) for x in row))
        
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end
    
    def getLength(self):
        return self.length
    
    def setSeen(self, row, col):
        self.graph[row][col] = 3
    
    def seen(self, row, col):
        num = self.graph[row][col]
        return num == 3 or num == 1