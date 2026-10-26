# file: project/tornado/queues.py:336-346
# asked: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}
# gained: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}

import asyncio

import pytest

from tornado.queues import Queue


def test_queue_format_empty_queue():
    """Covers line 337 and the False branches of lines 338, 340, 342, 344."""

    async def run():
        q = Queue()
        formatted = q._format()
        assert formatted == "maxsize=0", formatted
        # No queue/getters/putters/tasks sections must appear.
        assert "queue=" not in formatted
        assert "getters" not in formatted
        assert "putters" not in formatted
        assert "tasks=" not in formatted
        # repr/str wrap _format() with the class name.
        assert repr(q).endswith(" maxsize=0>")
        assert str(q) == "<Queue maxsize=0>"

    asyncio.run(run())


def test_queue_format_with_items_and_tasks():
    """Covers the True branch of line 338 (non-empty _queue) and
    lines 344-345 (unfinished tasks)."""

    async def run():
        q = Queue(maxsize=5)
        q.put_nowait("a")
        q.put_nowait("b")
        formatted = q._format()
        assert "maxsize=5" in formatted
        assert "queue=deque(['a', 'b'])" in formatted
        assert "tasks=2" in formatted
        assert "getters" not in formatted
        assert "putters" not in formatted

    asyncio.run(run())


def test_queue_format_with_getter():
    """Covers lines 340-341 (pending getters)."""

    async def run():
        q = Queue()
        getter = q.get()  # registers a waiter synchronously, then blocks
        try:
            formatted = q._format()
            assert "getters[1]" in formatted
            assert "putters" not in formatted
        finally:
            getter.cancel()
        # Drain the cancelled waiter so the queue is left clean.
        q._consume_expired()
        assert len(q._getters) == 0
        assert "getters" not in q._format()

    asyncio.run(run())


def test_queue_format_with_putter():
    """Covers lines 342-343 (pending putters on a full queue)."""

    async def run():
        q = Queue(maxsize=1)
        q.put_nowait("x")
        putter = q.put("y")  # blocks because the queue is full
        try:
            formatted = q._format()
            assert "putters[1]" in formatted
            assert "getters" not in formatted
        finally:
            putter.cancel()
        q._consume_expired()
        assert len(q._putters) == 0
        assert "putters" not in q._format()

    asyncio.run(run())


def test_queue_format_all_sections():
    """Exercises every branch of _format in a single formatted string."""

    async def run():
        q = Queue(maxsize=1)
        q.put_nowait(1)  # non-empty queue + 1 unfinished task
        putter = q.put(2)  # blocked putter (queue is full)
        getter_q = Queue()
        getter = getter_q.get()  # blocked getter
        try:
            formatted = q._format()
            assert "maxsize=1" in formatted
            assert "queue=deque([1])" in formatted
            assert "putters[1]" in formatted
            assert "tasks=1" in formatted
            assert "getters" not in formatted  # getter is on the other queue
            assert "getters[1]" in getter_q._format()
        finally:
            putter.cancel()
            getter.cancel()
        q._consume_expired()
        getter_q._consume_expired()
        assert len(q._putters) == 0
        assert len(getter_q._getters) == 0
        # Postcondition: marking the task done clears the tasks section.
        q.task_done()
        assert "tasks=" not in q._format()

    asyncio.run(run())
