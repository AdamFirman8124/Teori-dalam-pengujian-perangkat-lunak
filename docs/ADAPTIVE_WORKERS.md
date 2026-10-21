# Adaptive Task-Worker Formula

Reference for the worker-count derivation used by `experiments_linux.ipynb`
(`_adaptive_worker_count()` in the runner cell). Reported here so the paper can
cite the exact rule instead of a hand-waved "we tuned the parallelism".

## 1. Purpose

The notebook runs a **matrix of independent jobs**: one job per
`(method, model, dataset, task)` tuple. Jobs are dispatched to a thread pool.
The pool size is *not* fixed: it is recomputed right before the pool is created,
because a long run drifts (other desktop apps close, Docker containers end, RAM
is freed). The rule therefore takes the **minimum of four independent caps**.

## 2. Formula

```
per_task_threads = 1 + max(1, EVAL_MUTANT_WORKERS)

by_cpu  = max(1, floor((CPU - CPU_RESERVED_THREADS) / per_task_threads))

if CodaMOSA is enabled:
    by_cpu = max(1, min(by_cpu,
                        floor((CPU - CPU_RESERVED_THREADS) / CODAMOSA_DOCKER_CPUS)))

by_ram  = max_load                                    if CodaMOSA disabled or RAM unknown
        = max(1, floor((RAM_available_GB - DESKTOP_HEADROOM_GB)
                       / CODAMOSA_RAM_GB_PER_WORKER))  otherwise

workers = max(1, min(by_cpu, by_ram, CONFIG_MAX_LOAD, number_of_pending_jobs))
```

If `AUTO_SCALE` is off, the pool is instead pinned to
`max(1, min(TASK_WORKERS, number_of_pending_jobs))`.

## 3. Why each term exists

| Term | Rationale |
|---|---|
| `per_task_threads = 1 + EVAL_MUTANT_WORKERS` | One pipeline thread dispatches a generator, then evaluates mutants in `EVAL_MUTANT_WORKERS` subprocesses. A slot therefore costs that many CPU threads while measuring. |
| `CPU_RESERVED_THREADS` (default 2) | Kept free for the desktop and for the SSH/VS Code Remote session. Without it a saturated host drops the remote connection. |
| `CODAMOSA_DOCKER_CPUS` | Each CodaMOSA job starts a container capped at this many CPUs. When this cap is *larger* than `per_task_threads`, the container — not the host pool — becomes the CPU bound. |
| `RAM_available_GB` | Read live via `psutil.virtual_memory().available`, not total RAM, so buff/cache is excluded. |
| `DESKTOP_HEADROOM_GB` (default 4, floor 2) | Reserve for the OS, the remote session and the Docker VM itself. |
| `CODAMOSA_RAM_GB_PER_WORKER` | Expected peak RAM of one container. Must be set below the Docker VM limit, otherwise `by_ram` collapses to 1. |
| `CONFIG_MAX_LOAD` | Hard operator cap; the formula may never exceed it. |
| `len(_task_jobs)` | No point starting more workers than there are remaining jobs. |

`by_ram` deliberately uses `CONFIG_MAX_LOAD` when CodaMOSA is disabled: a
CoverUp-only run spawns no containers, so the container-RAM term does not apply.

## 4. Worked example (the machine used for the reported run)

Measured inputs: `CPU = 12`, `CPU_RESERVED_THREADS = 2`, `EVAL_MUTANT_WORKERS = 2`,
`CODAMOSA_DOCKER_CPUS = 2`, `RAM_available ≈ 7.8 GB`, `DESKTOP_HEADROOM_GB = 2`,
`CODAMOSA_RAM_GB_PER_WORKER = 1`, `CONFIG_MAX_LOAD = 4`, both methods enabled.

```
per_task_threads = 1 + 2 = 3
by_cpu  = floor((12 - 2) / 3) = 3
          CodaMOSA: floor((12 - 2) / 2) = 5  ->  min(3, 5) = 3
by_ram  = floor((7.8 - 2) / 1) = 5
workers = max(1, min(3, 5, 4, pending)) = 3
```

So the pool runs **3 workers**, even though `TASK_WORKERS` and
`CONFIG_MAX_LOAD` allow 4: the binding term is `by_cpu`.

## 5. Sensitivity table (same machine)

| `EVAL_MUTANT_WORKERS` | `per_task_threads` | `by_cpu` | Effective workers |
|---|---|---|---|
| 1 | 2 | 5 | 4 (capped by `CONFIG_MAX_LOAD=4`) |
| 2 | 3 | 3 | **3 (current)** |
| 3 | 4 | 2 | 2 |

Raising `TASK_WORKERS` alone does nothing while `by_cpu` is the minimum. To
raise the pool, lower `EVAL_MUTANT_WORKERS` or raise `CONFIG_MAX_LOAD` *and*
keep `by_cpu` above the desired value.

## 6. Measured effect of the correction

Before the fix the setup cell overwrote `.env` with `os.environ.update()`,
pinning `TASK_WORKERS=2`, `CODAMOSA_RAM_GB_PER_WORKER=5` and
`CODAMOSA_DOCKER_CPUS=3`. With `RAM_available ≈ 7.4 GB` and
`DESKTOP_HEADROOM_GB=4`, `by_ram` became `floor((7.4-4)/5) = 0 -> 1`, so the
pool ran **1 worker**. After switching the preset to `setdefault()` and tuning
`.env` (`RAM_PER_WORKER=1`, `HEADROOM=2`, `CONFIG_MAX_LOAD=4`), the pool runs
**3 workers**.

Observed throughput on the MT suite (163 tasks x 2 methods):

| Configuration | Effective workers | Throughput |
|---|---|---|
| Old (`_HW_PROFILE` forced, RAM_PER_WORKER=5) | 1 | ~50 task/h |
| Current (`.env` respected, 3 workers) | 3 | ~145 task/h |

That is a **~2.9x** speed-up, consistent with the 3x worker increase (the run is
I/O-bound on the provider, so per-worker latency is roughly unchanged).

## 7. What this formula does *not* model

- **Provider rate limit.** `RPM_LIMIT` throttles only the discovery/preflight
  probes, not the per-task generator loop. Raising workers past the provider's
  real throughput yields queuing and HTTP 429 retries rather than speed-up.
- **Per-task latency variance.** CodaMOSA median wall time is ~36 s versus
  ~9 s for CoverUp on MT, so throughput depends on the method mix still pending.
- **Docker VM memory.** `docker info` reports the VM limit (3.57 GiB here), not
  host RAM. Containers measured ~51 MB each, so this was not binding, but
  `CODAMOSA_RAM_GB_PER_WORKER` must stay below the VM limit or `by_ram` collapses.

## 8. Reproducing the numbers

```bash
grep -E "^(TASK_WORKERS|CONFIG_MAX_LOAD|EVAL_MUTANT_WORKERS|CODAMOSA_DOCKER_CPUS|CODAMOSA_RAM_GB_PER_WORKER|DESKTOP_HEADROOM_GB|CPU_RESERVED_THREADS|AUTO_SCALE)=" config/.env
docker info --format 'MemTotal={{.MemTotal}} NCPU={{.NCPU}}'
```

The runner prints the resolved values once per run:

```
Adaptive workers: <n> (cpu=..., ram_avail=..., by_cpu=..., by_ram=..., cap=...)
```

Because `nbclient` buffers stdout until the notebook finishes, this line is
written to the executed notebook (`executed.ipynb`) rather than the live log.
