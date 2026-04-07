class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                index = ord(ch) - ord('a')
                count[index] += 1

            groups[tuple(count)].append(s)

        return list(groups.values())     



