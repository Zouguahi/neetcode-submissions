from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1: return [strs]
        d_strs={}
        d_strs = defaultdict(list)
        for word in strs :
            key = "".join(sorted(word))
            d_strs[key].append(word)
        return list(d_strs.values())