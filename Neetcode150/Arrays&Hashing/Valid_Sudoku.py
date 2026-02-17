from typing import List
from collections import defaultdict

# best solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subBoxes = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in subBoxes[(i // 3, j // 3)]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                subBoxes[(i // 3, j // 3)].add(board[i][j])
        
        return True

# alternate solution (the first that I have come up when I have seen this question)
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkSubBox() -> bool:
            okSubBox = True

            for i in range(0, len(board), 3):
                for j in range(len(board)):
                    if j % 3 == 0:
                        setSubBox = set()
                    
                    num1 = board[i][j]
                    num2 = board[i + 1][j]
                    num3 = board[i + 2][j]

                    if num1 != '.':
                        if num1 not in setSubBox:
                            setSubBox.add(num1)
                        
                        else:
                            okSubBox = False
                            break
                    
                    if num2 != '.':
                        if num2 not in setSubBox:
                            setSubBox.add(num2)
                        
                        else:
                            okSubBox = False
                            break
                    
                    if num3 != '.':
                        if num3 not in setSubBox:
                            setSubBox.add(num3)
                        
                        else:
                            okSubBox = False
                            break
                
                if okSubBox == False:
                    break
            
            return okSubBox

        def checkRow() -> bool:
            okRow = True
            for row in board:
                setRow = set()
                for num in row:
                    if num != '.':
                        if num not in setRow:
                            setRow.add(num)
                        
                        else:
                            okRow = False
                            break
                
                if okRow == False:
                    break
            
            return okRow
        
        def checkCol() -> bool:
            okCol = True
            for j in range(len(board)):
                setCol = set()
                for i in range(len(board)):
                    num = board[i][j]
                    if num != '.':
                        if num not in setCol:
                            setCol.add(num)
                        
                        else:
                            okCol = False
                            break
                
                if okCol == False:
                    break
            
            return okCol

        return checkCol() and checkRow() and checkSubBox()