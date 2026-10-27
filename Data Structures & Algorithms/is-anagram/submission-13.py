class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (not s and t) or (s and not t):
            return False
            
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return sorted_s == sorted_t