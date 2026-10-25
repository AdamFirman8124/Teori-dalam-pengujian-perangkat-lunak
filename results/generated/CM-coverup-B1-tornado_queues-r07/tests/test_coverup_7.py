# file: project/tornado/queues.py:186-207
# asked: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}

import asyncio
import datetime

import pytest

import tornado.queues as queues_mod
from tornado.queues import Queue, QueueFull


def test_put_fast_path_sets_result():
    async def main():
        q = Queue(maxsize=2)
        fut = q.put("a")
        # else-branch: put_nowait succeeded, so the future is resolved at once
        assert fut.done()
        assert fut.result() is None
        assert q.qsize() == 1
        assert len(q._putters) == 0
        assert q.get_nowait() == "a"
        assert q.empty()

    asyncio.run(main())


def test_put_full_no_timeout_queues_putter():
    async def main():
        q = Queue(maxsize=1)
        q.put_nowait("first")
        assert q.full()

        fut = q.put("second")
        # except QueueFull branch, timeout=None -> no timer scheduled
        assert not fut.done()
        assert len(q._putters) == 1
        item, stored_fut = q._putters[0]
        assert item == "second"
        assert stored_fut is fut
        assert q.qsize() == 1

        # cleanup
        fut.cancel()
        q._consume_expired()
        assert len(q._putters) == 0
        assert q.get_nowait() == "first"
        assert q.empty()

    asyncio.run(main())


def test_put_full_with_float_timeout_calls_set_timeout(monkeypatch):
    seen = {}
    orig_set_timeout = queues_mod._set_timeout

    def spy_set_timeout(future, timeout):
        seen["timeout"] = timeout
        seen["future"] = future
        return orig_set_timeout(future, timeout)

    monkeypatch.setattr(queues_mod, "_set_timeout", spy_set_timeout)

    async def main():
        q = Queue(maxsize=1)
        q.put_nowait("x")
        assert q.full()

        fut = q.put("y", timeout=100.0)
        assert seen["timeout"] == 100.0
        assert seen["future"] is fut
        assert len(q._putters) == 1
        assert q._putters[0][0] == "y"
        assert q._putters[0][1] is fut
        assert not fut.done()

        # cleanup: cancel removes the scheduled timeout via done-callback
        fut.cancel()
        q._consume_expired()
        assert len(q._putters) == 0
        assert q.get_nowait() == "x"
        assert q.empty()

    asyncio.run(main())


def test_put_full_with_timedelta_timeout():
    async def main():
        q = Queue(maxsize=1)
        q.put_nowait("a")
        assert q.full()

        td = datetime.timedelta(seconds=5)
        fut = q.put("b", timeout=td)
        # except QueueFull branch with a timedelta timeout
        assert not fut.done()
        assert len(q._putters) == 1
        assert q._putters[0][0] == "b"
        assert q._putters[0][1] is fut

        # cleanup
        fut.cancel()
        q._consume_expired()
        assert len(q._putters) == 0
        assert q.get_nowait() == "a"
        assert q.empty()

    asyncio.run(main())
