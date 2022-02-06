class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for i in range(0,len(operations)):
            if ((operations[i] == "++X") or (operations[i] == "X++")):
                x += 1
            if ((operations[i] == "--X") or (operations[i] == "X--")):
                x -= 1
        return x