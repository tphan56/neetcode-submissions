class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check both string if they have the same strings

        if len(s) != len(t):
            return False


        char_count = {}

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for char in t:
            if char in char_count and char_count[char] > 0:
                char_count[char] -= 1
            else:
                return False

        return True

        





       





            



        



        