class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d_nums={}
        for num in nums :
            d_nums[num]=d_nums.get(num,0)+1
        sorted_nums=sorted(d_nums,key=d_nums.get,reverse=True)
        most_frequent=[]
        for i in range(k):
            most_frequent.append(sorted_nums[i])
        return most_frequent