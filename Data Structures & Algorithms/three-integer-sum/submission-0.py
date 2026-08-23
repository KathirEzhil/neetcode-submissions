class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        c = defaultdict(int)

        for n in nums:
            c[n] += 1
        
        ans = []

        for i in range(len(nums)):
            c[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)):
                c[nums[j]] -= 1
                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                t = -(nums[i] + nums[j])
                if c[t] > 0:
                    ans.append([nums[i],nums[j],t])
            for k in range(i+1, len(nums)):
                c[nums[k]] += 1
        return ans
        
        