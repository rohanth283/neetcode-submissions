class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mp = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or stack[-1] != mp[ch]:
                    return False

                else:
                    stack.pop()

        return len(stack) == 0

