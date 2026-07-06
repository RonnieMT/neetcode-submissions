class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        square_set = [set() for i in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr_num = board[i][j]
                if curr_num == ".":
                    continue
                if curr_num in row_set[i] or curr_num in col_set[j]:
                    return False
                if curr_num in square_set[(3 * (i//3) + (j//3))]:
                    return False
                
                row_set[i].add(curr_num)
                col_set[j].add(curr_num)
                square_set[(3 * (i//3) + (j//3))].add(curr_num)

        return True
