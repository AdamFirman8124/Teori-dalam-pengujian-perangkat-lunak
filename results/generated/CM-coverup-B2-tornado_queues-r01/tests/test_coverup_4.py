# file: project/tornado/queues.py:59-70
# asked: {"lines": [62, 64, 65, 66, 68, 69, 70], "branches": [[62, 0], [62, 64], [65, 0], [65, 66]]}
# gained: {"lines": [62, 64, 65, 66, 68, 69, 70], "branches": [[62, 0], [62, 64], [65, 0], [65, 66]]}

import datetime
from unittest.mock import Mock

import pytest
from tornado import gen, ioloop
from tornado.concurrent import Future
from tornado.queues import _set_timeout


def test_set_timeout_expires_pending_future_and_removes_timeout(monkeypatch):
    future = Mock(spec=Future)
    future.done.return_value = False

    loop = Mock()
    timeout_handle = object()
    loop.add_timeout.return_value = timeout_handle

    current = Mock(return_value=loop)
    monkeypatch.setattr(ioloop.IOLoop, "current", current)

    _set_timeout(future, 1.25)

    current.assert_called_once_with()
    loop.add_timeout.assert_called_once()
    timeout, on_timeout = loop.add_timeout.call_args.args
    assert timeout == 1.25

    on_timeout()

    future.done.assert_called_once_with()
    future.set_exception.assert_called_once()
    assert isinstance(future.set_exception.call_args.args[0], gen.TimeoutError)

    done_callback = future.add_done_callback.call_args.args[0]
    done_callback(future)

    loop.remove_timeout.assert_called_once_with(timeout_handle)


def test_set_timeout_does_not_overwrite_completed_future(monkeypatch):
    future = Mock(spec=Future)
    future.done.return_value = True

    loop = Mock()
    timeout_handle = object()
    loop.add_timeout.return_value = timeout_handle
    monkeypatch.setattr(ioloop.IOLoop, "current", Mock(return_value=loop))

    _set_timeout(future, datetime.timedelta(seconds=1))

    _, on_timeout = loop.add_timeout.call_args.args
    on_timeout()

    future.done.assert_called_once_with()
    future.set_exception.assert_not_called()

    done_callback = future.add_done_callback.call_args.args[0]
    done_callback(future)

    loop.remove_timeout.assert_called_once_with(timeout_handle)


@pytest.mark.parametrize("timeout", [None, 0, 0.0, datetime.timedelta(0)])
def test_set_timeout_ignores_falsy_timeout(monkeypatch, timeout):
    future = Mock(spec=Future)
    current = Mock()
    monkeypatch.setattr(ioloop.IOLoop, "current", current)

    _set_timeout(future, timeout)

    current.assert_not_called()
    future.add_done_callback.assert_not_called()
    future.set_exception.assert_not_called()
