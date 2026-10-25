# file: project/tornado/queues.py:336-346
# asked: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}
# gained: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueEmpty


def test_format_empty_queue():
    queue = Queue(maxsize=3)

    assert queue._format() == "maxsize=3"
    assert queue.empty()
    assert queue._unfinished_tasks == 0


def test_format_with_waiting_getter():
    async def run_test():
        queue = Queue()
        getter = queue.get()

        try:
            assert queue._format() == "maxsize=0 getters[1]"
            assert len(queue._getters) == 1
            assert not getter.done()
        finally:
            getter.cancel()
            with pytest.raises(QueueEmpty):
                queue.get_nowait()

        assert not queue._getters
        assert queue.empty()

    asyncio.run(run_test())


def test_format_with_queue_putter_and_unfinished_task():
    async def run_test():
        queue = Queue(maxsize=1)
        queue.put_nowait("first")
        putter = queue.put("second")

        try:
            assert queue._format() == (
                "maxsize=1 queue=deque(['first']) putters[1] tasks=1"
            )
            assert queue.full()
            assert len(queue._putters) == 1
            assert queue._unfinished_tasks == 1
            assert not putter.done()
        finally:
            putter.cancel()
            assert queue.get_nowait() == "first"
            queue.task_done()

        assert not queue._putters
        assert queue.empty()
        assert queue._unfinished_tasks == 0

    asyncio.run(run_test())
