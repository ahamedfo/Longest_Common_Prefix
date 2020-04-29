class Solution(object):
    def longestCommonPrefix(self, strs):

        if len(strs) == 0:
            return ""

        minimum_length = len(strs[0])
        for i in range(len(strs)):
            minimum_length = min(len(strs[i]), minimum_length)

            i = 0
        chars = ""
        while i < minimum_length:
            StrMe = strs[0][i]
            for j in range(1, len(strs)):

                if strs[j][i] != StrMe:
                    return chars

            chars = chars + StrMe
            i += 1

        return chars