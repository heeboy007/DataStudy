
import time
from collections import Counter
from dataclasses import dataclass, field
from functools import wraps
import tracemalloc

def timed(repeat=1):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            t = time.perf_counter()
            for _ in range(repeat):
                r = fn(*args, **kwargs)
            ms = (time.perf_counter() - t) / repeat * 1000
            print(f"{fn.__name__}: {ms:.3f} ms/call")
            return r
        return wrapper
    return deco

@dataclass(frozen=True, slots=True)
class Record:
    ts: str
    level: str
    user: str
    action: str
    ms: int

@dataclass
class ParseStats:
    errors: Counter = field(default_factory=Counter)
    samples: list = field(default_factory=list)

def read_lines(path):
    with open(path, "r") as f:
        for line in f:
            yield line.rstrip()

def parse_line(line):
    tokens = line.split()
    if len(tokens) != 6:
        #print("format err")
        raise ValueError("format")
    # f.write(f"{stamp} {level} user={user} action={action} ms={ms}\n")
    tokens[3:] = (t.split("=")[1] for t in tokens[3:])
    date_stamp, time_stamp, level, user, action, ms = tokens
    try:
        ms = int(ms)
    except ValueError:
        #print("ms err")
        raise ValueError("ms")
    return Record(f"{date_stamp} {time_stamp}", level, user, action, ms)

def parse_records(lines, stats):
    for no, line in enumerate(lines, start=1):
        try:
            rec = parse_line(line)
            if len(stats.samples) >= 3:
                _, *stats.samples = [*stats.samples[-3:], (no, rec)]
            else:
                stats.samples.append((no, rec))
            yield rec
        except ValueError as e:
            #print("error: ", e)
            stats.errors[e.args[0]] += 1

@timed()
def analyze(path):
    stats = ParseStats()
    by_level = Counter()
    pair_count = Counter()
    ms_sum, ms_cnt = Counter(), Counter()
    for rec in parse_records(read_lines(path), stats):
        by_level[rec.level] += 1 
        pair_count[(rec.user, rec.action)] += 1
        ms_sum[rec.action] += rec.ms
        ms_cnt[rec.action] += 1
    return {
        "stats": stats,
        "by_level": by_level,
        "pair_count": pair_count,
        "avg_ms": {a: ms_sum[a] / ms_cnt[a] for a in ms_cnt}
    }

# test1
@timed()
def lazy_read(path):
    yield from read_lines(path)

# test2
def peak_mb(fn):
    tracemalloc.start()
    fn()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1e6

def as_list():
    return len(list(parse_records(read_lines("access.log"), ParseStats())))

def as_stream():
    return sum(1 for _ in parse_records(read_lines("access.log"), ParseStats()))

if __name__ == "__main__":
    # result = analyze("access.log")
    # stats = result["stats"]
    # print(result)
    # assert stats.errors == Counter(format=200, ms=200), stats.errors
    # assert sum(result["by_level"].values()) == 199_600
    # assert sum(result["pair_count"].values()) == 199_600
    # assert len(stats.samples) == 3
    # print("검증 통과")
    # print(stats.samples)
    # print(result["by_level"].most_common())
    # print(result["pair_count"].most_common(3))
    # slowest = sorted(result["avg_ms"].items(), key=lambda kv: kv[1], reverse=True)
    # print(slowest[:3])    # 예측: 1위와 2위는? 생성기의 EXTRA를 보고 먼저 맞혀 보기

    # g = lazy_read("access.log")
    # print("생성 직후")
    # n = sum(1 for _ in g)

    as_list_peak, as_stream_peak = peak_mb(as_list), peak_mb(as_stream)
    print(f"list: {as_list_peak:.1f} MB / stream: {as_stream_peak:.3f} MB x{as_list_peak / as_stream_peak}")

