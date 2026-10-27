class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1: return [strs]
        d_strs={}
        for word in strs :
            key = "".join(sorted(word))
            if key in d_strs :
                d_strs[key].append(word)
            else : d_strs[key]=[word]
        return list(d_strs.values())