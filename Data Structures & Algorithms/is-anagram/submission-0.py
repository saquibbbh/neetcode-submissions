class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        new_s = sorted(s)
        new_t = sorted(t)

        if len(new_s) != len(new_t):
            return False

        for a, b in zip(new_s, new_t):
            if a != b:
                return False

        return True