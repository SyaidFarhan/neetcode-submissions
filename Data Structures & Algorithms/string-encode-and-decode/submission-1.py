class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        if len(strs) == 0:
            return encodedStr
        
        for word in strs:
            encodedStr += str(len(word)) + "#" + word
        return encodedStr

    def decode(self, s: str) -> List[str]:
        strs, i = [], 0
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            strs.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return strs
                


        
        