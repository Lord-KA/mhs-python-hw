import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

n_iter = 10000000

def bench(fn, *args):
    t0 = time.perf_counter()
    res = fn(*args)
    t1 = time.perf_counter()
    return t1 - t0, res

def integral(f, a, step, start_i, end_i):
    acc = 0.0
    x = a + start_i * step
    for _ in range(start_i, end_i):
        acc += f(x) * step
        x += step
    return acc

def integrate_parallel(executor_cls, f, a, b, n_jobs):
    step = (b - a) / n_iter
    n_jobs = min(n_jobs, n_iter)

    chunk = n_iter // n_jobs
    ranges = []
    start = 0
    for j in range(n_jobs):
        end = start + chunk
        if j == n_jobs - 1:
            end = n_iter
        ranges.append((start, end))
        start = end

    with executor_cls(max_workers =n_jobs) as ex:
        futs = [
            ex.submit(integral, f, a, step, start_i, end_i)
            for (start_i, end_i) in ranges
        ]
        return sum(f.result() for f in futs)

a = 0.0
b = math.pi / 2
max_jobs = 8
EPS = 0.0000001

for n_jobs in range(1, max_jobs + 1):
    t_thr, r_thr = bench(
        integrate_parallel, ThreadPoolExecutor, math.cos, a, b, n_jobs
    )
    t_proc, r_proc = bench(
        integrate_parallel, ProcessPoolExecutor, math.cos, a, b, n_jobs
    )
    assert(r_thr - r_proc < EPS)
    print(f"{n_jobs} | {t_thr:3f} | {t_proc:3f}")
