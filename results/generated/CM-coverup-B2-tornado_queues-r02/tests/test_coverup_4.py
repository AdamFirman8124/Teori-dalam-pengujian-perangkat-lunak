# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueFull


def test_put_nowait_hands_item_to_waiting_getter():
    # Lines 215-219: a getter is already waiting, so the item is delivered
    # straight to it instead of being stored in the queue.
    async def main():
        q = Queue(maxsize=1)
        getter = q.get()
        assert not getter.done()

        q.put_nowait("item")

        assert getter.done()
        assert getter.result() == "item"
        assert q.empty()
        assert q.qsize() == 0
        assert len(q._getters) == 0

    asyncio.run(main())


def test_put_nowait_raises_when_full():
    # Lines 220-221: queue is full and no getters are waiting.
    async def main():
        q = Queue(maxsize=1)
        q.put_nowait("first")
        assert q.full()

        with pytest.raises(QueueFull):
            q.put_nowait("second")

        # Failed put left the queue untouched.
        assert q.qsize() == 1
        assert q.get_nowait() == "first"
        assert q.empty()

    asyncio.run(main())


def test_put_nowait_stores_item_when_not_full():
    # Line 223: no getters waiting and queue has room.
    async def main():
        q = Queue(maxsize=2)
        assert q.empty()

        q.put_nowait("a")

        assert not q.empty()
        assert q.qsize() == 1
        assert q.get_nowait() == "a"
        assert q.empty()

    asyncio.run(main())


def test_put_nowait_unbounded_queue():
    # Line 223 again, with maxsize=0 (never full).
    async def main():
        q = Queue()
        assert q.maxsize == 0
        assert not q.full()

        q.put_nowait("x")
        q.put_nowait("y")

        assert q.qsize() == 2
        assert q.get_nowait() == "x"
        assert q.get_nowait() == "y"

    asyncio.run(main())


def test_put_nowait_consumes_expired_getter():
    # Line 214 (_consume_expired): a cancelled getter is discarded before
    # the put proceeds, so the item goes to storage rather than a dead future.
    async def main():
        q = Queue(maxsize=1)
        stale_getter = q.get()
        stale_getter.cancel()
        assert stale_getter.done()
        assert len(q._getters) == 1

        q.put_nowait("value")

        assert len(q._getters) == 0
        assert q.qsize() == 1
        assert q.get_nowait() == "value"

    asyncio.run(main())
