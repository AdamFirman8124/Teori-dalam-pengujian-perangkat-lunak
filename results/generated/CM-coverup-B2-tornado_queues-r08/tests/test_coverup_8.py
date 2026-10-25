# file: project/tornado/queues.py:322-328
# asked: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}
# gained: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}

import asyncio

from tornado.queues import Queue


def test_consume_expired_putters():
    async def exercise():
        queue = Queue(maxsize=1)
        queue.put_nowait("resident")

        expired = queue.put("expired")
        live = queue.put("live")
        assert expired.cancel()
        assert expired.cancelled()
        assert not live.done()

        assert queue.get_nowait() == "resident"
        assert await live is None
        assert queue.get_nowait() == "live"

        assert queue.empty()
        assert not queue._putters
        assert not queue._getters

    asyncio.run(exercise())


def test_consume_expired_getters():
    async def exercise():
        queue = Queue()

        expired = queue.get()
        live = queue.get()
        assert expired.cancel()
        assert expired.cancelled()
        assert not live.done()

        queue.put_nowait("delivered")
        assert await live == "delivered"

        queue.put_nowait("remaining")
        assert queue.get_nowait() == "remaining"

        assert queue.empty()
        assert not queue._putters
        assert not queue._getters

    asyncio.run(exercise())
