class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # at most ONE letter appears an odd number of times
        # surely there is some sort of math solution for this?
        # nope, bit manipulation. gotta get better at this!
        ans = 0
        bitmask = 0
        # this dict stores the value of the bitmask encountered
        counts = defaultdict(int)
        # this assumes the empty string case
        counts[0] = 1
        for c in word:
            # toggles the bit for the current character in masked state
            # this is accomplished by xoring
            bitmask ^= 1 << (ord(c) - ord('a'))
            # and adds to answer based on counts previously seen
            # as duplicate substrings in different positions count
            ans += counts[bitmask]
            # check all masks that differ by one bit
            # must iterate over the letters we can see (a~j)
            for i in range(10):
                # need to complement the current state to add to ans
                # this is the number of times the bit state
                # differs
                ans += counts[bitmask^(1<<i)]
            # finished processing this substring so we've seen before
            counts[bitmask] += 1
        return ans
