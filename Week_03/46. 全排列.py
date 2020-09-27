class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length=len(nums)
        res=[]
        def helper(nums,curr_nums):
            if(not nums):
                res.append(curr_nums[:])
                return
            for i,v in enumerate(nums):
                curr_nums.append(v)
                a=nums[:]
                a.pop(i)
                helper(a,curr_nums)
                curr_nums.pop()
        helper(nums,[])
        return res