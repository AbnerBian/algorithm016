# import functools 
# class Solution:
#     @functools.lru_cache
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res=[]
#         path=[x for x in range(1,n+1)]
#         def helper(i,s):
#             if(i==k):
#                 res.append(s)
            
#             if(i<k):
#                 for x in path :
#                     if(x not in s and s and path.index(x)>path.index(s[-1])):
#                         helper(i+1,s+[x])
#                     if(not s):
#                         helper(i+1,s+[x])
#         helper(0,[])
#         return res

# import itertools
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         return list(itertools.combinations(range(1,n+1),k))
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=list(range(1,n+1))
        res=[]
        if(k==0 or k==0):return []
        def helper(nums,curr_nums,i):
            if(i==k):
                res.append(curr_nums[:])
            for index,value in enumerate(nums):
                curr_nums.append(value)
                helper(nums[index+1:],curr_nums,i+1)
                curr_nums.pop()
        helper(nums,[],0)
        return res