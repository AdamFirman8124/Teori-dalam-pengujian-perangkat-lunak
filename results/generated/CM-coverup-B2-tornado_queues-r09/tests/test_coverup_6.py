# file: project/tornado/queues.py:274-290
# asked: {"lines": [286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 0], [289, 290]]}
# gained: {"lines": [286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 0], [289, 290]]}

import pytest

from tornado.queues import Queue


def test_task_done_raises_when_no_unfinished_tasks():
    q = Queue()
    assert q._unfinished_tasks == 0
    with pytest.raises(ValueError, match="task_done.*too many times"):
        q.task_done()
    # postcondition: state unchanged, still no unfinished tasks
    assert q._unfinished_tasks == 0


def test_task_done_decrements_without_setting_finished():
    q = Queue()
    q.put_nowait("a")
    q.put_nowait("b")
    assert q._unfinished_tasks == 2
    # normalize precondition so postcondition check is deterministic
    q._finished.clear()
    assert q._finished.is_set() is False
    q.task_done()
    # postconditions: decremented by one, finished event not set
    assert q._unfinished_tasks == 1
    assert q._finished.is_set() is False
    # cleanup remaining task to avoid state pollution / pending join
    q.task_done()
    assert q._unfinished_tasks == 0
    assert q._finished.is_set() is True


def test_task_done_sets_finished_on_last_task():
    q = Queue()
    q.put_nowait("x")
    assert q._unfinished_tasks == 1
    q._finished.clear()
    assert q._finished.is_set() is False
    q.task_done()
    # postconditions: counter reaches zero and finished event is set
    assert q._unfinished_tasks == 0
    assert q._finished.is_set() is True
