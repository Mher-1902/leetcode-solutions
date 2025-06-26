class Solution:
    def totalMoney(self, n: int) -> int:
        week = n // 7
        days = n % 7
        full_week = 7 * week * (week-1) // 2 + 28 * week
        remindings = days * (week + 1) + days * (days - 1) // 2
        return full_week + remindings
         



        