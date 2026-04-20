class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops= ['+','-','/','*']
        stack = deque()
        for t in tokens:
            if t == '+':
                temp = stack.pop() + stack.pop()
                stack.append(temp)
            elif t =='*':
                temp =stack.pop() * stack.pop()
                stack.append(temp)
            elif t == '-':
                a,b =stack.pop(),stack.pop()
                stack.append(b-a)
            elif t == '/':
                a,b =stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(t))
        return int(stack.pop())
