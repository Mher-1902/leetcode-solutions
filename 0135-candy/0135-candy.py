class Solution:
    def candy(self, ratings: List[int]) -> int:
        l_t_r = 1
        r_t_l = len(ratings) -2
        candies = [1 for i in range(len(ratings))]
        while l_t_r < len(ratings):
            if ratings[l_t_r] > ratings[l_t_r-1]:
                candies[l_t_r] = candies[l_t_r-1] + 1
            l_t_r += 1
        while r_t_l >= 0:
            if ratings[r_t_l] > ratings[r_t_l+1]:
                candies[r_t_l] = max(candies[r_t_l],candies[r_t_l+1]+1)
            r_t_l -= 1
        return sum(candies)

        