class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods=[1]*len(nums)
        pref = 1
        for i in range(len(nums)):
            prods[i]=pref
            pref= pref*nums[i]
        post=1
        for i in range(len(nums)-1,-1,-1) :
            prods[i]*=post
            post*=nums[i]
        return prods