from itertools import combinations
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ls = []
        def tri_area(x1,y1,x2,y2,x3,y3):
            return 0.5 * abs(x1*(y2-y3) + x2*(y3 - y1) + x3*(y1-y2))          
        comb = combinations(points,3)
        for i in comb:
            (x1, y1), (x2, y2), (x3, y3) = i
            ls.append(tri_area(x1, y1, x2, y2, x3, y3))
        return max(ls)