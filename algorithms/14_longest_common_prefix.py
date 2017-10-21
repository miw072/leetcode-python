class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ''
        if not strs:
            return ret
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs, key=lambda k: len(k))
        for i, c in enumerate(strs[0]):
            for curr_str in strs[1:]:
                if curr_str[i] != c:
                    return ret
            else:
                ret += c
        return ret
