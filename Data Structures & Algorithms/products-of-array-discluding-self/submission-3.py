class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        op = []
        
        def find_prod(nums,i):

            prod = 1

            for j in range(len(nums)):
                if j != i:
                    prod *= nums[j]
            
            return prod
        
        for k in range(len(nums)):
            op.append(find_prod(nums,k))
            
        return op
        

                