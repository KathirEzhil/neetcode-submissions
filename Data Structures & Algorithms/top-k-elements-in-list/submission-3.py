class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create histogram
        op = []
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        def return_max_and_pop(d):
            max_key = 0
            max_val = 0
            for i in d:
                if d[i] > max_val:
                    max_key = i
                    max_val = d[i]
            d.pop(max_key,None)
            return max_key
        
        for i in range(k):
            op.append(return_max_and_pop(d))
        return op
            
        
        return op