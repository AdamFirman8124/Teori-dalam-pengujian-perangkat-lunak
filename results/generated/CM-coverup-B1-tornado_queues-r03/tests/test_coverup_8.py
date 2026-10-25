# file: project/tornado/queues.py:322-328
# asked: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}
# gained: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}

import collections
from unittest.mock import Mock

from tornado.queues import Queue


def _done_waiter():
    m = Mock()
    m.done.return_value = True
    return m


def _pending_waiter():
    m = Mock()
    m.done.return_value = False
    return m


def test_consume_expired_drops_done_putters_and_getters():
    q = Queue(maxsize=1)
    q.put_nowait("item")
    stale_putter1 = _done_waiter()
    stale_putter2 = _done_waiter()
    stale_getter1 = _done_waiter()
    stale_getter2 = _done_waiter()
    q._putters.extend([("stale1", stale_putter1), ("stale2", stale_putter2)])
    q._getters.extend([stale_getter1, stale_getter2])

    q._consume_expired()

    assert len(q._putters) == 0
    assert len(q._getters) == 0
    assert stale_putter1.done.call_count >= 1
    assert stale_getter1.done.call_count >= 1
    # Original item untouched.
    assert q.get_nowait() == "item"
    assert q.empty()


def test_consume_expired_keeps_pending_waiters():
    q = Queue(maxsize=1)
    q.put_nowait("item")
    pending_putter = _pending_waiter()
    pending_getter = _pending_waiter()
    q._putters.append(("pending-item", pending_putter))
    q._getters.append(pending_getter)

    q._consume_expired()

    assert list(q._putters) == [("pending-item", pending_putter)]
    assert list(q._getters) == [pending_getter]
    assert q.qsize() == 1


def test_consume_expired_on_empty_queue_is_noop():
    q = Queue()

    q._consume_expired()

    assert len(q._putters) == 0
    assert len(q._getters) == 0
    assert q.qsize() == 0


def test_consume_expired_mixed_done_then_pending():
    q = Queue()
    done_putter = _done_waiter()
    pending_putter = _pending_waiter()
    done_getter = _done_waiter()
    pending_getter = _pending_waiter()
    q._putters.extend([("stale", done_putter), ("fresh", pending_putter)])
    q._getters.extend([done_getter, pending_getter])

    q._consume_expired()

    assert list(q._putters) == [("fresh", pending_putter)]
    assert list(q._getters) == [pending_getter]
