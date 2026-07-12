def areCompatible(p1,p2):
    if (p1 == '(' and p2 == ')') or (p1 == '{' and p2 == '}') or (p1 == '[' and p2 == ']') :
        return True
    return False
class Solution:
    def isValid(self, s: str) -> bool:
        opening_stack = []
        op = ['(','{','[']
        cl = []
        for c in s:
            if c in op :
                opening_stack.append(c)
            elif len(opening_stack) != 0 and areCompatible(opening_stack[-1],c):
                opening_stack.pop()
            else:
                return False
        return len(opening_stack)==0

