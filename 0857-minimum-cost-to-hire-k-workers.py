class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # is this some sort of minheap question
        # yes, minheap!!!!!!!! thanks @bhanu_bhakta
        n = len(quality)
        # sum of all workers considered
        qual = 0.0
        ans = float('inf')
        # minheap based on worker's wage-quality ratio
        wq_ratio = []
        for i in range(n):
            # (ratio from division, quality)
            heappush(wq_ratio, (wage[i]/quality[i], quality[i]))
        # maxheap for highest quality workers
        hq_workers = []
        # now for all the workers:
        for i in range(n):
            r, q = heappop(wq_ratio)
            qual += q
            heappush(hq_workers, -q)
            # maintains the k-required group size
            # removes the highest-quality worker
            # if more than k workers
            if len(hq_workers) > k:
                qual += heappop(hq_workers)
            # update answer accordingly if exactly k
            if len(hq_workers) == k:
                ans = min(ans, qual * r)
        return ans
