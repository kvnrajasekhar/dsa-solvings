from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for v in cnt.values():
            if v>1:
                return True
        return False
        