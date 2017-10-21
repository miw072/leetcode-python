class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        parenthese_dict = {"{": "}", "[": "]", "(": ")"}
        existing_parenthese = []
        for c in s:
            if c in parenthese_dict.keys():
                existing_parenthese.append(c)
            elif c in parenthese_dict.values():
                if not existing_parenthese or parenthese_dict.get(existing_parenthese.pop()) != c:
                    return False
        return not existing_parenthese
