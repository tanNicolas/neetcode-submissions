class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        s_letters = set(s_list)

        t_list = list(t)
        t_letters = set(t_list)

        if s_letters != t_letters:
            return False

        s_hash = {l: s_list.count(l) for l in s_letters}
        t_hash = {l: t_list.count(l) for l in t_letters}

        return True if s_hash == t_hash else False