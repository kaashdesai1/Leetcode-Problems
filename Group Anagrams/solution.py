from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m=defaultdict(lambda:[])
        for s in strs:
            key=''.join(sorted(list(s)))
            m[key].append(s)   
        return [v for k,v in m.items()]
