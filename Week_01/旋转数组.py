class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(nums,start,end):
            while(start<end):
                nums[start],nums[end]=nums[end],nums[start]
                start,end=start+1,end-1
        k=k%len(nums)
        reverse(nums,0,len(nums)-k-1)
        reverse(nums,len(nums)-k,len(nums)-1)
        reverse(nums,0,len(nums)-1)