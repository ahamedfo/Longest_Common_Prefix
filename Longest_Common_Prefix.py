class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = list()

        for chars in zip(*strs):
            print(chars)
            print(zip(strs))
            if len(set(chars)) != 1:
                break
            else:
                prefix.append(chars[0])

        return ''.join(prefix)