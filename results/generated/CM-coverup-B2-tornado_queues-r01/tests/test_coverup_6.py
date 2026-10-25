# file: project/tornado/queues.py:186-207
# asked: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}

import asyncio

import pytest
from tornado.queues import Queue


@pytest.fixture
def current_event_loop():
    try:
        previous_loop = asyncio.get_event_loop()
    except RuntimeError:
        previous_loop = None

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
        asyncio.set_event_loop(previous_loop)


def test_put_immediately_adds_item_and_returns_completed_future(current_event_loop):
    queue = Queue(maxsize=1)

    put_future = queue.put("item")

    assert put_future.done()
    assert put_future.result() is None
    assert queue.qsize() == 1
    assert queue.get_nowait() == "item"

    queue.task_done()
    assert queue.empty()
    assert queue.join().done()


def test_put_waits_when_full_and_completes_after_space_is_available(
    current_event_loop,
):
    queue = Queue(maxsize=1)
    queue.put_nowait("first")

    put_future = queue.put("second")

    assert not put_future.done()
    assert queue.qsize() == 1
    assert len(queue._putters) == 1

    assert queue.get_nowait() == "first"
    queue.task_done()

    assert put_future.done()
    assert put_future.result() is None
    assert len(queue._putters) == 0
    assert queue.qsize() == 1
    assert queue.get_nowait() == "second"

    queue.task_done()
    assert queue.empty()
    assert queue.join().done()
