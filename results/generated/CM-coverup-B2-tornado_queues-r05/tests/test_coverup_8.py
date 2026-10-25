# file: project/tornado/queues.py:322-328
# asked: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}
# gained: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}

from unittest.mock import Mock
from tornado.queues import Queue


def _done_putter(item="item"):
    m = Mock()
    m.done.return_value = True
    return (item, m)


def _pending_putter(item="item"):
    m = Mock()
    m.done.return_value = False
    return (item, m)


def _done_getter():
    m = Mock()
    m.done.return_value = True
    return m


def _pending_getter():
    m = Mock()
    m.done.return_value = False
    return m


def test_consume_expired_empty_queues_noop():
    q = Queue()
    try:
        assert len(q._putters) == 0
        assert len(q._getters) == 0
        q._consume_expired()
        assert len(q._putters) == 0
        assert len(q._getters) == 0
    finally:
        q._putters.clear()
        q._getters.clear()


def test_consume_expired_removes_all_done_putters_and_getters():
    q = Queue()
    try:
        q._putters.append(_done_putter("a"))
        q._putters.append(_done_putter("b"))
        q._getters.append(_done_getter())
        q._getters.append(_done_getter())
        assert len(q._putters) == 2
        assert len(q._getters) == 2
        q._consume_expired()
        assert len(q._putters) == 0
        assert len(q._getters) == 0
    finally:
        q._putters.clear()
        q._getters.clear()


def test_consume_expired_keeps_pending_putters_and_getters():
    q = Queue()
    try:
        putter = _pending_putter("x")
        getter = _pending_getter()
        q._putters.append(putter)
        q._getters.append(getter)
        q._consume_expired()
        assert len(q._putters) == 1
        assert len(q._getters) == 1
        assert q._putters[0] is putter
        assert q._getters[0] is getter
        # done() must have been consulted for both heads
        putter[1].done.assert_called()
        getter.done.assert_called()
    finally:
        q._putters.clear()
        q._getters.clear()


def test_consume_expired_stops_at_first_pending():
    q = Queue()
    try:
        done1 = _done_putter("done1")
        pending = _pending_putter("pending")
        trailing_done = _done_putter("trailing")
        q._putters.append(done1)
        q._putters.append(pending)
        q._putters.append(trailing_done)

        done_g1 = _done_getter()
        pending_g = _pending_getter()
        trailing_g = _done_getter()
        q._getters.append(done_g1)
        q._getters.append(pending_g)
        q._getters.append(trailing_g)

        q._consume_expired()

        # Only the leading done entries are consumed; iteration stops
        # at the first pending entry.
        assert len(q._putters) == 2
        assert q._putters[0] is pending
        assert q._putters[1] is trailing_done
        assert len(q._getters) == 2
        assert q._getters[0] is pending_g
        assert q._getters[1] is trailing_g
    finally:
        q._putters.clear()
        q._getters.clear()
