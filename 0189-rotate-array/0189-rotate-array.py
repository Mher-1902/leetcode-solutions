from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        dq = deque(nums)
        dq.rotate(k)
        nums[:]=dq
        return nums
        