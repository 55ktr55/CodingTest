from collections import deque


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        dict1 = {"(" : ")", "[" : "]", "{" : "}"}
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if(len(stack) == 0 or s[i] != dict1[stack.pop()]):
                    return False

        return True if len(stack) == 0 else False

