class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        s_letters = set(s_list)
        s_hash = {l: s_list.count(l) for l in s_letters}

        t_list = list(t)
        t_letters = set(t_list)
        t_hash = {l: t_list.count(l) for l in t_letters}

        return True if s_hash == t_hash else False