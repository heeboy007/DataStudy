import numpy as np
from scipy import stats

a = np.array([2, 4, 6, 8, 10])
b = np.array([1, 2, 3])

va, vb = a.var(ddof=1), b.var(ddof=1)
dfa, dfb = len(a) - 1, len(b) - 1
print(va, vb, dfa, dfb)

if dfa >= dfb:
    F, d1, d2 = va / vb, dfa, dfb
else: 
    F, d1, d2 = vb / va, dfb, dfa
print(F, d1, d2)

p_two = min(1.0, 2 * min(stats.f.cdf(F, d1, d2), stats.f.sf(F, d1, d2)))
print(round(F, 2), round(p_two, 4))

pooled = (dfa * va + dfb * vb) / (dfa + dfb)
print(pooled)

