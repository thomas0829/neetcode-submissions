class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for v in s:
            if v == "{" or v == "(" or v == "[":
                ans.append(v)
            else:
                if len(ans) == 0:
                    return False
                p = ans.pop()
                if p == "{" and v != "}":
                    return False
                elif p == "(" and v != ")":
                    return False
                elif p == "[" and v != "]":
                    return False
        if len(ans) != 0:
            return False

        return True