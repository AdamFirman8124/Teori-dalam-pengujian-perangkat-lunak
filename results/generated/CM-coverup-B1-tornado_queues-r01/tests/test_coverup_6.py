# file: project/tornado/queues.py:274-290
# asked: {"lines": [286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 0], [289, 290]]}
# gained: {"lines": [286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 0], [289, 290]]}

import asyncio

import pytest

from tornado.queues import Queue


def test_task_done_too_many_times_raises_valueerror():
    """Lines 286-287: task_done() with no pending tasks raises ValueError."""
    q = Queue()
    with pytest.raises(ValueError, match="task_done\\(\\) called too many times"):
        q.task_done()


def test_task_done_decrements_and_sets_finished():
    """Lines 288-290: task_done() decrements the counter and sets _finished at zero."""
    q = Queue()
    q.put_nowait("a")
    q.put_nowait("b")
    assert q._unfinished_tasks == 2
    assert not q._finished.is_set()

    q.task_done()
    assert q._unfinished_tasks == 1
    assert not q._finished.is_set()

    q.task_done()
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()


def test_task_done_exhausted_then_raises():
    """After consuming all task_done() credits, a further call raises ValueError."""
    q = Queue()
    q.put_nowait("x")
    q.task_done()
    assert q._unfinished_tasks == 0
    with pytest.raises(ValueError):
        q.task_done()


def test_join_resumes_after_all_tasks_done():
    """A join() blocked on _finished resumes once every put is matched by task_done."""
    async def main():
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        join_task = asyncio.ensure_future(q.join())
        await asyncio.sleep(0.01)
        assert not join_task.done()
        q.task_done()
        q.task_done()
        await asyncio.wait_for(join_task, timeout=1.0)
        assert join_task.done()
        assert not join_task.exception()
        assert q._finished.is_set()

    asyncio.run(main())
