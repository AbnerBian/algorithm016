class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        import heapq
        hashmap=defaultdict(int)
        for i,v in enumerate(nums):
            hashmap[v]+=1
        return [i[0] for i in heapq.nlargest(k,hashmap.items(),key=lambda x:x[1])]

