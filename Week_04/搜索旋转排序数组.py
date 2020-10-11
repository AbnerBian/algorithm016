class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=left+(right-left)//2  
            if(nums[mid]==target):
                return mid
            if(nums[mid]>nums[right]):
                if(nums[mid]>target and target>=nums[0]):
                    right=mid-1
                else:
                    left=mid+1
            else:
                if(nums[mid]<target and target<=nums[right]):
                    left=mid+1
                else:
                    right=mid-1
        return -1