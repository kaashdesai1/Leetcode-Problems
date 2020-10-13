class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = ['(', '[', '{']
        closings = [')', ']', '}']
        is_valid = True
        for char in s:
            if char in openings:
                stack.append(char)
            if char in closings:
                if stack:
                    last = stack.pop(-1)
                else:
                    return False
                if (char == ')' and last != '(') or\
                   (char == '}' and last != '{') or \
                   (char == ']' and last != '['):
                    return False
        if stack:
            is_valid = False
        return is_valid
