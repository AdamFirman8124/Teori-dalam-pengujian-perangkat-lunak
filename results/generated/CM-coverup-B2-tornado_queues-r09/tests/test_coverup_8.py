# file: project/tornado/queues.py:322-328
# asked: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}
# gained: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}

from unittest.mock import Mock

from tornado.queues import Queue


def test_consume_expired_removes_completed_waiters() -> None:
    queue = Queue()

    done_putter = Mock()
    done_putter.done.return_value = True
    pending_putter = Mock()
    pending_putter.done.return_value = False

    done_getter = Mock()
    done_getter.done.return_value = True
    pending_getter = Mock()
    pending_getter.done.return_value = False

    queue._putters.extend(
        [("expired", done_putter), ("pending", pending_putter)]
    )
    queue._getters.extend([done_getter, pending_getter])

    queue._consume_expired()

    assert list(queue._putters) == [("pending", pending_putter)]
    assert list(queue._getters) == [pending_getter]
    done_putter.done.assert_called_once_with()
    pending_putter.done.assert_called_once_with()
    done_getter.done.assert_called_once_with()
    pending_getter.done.assert_called_once_with()


def test_consume_expired_handles_empty_waiter_queues() -> None:
    queue = Queue()

    queue._consume_expired()

    assert not queue._putters
    assert not queue._getters
