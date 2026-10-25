# file: project/tornado/queues.py:336-346
# asked: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}
# gained: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}

import collections
import pytest
from tornado.queues import Queue


def test_format_empty_queue():
    q = Queue()
    try:
        assert q.qsize() == 0
        assert len(q._getters) == 0
        assert len(q._putters) == 0
        assert q._unfinished_tasks == 0
        result = q._format()
        assert result == "maxsize=0"
        assert "queue=" not in result
        assert "getters" not in result
        assert "putters" not in result
        assert "tasks=" not in result
    finally:
        q._getters.clear()
        q._putters.clear()


def test_format_nonempty_queue_and_tasks():
    q = Queue()
    q.put_nowait(1)
    q.put_nowait(2)
    try:
        assert q.qsize() == 2
        assert q._unfinished_tasks == 2
        assert getattr(q, "_queue", None)
        result = q._format()
        # line 337
        assert result.startswith("maxsize=0")
        # lines 338-339
        assert "queue=%r" % (q._queue,) in result
        assert repr(q._queue) in result
        # lines 344-345
        assert "tasks=2" in result
    finally:
        q.get_nowait()
        q.task_done()
        q.get_nowait()
        q.task_done()
    assert q._unfinished_tasks == 0
    assert q.qsize() == 0


def test_format_getters_branch():
    q = Queue()
    assert len(q._getters) == 0
    assert "getters" not in q._format()
    q._getters.append(object())
    try:
        assert len(q._getters) == 1
        result = q._format()
        # lines 340-341
        assert "getters[1]" in result
    finally:
        q._getters.clear()
    assert len(q._getters) == 0
    assert "getters" not in q._format()


def test_format_putters_branch():
    q = Queue(maxsize=1)
    assert len(q._putters) == 0
    assert "putters" not in q._format()
    q._putters.append((object(), object()))
    try:
        assert len(q._putters) == 1
        result = q._format()
        # lines 342-343
        assert "putters[1]" in result
    finally:
        q._putters.clear()
    assert len(q._putters) == 0
    assert "putters" not in q._format()


def test_format_all_branches_combined():
    q = Queue(maxsize=10)
    q.put_nowait("a")
    q._getters.append(object())
    q._getters.append(object())
    q._putters.append(object())
    try:
        assert q._queue
        assert q._getters
        assert q._putters
        assert q._unfinished_tasks == 1
        result = q._format()
        assert "maxsize=10" in result
        assert "queue=%r" % (q._queue,) in result
        assert "getters[2]" in result
        assert "putters[1]" in result
        assert "tasks=1" in result
        assert result == (
            "maxsize=%r queue=%r getters[%s] putters[%s] tasks=%s"
            % (q.maxsize, q._queue, len(q._getters), len(q._putters), q._unfinished_tasks)
        )
    finally:
        q._getters.clear()
        q._putters.clear()
        q.get_nowait()
        q.task_done()
    assert q._unfinished_tasks == 0
    assert len(q._getters) == 0
    assert len(q._putters) == 0


def test_format_queue_none_covers_falsy_branch(monkeypatch):
    q = Queue()
    q.put_nowait("x")
    assert "queue=" in q._format()
    monkeypatch.setattr(q, "_queue", None)
    try:
        result = q._format()
        assert result.startswith("maxsize=0")
        assert "queue=" not in result
        # tasks still reported
        assert "tasks=1" in result
    finally:
        monkeypatch.undo()
    # _queue restored by undo; drain it
    assert q.qsize() == 1
    assert q.get_nowait() == "x"
    q.task_done()
    assert q._unfinished_tasks == 0


def test_format_queue_missing_attr_covers_getattr_default(monkeypatch):
    q = Queue()
    q.put_nowait("y")
    assert "queue=" in q._format()
    monkeypatch.delattr(q, "_queue", raising=True)
    try:
        assert getattr(q, "_queue", None) is None
        result = q._format()
        assert "queue=" not in result
        assert "tasks=1" in result
    finally:
        monkeypatch.undo()
    assert q.qsize() == 1
    item = q.get_nowait()
    assert item == "y"
    q.task_done()
    assert q._unfinished_tasks == 0
