class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans  = 0
        for i in num_set:
            if (i-1) not in num_set:
                size = 0
                while (i+size) in num_set:
                    size += 1
                ans = max(ans,size) 
        return ans       