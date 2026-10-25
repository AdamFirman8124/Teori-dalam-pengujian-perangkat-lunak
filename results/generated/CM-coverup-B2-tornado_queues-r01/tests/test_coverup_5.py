# file: project/tornado/queues.py:274-290
# asked: {"lines": [286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 0], [289, 290]]}
# gained: {"lines": [286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 0], [289, 290]]}

import pytest

from tornado.queues import Queue


def test_task_done_raises_when_no_tasks_are_unfinished():
    queue = Queue()

    with pytest.raises(ValueError, match=r"^task_done\(\) called too many times$"):
        queue.task_done()

    assert queue.empty()
    assert queue._unfinished_tasks == 0
    assert queue._finished.is_set()


def test_task_done_sets_finished_after_all_tasks_are_completed():
    queue = Queue()
    queue.put_nowait("first")
    queue.put_nowait("second")

    assert not queue._finished.is_set()
    assert queue._unfinished_tasks == 2
    assert queue.get_nowait() == "first"
    assert queue.get_nowait() == "second"

    queue.task_done()

    assert queue._unfinished_tasks == 1
    assert not queue._finished.is_set()

    queue.task_done()

    assert queue._unfinished_tasks == 0
    assert queue._finished.is_set()
    assert queue.empty()
