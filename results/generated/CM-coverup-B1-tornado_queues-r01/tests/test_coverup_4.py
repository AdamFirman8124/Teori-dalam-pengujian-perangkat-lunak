# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio
import datetime

import pytest

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue, QueueFull


@pytest.fixture
def io_loop():
    """Provide a fresh, current asyncio event loop and clean it up after."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        asyncio.set_event_loop(None)
        loop.close()


def test_put_nowait_resolves_waiting_getter(io_loop):
    """Lines 215-219: a waiting getter is resolved with the put item."""
    async def body():
        q = Queue()
        getter = q.get()
        assert not getter.done()
        assert q.empty()

        q.put_nowait("item")

        assert getter.done()
        assert getter.result() == "item"
        # The item was handed directly to the getter, not stored in the queue.
        assert q.empty()
        assert q._unfinished_tasks == 1

    io_loop.run_until_complete(body())


def test_put_nowait_full_raises_queuefull(io_loop):
    """Lines 220-221: putting into a full queue raises QueueFull."""
    async def body():
        q = Queue(maxsize=1)
        q.put_nowait("first")
        assert q.full()

        with pytest.raises(QueueFull):
            q.put_nowait("second")

        # Queue state is unchanged by the failed put.
        assert q.qsize() == 1
        assert q._unfinished_tasks == 1

    io_loop.run_until_complete(body())


def test_put_nowait_normal_put(io_loop):
    """Line 223: with no getters and room available, item is stored."""
    async def body():
        q = Queue()
        q.put_nowait("a")
        q.put_nowait("b")

        assert q.qsize() == 2
        assert not q.empty()
        assert q.get_nowait() == "a"
        assert q.get_nowait() == "b"
        assert q.empty()

    io_loop.run_until_complete(body())


def test_put_nowait_consumes_cancelled_getter(io_loop):
    """Line 214 + getter-expiry loop in _consume_expired: a done
    (cancelled) getter is discarded instead of being resolved."""
    async def body():
        q = Queue()
        getter = q.get()
        assert getter.cancel()
        assert getter.done()

        q.put_nowait("item")

        # The cancelled getter was consumed, so the item stays in the queue.
        assert getter.cancelled()
        assert q.qsize() == 1
        assert q.get_nowait() == "item"

    io_loop.run_until_complete(body())


def test_put_nowait_consumes_expired_putter(io_loop):
    """Line 214 + putter-expiry loop in _consume_expired: a timed-out
    putter is discarded, and the queue is still full so QueueFull is
    raised."""
    async def body():
        q = Queue(maxsize=1)
        q.put_nowait("first")

        # A put that times out on a full queue leaves a done (failed) putter.
        with pytest.raises(gen.TimeoutError):
            await q.put("second", timeout=datetime.timedelta(milliseconds=10))

        assert len(q._putters) == 1
        assert q._putters[0][1].done()

        with pytest.raises(QueueFull):
            q.put_nowait("third")

        # The expired putter was consumed by _consume_expired.
        assert len(q._putters) == 0
        assert q.qsize() == 1
        assert q.get_nowait() == "first"

    io_loop.run_until_complete(body())
