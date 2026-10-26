# file: project/tornado/queues.py:59-70
# asked: {"lines": [62, 64, 65, 66, 68, 69, 70], "branches": [[62, 0], [62, 64], [65, 0], [65, 66]]}
# gained: {"lines": [62, 64, 65, 66, 68, 69, 70], "branches": [[62, 64], [65, 66]]}

import datetime

import pytest

from tornado import gen, ioloop
from tornado.concurrent import Future
from tornado.queues import _set_timeout


def test_set_timeout_fires_and_raises_timeout_error():
    """Covers lines 62, 64-66, 68-69: a truthy timeout that expires on a
    not-yet-done future sets a gen.TimeoutError on it."""
    io_loop = ioloop.IOLoop()
    try:

        async def main():
            future = Future()
            _set_timeout(future, datetime.timedelta(seconds=0.01))
            assert not future.done()
            with pytest.raises(gen.TimeoutError):
                await future
            assert future.done()
            assert isinstance(future.exception(), gen.TimeoutError)

        io_loop.run_sync(main)
    finally:
        io_loop.close(all_fds=False)


def test_set_timeout_removes_handle_when_future_completes_first(monkeypatch):
    """Covers lines 62, 68-70: when the future resolves before the timeout
    expires, the done-callback removes the pending timeout handle, and
    on_timeout never fires (no TimeoutError is set)."""
    io_loop = ioloop.IOLoop()
    try:
        removed_handles = []
        original_remove_timeout = io_loop.remove_timeout

        def spy_remove_timeout(handle):
            removed_handles.append(handle)
            return original_remove_timeout(handle)

        monkeypatch.setattr(io_loop, "remove_timeout", spy_remove_timeout)

        async def main():
            future = Future()
            _set_timeout(future, 60.0)  # float timeout: would fire long after
            future.set_result(42)
            # Yield to the IOLoop so the done-callback (which removes the
            # timeout handle) gets a chance to run.
            await gen.sleep(0.01)
            assert future.done()
            assert future.result() == 42
            assert future.exception() is None

        io_loop.run_sync(main)

        # The done-callback must have removed exactly the one pending timeout.
        assert len(removed_handles) == 1
    finally:
        io_loop.close(all_fds=False)
