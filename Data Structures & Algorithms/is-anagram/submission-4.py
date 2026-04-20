class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s ={}
        set_s=set()
        hash_t ={}
        set_t =set()
        for i in s:
            set_s.add(i)
            if i in set_s:
                hash_s[i] = hash_s.get(i,0)+1
            else:
                hash_s[i] = 0
        for i in t:
            set_t.add(i)
            if i in set_t:
                hash_t[i] = hash_t.get(i,0)+1
            else:
                hash_t[i] = 0
        return hash_s == hash_t        