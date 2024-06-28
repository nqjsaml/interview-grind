class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # from the output it looks like there's just one task
        # here it's to find the common node
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
