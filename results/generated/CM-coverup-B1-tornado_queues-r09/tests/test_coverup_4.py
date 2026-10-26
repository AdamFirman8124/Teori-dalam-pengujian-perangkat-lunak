# file: project/tornado/queues.py:59-70
# asked: {"lines": [62, 64, 65, 66, 68, 69, 70], "branches": [[62, 0], [62, 64], [65, 0], [65, 66]]}
# gained: {"lines": [62, 64, 65, 66, 68, 69, 70], "branches": [[62, 0], [62, 64], [65, 0], [65, 66]]}

import asyncio
import datetime
import types

import pytest

from tornado import gen, ioloop
from tornado.concurrent import Future
from tornado.queues import _set_timeout


class FakeIOLoop:
    def __init__(self):
        self.added = []
        self.removed = []

    def add_timeout(self, timeout, callback):
        handle = object()
        self.added.append((handle, timeout, callback))
        return handle

    def remove_timeout(self, handle):
        self.removed.append(handle)


@pytest.fixture
def fake_loop(monkeypatch):
    loop = FakeIOLoop()
    fake_module = types.SimpleNamespace(
        IOLoop=types.SimpleNamespace(current=lambda: loop)
    )
    monkeypatch.setattr("tornado.queues.ioloop", fake_module)
    return loop


def test_timeout_fires_and_sets_exception(fake_loop):
    async def main():
        future = Future()
        _set_timeout(future, 0.5)

        assert len(fake_loop.added) == 1
        handle, timeout, on_timeout = fake_loop.added[0]
        assert timeout == 0.5

        on_timeout()

        assert future.done()
        with pytest.raises(gen.TimeoutError):
            future.result()

        await asyncio.sleep(0)
        assert fake_loop.removed == [handle]

    asyncio.run(main())


def test_timeout_does_not_override_completed_future(fake_loop):
    async def main():
        future = Future()
        future.set_result("already-done")

        _set_timeout(future, 1.0)
        assert len(fake_loop.added) == 1
        handle, _, on_timeout = fake_loop.added[0]

        on_timeout()

        assert future.done()
        assert future.result() == "already-done"

        await asyncio.sleep(0)
        assert fake_loop.removed == [handle]

    asyncio.run(main())


@pytest.mark.parametrize("timeout", [None, 0, 0.0, datetime.timedelta(0)])
def test_falsy_timeout_registers_nothing(fake_loop, timeout):
    async def main():
        future = Future()
        _set_timeout(future, timeout)

        assert fake_loop.added == []
        assert fake_loop.removed == []
        assert not future.done()

    asyncio.run(main())


def test_real_ioloop_timeout_raises_and_cleans_up():
    async def main():
        future = Future()
        _set_timeout(future, 0.01)
        with pytest.raises(gen.TimeoutError):
            await future
        assert future.done()

    io_loop = ioloop.IOLoop()
    try:
        io_loop.run_sync(main)
        assert not getattr(io_loop, "_timeouts", [])
    finally:
        io_loop.close()
