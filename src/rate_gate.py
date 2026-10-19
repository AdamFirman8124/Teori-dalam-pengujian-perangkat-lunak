"""Cross-process sliding-window rate gate for provider calls.

CoverUp runs in a child ``python`` process and CodaMOSA runs inside Docker, so
an in-memory limiter in the notebook kernel cannot see their calls.  This gate
keeps one tiny state file (a lock plus a JSON list of call timestamps) that
every producer appends to before each provider request:

- ``acquire(path, limit_per_minute)`` blocks until the last 60 seconds contain
  fewer than ``limit_per_minute`` timestamps, then records the new call.
- ``limit_per_minute <= 0`` (or unset env) disables the gate entirely.
- The gate never fails a call: any I/O problem degrades to "allow".

Only timestamps are stored, so even a burst leaves a file of a few kilobytes.
"""
from __future__ import annotations

import json
import os
import tempfile
import time
from pathlib import Path


def _limit_from_env(default: int = 0) -> int:
    """Read the RPM budget without importing notebook helpers."""
    try:
        return max(0, int(os.getenv("RPM_LIMIT", str(default))))
    except ValueError:
        return 0


def _read_timestamps(path: Path) -> list:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    if not isinstance(data, list):
        return []
    now = time.time()
    return [float(t) for t in data if isinstance(t, (int, float)) and now - t < 75.0]


def _locked(path: Path, mode: str):
    """Best-effort exclusive lock; falls back to no locking on exotic FS."""
    handle = path.open(mode)
    try:
        if os.name == "nt":
            import msvcrt  # noqa: PLC0415

            handle.seek(0, os.SEEK_END)
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl  # noqa: PLC0415

            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
    except OSError:
        pass
    return handle


def _unlock(handle) -> None:
    try:
        if os.name == "nt":
            import msvcrt  # noqa: PLC0415

            handle.seek(0, os.SEEK_END)
            msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            import fcntl  # noqa: PLC0415

            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
    except OSError:
        pass
    finally:
        handle.close()


def acquire(path: str | Path, limit_per_minute: int | None = None) -> float:
    """Block until one provider call fits in the RPM budget; return wait time.

    Returns ``0.0`` when the gate is disabled or cannot be enforced.
    """
    limit = _limit_from_env() if limit_per_minute is None else max(0, int(limit_per_minute))
    if limit <= 0:
        return 0.0
    state = Path(path)
    try:
        state.parent.mkdir(parents=True, exist_ok=True)
    except OSError:
        return 0.0
    waited = 0.0
    lock_path = state.with_suffix(state.suffix + ".lock")
    while True:
        lock = None
        try:
            lock = _locked(lock_path, "a+b")
            now = time.time()
            calls = _read_timestamps(state)
            window = [t for t in calls if now - t < 60.0]
            if len(window) < limit:
                window.append(now)
                tmp_fd, tmp_name = tempfile.mkstemp(
                    dir=str(state.parent), prefix=state.name + ".")
                try:
                    with os.fdopen(tmp_fd, "w", encoding="utf-8") as tmp:
                        json.dump(window, tmp)
                    os.replace(tmp_name, state)
                finally:
                    try:
                        os.unlink(tmp_name)
                    except OSError:
                        pass
                return waited
            sleep_for = 60.0 - (now - window[0]) + 0.05
        except OSError:
            return waited
        finally:
            if lock is not None:
                _unlock(lock)
        time.sleep(max(0.05, min(sleep_for, 2.0)))
        waited += max(0.05, min(sleep_for, 2.0))
