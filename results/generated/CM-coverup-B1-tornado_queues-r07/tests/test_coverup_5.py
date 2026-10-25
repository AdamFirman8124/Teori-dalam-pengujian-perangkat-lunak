# file: project/tornado/queues.py:59-70
# asked: {"lines": [62, 64, 65, 66, 68, 69, 70], "branches": [[62, 0], [62, 64], [65, 0], [65, 66]]}
# gained: {"lines": [62, 64, 65, 66, 68, 69, 70], "branches": [[62, 0], [62, 64], [65, 66]]}

import datetime

import pytest
from tornado import gen, ioloop
from tornado.concurrent import Future
from tornado.queues import _set_timeout


def _run_loop(coro_func):
    """Run a coroutine on a fresh, isolated IOLoop and clean it up."""
    io_loop = ioloop.IOLoop()
    io_loop.make_current()
    try:
        return io_loop.run_sync(coro_func)
    finally:
        io_loop.clear_current()
        io_loop.close(all_fds=True)


def test_set_timeout_fires_when_future_not_done():
    """Lines 64-66: on_timeout sets a TimeoutError on a pending future."""

    async def main():
        future = Future()
        _set_timeout(future, datetime.timedelta(milliseconds=10))
        assert not future.done()
        await gen.sleep(0.05)
        return future

    future = _run_loop(main)
    assert future.done()
    exception = future.exception()
    assert isinstance(exception, gen.TimeoutError)


def test_set_timeout_removed_when_future_completes_first(monkeypatch):
    """Lines 68-70: timeout handle is removed once the future resolves."""

    async def main():
        io_loop = ioloop.IOLoop.current()
        removed_handles = []
        original_remove = io_loop.remove_timeout

        def recording_remove(handle):
            removed_handles.append(handle)
            return original_remove(handle)

        monkeypatch.setattr(io_loop, "remove_timeout", recording_remove)

        future = Future()
        _set_timeout(future, datetime.timedelta(seconds=30))
        future.set_result("done")
        # Yield so the add_done_callback lambda runs and removes the timeout.
        await gen.sleep(0.01)
        return future, removed_handles

    future, removed_handles = _run_loop(main)
    assert future.done()
    assert future.result() == "done"
    assert future.exception() is None
    assert len(removed_handles) == 1


def test_set_timeout_with_none_does_nothing(monkeypatch):
    """Line 62 false branch: no timeout is registered for a falsy timeout."""

    async def main():
        io_loop = ioloop.IOLoop.current()
        added = []
        monkeypatch.setattr(io_loop, "add_timeout", lambda *a, **k: added.append(a))
        future = Future()
        _set_timeout(future, None)
        future.set_result(42)
        await gen.sleep(0)
        return future, added

    future, added = _run_loop(main)
    assert future.result() == 42
    assert added == []
