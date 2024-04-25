class Solution:
    def tribonacci(self, n: int) -> int:
        # very easy if done recursively with memoization
        # so we'll implement it in this way first
        '''
        memo = [0] * 40
        memo[1] = 1
        memo[2] = 1
        for i in range(n):
            memo[i+3] = memo[i] + memo[i+1] + memo[i+2]
        return memo[n]
        '''
        # here, we have a math solution with some known cases
        # thanks @anwendeng
        import numpy as np
        if n == 0:
            return 0
        if n <= 2:
            return 1
        # we have a matrix solution for this, too
        # we have in general a matrix A[0][0] = [[T_n], [T_(n-1)], [T_(n-2)]]
        # where A = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]^(n-2) * [[1], [1], [0]]
        M = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
        A = np.linalg.matrix_power(M, n-2) @ np.array([[1], [1], [0]])
        return A[0, 0]
