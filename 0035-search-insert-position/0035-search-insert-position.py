class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            pass
        else:
            nums.append(target)
        nums.sort()
        arr = nums[:]
        start = 0
        end = len(arr) - 1
        while start <= end:
            middle = (start + end) // 2
            finding_number = arr[middle]
            if target == finding_number:
                return middle
            elif target < finding_number:
                end = middle - 1
            else:
                start = middle + 1
        return -1