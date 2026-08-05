class Solution:
    def isValid(self, s: str) -> bool:

        stack = list()

        for c in s:
            if c == ' ':
                continue
            if c == '[' or c == '{' or c == '(':
                stack.append(c)

            elif(not stack):
                return False
            else: 
                top_element = stack.pop()

                if (top_element == '[' and c == ']') or (top_element == '{' and c == '}' or (top_element == '(' and c == ')')):
                    continue

                else:
                    return False

        return True if (not stack) else False