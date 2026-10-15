import numpy as np
from analyze import parse_records, read_lines, ParseStats

actions, ms = [], []
for rec in parse_records(read_lines("access.log"), ParseStats()):
    actions.append(rec.action)
    ms.append(rec.ms)

actions = np.array(actions)
ms = np.array(ms, dtype=np.int32)
print(actions.dtype, actions.nbytes, ms.nbytes)       # 문자열 배열의 dtype은?

names, codes = np.unique(actions, return_inverse=True)
sums = np.bincount(codes, weights=ms)
cnts = np.bincount(codes)
print(dict(zip(names.tolist(), (sums / cnts).round(2).tolist())))