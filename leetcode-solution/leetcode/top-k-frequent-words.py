class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        freq = list(count.values())
        buckets=[[] for i in range(max(freq)+1)]
        for key,val in count.items():
            buckets[val].append(key)
        ans = []
        for i in range(len(buckets)-1,-1,-1):
            buckets[i].sort()
            for j in range(len(buckets[i])):
                if len(ans) < k:
                    ans.append(buckets[i][j])
                else:
                    break
        return ans
        
        
