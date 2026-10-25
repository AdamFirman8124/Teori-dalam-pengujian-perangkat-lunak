# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueFull


def test_put_nowait_else_branch_stores_item():
    q = Queue(maxsize=2)
    try:
        assert q.empty()
        assert not q.full()
        assert len(q._getters) == 0

        q.put_nowait("a")

        assert q.qsize() == 1
        assert not q.empty()
        assert q.get_nowait() == "a"
        assert q.empty()
    finally:
        while not q.empty():
            q.get_nowait()
            q.task_done()
        if q._unfinished_tasks:
            q.task_done()
    assert q._unfinished_tasks == 0


def test_put_nowait_unbounded_else_branch_stores_multiple_items():
    q = Queue()
    try:
        q.put_nowait(1)
        q.put_nowait(2)

        assert q.qsize() == 2
        assert q.get_nowait() == 1
        q.task_done()
        assert q.get_nowait() == 2
        q.task_done()
    finally:
        while not q.empty():
            q.get_nowait()
            q.task_done()
    assert q._unfinished_tasks == 0


def test_put_nowait_full_branch_raises_queue_full():
    q = Queue(maxsize=1)
    try:
        q.put_nowait("first")
        assert q.full()
        assert q.qsize() == 1

        with pytest.raises(QueueFull):
            q.put_nowait("second")

        assert q.qsize() == 1
        assert q.get_nowait() == "first"
        q.task_done()
    finally:
        while not q.empty():
            q.get_nowait()
            q.task_done()
    assert q._unfinished_tasks == 0


def test_put_nowait_with_waiting_getter_hands_off_item():
    async def main():
        q = Queue()
        getter = q.get()
        try:
            assert not getter.done()
            assert len(q._getters) == 1
            assert q.empty()

            q.put_nowait("hello")

            assert len(q._getters) == 0
            assert getter.done()
            assert not getter.cancelled()
            assert getter.result() == "hello"
            # Item was passed directly to the getter via _get().
            assert q.empty()
            assert q.qsize() == 0
            assert q._unfinished_tasks == 1

            q.task_done()
            assert q._unfinished_tasks == 0
        finally:
            if not getter.done():
                getter.cancel()
            while q._getters:
                pending = q._getters.popleft()
                if not pending.done():
                    pending.cancel()
            while not q.empty():
                q.get_nowait()
                q.task_done()

    asyncio.run(main())


def test_put_nowait_with_multiple_waiting_getters_fifo():
    async def main():
        q = Queue()
        getter1 = q.get()
        getter2 = q.get()
        try:
            assert len(q._getters) == 2

            q.put_nowait(1)
            assert getter1.done()
            assert getter1.result() == 1
            assert not getter2.done()
            assert len(q._getters) == 1
            assert q.empty()

            q.put_nowait(2)
            assert getter2.done()
            assert getter2.result() == 2
            assert len(q._getters) == 0
            assert q.empty()
            assert q._unfinished_tasks == 2

            q.task_done()
            q.task_done()
            assert q._unfinished_tasks == 0
        finally:
            for getter in (getter1, getter2):
                if not getter.done():
                    getter.cancel()
            while q._getters:
                pending = q._getters.popleft()
                if not pending.done():
                    pending.cancel()
            while not q.empty():
                q.get_nowait()
                q.task_done()

    asyncio.run(main())


def test_put_nowait_consumes_expired_cancelled_getter_and_stores_item():
    async def main():
        q = Queue()
        getter = q.get()
        try:
            assert len(q._getters) == 1
            getter.cancel()
            assert getter.done()

            # _consume_expired() removes the cancelled getter, so
            # put_nowait takes the else branch and stores the item.
            q.put_nowait("stored")

            assert len(q._getters) == 0
            assert getter.cancelled()
            assert q.qsize() == 1
            assert q.get_nowait() == "stored"
            q.task_done()
            assert q._unfinished_tasks == 0
        finally:
            if not getter.done():
                getter.cancel()
            while q._getters:
                pending = q._getters.popleft()
                if not pending.done():
                    pending.cancel()
            while not q.empty():
                q.get_nowait()
                q.task_done()

    asyncio.run(main())
