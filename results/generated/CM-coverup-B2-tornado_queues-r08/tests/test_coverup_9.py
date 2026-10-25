# file: project/tornado/queues.py:225-254
# asked: {"lines": [248, 249, 250, 251, 252, 253, 254], "branches": []}
# gained: {"lines": [248, 249, 250, 251, 252, 253, 254], "branches": []}

import asyncio

from tornado.queues import Queue


def test_get_returns_immediately_when_item_is_available():
    async def run_test():
        queue = Queue()
        queue.put_nowait("item")

        future = queue.get()

        assert future.done()
        assert await future == "item"
        assert queue.empty()

    asyncio.run(run_test())


def test_get_waits_when_queue_is_empty_and_resolves_after_put():
    async def run_test():
        queue = Queue()
        future = queue.get()

        try:
            assert not future.done()
            assert list(queue._getters) == [future]

            queue.put_nowait("item")

            assert await future == "item"
            assert future.done()
            assert queue.empty()
            assert not queue._getters
        finally:
            if not future.done():
                future.cancel()
            queue._consume_expired()

    asyncio.run(run_test())
