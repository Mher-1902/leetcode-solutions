class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ls = []
        row = len(mat)
        column = len(mat[0])
        if row*column != r*c:
            return mat        
        for i in range(row):
            for j in range(column):
                ls.append(mat[i][j])
        answ = [[0 for _ in range(c)]for _ in range(r)]
        if r == 4 and c == 1:
            for i in range(len(answ)):
                answ[i][0] = ls[i] 
        else:
            for i in range(r):
                for j in range(c):
                    answ[i][j] = ls[i * c + j]
        return answ

        