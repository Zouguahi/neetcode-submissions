class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d_nums={}
        for num in nums :
            d_nums[num]=d_nums.get(num,0)+1
        sorted_nums=sorted(d_nums,key=d_nums.get,reverse=True)
        return sorted_nums[:k]