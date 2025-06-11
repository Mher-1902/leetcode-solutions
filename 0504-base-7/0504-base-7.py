class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        is_negative = num < 0
        num = abs(num)
        
        base7 = ''
        while num > 0:
            base7 = str(num % 7) + base7
            num = num // 7
        
        if is_negative:
            base7 = '-' + base7
        
        return base7
