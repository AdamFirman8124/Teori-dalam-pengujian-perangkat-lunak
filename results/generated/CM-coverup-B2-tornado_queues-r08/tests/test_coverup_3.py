# file: project/tornado/queues.py:256-272
# asked: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}
# gained: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueEmpty


def test_get_nowait_empty_raises_queue_empty():
    q = Queue()
    try:
        assert q.empty()
        assert q.qsize() == 0
        with pytest.raises(QueueEmpty):
            q.get_nowait()
        assert q.empty()
        assert q.qsize() == 0
    finally:
        q._putters.clear()
        q._getters.clear()


def test_get_nowait_returns_item_without_waiting_putters():
    q = Queue(maxsize=2)
    try:
        q.put_nowait("first")
        q.put_nowait("second")
        assert not q._putters
        assert q.qsize() == 2

        assert q.get_nowait() == "first"
        assert q.qsize() == 1
        assert q.get_nowait() == "second"
        assert q.empty()

        with pytest.raises(QueueEmpty):
            q.get_nowait()
    finally:
        q._putters.clear()
        q._getters.clear()


def test_get_nowait_with_waiting_putter_unblocks_putter():
    async def scenario():
        q = Queue(maxsize=1)
        putter = None
        try:
            q.put_nowait(1)
            assert q.full()

            putter = q.put(2)
            assert not putter.done()
            assert len(q._putters) == 1
            assert q.qsize() == 1

            result = q.get_nowait()

            assert result == 1
            assert putter.done()
            assert not putter.cancelled()
            assert putter.result() is None
            assert len(q._putters) == 0
            assert q.qsize() == 1

            assert q.get_nowait() == 2
            q.task_done()
            q.task_done()
            assert q.empty()
        finally:
            if putter is not None and not putter.done():
                putter.cancel()
            q._putters.clear()
            q._getters.clear()

    asyncio.run(scenario())


def test_get_nowait_consumes_expired_putter_and_returns_existing_item():
    async def scenario():
        q = Queue(maxsize=1)
        putter = None
        try:
            q.put_nowait("existing")
            putter = q.put("waiting")
            assert len(q._putters) == 1

            putter.cancel()
            assert putter.done()

            result = q.get_nowait()

            assert result == "existing"
            assert putter.cancelled()
            assert len(q._putters) == 0
            assert q.empty()
            q.task_done()

            with pytest.raises(QueueEmpty):
                q.get_nowait()
        finally:
            if putter is not None and not putter.done():
                putter.cancel()
            q._putters.clear()
            q._getters.clear()

    asyncio.run(scenario())
