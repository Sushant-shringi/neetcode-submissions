class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        if not nums:
            return 0
        
        
        n = sorted(nums)
        
        
        count = 1
        
        max_count = 1
        
        
        for i in range(len(n) - 1):
            
            if n[i+1] - n[i] == 1:
            
                count += 1
            
            elif n[i+1] == n[i]:
                
                continue
            
            else:
            
                max_count = max(max_count, count)
                
                count = 1
                
        
        max_count = max(max_count, count)
        
        
        return max_count
