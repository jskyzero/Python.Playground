class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        if 0 == num :
            return ans
        num+=1
        ans.append(1)
        
        temp = ans
        for x in temp:
            if len(ans) == num:
                break
            ans.append(x+1)
            if x == temp[-1]:
                
        return ans

while 1:
    a = Solution()
    n = int(raw_input('>'))
    print a.countBits(n)