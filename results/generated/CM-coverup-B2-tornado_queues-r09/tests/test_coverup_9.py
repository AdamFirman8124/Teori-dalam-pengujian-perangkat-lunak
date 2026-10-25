# file: project/tornado/queues.py:225-254
# asked: {"lines": [248, 249, 250, 251, 252, 253, 254], "branches": []}
# gained: {"lines": [248, 249, 250, 251, 252, 253, 254], "branches": []}

import asyncio
import datetime

import pytest
from tornado import queues


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
        asyncio.set_event_loop(previous_loop)
        loop.close()


def test_get_returns_immediately_when_item_is_available(
    monkeypatch, current_event_loop
):
    def unexpected_timeout(*args, **kwargs):
        raise AssertionError("_set_timeout must not be called for an available item")

    monkeypatch.setattr(queues, "_set_timeout", unexpected_timeout)

    queue = queues.Queue()
    item = object()
    queue.put_nowait(item)

    future = queue.get()

    assert future.done()
    assert future.result() is item
    assert queue.empty()

    queue.task_done()
    assert queue._unfinished_tasks == 0


def test_get_waits_when_queue_is_empty(monkeypatch, current_event_loop):
    timeout = datetime.timedelta(seconds=5)
    timeout_calls = []

    def record_timeout(future, supplied_timeout):
        timeout_calls.append((future, supplied_timeout))

    monkeypatch.setattr(queues, "_set_timeout", record_timeout)

    queue = queues.Queue()
    item = object()
    future = queue.get(timeout=timeout)

    try:
        assert not future.done()
        assert list(queue._getters) == [future]
        assert timeout_calls == [(future, timeout)]

        queue.put_nowait(item)

        assert future.done()
        assert future.result() is item
        assert not queue._getters
        assert queue.empty()

        queue.task_done()
        assert queue._unfinished_tasks == 0
    finally:
        if not future.done():
            future.cancel()
        try:
            queue._getters.remove(future)
        except ValueError:
            pass
