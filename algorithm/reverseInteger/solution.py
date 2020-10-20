class Solution:
    def reverse(self, x: int) -> int:
        rv = 0
        Max = 2**31-1
        Min = -2**31
        while x != 0:
            if x >= 0:
                pop = x%10
                x //=10
            else:
                pop = x%-10
                x //=-10
                x *= -1
           
            if( rv > Max//10 or (rv == Max//10 and pop > 7) ):
                return 0
            if( rv < -1*(Min//-10) or (rv == -1*(Min//-10) and pop < -8)):
                return 0
            rv = rv*10 + pop
        return rv