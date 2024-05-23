class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # more backtracking, which...
        ans = []

        # helper function to check if string is a palindrome
        # we'll use two pointers here as slicing is less-efficient
        def is_pal(s: str) -> bool:
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        # what we'll probably do is generate every possible substring
        # and go from there.
        def backtrack(start: int, cur: List[str]) -> None:
            # checks if last string is a palindrome
            is_last_pal = is_pal(cur[-1])
            # reached max possible length, so return
            # and add if the last substring was a palindrome
            if start == n:
                if is_last_pal:
                    ans.append(cur[:])
                return
            # appends to the substring if possible
            if is_last_pal:
                cur.append(s[start])
                backtrack(start+1, cur)
                cur.pop()
            # otherwise, add the letter to the last string
            # we will always perform backtracking in this way
            cur[-1] = cur[-1] + s[start]
            backtrack(start+1, cur)
            cur[-1] = cur[-1][:-1]
        
        # notice here we will pass 1, as if the length of s is 1
        # it will always be its own palindrome
        backtrack(1, [s[0]])
        return ans
