class Solution(object):
    def productExceptSelf(self, nums):
        
        p, result = 1, [1]*len(nums)
        
        for i in range(len(nums)-1):
            p = p*nums[i]            
            result[i+1] *= p
        
        p = 1
        
        for i in range(len(nums)-2, -1, -1):
            p = p*nums[i+1]
            result[i] *= p
            
        return result