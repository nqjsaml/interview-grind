class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # could just sort the array in decreasing order
        # and then return the array as it appears
        # before we sort, though, we need to keep track of the index
        # of each athlete's score, maybe a map?
        sorted_score = sorted(score, reverse=True)
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        mp = {score: medals[i] if i < 3 else str(i+1) for i, score in enumerate(sorted_score)}
        return [mp[s] for s in score]
