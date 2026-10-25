# file: project/tornado/queues.py:336-346
# asked: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}
# gained: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}

import collections
from tornado.queues import Queue


class _Dummy:
    pass


def test_format_empty_all_false():
    q = Queue()
    try:
        assert len(q._queue) == 0
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
        q._queue.clear()
        q._unfinished_tasks = 0


def test_format_queue_nonempty():
    q = Queue(maxsize=10)
    try:
        q._queue.append("a")
        q._queue.append("b")
        q._unfinished_tasks = 2
        assert getattr(q, "_queue", None)
        result = q._format()
        assert "maxsize=10" in result
        assert "queue=%r" % (q._queue,) in result
        assert "tasks=2" in result
    finally:
        q._queue.clear()
        q._getters.clear()
        q._putters.clear()
        q._unfinished_tasks = 0


def test_format_getters_branch():
    q = Queue()
    try:
        q._getters.append(_Dummy())
        assert q._getters
        result = q._format()
        assert "getters[1]" in result
        assert "getters[%s]" % len(q._getters) in result
    finally:
        q._getters.clear()
        q._putters.clear()
        q._queue.clear()
        q._unfinished_tasks = 0


def test_format_putters_branch():
    q = Queue(maxsize=1)
    try:
        q._queue.append("x")
        q._unfinished_tasks = 1
        q._putters.append(("y", _Dummy()))
        assert q._putters
        result = q._format()
        assert "queue=" in result
        assert "putters[1]" in result
        assert "putters[%s]" % len(q._putters) in result
        assert "tasks=1" in result
    finally:
        q._putters.clear()
        q._getters.clear()
        q._queue.clear()
        q._unfinished_tasks = 0


def test_format_all_branches_true():
    q = Queue(maxsize=5)
    try:
        q._queue.append(1)
        q._getters.append(_Dummy())
        q._putters.append((2, _Dummy()))
        q._unfinished_tasks = 1
        assert getattr(q, "_queue", None)
        assert q._getters
        assert q._putters
        assert q._unfinished_tasks
        result = q._format()
        assert result.startswith("maxsize=5 queue=")
        assert "queue=%r" % (q._queue,) in result
        assert "getters[1]" in result
        assert "putters[1]" in result
        assert "tasks=1" in result
        assert result.index("queue=") < result.index("getters[")
        assert result.index("getters[") < result.index("putters[")
        assert result.index("putters[") < result.index("tasks=")
    finally:
        q._getters.clear()
        q._putters.clear()
        q._queue.clear()
        q._unfinished_tasks = 0


def test_format_missing_queue_attr(monkeypatch):
    q = Queue()
    try:
        q._queue.append("item")
        q._unfinished_tasks = 1
        assert q._queue
        monkeypatch.delattr(q, "_queue", raising=True)
        assert getattr(q, "_queue", None) is None
        result = q._format()
        assert "maxsize=" in result
        assert "queue=" not in result
        assert "tasks=1" in result
    finally:
        q._getters.clear()
        q._putters.clear()
        q._unfinished_tasks = 0
