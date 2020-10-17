"""
Problem 15: https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid??
"""


class GridNode:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


class Solution:
    def makeStep(self, nextGridNode: GridNode, currentNodeValue: int):

        if nextGridNode in self.paths:
            nextValue = self.paths.get(nextGridNode)
            self.paths[nextGridNode] = nextValue + currentNodeValue
        else:
            self.paths[nextGridNode] = currentNodeValue
            self.nodes.append(nextGridNode)

    def treverseNode(self, currentNode: GridNode):
        if currentNode.x == 0 and currentNode.y == 0:
            return

        currentValue = self.paths.get(currentNode)

        if currentNode.x > 0:
            nextGridNode = GridNode(currentNode.x - 1, currentNode.y)
            self.makeStep(nextGridNode, currentValue)

        if currentNode.y > 0:
            nextGridNode = GridNode(currentNode.x, currentNode.y - 1)
            self.makeStep(nextGridNode, currentValue)

    def calculateRoutes(self) -> int:
        self.paths = dict()
        goalNode = GridNode(20, 20)
        # only one path from end node to adjacent ones
        self.paths[goalNode] = 1
        self.nodes = [goalNode]

        for currentNode in self.nodes:
            self.treverseNode(currentNode)

        return self.paths.get(GridNode(0, 0))


print(Solution().calculateRoutes())
