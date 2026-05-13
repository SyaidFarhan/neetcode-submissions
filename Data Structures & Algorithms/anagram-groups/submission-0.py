from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}

        for word in strs:
            key = ''.join(sorted(word))  # contoh: "act" -> "act", "cat" -> "act"

            if key not in anag:
                anag[key] = []

            anag[key].append(word)

        return list(anag.values())