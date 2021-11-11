class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        LCP, cmp = "", strs[0]
        for i in range(len(cmp)):
            for str in reversed(strs[1:]):
                if cmp[i] != str[i]:
                    return LCP
            LCP += cmp[i]
        return LCP
