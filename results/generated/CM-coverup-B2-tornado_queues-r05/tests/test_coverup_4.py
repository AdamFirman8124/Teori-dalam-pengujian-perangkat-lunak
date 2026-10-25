# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import concurrent.futures

import pytest

from tornado.queues import Queue, QueueFull


def test_put_nowait_empty_no_getters():
    q = Queue()
    assert q.empty()
    assert len(q._getters) == 0
    assert not q.full()
    q.put_nowait(42)
    assert q.qsize() == 1
    assert not q.empty()
    assert q.get_nowait() == 42
    q.task_done()
    assert q.empty()


def test_put_nowait_full_raises_queue_full():
    q = Queue(maxsize=1)
    assert len(q._getters) == 0
    q.put_nowait("a")
    assert q.full()
    assert q.qsize() == 1
    with pytest.raises(QueueFull):
        q.put_nowait("b")
    # postcondition: failed put did not change queue
    assert q.qsize() == 1
    assert q.full()
    assert q.get_nowait() == "a"
    q.task_done()
    assert q.empty()


def test_put_nowait_handoff_to_waiting_getter():
    q = Queue()
    assert q.empty()
    assert len(q._getters) == 0
    getter = concurrent.futures.Future()
    assert not getter.done()
    q._getters.append(getter)
    assert len(q._getters) == 1
    q.put_nowait("hello")
    # getter was popped and resolved with the item
    assert len(q._getters) == 0
    assert getter.done()
    assert not getter.cancelled()
    assert getter.result() == "hello"
    # item was handed directly to getter, nothing left queued
    assert q.empty()
    assert q.qsize() == 0
    q.task_done()
