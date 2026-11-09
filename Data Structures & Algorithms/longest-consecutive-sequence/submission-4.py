class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans  = 0
        for i in num_set:
            if (i-1) not in num_set: # group the sequences by checking the previous of cur num is present or not
                size = 0
                while (i+size) in num_set: # checking the sequence, if the next is present or not
                    size += 1
                ans = max(ans,size) 
        return ans       