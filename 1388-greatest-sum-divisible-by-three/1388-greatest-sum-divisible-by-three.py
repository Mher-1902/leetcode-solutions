class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        bucket1,bucket2,bucket3 = [],[],[]
        for i in nums:
            if i % 3 == 0:
                bucket1.append(i)
            elif i % 3 == 1:
                bucket2.append(i)
            else:
                bucket3.append(i)
        bucket2.sort()
        bucket3.sort()
        sum_arr = sum(nums)
        reminder = sum_arr % 3
        if reminder == 1:
            remove2 = bucket2[0] if bucket2 else float('inf')
            remove3 = sum(bucket3[:2]) if len(bucket3) >= 2 else float('inf')  
            if remove2 < remove3:
                sum_arr -= remove2
            else:
                sum_arr -= remove3
        if reminder == 2:
            remove3 = bucket3[0] if bucket3 else float('inf')
            remove2 = sum(bucket2[:2]) if len(bucket2) >= 2 else float('inf')
            if remove2 < remove3:
                sum_arr -= remove2
            else:
                sum_arr -= remove3
        return sum_arr


        