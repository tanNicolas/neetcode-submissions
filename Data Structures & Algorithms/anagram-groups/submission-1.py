from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        original = strs.copy()
        answer = []
        sorted_strs = ["".join(sorted(word)) for word in strs]
        index_map = defaultdict(list)
        answer = []
        for idx, val in enumerate(sorted_strs):
            index_map[val].append(idx)

        for key, val in index_map.items():
            group = [original[i] for i in val]
            answer.append(group)
        return answer
