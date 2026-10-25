# file: project/tornado/queues.py:322-328
# asked: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}
# gained: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueEmpty


def test_consume_expired_pops_done_putters():
    async def main():
        q = Queue(maxsize=1)
        q.put_nowait("first")
        p1 = q.put("second")
        p2 = q.put("third")
        assert len(q._putters) == 2

        p1.set_result(None)
        q._consume_expired()
        assert len(q._putters) == 1
        assert q._putters[0][0] == "third"

        p2.set_result(None)
        q._consume_expired()
        assert len(q._putters) == 0
        assert q.qsize() == 1

    asyncio.run(main())


def test_consume_expired_pops_done_getters():
    async def main():
        q = Queue()
        g1 = q.get()
        g2 = q.get()
        assert len(q._getters) == 2

        g1.set_result("a")
        q._consume_expired()
        assert len(q._getters) == 1
        assert q._getters[0] is g2

        g2.set_result("b")
        q._consume_expired()
        assert len(q._getters) == 0
        with pytest.raises(QueueEmpty):
            q.get_nowait()

    asyncio.run(main())


def test_consume_expired_stops_at_pending_putter():
    async def main():
        q = Queue(maxsize=1)
        q.put_nowait(1)
        p1 = q.put(2)
        p2 = q.put(3)
        p1.set_result(None)
        q._consume_expired()
        assert [item for item, _ in q._putters] == [3]
        assert q._putters[0][1] is p2

    asyncio.run(main())


def test_consume_expired_stops_at_pending_getter():
    async def main():
        q = Queue()
        g1 = q.get()
        g2 = q.get()
        g1.set_result("a")
        q._consume_expired()
        assert len(q._getters) == 1
        assert q._getters[0] is g2

    asyncio.run(main())


def test_consume_expired_with_no_waiters_is_noop():
    async def main():
        q = Queue()
        q._consume_expired()
        assert len(q._putters) == 0
        assert len(q._getters) == 0
        assert q.empty()

    asyncio.run(main())
