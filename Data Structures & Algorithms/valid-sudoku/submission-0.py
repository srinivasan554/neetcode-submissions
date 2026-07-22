class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(0,9)]
        col_set = [set() for _ in range(0,9)]
        sq_set = [[set() for _ in range(0,3)] for _ in range(3)]


        for i in range (9):
            for j in range(9):
                cur = board[i][j]
                if(cur == "."):
                    continue
                else:
                    if(cur in row_set[i] or cur in col_set[j] or cur in sq_set[i//3][j//3]):
                        return False
                    else:
                        row_set[i].add(cur)
                        col_set[j].add(cur)
                        sq_set[i//3][j//3].add(cur)

        return True
