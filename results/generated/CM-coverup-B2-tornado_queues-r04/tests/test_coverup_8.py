# file: project/tornado/queues.py:322-328
# asked: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}
# gained: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}

import asyncio

from tornado.queues import Queue


def test_consume_expired_putters_cleans_up_cancelled_putters():
    """Lines 324-325: done putter futures are popped from _putters."""

    async def main():
        q = Queue(maxsize=1)
        q.put_nowait("first")

        # Queue is full, so put() appends (item, future) to _putters.
        putter = q.put("second")
        assert not putter.done()
        assert len(q._putters) == 1

        # Simulate the waiter timing out / being cancelled.
        putter.cancel()
        assert putter.done()

        # get_nowait() calls _consume_expired(), which must drop the
        # expired putter instead of treating it as a live waiter.
        item = q.get_nowait()
        assert item == "first"
        assert len(q._putters) == 0
        assert putter.cancelled()

        # The freed slot is usable again.
        q.put_nowait("third")
        assert q.get_nowait() == "third"

    asyncio.run(main())


def test_consume_expired_putters_pops_all_expired_putters():
    """The while loop at 324-325 removes every expired putter, not just one."""

    async def main():
        q = Queue(maxsize=1)
        q.put_nowait("first")

        putter1 = q.put("second")
        putter2 = q.put("third")
        assert len(q._putters) == 2

        putter1.cancel()
        putter2.cancel()

        item = q.get_nowait()
        assert item == "first"
        assert len(q._putters) == 0
        assert putter1.cancelled()
        assert putter2.cancelled()

    asyncio.run(main())


def test_consume_expired_getters_cleans_up_cancelled_getters():
    """Lines 327-328: done getter futures are popped from _getters."""

    async def main():
        q = Queue()

        # Queue is empty, so get() appends its future to _getters.
        getter = q.get()
        assert not getter.done()
        assert len(q._getters) == 1

        # Simulate the waiter timing out / being cancelled.
        getter.cancel()
        assert getter.done()

        # put_nowait() calls _consume_expired(), which must drop the
        # expired getter instead of resolving it with the new item.
        q.put_nowait("item")
        assert len(q._getters) == 0
        assert getter.cancelled()
        assert not getter.done() or getter.cancelled()

        # The item is still in the queue for the next consumer.
        assert q.get_nowait() == "item"
        assert q.empty()

    asyncio.run(main())


def test_consume_expired_getters_pops_all_expired_getters():
    """The while loop at 327-328 removes every expired getter, not just one."""

    async def main():
        q = Queue()

        getter1 = q.get()
        getter2 = q.get()
        assert len(q._getters) == 2

        getter1.cancel()
        getter2.cancel()

        q.put_nowait("item")
        assert len(q._getters) == 0
        assert getter1.cancelled()
        assert getter2.cancelled()
        assert q.get_nowait() == "item"

    asyncio.run(main())
