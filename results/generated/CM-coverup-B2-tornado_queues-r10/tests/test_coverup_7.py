# file: project/tornado/queues.py:186-207
# asked: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}

import asyncio
import datetime
import time

import pytest

from tornado.queues import Queue
from tornado.util import TimeoutError


def test_put_success_immediately():
    # Covers the else branch: put_nowait succeeds -> future.set_result(None).
    async def main():
        q = Queue(maxsize=1)
        future = q.put(1)
        assert future.done()
        assert future.result() is None
        assert q.qsize() == 1
        assert len(q._putters) == 0
        assert q.get_nowait() == 1
        assert q.qsize() == 0

    asyncio.run(main())


def test_put_blocks_when_full():
    # Covers the QueueFull branch: item + future stored in _putters and the
    # future resolves once a getter frees up room.
    async def main():
        q = Queue(maxsize=1)
        q.put_nowait(1)
        future = q.put(2)
        assert not future.done()
        assert len(q._putters) == 1
        assert q._putters[0][0] == 2
        assert q._putters[0][1] is future

        item = await q.get()
        assert item == 1
        await future
        assert future.done()
        assert future.result() is None
        assert len(q._putters) == 0
        assert q.qsize() == 1
        assert q.get_nowait() == 2
        assert q.qsize() == 0

    asyncio.run(main())


def test_put_timeout_numeric():
    # Covers _set_timeout with a numeric (absolute) deadline.
    async def main():
        q = Queue(maxsize=1)
        q.put_nowait(1)
        future = q.put(2, timeout=time.time() + 0.01)
        assert not future.done()
        with pytest.raises(TimeoutError):
            await future
        assert future.done()
        assert isinstance(future.exception(), TimeoutError)
        # The item was never enqueued; the expired putter is discarded.
        assert q.qsize() == 1
        assert q.get_nowait() == 1
        assert q.qsize() == 0
        assert len(q._putters) == 0

    asyncio.run(main())


def test_put_timeout_timedelta():
    # Covers _set_timeout with a datetime.timedelta relative timeout.
    async def main():
        q = Queue(maxsize=1)
        q.put_nowait(1)
        future = q.put(2, timeout=datetime.timedelta(seconds=0.01))
        assert not future.done()
        with pytest.raises(TimeoutError):
            await future
        assert future.done()
        assert isinstance(future.exception(), TimeoutError)
        assert q.qsize() == 1
        assert q.get_nowait() == 1
        assert q.qsize() == 0
        assert len(q._putters) == 0

    asyncio.run(main())
