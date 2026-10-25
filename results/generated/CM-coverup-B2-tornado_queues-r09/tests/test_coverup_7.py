# file: project/tornado/queues.py:186-207
# asked: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}

import asyncio
import datetime

import pytest
from tornado import queues
from tornado.queues import Queue


@pytest.fixture
def event_loop():
    try:
        previous_loop = asyncio.get_event_loop()
    except RuntimeError:
        previous_loop = None

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        asyncio.set_event_loop(None)
        loop.close()
        if previous_loop is not None and not previous_loop.is_closed():
            asyncio.set_event_loop(previous_loop)


def test_put_succeeds_immediately_when_queue_has_room(event_loop):
    queue = Queue(maxsize=1)

    future = queue.put("item")

    assert future.done()
    assert future.result() is None
    assert queue.qsize() == 1
    assert queue.get_nowait() == "item"

    queue.task_done()
    assert queue.empty()


def test_put_waits_when_queue_is_full(event_loop, monkeypatch):
    queue = Queue(maxsize=1)
    queue.put_nowait("first")
    timeout = datetime.timedelta(seconds=10)
    timeout_calls = []

    def record_timeout(future, requested_timeout):
        timeout_calls.append((future, requested_timeout))

    monkeypatch.setattr(queues, "_set_timeout", record_timeout)

    future = queue.put("second", timeout=timeout)

    assert not future.done()
    assert list(queue._putters) == [("second", future)]
    assert timeout_calls == [(future, timeout)]

    assert queue.get_nowait() == "first"
    queue.task_done()

    assert future.done()
    assert future.result() is None
    assert queue.get_nowait() == "second"
    queue.task_done()

    assert queue.empty()
    assert not queue._putters
