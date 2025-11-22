class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        column = len(mat[0])
        new_row = r
        new_column = c
        if row*column != new_row*new_column:
            return mat

        flatten = [j for i in mat for j in i]
        res = []
        for i in range(new_row):
            start = i * new_column
            end = start + new_column
            res.append(flatten[start:end])
        return res
