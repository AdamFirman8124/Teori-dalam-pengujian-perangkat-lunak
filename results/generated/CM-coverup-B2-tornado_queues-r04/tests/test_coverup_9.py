# file: project/tornado/queues.py:180-184
# asked: {"lines": [181, 182, 184], "branches": [[181, 182], [181, 184]]}
# gained: {"lines": [181, 182, 184], "branches": [[181, 182], [181, 184]]}

import pytest

from tornado.queues import Queue


def test_full_unbounded_maxsize_zero_is_never_full():
    q = Queue(maxsize=0)
    try:
        assert q.maxsize == 0
        assert q.qsize() == 0
        assert q.full() is False

        q.put_nowait("a")
        q.put_nowait("b")
        q.put_nowait("c")

        assert q.qsize() == 3
        assert q.full() is False
    finally:
        while not q.empty():
            q.get_nowait()
            q.task_done()
        assert q.qsize() == 0


def test_full_default_queue_is_unbounded_and_not_full():
    q = Queue()
    try:
        assert q.maxsize == 0
        assert q.full() is False

        q.put_nowait(1)

        assert q.qsize() == 1
        assert q.full() is False
    finally:
        while not q.empty():
            q.get_nowait()
            q.task_done()
        assert q.qsize() == 0


def test_full_bounded_queue_below_maxsize():
    q = Queue(maxsize=2)
    try:
        assert q.maxsize == 2
        assert q.qsize() == 0
        assert q.full() is False

        q.put_nowait("a")

        assert q.qsize() == 1
        assert q.full() is False
    finally:
        while not q.empty():
            q.get_nowait()
            q.task_done()
        assert q.qsize() == 0


def test_full_bounded_queue_at_maxsize_and_after_removal():
    q = Queue(maxsize=2)
    try:
        q.put_nowait("a")
        assert q.full() is False

        q.put_nowait("b")

        assert q.qsize() == 2
        assert q.full() is True

        item = q.get_nowait()
        q.task_done()

        assert item == "a"
        assert q.qsize() == 1
        assert q.full() is False

        q.put_nowait("c")

        assert q.qsize() == 2
        assert q.full() is True
    finally:
        while not q.empty():
            q.get_nowait()
            q.task_done()
        assert q.qsize() == 0
        assert q.full() is False


def test_full_bounded_queue_maxsize_one():
    q = Queue(maxsize=1)
    try:
        assert q.full() is False

        q.put_nowait(42)

        assert q.qsize() == 1
        assert q.full() is True
    finally:
        while not q.empty():
            q.get_nowait()
            q.task_done()
        assert q.qsize() == 0
        assert q.full() is False
