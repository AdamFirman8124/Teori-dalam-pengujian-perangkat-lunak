# file: project/tornado/queues.py:336-346
# asked: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}
# gained: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}

import collections
from tornado.queues import Queue


def test_format_empty_all_branches_false():
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


def test_format_all_branches_true():
    q = Queue(maxsize=5)
    try:
        q._queue.append(1)
        q._queue.append(2)
        q._getters.append(object())
        q._putters.append((3, object()))
        q._unfinished_tasks = 2
        assert getattr(q, "_queue", None)
        assert q._getters
        assert q._putters
        assert q._unfinished_tasks
        result = q._format()
        expected = "maxsize=%r" % (q.maxsize,)
        expected += " queue=%r" % q._queue
        expected += " getters[%s]" % len(q._getters)
        expected += " putters[%s]" % len(q._putters)
        expected += " tasks=%s" % q._unfinished_tasks
        assert result == expected
        assert "maxsize=5" in result
        assert ("queue=%r" % q._queue) in result
        assert "getters[1]" in result
        assert "putters[1]" in result
        assert "tasks=2" in result
    finally:
        q._getters.clear()
        q._putters.clear()
        q._queue.clear()
        q._unfinished_tasks = 0


def test_format_queue_only():
    q = Queue(maxsize=10)
    try:
        q._queue.append("a")
        q._unfinished_tasks = 1
        result = q._format()
        assert "queue=%r" % (q._queue,) in result
        assert "tasks=1" in result
        assert "getters" not in result
        assert "putters" not in result
    finally:
        q._queue.clear()
        q._unfinished_tasks = 0


def test_format_getters_only():
    q = Queue()
    try:
        q._getters.append(object())
        q._getters.append(object())
        result = q._format()
        assert "getters[2]" in result
        assert "queue=" not in result
        assert "putters" not in result
        assert "tasks=" not in result
    finally:
        q._getters.clear()


def test_format_putters_only():
    q = Queue(maxsize=1)
    try:
        q._putters.append(("x", object()))
        result = q._format()
        assert "putters[1]" in result
        assert "queue=" not in result
        assert "getters" not in result
        assert "tasks=" not in result
    finally:
        q._putters.clear()


def test_format_tasks_only():
    q = Queue()
    try:
        q._unfinished_tasks = 3
        result = q._format()
        assert "tasks=3" in result
        assert "queue=" not in result
        assert "getters" not in result
        assert "putters" not in result
    finally:
        q._unfinished_tasks = 0


def test_format_no_queue_attr_false_branch(monkeypatch):
    q = Queue()
    try:
        q._queue.append("item")
        q._unfinished_tasks = 1
        assert q._format().find("queue=") != -1
        monkeypatch.delattr(q, "_queue", raising=True)
        assert getattr(q, "_queue", None) is None
        result = q._format()
        assert result.startswith("maxsize=0")
        assert "queue=" not in result
        assert "tasks=1" in result
    finally:
        pass
