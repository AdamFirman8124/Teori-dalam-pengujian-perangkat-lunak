# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio

import pytest
from tornado.queues import Queue, QueueEmpty, QueueFull


def test_put_nowait_delivers_to_waiting_getter():
    async def main():
        queue = Queue()
        getter = queue.get()

        assert len(queue._getters) == 1
        assert not getter.done()

        queue.put_nowait("hello")

        assert not queue._getters
        assert getter.done()
        assert getter.result() == "hello"
        assert queue.empty()
        assert queue.qsize() == 0

        queue.task_done()
        await queue.join()

    asyncio.run(main())


def test_put_nowait_raises_when_full_without_modifying_queue():
    async def main():
        queue = Queue(maxsize=1)

        queue.put_nowait("first")
        assert queue.full()

        with pytest.raises(QueueFull):
            queue.put_nowait("second")

        assert queue.qsize() == 1
        assert queue.get_nowait() == "first"
        assert queue.empty()

        queue.task_done()
        await queue.join()

    asyncio.run(main())


def test_put_nowait_buffers_item_when_no_getter_is_waiting():
    async def main():
        queue = Queue(maxsize=2)

        queue.put_nowait("first")
        queue.put_nowait("second")

        assert queue.full()
        assert queue.qsize() == 2
        assert queue.get_nowait() == "first"
        queue.task_done()
        assert queue.get_nowait() == "second"
        queue.task_done()

        assert queue.empty()
        with pytest.raises(QueueEmpty):
            queue.get_nowait()

        await queue.join()

    asyncio.run(main())


def test_put_nowait_consumes_cancelled_getter_before_buffering_item():
    async def main():
        queue = Queue()
        getter = queue.get()

        assert len(queue._getters) == 1
        assert getter.cancel()

        queue.put_nowait("replacement")

        assert not queue._getters
        assert getter.cancelled()
        assert queue.qsize() == 1
        assert queue.get_nowait() == "replacement"

        queue.task_done()
        await queue.join()

    asyncio.run(main())


def test_put_nowait_asserts_if_getter_waits_for_nonempty_queue():
    async def main():
        queue = Queue()
        queue.put_nowait("existing")

        getter = asyncio.get_running_loop().create_future()
        queue._getters.append(getter)

        with pytest.raises(
            AssertionError, match="queue non-empty, why are getters waiting"
        ):
            queue.put_nowait("new")

        assert queue.qsize() == 1
        assert queue._getters.popleft() is getter
        assert queue.get_nowait() == "existing"

        getter.cancel()
        queue.task_done()
        await queue.join()

    asyncio.run(main())
