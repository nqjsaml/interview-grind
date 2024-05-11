class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # can we do better than O(n^2)? iterating through
        # the list twice can't be that bad.
        # observe all fractions p/q are reduced! minheap!
        # (fraction, numerator index, denominator index)
        pq =[(arr[0]/arr[j], 0, j) for j in range(1, len(arr))]
        heapify(pq)
        # now deal with this (k-1) times
        for _ in range(k-1):
            # the top of the minheap is gonna be the smallest
            # fraction
            temp, i, j = heappop(pq)
            # can we get another fraction with the same denom?
            # if yes, push that to the minheap
            if i + 1 < j:
                heappush(pq, (arr[i+1]/arr[j], i+1, j))
        # recall the note from above, same applies
        # and recall the tuple feature
        ans, i, j = pq[0]
        return [arr[i], arr[j]]
