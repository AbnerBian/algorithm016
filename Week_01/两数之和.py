#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,v in enumerate(nums):
            hashmap[v]=i
        for i,v in enumerate(nums):
            if(target-v in hashmap and hashmap.get(target-v)!=i):
                return [i,hashmap.get(target-v)]
        return []

# @lc code=end

