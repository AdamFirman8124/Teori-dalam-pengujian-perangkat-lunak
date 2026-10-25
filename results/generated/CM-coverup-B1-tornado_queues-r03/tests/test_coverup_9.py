# file: project/tornado/queues.py:225-254
# asked: {"lines": [248, 249, 250, 251, 252, 253, 254], "branches": []}
# gained: {"lines": [248, 249, 250, 251, 252, 253, 254], "branches": []}

import datetime

from tornado.ioloop import IOLoop
from tornado.queues import Queue
from tornado.util import TimeoutError


def run_sync(coro):
    """Run a coroutine on a fresh IOLoop (Python 3.12+ has no implicit loop)."""
    loop = IOLoop()
    try:
        return loop.run_sync(coro)
    finally:
        loop.close(all_fds=False)


def test_get_returns_item_immediately():
    """Covers lines 248-250: future created and resolved via get_nowait."""
    q = Queue()
    q.put_nowait("item")

    async def main():
        return await q.get()

    result = run_sync(main)
    assert result == "item"
    assert q.empty()
    assert len(q._getters) == 0


def test_get_blocks_until_put():
    """Covers lines 251-253 (QueueEmpty branch, timeout=None)."""
    q = Queue()

    async def main():
        fut = q.get()
        assert not fut.done()
        assert len(q._getters) == 1
        q.put_nowait(42)
        return await fut

    result = run_sync(main)
    assert result == 42
    assert len(q._getters) == 0


def test_get_timeout_raises():
    """Covers line 253 with a numeric timeout, exercising _set_timeout."""
    q = Queue()

    async def main():
        fut = q.get(timeout=0.01)
        try:
            await fut
        except TimeoutError:
            return fut
        return None

    fut = run_sync(main)
    assert fut is not None
    assert fut.done()
    assert isinstance(fut.exception(), TimeoutError)
    # The expired getter is only reaped by _consume_expired (called from
    # put_nowait/get_nowait), so it is still queued here.
    assert len(q._getters) == 1
    q.put_nowait("later")
    assert len(q._getters) == 0
    assert q.get_nowait() == "later"
    assert q.empty()


def test_get_timedelta_timeout():
    """Covers line 253 with a datetime.timedelta timeout."""
    q = Queue()

    async def main():
        fut = q.get(timeout=datetime.timedelta(seconds=0.01))
        try:
            await fut
        except TimeoutError:
            return fut
        return None

    fut = run_sync(main)
    assert fut is not None
    assert fut.done()
    assert isinstance(fut.exception(), TimeoutError)
    assert len(q._getters) == 1
    q.put_nowait("later")
    assert len(q._getters) == 0
    assert q.get_nowait() == "later"
    assert q.empty()
