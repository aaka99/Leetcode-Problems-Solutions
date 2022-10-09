    # 2433. Find The Original Array of Prefix Xor
    def findArray(self, A):
        for i in range(len(A) - 1, 0, -1):
            A[i] ^= A[i - 1]
        return A
