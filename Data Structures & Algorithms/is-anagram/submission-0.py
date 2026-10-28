class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortS = sorted(s)
        sortT = sorted(t)

        if len(s) != len(t) or sortS != sortT:
            return False
        if sortS == sortT:
            return True
        