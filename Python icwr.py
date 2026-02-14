from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)

# Urutkan string
s = sorted(s)

# Generate dan print kombinasi
for comb in combinations_with_replacement(s, k):
    print(''.join(comb))
