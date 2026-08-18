class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        for i, v in enumerate(t):
            if t[i] in s:
                s = s[:s.find(v)] + s[s.find(v)+1:]
            else:
                return False

        return True
        