# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res=set()
#         def helper(nums,curr_nums,used,depth):
#             if(depth==len(nums)):
#                 res.add(tuple(curr_nums))
#                 return
#             for i,v in enumerate(nums):
#                 if(not used[i]):
#                     if(i>0 and nums[i-1]==nums[i] and not used[i-1]):
#                         continue
#                     used[i]=True
#                     curr_nums.append(v)
#                     helper(nums,curr_nums,used,depth+1)
#                     curr_nums.pop()
#                     used[i]=False
#         helper(nums,[],[False for i in nums],0)
#         return list(res)

import itertools
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(itertools.permutations(iter(nums))))