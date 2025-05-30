class Solution:
    def dayOfYear(self, date: str) -> int:
        year,month,day = (int(i)for i in date.split('-'))
        feb = 29 if year%400==0 or (year % 4 == 0 and year %100 != 0) else 28
        days_in_month = [0, 31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = sum(days_in_month[:month]) + day
        return res