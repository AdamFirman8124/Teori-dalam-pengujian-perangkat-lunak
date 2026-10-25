# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueFull


def test_put_nowait_resolves_waiting_getter():
    """Covers lines 214-219: the getter branch."""

    async def main():
        q = Queue()
        getter = q.get()
        assert not getter.done()
        assert len(q._getters) == 1

        q.put_nowait("item")

        assert getter.done()
        assert getter.result() == "item"
        assert q.empty()
        assert q.qsize() == 0
        assert len(q._getters) == 0

    asyncio.run(main())


def test_put_nowait_raises_queue_full():
    """Covers lines 220-221: the full() branch."""
    q = Queue(maxsize=1)
    q.put_nowait("first")
    assert q.full()
    assert q.qsize() == 1

    with pytest.raises(QueueFull):
        q.put_nowait("second")

    # Postcondition: the queue is unchanged by the failed put.
    assert q.qsize() == 1
    assert q.get_nowait() == "first"
    assert q.empty()


def test_put_nowait_without_getters_or_full():
    """Covers line 223: the plain else branch."""
    q = Queue(maxsize=2)
    assert not q.full()
    assert not q._getters

    q.put_nowait("a")
    assert q.qsize() == 1
    assert not q.empty()

    q.put_nowait("b")
    assert q.qsize() == 2
    assert q.full()

    assert q.get_nowait() == "a"
    assert q.get_nowait() == "b"
    assert q.empty()


def test_put_nowait_unbounded_queue_never_full():
    """Covers line 223 for the default (maxsize=0) queue."""
    q = Queue()
    for i in range(5):
        q.put_nowait(i)

    assert q.qsize() == 5
    assert not q.full()
    assert [q.get_nowait() for _ in range(5)] == [0, 1, 2, 3, 4]
    assert q.empty()
