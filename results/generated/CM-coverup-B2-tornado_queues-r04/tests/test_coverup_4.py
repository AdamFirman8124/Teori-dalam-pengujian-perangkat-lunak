# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueFull


def test_put_nowait_wakes_waiting_getter():
    """Covers lines 214-219: put_nowait when getters are waiting."""

    async def main():
        q = Queue(maxsize=1)
        assert q.empty()

        # q.get() returns a Future immediately and registers it in _getters
        # because the queue is empty. This requires a running event loop
        # (Future creation), hence the asyncio.run wrapper.
        getter = q.get()
        assert not getter.done()
        assert len(q._getters) == 1

        # put_nowait must consume expired timeouts, pop the getter, put the
        # item internally, and resolve the getter's future with the item.
        q.put_nowait("item")

        assert getter.done()
        assert getter.result() == "item"
        # The item was handed directly to the getter, so the queue is empty
        # and no getters remain waiting.
        assert q.empty()
        assert len(q._getters) == 0
        assert q._unfinished_tasks == 1
        q.task_done()  # restore the finished state, avoiding state pollution

    asyncio.run(main())


def test_put_nowait_raises_when_full():
    """Covers lines 220-221: put_nowait on a full queue raises QueueFull."""
    q = Queue(maxsize=1)
    q.put_nowait("first")
    assert q.full()

    with pytest.raises(QueueFull):
        q.put_nowait("second")

    # The rejected item must not have been stored.
    assert q.qsize() == 1
    assert q.get_nowait() == "first"
    q.task_done()


def test_put_nowait_stores_item_when_not_full():
    """Covers line 223: put_nowait on a non-full queue with no getters."""
    q = Queue()
    q.put_nowait("only")

    assert q.qsize() == 1
    assert not q.empty()
    assert q.get_nowait() == "only"
    q.task_done()
    assert q.empty()
