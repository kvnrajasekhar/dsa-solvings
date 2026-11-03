class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            curr = ''.join(sorted(s))
            result[curr].append(s)
        return list(result.values())
        