# file: project/tornado/queues.py:225-254
# asked: {"lines": [248, 249, 250, 251, 252, 253, 254], "branches": []}
# gained: {"lines": [248, 249, 250, 251, 252, 253, 254], "branches": []}

import asyncio
import datetime

from tornado.queues import Queue


def test_get_returns_immediately_when_item_available(monkeypatch):
    import tornado.queues as queues_mod

    calls = []
    orig = queues_mod._set_timeout

    def spy(future, timeout):
        calls.append(timeout)
        return orig(future, timeout)

    monkeypatch.setattr(queues_mod, "_set_timeout", spy)

    async def main():
        q = Queue()
        q.put_nowait(123)
        fut = q.get()
        assert fut.done()
        assert len(q._getters) == 0
        result = await fut
        assert result == 123
        assert q.qsize() == 0
        # fast path must not call _set_timeout
        assert calls == []

    asyncio.run(main())


def test_get_waits_when_empty_then_resolved_by_put(monkeypatch):
    import tornado.queues as queues_mod

    calls = []
    orig = queues_mod._set_timeout

    def spy(future, timeout):
        calls.append(timeout)
        return orig(future, timeout)

    monkeypatch.setattr(queues_mod, "_set_timeout", spy)

    async def main():
        q = Queue()
        assert q.empty()
        fut = q.get()
        # except QueueEmpty path: getter registered + _set_timeout called
        assert not fut.done()
        assert len(q._getters) == 1
        assert calls == [None]
        await q.put("value")
        assert fut.done()
        result = await fut
        assert result == "value"
        assert len(q._getters) == 0

    asyncio.run(main())


def test_get_with_timedelta_timeout_expires():
    async def main():
        q = Queue()
        fut = q.get(timeout=datetime.timedelta(seconds=0.01))
        assert not fut.done()
        assert len(q._getters) == 1
        try:
            await fut
            assert False, "expected TimeoutError"
        except Exception as e:
            assert "Timeout" in type(e).__name__
        assert fut.done()
        # expired getter stays until consumed; clean it explicitly
        q._consume_expired()
        assert len(q._getters) == 0

    asyncio.run(main())


def test_get_with_absolute_deadline_timeout_expires():
    async def main():
        q = Queue()
        deadline = asyncio.get_running_loop().time() + 0.01
        fut = q.get(timeout=deadline)
        assert not fut.done()
        assert len(q._getters) == 1
        try:
            await fut
            assert False, "expected TimeoutError"
        except Exception as e:
            assert "Timeout" in type(e).__name__
        assert fut.done()
        # expired getter stays until consumed; clean it explicitly
        q._consume_expired()
        assert len(q._getters) == 0

    asyncio.run(main())


def test_get_with_timeout_resolved_before_expiry():
    async def main():
        q = Queue()
        fut = q.get(timeout=datetime.timedelta(seconds=10))
        assert not fut.done()
        assert len(q._getters) == 1
        await q.put("early")
        result = await fut
        assert result == "early"
        assert len(q._getters) == 0

    asyncio.run(main())
