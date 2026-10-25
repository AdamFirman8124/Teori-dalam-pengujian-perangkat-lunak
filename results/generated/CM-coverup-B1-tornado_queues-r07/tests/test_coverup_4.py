# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio
import contextlib

import pytest

from tornado.queues import Queue, QueueFull, QueueEmpty
from tornado.concurrent import Future


def _run(coro):
    """Run a coroutine to completion on a fresh event loop, then clean up."""
    loop = asyncio.new_event_loop()
    try:
        with contextlib.closing(loop):
            return loop.run_until_complete(coro)
    finally:
        asyncio.set_event_loop(None)


def test_put_nowait_plain_put_else_branch():
    """Covers lines 222-223: no getters waiting, queue not full."""
    q = Queue(maxsize=2)

    async def main():
        q.put_nowait("a")
        assert q.qsize() == 1
        assert not q.empty()
        assert not q.full()
        assert q.get_nowait() == "a"
        assert q.empty()

    _run(main())


def test_put_nowait_full_raises_queuefull():
    """Covers lines 220-221: queue full and no getters waiting."""
    q = Queue(maxsize=1)

    async def main():
        q.put_nowait("only")
        assert q.full()
        with pytest.raises(QueueFull):
            q.put_nowait("overflow")
        # The rejected item must not have been stored.
        assert q.qsize() == 1
        assert q.get_nowait() == "only"

    _run(main())


def test_put_nowait_wakes_waiting_getter():
    """Covers lines 215-219: a getter is waiting, so the item is
    handed directly to it instead of being stored in the queue."""
    q = Queue(maxsize=1)

    async def main():
        getter = q.get()
        assert not getter.done()
        assert q._getters  # getter is registered as waiting

        q.put_nowait("handoff")

        assert getter.done()
        assert getter.result() == "handoff"
        # The item went to the getter, not into the queue.
        assert q.empty()
        assert not q._getters
        with pytest.raises(QueueEmpty):
            q.get_nowait()

    _run(main())


def test_put_nowait_consumes_expired_getter():
    """Covers the loop body of _consume_expired() on line 214 via the
    getters branch: a done (expired) getter is discarded before the
    live getter receives the item."""
    q = Queue()

    async def main():
        # Simulate a getter whose timeout already fired. The Future must
        # be created while the event loop is running.
        expired = Future()
        expired.set_result(None)
        q._getters.append(expired)

        live = q.get()
        assert not live.done()

        q.put_nowait("value")

        # The expired getter was consumed, the live one got the item.
        assert expired not in q._getters
        assert live.done()
        assert live.result() == "value"
        assert q.empty()
        assert not q._getters

    _run(main())


def test_put_nowait_consumes_expired_putter():
    """Covers the loop body of _consume_expired() on line 214 via the
    putters branch: a done (cancelled) putter is discarded, then the
    item is stored normally."""
    q = Queue(maxsize=1)

    async def main():
        q.put_nowait("first")
        assert q.full()

        # q.put() finds the queue full and parks (item, future) in _putters.
        putter = q.put("second")
        assert not putter.done()
        assert len(q._putters) == 1

        # Simulate the putter's timeout having fired.
        putter.cancel()
        assert putter.cancelled()

        # Free the slot, then put again: the expired putter must be
        # consumed by _consume_expired() before the item is stored.
        assert q.get_nowait() == "first"
        q.put_nowait("third")

        assert not q._putters
        assert q.qsize() == 1
        assert q.get_nowait() == "third"
        assert q.empty()

    _run(main())
