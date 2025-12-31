import time
import threading
import multiprocessing as mp

n = 35
tasks = 10

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def run_sync():
    for _ in range(tasks):
        fib(n)

def run_threads():
    threads = [threading.Thread(target=fib, args=(n,)) for _ in range(tasks)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

def run_processes():
    def _proc_worker(n):
        fib(n)
    procs = [mp.Process(target=_proc_worker, args=(n,)) for _ in range(tasks)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()

def bench(fn):
    t0 = time.perf_counter()
    fn()
    t1 = time.perf_counter()
    return t1 - t0

t_sync = bench(run_sync)
t_thr  = bench(run_threads)
t_proc = bench(run_processes)

print(f"sync:           {t_sync:.3f} s")
print(f"threading:      {t_thr:.3f} s")
print(f"multiprocessing:{t_proc:.3f} s")
