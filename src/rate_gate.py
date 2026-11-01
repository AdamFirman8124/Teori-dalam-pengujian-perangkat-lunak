"""Cross-process sliding-window rate gate and in-flight serializer for provider calls.

CoverUp runs in a child ``python`` process and CodaMOSA runs inside Docker, so
an in-memory limiter in the notebook kernel cannot see their calls.  This gate
keeps one tiny state file (a lock plus a JSON list of call timestamps) and an
in-flight lock that every producer coordinates on before each provider request:

- ``acquire(path, limit_per_minute)``:
  1. Serializes in-flight execution: blocks while any previous request is still
     in-flight (waiting for the provider to answer), preventing overlapping calls.
  2. Enforces RPM budget: ensures fewer than ``limit_per_minute`` (default 20)
     requests in any 60-second window.
  3. Enforces inter-call spacing: requires at least ``60.0 / limit_per_minute``
     seconds (e.g. 3.0s for 20 RPM) between calls to prevent prompt cache collisions.
  4. Keeps the in-flight lock held until ``release(path)`` is called.
- ``release(path)``:
  Releases the in-flight lock once the LLM response is received and records
  completion time.
- ``limit_per_minute <= 0`` disables rate gating.
"""
from __future__ import annotations

import contextlib
import json
import os
import tempfile
import time
from pathlib import Path
from typing import Any

_INFLIGHT_LOCKS: dict[str, Any] = {}


def _limit_from_env(default: int = 20) -> int:
    """Read the RPM budget without importing notebook helpers."""
    try:
        return max(0, int(os.getenv("RPM_LIMIT", str(default))))
    except ValueError:
        return default


def _read_timestamps(path: Path) -> list[float]:
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
        try:
            handle.close()
        except OSError:
            pass


def acquire(path: str | Path, limit_per_minute: int | None = None) -> float:
    """Block until one provider call fits in the RPM budget and previous call answered.

    Returns waited seconds. Keeps an in-flight lock held until ``release(path)``
    is called.
    """
    limit = _limit_from_env() if limit_per_minute is None else max(0, int(limit_per_minute))
    state = Path(path)
    try:
        state.parent.mkdir(parents=True, exist_ok=True)
    except OSError:
        return 0.0

    waited = 0.0
    state_str = str(state.resolve())

    # 1. Release previous in-flight lock held by this thread/process if not freed
    if state_str in _INFLIGHT_LOCKS:
        old_lock = _INFLIGHT_LOCKS.pop(state_str, None)
        if old_lock is not None:
            _unlock(old_lock)

    # 2. Acquire in-flight serialization lock (blocks while another request is in-flight)
    inflight_path = state.with_suffix(state.suffix + ".inflight")
    t_lock_start = time.time()
    inflight_lock = _locked(inflight_path, "a+b")
    waited += time.time() - t_lock_start

    if limit <= 0:
        _INFLIGHT_LOCKS[state_str] = inflight_lock
        return waited

    min_spacing = 60.0 / limit  # 3.0 seconds for 20 RPM
    lock_path = state.with_suffix(state.suffix + ".lock")

    while True:
        lock = None
        sleep_for = 0.0
        try:
            lock = _locked(lock_path, "a+b")
            now = time.time()
            calls = _read_timestamps(state)
            window = [t for t in calls if now - t < 60.0]

            # Spacing check: ensure at least min_spacing since last registered call
            if window and (now - window[-1]) < min_spacing:
                sleep_for = max(sleep_for, min_spacing - (now - window[-1]))

            # Capacity check: ensure fewer than limit calls in 60s window
            if len(window) >= limit:
                sleep_for = max(sleep_for, 60.0 - (now - window[0]) + 0.05)

            if sleep_for <= 0.0:
                window.append(now)
                tmp_fd, tmp_name = tempfile.mkstemp(dir=str(state.parent), prefix=state.name + ".")
                try:
                    with os.fdopen(tmp_fd, "w", encoding="utf-8") as tmp:
                        json.dump(window, tmp)
                    os.replace(tmp_name, state)
                finally:
                    try:
                        os.unlink(tmp_name)
                    except OSError:
                        pass
                _INFLIGHT_LOCKS[state_str] = inflight_lock
                return waited
        except OSError:
            _INFLIGHT_LOCKS[state_str] = inflight_lock
            return waited
        finally:
            if lock is not None:
                _unlock(lock)

        step = max(0.05, min(sleep_for, 2.0))
        time.sleep(step)
        waited += step
        _add_wait(state, step)


def release(path: str | Path) -> None:
    """Release the in-flight lock after the provider response has answered."""
    state = Path(path)
    state_str = str(state.resolve())
    lock = _INFLIGHT_LOCKS.pop(state_str, None)
    if lock is not None:
        _unlock(lock)


@contextlib.contextmanager
def gate(path: str | Path, limit_per_minute: int | None = None):
    """Context manager wrapping request in rate gate and in-flight lock."""
    acquire(path, limit_per_minute)
    try:
        yield
    finally:
        release(path)


def _add_wait(state: Path, seconds: float) -> None:
    """Accumulate total quota-wait seconds in ``<state>.wait`` (best effort)."""
    try:
        path = state.with_suffix(state.suffix + ".wait")
        previous = 0.0
        if path.exists():
            previous = float(path.read_text(encoding="utf-8").strip() or 0.0)
        path.write_text(f"{previous + seconds:.3f}\n", encoding="utf-8")
    except (OSError, ValueError):
        pass


def total_wait(path: str | Path) -> float:
    """Seconds spent waiting for the RPM gate, or 0.0 when unavailable."""
    try:
        return float(Path(str(path) + ".wait").read_text(encoding="utf-8").strip() or 0.0)
    except (OSError, ValueError):
        return 0.0
