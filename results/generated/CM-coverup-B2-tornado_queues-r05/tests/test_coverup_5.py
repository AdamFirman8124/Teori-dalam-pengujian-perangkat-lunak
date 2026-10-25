# file: project/tornado/queues.py:59-70
# asked: {"lines": [62, 64, 65, 66, 68, 69, 70], "branches": [[62, 0], [62, 64], [65, 0], [65, 66]]}
# gained: {"lines": [62, 64, 65, 66, 68, 69, 70], "branches": [[62, 0], [62, 64], [65, 0], [65, 66]]}

import asyncio
import datetime

import pytest
from tornado import gen, ioloop
from tornado.concurrent import Future
from tornado.queues import _set_timeout


class _StubFuture:
    def __init__(self):
        self._done = False
        self._exc = None
        self._result = None
        self._callbacks = []

    def done(self):
        return self._done

    def set_exception(self, exc):
        if self._done:
            raise asyncio.InvalidStateError("already done")
        self._exc = exc
        self._done = True
        for cb in list(self._callbacks):
            cb(self)

    def set_result(self, result):
        if self._done:
            raise asyncio.InvalidStateError("already done")
        self._result = result
        self._done = True
        for cb in list(self._callbacks):
            cb(self)

    def result(self):
        if self._exc is not None:
            raise self._exc
        return self._result

    def exception(self):
        return self._exc

    def add_done_callback(self, cb):
        self._callbacks.append(cb)
        if self._done:
            cb(self)


class _FakeLoop:
    def __init__(self):
        self.add_calls = []
        self.remove_calls = []
        self._handles = {}
        self._counter = 0

    def add_timeout(self, deadline, callback):
        self._counter += 1
        handle = ("handle-%d" % self._counter)
        self._handles[handle] = callback
        self.add_calls.append((deadline, callback, handle))
        return handle

    def remove_timeout(self, handle):
        self.remove_calls.append(handle)
        self._handles.pop(handle, None)

    def fire(self, handle):
        self._handles[handle]()


def test_set_timeout_none_does_nothing(monkeypatch):
    def _fail_current():
        raise AssertionError("IOLoop.current() must not be called for falsy timeout")
    monkeypatch.setattr(ioloop.IOLoop, "current", staticmethod(_fail_current))
    fut = _StubFuture()
    _set_timeout(fut, None)  # type: ignore[arg-type]
    assert not fut.done()
    assert fut._callbacks == []
    assert fut.exception() is None


def test_set_timeout_zero_does_nothing(monkeypatch):
    def _fail_current():
        raise AssertionError("IOLoop.current() must not be called for falsy timeout")
    monkeypatch.setattr(ioloop.IOLoop, "current", staticmethod(_fail_current))
    fut = _StubFuture()
    _set_timeout(fut, 0)  # type: ignore[arg-type]
    assert not fut.done()
    assert fut._callbacks == []


def test_set_timeout_pending_future_times_out(monkeypatch):
    fake_loop = _FakeLoop()
    monkeypatch.setattr(ioloop.IOLoop, "current", staticmethod(lambda: fake_loop))
    fut = _StubFuture()
    _set_timeout(fut, 0.05)
    # lines 68-70 executed
    assert len(fake_loop.add_calls) == 1
    deadline, on_timeout, handle = fake_loop.add_calls[0]
    assert deadline == 0.05
    assert len(fut._callbacks) == 1
    # future still pending, so on_timeout takes `if not future.done()` True branch
    assert not fut.done()
    on_timeout()
    assert fut.done()
    assert isinstance(fut.exception(), gen.TimeoutError)


def test_set_timeout_already_done_no_overwrite(monkeypatch):
    fake_loop = _FakeLoop()
    monkeypatch.setattr(ioloop.IOLoop, "current", staticmethod(lambda: fake_loop))
    fut = _StubFuture()
    fut.set_result(123)
    assert fut.done()
    _set_timeout(fut, 0.05)
    assert len(fake_loop.add_calls) == 1
    _, on_timeout, handle = fake_loop.add_calls[0]
    # done-callback registered at line 70 fires immediately for already-done future
    assert handle in fake_loop.remove_calls
    # on_timeout takes `if not future.done()` False branch: must not overwrite
    on_timeout()
    assert fut.done()
    assert fut.exception() is None
    assert fut.result() == 123


def test_set_timeout_done_callback_removes_timeout(monkeypatch):
    fake_loop = _FakeLoop()
    monkeypatch.setattr(ioloop.IOLoop, "current", staticmethod(lambda: fake_loop))
    fut = _StubFuture()
    _set_timeout(fut, datetime.timedelta(seconds=5))
    assert len(fake_loop.add_calls) == 1
    deadline, _, handle = fake_loop.add_calls[0]
    assert isinstance(deadline, datetime.timedelta)
    assert fake_loop.remove_calls == []
    # completing the future must trigger `lambda _: io_loop.remove_timeout(handle)`
    done_cb = fut._callbacks[0]
    done_cb(fut) if False else fut.set_result("ok")
    assert fut.done()
    assert fut.result() == "ok"
    assert fake_loop.remove_calls == [handle]


def test_set_timeout_real_loop_timedelta_fires():
    async def _main():
        fut = Future()
        assert not fut.done()
        _set_timeout(fut, datetime.timedelta(seconds=0.01))
        with pytest.raises(gen.TimeoutError):
            await fut
        assert fut.done()
        assert isinstance(fut.exception(), gen.TimeoutError)
    asyncio.run(_main())


def test_set_timeout_real_loop_result_before_timeout_no_error():
    async def _main():
        fut = Future()
        _set_timeout(fut, datetime.timedelta(seconds=10))
        fut.set_result(42)
        assert await fut == 42
        await asyncio.sleep(0)
        assert fut.done()
        assert fut.result() == 42
    asyncio.run(_main())
