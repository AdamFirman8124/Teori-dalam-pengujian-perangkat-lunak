# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueFull


@pytest.fixture
def io_loop():
    """Provide a current event loop so tornado.concurrent.Future() can be created."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        try:
            loop.close()
        finally:
            asyncio.set_event_loop(None)


def test_put_nowait_with_waiting_getter(io_loop):
    q = Queue()
    try:
        getter = q.get()
        assert len(q._getters) == 1
        assert q.empty()
        q.put_nowait("hello")
        # getter must have been popped and resolved with the item
        assert len(q._getters) == 0
        assert getter.done()
        assert getter.result() == "hello"
        # item was put then immediately removed for the getter
        assert q.empty()
        assert q.qsize() == 0
    finally:
        # cleanup: cancel any leftover getter and drain queue
        for pending in list(q._getters):
            if not pending.done():
                pending.cancel()
        q._getters.clear()
        while not q.empty():
            try:
                q.get_nowait()
            except Exception:
                break


def test_put_nowait_full_raises(io_loop):
    q = Queue(maxsize=1)
    try:
        q.put_nowait("a")
        assert q.full()
        assert q.qsize() == 1
        with pytest.raises(QueueFull):
            q.put_nowait("b")
        # failed put must not change the queue
        assert q.qsize() == 1
        assert q.full()
        assert q.get_nowait() == "a"
        assert q.empty()
    finally:
        while not q.empty():
            try:
                q.get_nowait()
            except Exception:
                break
        q._getters.clear()


def test_put_nowait_else_branch_stores_item(io_loop):
    q = Queue()
    try:
        assert not q._getters
        assert not q.full()
        q.put_nowait(42)
        assert q.qsize() == 1
        assert not q.empty()
        assert not q.full()
        assert q.get_nowait() == 42
        assert q.empty()
        assert q.qsize() == 0
    finally:
        while not q.empty():
            try:
                q.get_nowait()
            except Exception:
                break
        q._getters.clear()
