from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        elements = counter.most_common(k)

        return list(dict(elements))
        #answer = []
        #for i in (new.keys()):
        #    answer.append(i)

        #return answer

        
        