# file: project/tornado/queues.py:186-207
# asked: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}

import asyncio
import datetime

import tornado.queues
from tornado.queues import Queue


async def _put_immediately_adds_item_and_resolves_future():
    queue = Queue(maxsize=1)

    future = queue.put("item")

    assert future.done()
    assert future.result() is None
    assert queue.qsize() == 1
    assert queue.get_nowait() == "item"

    queue.task_done()
    assert queue.empty()
    await queue.join()


def test_put_immediately_adds_item_and_resolves_future():
    asyncio.run(_put_immediately_adds_item_and_resolves_future())


async def _put_waits_when_queue_is_full(monkeypatch):
    queue = Queue(maxsize=1)
    timeout = datetime.timedelta(seconds=10)
    timeout_calls = []

    def record_timeout(future, supplied_timeout):
        timeout_calls.append((future, supplied_timeout))

    monkeypatch.setattr(tornado.queues, "_set_timeout", record_timeout)

    queue.put_nowait("first")
    future = queue.put("second", timeout=timeout)

    assert not future.done()
    assert list(queue._putters) == [("second", future)]
    assert timeout_calls == [(future, timeout)]

    assert queue.get_nowait() == "first"
    assert future.done()
    assert future.result() is None
    queue.task_done()

    assert queue.get_nowait() == "second"
    queue.task_done()

    assert queue.empty()
    assert not queue._putters
    await queue.join()


def test_put_waits_when_queue_is_full(monkeypatch):
    asyncio.run(_put_waits_when_queue_is_full(monkeypatch))
