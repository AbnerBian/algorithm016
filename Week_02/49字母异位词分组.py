# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         from collections import defaultdict
#         res=defaultdict()
#         for item in strs:
#             res[sorted(item)].append(item)
#         return res.values
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            print(key)
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())