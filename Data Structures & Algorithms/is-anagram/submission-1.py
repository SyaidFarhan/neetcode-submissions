class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            if c not in count:
                return False

            count[c] -=1
        for val in count.values():
            if val !=0:
                return False
        
        return True