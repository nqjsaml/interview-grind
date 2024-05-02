class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # this should not be a problem, but python strings are immutable
        # let's find first the index
        k = word.find(ch)
        return word[:k+1][::-1] + word[k+1:] if k != -1 else word
