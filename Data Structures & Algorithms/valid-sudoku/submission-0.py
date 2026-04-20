class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def valid(lis):
            unique = set()
            for i in lis:
                if i==".":
                    continue
                if (i < "1") or (i >"9") or (i in unique):
                    return False
                unique.add(i)
            return True

        def flatten(lis):
            out = []
            for i in range(len(lis)):
                for j in range(len(lis[0])):
                    out.append(lis[i][j])
            return out
        
        for i in range(9):
            row = board[i]
            col = [board[r][i] for r in range(9)]

            if not valid(row) or not valid(col):
                return False
        

        # for r in range(9):
        #     for c in range(9):
        #         if ((r+1)%3==0 and (c+1)%3==0):
        #             block =[]
        #             block = board[r-2:r+1][c-2:c+1]
        #             lis = flatten(block)
        #             if not valid(lis):
        #                 return block

        for r in range(9):
            for c in range(9):
                if (r + 1) % 3 == 0 and (c + 1) % 3 == 0:
                    block = []
                    for i in range(r - 2, r + 1):
                        block.extend(board[i][c - 2:c + 1])
        
                    if not valid(block):
                        return False

        
        return True