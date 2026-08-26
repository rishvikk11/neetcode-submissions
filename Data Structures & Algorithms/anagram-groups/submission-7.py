from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create result array and anagram hashmap
        res = []
        mapping = defaultdict(list)

        # create your map of anagrams by using a tuple to make it immutable
        # in your tuple, you need to sort the items in Counter to make it a common item amongst words
        for s in strs:
            t = tuple(sorted(Counter(s).items()))
            mapping[t].append(s)

        # create your result array using your mapping
        for value in mapping.values():
            res.append(value)

        return res