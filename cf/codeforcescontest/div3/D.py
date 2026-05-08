from math import comb

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        # Since n = 2^d, we can find d
        d = n.bit_length() - 1
        
        count_can_win = 0
        
        # For each bit length from 1 to d (numbers less than n)
        for bits in range(1, d + 1):
            # Maximum popcount that allows winning within k moves
            max_popcount = k - bits + 1
            
            if max_popcount < 1:
                continue
            
            # Count numbers with this bit length and popcount ≤ max_popcount
            for pc in range(1, min(max_popcount + 1, bits + 1)):
                # Numbers with bit_length = bits and popcount = pc
                # The first bit is always 1, choose pc-1 ones from remaining bits-1
                count_can_win += comb(bits - 1, pc - 1)
        
        # Handle n itself (bit_length = d+1, popcount = 1)
        max_popcount_for_n = k - (d + 1) + 1
        if max_popcount_for_n >= 1:
            count_can_win += 1
        
        # Numbers where Alice cannot win are total minus those where she can win
        print(n - count_can_win)

if __name__ == "__main__":
    solve()