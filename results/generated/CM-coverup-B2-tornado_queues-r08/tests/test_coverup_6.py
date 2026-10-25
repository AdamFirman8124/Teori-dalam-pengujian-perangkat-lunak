# file: project/tornado/queues.py:274-290
# asked: {"lines": [286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 0], [289, 290]]}
# gained: {"lines": [286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 290]]}

import pytest

from tornado.queues import Queue


def test_task_done_sets_finished_event():
    q = Queue()
    # A fresh queue starts in a "finished" state.
    assert q._finished.is_set()

    q.put_nowait("item")
    # Putting a task marks the queue as unfinished.
    assert not q._finished.is_set()
    assert q._unfinished_tasks == 1

    q.task_done()
    # Lines 288-290: decrement reaches zero, so the event is set again.
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()


def test_task_done_too_many_times_raises_value_error():
    q = Queue()
    # Lines 286-287: calling task_done with no outstanding tasks raises.
    with pytest.raises(ValueError, match="task_done\\(\\) called too many times"):
        q.task_done()

    # Also after fully consuming outstanding tasks.
    q.put_nowait("item")
    q.task_done()
    with pytest.raises(ValueError, match="task_done\\(\\) called too many times"):
        q.task_done()
    # State is unchanged by the failed call.
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()
