class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # can this be simply brute forced? or we can do bin search
        # let's note that the best way to fit TWO people on a boat
        # is the heaviest person and lightest person
        people.sort()
        ans = 0
        i, j = 0, len(people) - 1
        # two pointers
        while i <= j:
            ans += 1
            # check if can have two people on the boat
            # if yes then can add the lightest person
            if people[i] + people[j] <= limit:
               i += 1
            # must always add the heaviest person
            j -= 1
        return ans
