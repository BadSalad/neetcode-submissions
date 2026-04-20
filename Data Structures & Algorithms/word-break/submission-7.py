class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def sub(t):
            if t in memo: return memo[t]
            for w in wordDict:
                if not t.startswith(w):
                    continue
                c = t[len(w):]
                if c == "":
                    memo[t] = True
                    return True
                if sub(c):
                    memo[t] = True
                    return True
            memo[t] = False
            return False

        return sub(s)
