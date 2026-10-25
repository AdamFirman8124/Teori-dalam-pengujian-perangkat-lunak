# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueFull


def test_put_nowait_no_getters_not_full():
    q = Queue()
    assert q.empty()
    q.put_nowait("a")
    # else branch (line 223): stored internally
    assert q.qsize() == 1
    assert not q.empty()
    assert not q.full()
    assert q.get_nowait() == "a"
    assert q.empty()


def test_put_nowait_full_raises():
    q = Queue(maxsize=1)
    q.put_nowait("first")
    assert q.full()
    assert q.qsize() == 1
    with pytest.raises(QueueFull):
        q.put_nowait("second")
    # postcondition: failed put did not mutate queue
    assert q.full()
    assert q.qsize() == 1
    assert q.get_nowait() == "first"
    assert q.empty()


def test_put_nowait_with_waiting_getter():
    async def _run():
        q = Queue()
        get_future = q.get()
        # getter is now waiting on empty queue
        assert len(q._getters) == 1
        assert q.empty()
        q.put_nowait("hello")
        # getter was popped and resolved with the item
        assert len(q._getters) == 0
        assert get_future.done()
        assert get_future.result() == "hello"
        assert await get_future == "hello"
        # put-then-get leaves queue empty
        assert q.empty()
        assert q.qsize() == 0

    asyncio.run(_run())
