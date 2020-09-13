#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new=[]
        while(digits and digits[-1]==9):
            digits.pop()
            new.append(0)
        if(not digits):
            return [1]+new
        else:
            digits[-1]+=1
            return digits+new


        
# @lc code=end

