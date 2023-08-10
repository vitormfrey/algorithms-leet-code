class SolutionAnagram():

#Essa solução funciona, porém não compara a quantidade de vezes que a letra aparece, podendo falar em test case
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        if len(s) != len(t):
            return False
        for letter in s:
            if letter in hash_map:
                hash_map[letter] += 1
                continue
            else:
                hash_map[letter] = 1
                continue

        for letterT in t:
            if not letterT in hash_map:
                return False
        return True


#Correct implementation
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         counterS, counterT = {}, {}
#
#         if (len(s) != len(t)):
#             return False
#
#         for i in range(len(s)):
#             counterS[s[i]] = 1 + counterS.get(s[i], 0)
#             counterT[t[i]] = 1 + counterT.get(t[i], 0)
#         for c in counterS:
#             if counterS[c] != counterT.get(c, 0):
#                 return False
#         return True