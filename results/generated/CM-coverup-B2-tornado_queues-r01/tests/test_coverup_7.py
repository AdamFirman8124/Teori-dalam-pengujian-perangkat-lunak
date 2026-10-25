# file: project/tornado/queues.py:322-328
# asked: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}
# gained: {"lines": [324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}

from unittest.mock import Mock

from tornado.queues import Queue


def test_consume_expired_removes_done_putters_and_getters():
    queue = Queue(maxsize=1)

    expired_putter_one = Mock()
    expired_putter_one.done.return_value = True
    expired_putter_two = Mock()
    expired_putter_two.done.return_value = True
    pending_putter = Mock()
    pending_putter.done.return_value = False

    expired_getter_one = Mock()
    expired_getter_one.done.return_value = True
    expired_getter_two = Mock()
    expired_getter_two.done.return_value = True
    pending_getter = Mock()
    pending_getter.done.return_value = False

    queue._putters.extend(
        [
            ("expired-one", expired_putter_one),
            ("expired-two", expired_putter_two),
            ("pending", pending_putter),
        ]
    )
    queue._getters.extend(
        [expired_getter_one, expired_getter_two, pending_getter]
    )

    try:
        queue._consume_expired()

        assert len(queue._putters) == 1
        assert queue._putters[0][0] == "pending"
        assert queue._putters[0][1] is pending_putter
        assert len(queue._getters) == 1
        assert queue._getters[0] is pending_getter
        pending_putter.done.assert_called_once_with()
        pending_getter.done.assert_called_once_with()
    finally:
        queue._putters.clear()
        queue._getters.clear()
