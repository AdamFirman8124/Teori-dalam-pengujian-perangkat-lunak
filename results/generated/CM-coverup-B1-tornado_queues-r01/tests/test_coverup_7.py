# file: project/tornado/queues.py:186-207
# asked: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}

import asyncio
import datetime

import pytest
from tornado.util import TimeoutError as TornadoTimeoutError

from tornado.queues import Queue


def test_put_immediate_success():
    async def main():
        q = Queue(maxsize=2)
        try:
            future = q.put("hello")

            assert future.done()
            assert future.result() is None
            assert q.qsize() == 1
            assert not q.empty()
            assert len(q._putters) == 0

            assert q.get_nowait() == "hello"
            q.task_done()
            assert q.empty()
            assert q.qsize() == 0
        finally:
            while not q.empty():
                q.get_nowait()
                q.task_done()

    asyncio.run(main())


def test_put_unbounded_queue_immediate_success():
    async def main():
        q = Queue()
        try:
            future = q.put(42)

            assert future.done()
            assert future.result() is None
            assert q.qsize() == 1
            assert q.get_nowait() == 42
            q.task_done()
            assert q.empty()
        finally:
            while not q.empty():
                q.get_nowait()
                q.task_done()

    asyncio.run(main())


def test_put_when_full_defers_and_completes_after_get():
    async def main():
        q = Queue(maxsize=1)
        try:
            first_future = q.put("first")
            assert first_future.done()
            assert first_future.result() is None

            blocked_future = q.put("second")

            assert not blocked_future.done()
            assert q.qsize() == 1
            assert len(q._putters) == 1
            queued_item, queued_future = q._putters[0]
            assert queued_item == "second"
            assert queued_future is blocked_future

            assert q.get_nowait() == "first"
            q.task_done()

            assert blocked_future.done()
            assert blocked_future.result() is None
            assert len(q._putters) == 0
            assert q.qsize() == 1

            assert q.get_nowait() == "second"
            q.task_done()
            assert q.empty()
        finally:
            for _item, putter in list(q._putters):
                if not putter.done():
                    putter.cancel()
            q._putters.clear()
            while not q.empty():
                q.get_nowait()
                q.task_done()

    asyncio.run(main())


def test_put_when_full_with_timedelta_timeout():
    async def main():
        q = Queue(maxsize=1)
        try:
            q.put_nowait("first")

            future = q.put("second", timeout=datetime.timedelta(seconds=10))

            assert not future.done()
            assert len(q._putters) == 1
            assert q._putters[0][0] == "second"
            assert q._putters[0][1] is future

            assert q.get_nowait() == "first"
            q.task_done()

            assert future.done()
            assert future.result() is None
            assert len(q._putters) == 0

            assert q.get_nowait() == "second"
            q.task_done()
            assert q.empty()
        finally:
            for _item, putter in list(q._putters):
                if not putter.done():
                    putter.cancel()
            q._putters.clear()
            while not q.empty():
                q.get_nowait()
                q.task_done()

    asyncio.run(main())


def test_put_when_full_with_timeout_expires():
    async def main():
        q = Queue(maxsize=1)
        try:
            q.put_nowait("first")

            future = q.put(
                "second", timeout=datetime.timedelta(milliseconds=50)
            )
            assert not future.done()
            assert len(q._putters) == 1

            with pytest.raises(TornadoTimeoutError):
                await future

            assert future.done()

            # Consuming the existing item expires/cleans the timed-out putter.
            assert q.get_nowait() == "first"
            q.task_done()
            assert len(q._putters) == 0
            assert q.empty()
        finally:
            for _item, putter in list(q._putters):
                if not putter.done():
                    putter.cancel()
            q._putters.clear()
            while not q.empty():
                q.get_nowait()
                q.task_done()

    asyncio.run(main())
