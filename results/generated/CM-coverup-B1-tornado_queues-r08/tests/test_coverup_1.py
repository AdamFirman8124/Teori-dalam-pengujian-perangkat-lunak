# file: project/tornado/queues.py:336-346
# asked: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}
# gained: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}

import collections
import pytest
from tornado.queues import Queue


def test_format_empty_covers_all_false():
    q = Queue()
    try:
        assert q.qsize() == 0
        assert len(q._getters) == 0
        assert len(q._putters) == 0
        assert q._unfinished_tasks == 0
        result = q._format()
        assert result == "maxsize=%r" % (q.maxsize,)
        assert result == "maxsize=0"
        assert "queue=" not in result
        assert "getters" not in result
        assert "putters" not in result
        assert "tasks=" not in result
        assert result in str(q)
        assert result in repr(q)
    finally:
        q._getters.clear()
        q._putters.clear()
        if getattr(q, "_queue", None) is not None:
            q._queue.clear()
        q._unfinished_tasks = 0


def test_format_queue_and_tasks_via_put_nowait():
    q = Queue(maxsize=10)
    try:
        q.put_nowait("a")
        q.put_nowait("b")
        assert len(q._queue) == 2
        assert q._unfinished_tasks == 2
        result = q._format()
        assert "maxsize=10" in result
        assert "queue=%r" % (q._queue,) in result
        assert "queue=" in result
        assert "tasks=2" in result
        assert "tasks=%s" % q._unfinished_tasks in result
    finally:
        while True:
            try:
                q.get_nowait()
            except Exception:
                break
        while q._unfinished_tasks > 0:
            q.task_done()
        q._getters.clear()
        q._putters.clear()


def test_format_getters_branch():
    q = Queue()
    try:
        sentinel = object()
        q._getters.append(sentinel)
        assert len(q._getters) == 1
        result = q._format()
        assert "maxsize=0" in result
        assert "getters[1]" in result
        assert "getters[%s]" % len(q._getters) in result
    finally:
        q._getters.clear()
        try:
            q._queue.clear()
        except Exception:
            pass
        q._putters.clear()
        q._unfinished_tasks = 0


def test_format_putters_branch_when_full():
    q = Queue(maxsize=1)
    try:
        q.put_nowait("x")
        assert q.full()
        q._putters.append(("y", object()))
        assert len(q._putters) == 1
        result = q._format()
        assert "maxsize=1" in result
        assert "queue=" in result
        assert "putters[1]" in result
        assert "putters[%s]" % len(q._putters) in result
        assert "tasks=" in result
    finally:
        q._putters.clear()
        q._getters.clear()
        while True:
            try:
                q.get_nowait()
            except Exception:
                break
        while q._unfinished_tasks > 0:
            try:
                q.task_done()
            except Exception:
                break


def test_format_all_branches_combined():
    q = Queue(maxsize=5)
    try:
        q.put_nowait(1)
        q._getters.append(object())
        q._putters.append((2, object()))
        assert getattr(q, "_queue", None)
        assert q._getters
        assert q._putters
        assert q._unfinished_tasks
        result = q._format()
        assert "maxsize=5" in result
        assert "queue=%r" % (q._queue,) in result
        assert "getters[1]" in result
        assert "putters[1]" in result
        assert "tasks=%s" % q._unfinished_tasks in result
        assert result.startswith("maxsize=5 queue=")
        assert result.index("queue=") < result.index("getters[")
        assert result.index("getters[") < result.index("putters[")
        assert result.index("putters[") < result.index("tasks=")
    finally:
        q._getters.clear()
        q._putters.clear()
        try:
            q._queue.clear()
        except Exception:
            pass
        q._unfinished_tasks = 0


def test_format_missing_queue_attr(monkeypatch):
    q = Queue()
    try:
        q.put_nowait("item")
        assert q._queue
        monkeypatch.delattr(q, "_queue", raising=True)
        assert getattr(q, "_queue", None) is None
        result = q._format()
        assert "maxsize=" in result
        assert "queue=" not in result
        assert q._unfinished_tasks == 1
        assert "tasks=1" in result
    finally:
        q._getters.clear()
        q._putters.clear()
        q._unfinished_tasks = 0
