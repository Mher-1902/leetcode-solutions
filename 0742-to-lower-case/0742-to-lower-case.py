class Solution:
    def toLowerCase(self, s: str) -> str:
        srt = ''
        for i in s:
            if ord(i) in range(65,91):       
                srt += chr(ord(i) + 32)
            else:
                srt += i             
        return srt
        