from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k<0:
            return []
        frequency = Counter(nums)
        sorted_map = sorted(frequency.items(),key = lambda x:x[1],reverse = True)
        return [key for key,val in sorted_map[:k]]

        