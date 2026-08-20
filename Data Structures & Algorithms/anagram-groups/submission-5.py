class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for index in strs:
            key = "".join(sorted(index))
            if key not in seen:
                seen[key] = []

            seen[key].append(index)

        return list(seen.values())