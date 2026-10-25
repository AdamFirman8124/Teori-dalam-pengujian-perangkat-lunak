# file: project/tornado/queues.py:186-207
# asked: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}

import asyncio
import datetime

import pytest

from tornado.queues import Queue
from tornado.util import TimeoutError


def test_put_immediate_success_resolves_future():
    async def scenario():
        q = Queue(maxsize=1)
        future = q.put("a")
        assert future.done()
        assert future.result() is None
        assert q.qsize() == 1
        assert q.get_nowait() == "a"
        assert q.empty()

    asyncio.run(scenario())


def test_put_blocks_when_full_and_resolves_after_consumption():
    async def scenario():
        q = Queue(maxsize=1)
        q.put_nowait("first")
        future = q.put("second")
        # QueueFull branch: item parked in _putters, future still pending.
        assert not future.done()
        assert len(q._putters) == 1
        assert q._putters[0][0] == "second"
        # Consuming the queued item lets the parked putter through.
        assert await q.get() == "first"
        assert await future is None
        assert q.qsize() == 1
        assert q.get_nowait() == "second"
        assert q.empty()

    asyncio.run(scenario())


def test_put_timeout_raises_timeout_error():
    async def scenario():
        q = Queue(maxsize=1)
        q.put_nowait("full")
        future = q.put("late", timeout=0.01)
        with pytest.raises(TimeoutError):
            await future
        # Draining the queue triggers _consume_expired, dropping the
        # expired putter.
        assert q.get_nowait() == "full"
        assert len(q._putters) == 0
        assert q.empty()

    asyncio.run(scenario())


def test_put_timeout_accepts_timedelta():
    async def scenario():
        q = Queue(maxsize=1)
        q.put_nowait("full")
        future = q.put("late", timeout=datetime.timedelta(seconds=0.01))
        with pytest.raises(TimeoutError):
            await future
        assert q.get_nowait() == "full"
        assert len(q._putters) == 0

    asyncio.run(scenario())


def test_put_with_timeout_succeeds_before_deadline():
    async def scenario():
        q = Queue(maxsize=1)
        q.put_nowait("first")
        future = q.put("second", timeout=10.0)
        assert not future.done()
        assert await q.get() == "first"
        # Resolves with None well before the 10s deadline.
        assert await future is None
        assert q.get_nowait() == "second"
        assert q.empty()

    asyncio.run(scenario())
