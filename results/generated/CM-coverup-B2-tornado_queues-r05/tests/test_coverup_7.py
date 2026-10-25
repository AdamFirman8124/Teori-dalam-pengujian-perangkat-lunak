# file: project/tornado/queues.py:186-207
# asked: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}

import asyncio
import datetime
import tornado.ioloop
from tornado.queues import Queue


def test_put_unbounded_immediate_success():
    async def _main():
        q = Queue()
        try:
            fut = q.put("hello")
            assert fut.done()
            assert fut.result() is None
            assert q.qsize() == 1
            assert q.get_nowait() == "hello"
            assert q.empty()
        finally:
            while not q.empty():
                try:
                    q.get_nowait()
                except Exception:
                    break
            for _, f in list(q._putters):
                if not f.done():
                    f.cancel()
            q._putters.clear()
            for g in list(q._getters):
                if not g.done():
                    g.cancel()
            q._getters.clear()
            await asyncio.sleep(0)

    asyncio.run(_main())


def test_put_when_full_enqueues_putter_without_timeout():
    async def _main():
        q = Queue(maxsize=1)
        try:
            q.put_nowait("first")
            assert q.full()
            fut = q.put("second")
            assert not fut.done()
            assert len(q._putters) == 1
            stored_item, stored_fut = q._putters[0]
            assert stored_item == "second"
            assert stored_fut is fut
            assert q.qsize() == 1
            # unblock by consuming; pending putter stays pending until get path runs
            assert q.get_nowait() == "first"
        finally:
            for _, f in list(q._putters):
                if not f.done():
                    f.cancel()
            q._putters.clear()
            while not q.empty():
                try:
                    q.get_nowait()
                except Exception:
                    break
            for g in list(q._getters):
                if not g.done():
                    g.cancel()
            q._getters.clear()
            await asyncio.sleep(0)

    asyncio.run(_main())


def test_put_when_full_with_timeout_registers_timeout(monkeypatch):
    calls = []

    orig_add_timeout = tornado.ioloop.IOLoop.add_timeout

    def fake_add_timeout(self, deadline, callback, *args, **kwargs):
        calls.append((deadline, callback))
        return orig_add_timeout(self, datetime.timedelta(seconds=60), callback, *args, **kwargs)

    monkeypatch.setattr(tornado.ioloop.IOLoop, "add_timeout", fake_add_timeout)

    async def _main():
        q = Queue(maxsize=1)
        try:
            q.put_nowait("x")
            assert q.full()
            fut = q.put("y", timeout=10)
            assert not fut.done()
            assert len(q._putters) == 1
            assert q._putters[0][1] is fut
            assert len(calls) == 1
            # timedelta variant also goes through same except branch
            fut2 = q.put("z", timeout=datetime.timedelta(seconds=5))
            assert not fut2.done()
            assert len(q._putters) == 2
            assert len(calls) == 2
            assert fut2 is q._putters[1][1]
        finally:
            for _, f in list(q._putters):
                if not f.done():
                    f.cancel()
            q._putters.clear()
            while not q.empty():
                try:
                    q.get_nowait()
                except Exception:
                    break
            for g in list(q._getters):
                if not g.done():
                    g.cancel()
            q._getters.clear()
            await asyncio.sleep(0)

    asyncio.run(_main())
    assert len(calls) == 2
