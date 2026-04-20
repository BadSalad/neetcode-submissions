class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {']':'[',
                    '}':'{',
                    ')':'('
                    }
        stack = deque()
        for c in s:
            if c in hash_map:      #without enumerate this just loops over key not the value
                if(stack and stack[-1]==hash_map[c]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                    
        return True if not stack else False

        