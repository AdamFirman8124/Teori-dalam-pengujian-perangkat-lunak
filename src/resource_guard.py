from __future__ import annotations

import os
import re

RESERVE_RAM_MB = 2048  # 2 GB left free for OS / navigation / desktop


def read_mem_available_mb() -> int:
    try:
        with open("/proc/meminfo", "r", encoding="utf-8") as handle:
            for line in handle:
                if line.startswith("MemAvailable:"):
                    return int(line.split()[1]) // 1024
    except OSError:
        pass
    return 0


def parse_memory_mb(value: str | int) -> int:
    if isinstance(value, int):
        return value
    text = str(value).strip().lower()
    m = re.match(r"^(\d+)([kmg]?)$", text)
    if not m:
        return 0
    amount = int(m.group(1))
    unit = m.group(2)
    if unit == "g":
        return amount * 1024
    if unit == "m":
        return amount
    return amount // 1024


def physical_cpus() -> int:
    """Count physical CPU cores, not hardware threads."""
    try:
        cores = set()
        phys_id = None
        core_id = None
        with open("/proc/cpuinfo", "r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if line.startswith("physical id"):
                    phys_id = line.split(":", 1)[1].strip()
                elif line.startswith("core id"):
                    core_id = line.split(":", 1)[1].strip()
                elif not line:
                    if phys_id is not None and core_id is not None:
                        cores.add((phys_id, core_id))
                    phys_id = None
                    core_id = None
            if phys_id is not None and core_id is not None:
                cores.add((phys_id, core_id))
        if cores:
            return len(cores)
    except OSError:
        pass
    try:
        return len(os.sched_getaffinity(0))
    except AttributeError:
        return os.cpu_count() or 1


def plan_workers(
    configured_workers: int,
    worker_memory: str | int,
    *,
    reserve_mb: int = RESERVE_RAM_MB,
    max_workers: int | None = None,
) -> int:
    """Choose worker count that keeps ``reserve_mb`` free for the OS.

    Boosts workers only when spare RAM exceeds the reserve; never exceeds the
    configured limit or physical cores.
    """
    worker_mb = parse_memory_mb(worker_memory)
    if worker_mb <= 0:
        worker_mb = 512
    caps = physical_cpus() if max_workers is None else min(physical_cpus(), max_workers)
    available = read_mem_available_mb()
    headroom = max(0, available - reserve_mb)
    ram_workers = headroom // worker_mb if worker_mb else 0
    effective = max(1, min(configured_workers, caps, ram_workers))
    return effective
