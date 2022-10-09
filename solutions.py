# 2425. Bitwise XOR of All Pairings
  def xorAllNums(self, A, B):
      x = y = 0
      for a in A:
          x ^= a
      for b in B:
          y ^= b
      return (len(A) % 2 * y) ^ (len(B) % 2 * x)
