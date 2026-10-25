# file: project/tornado/queues.py:186-207
# asked: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}

import asyncio
import datetime

import tornado.queues


def test_put_succeeds_immediately():
    async def run_test():
        queue = tornado.queues.Queue(maxsize=1)

        future = queue.put("item")

        assert future.done()
        assert future.result() is None
        assert queue.qsize() == 1
        assert queue.get_nowait() == "item"

        queue.task_done()
        assert queue.empty()
        await queue.join()

    with asyncio.Runner() as runner:
        runner.run(run_test())


def test_put_waits_when_queue_is_full(monkeypatch):
    async def run_test():
        queue = tornado.queues.Queue(maxsize=1)
        queue.put_nowait("first")
        timeout = datetime.timedelta(seconds=5)
        timeout_calls = []

        def record_timeout(future, received_timeout):
            timeout_calls.append((future, received_timeout))

        monkeypatch.setattr(tornado.queues, "_set_timeout", record_timeout)

        future = queue.put("second", timeout=timeout)

        assert not future.done()
        assert timeout_calls == [(future, timeout)]
        assert queue.full()
        assert queue.qsize() == 1

        assert queue.get_nowait() == "first"
        assert future.done()
        assert future.result() is None
        assert queue.qsize() == 1

        assert queue.get_nowait() == "second"
        queue.task_done()
        queue.task_done()

        assert queue.empty()
        await queue.join()

    with asyncio.Runner() as runner:
        runner.run(run_test())
