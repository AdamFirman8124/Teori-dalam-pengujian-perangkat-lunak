# file: project/tornado/queues.py:186-207
# asked: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}
# gained: {"lines": [199, 200, 201, 202, 203, 204, 206, 207], "branches": []}

import asyncio
import datetime

import pytest

import tornado.queues as queues_mod
from tornado.concurrent import Future
from tornado.queues import Queue


@pytest.fixture
def io_loop():
    """Provide a current asyncio event loop (tornado Future needs one)."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        asyncio.set_event_loop(None)
        loop.close()


def test_put_immediate_success_sets_result_none(io_loop):
    q = Queue(maxsize=2)
    fut = q.put("a")
    try:
        assert isinstance(fut, Future)
        assert fut.done()
        assert fut.result() is None
        assert len(q._putters) == 0
        assert q.qsize() == 1
        assert q.get_nowait() == "a"
        assert q.empty()
    finally:
        q._putters.clear()


def test_put_full_appends_putter_and_calls_set_timeout(io_loop, monkeypatch):
    q = Queue(maxsize=1)
    q.put_nowait("first")
    assert q.full()

    calls = []
    orig_set_timeout = queues_mod._set_timeout

    def spy(future, timeout):
        calls.append((future, timeout))
        # delegate with None so no real IOLoop timeout is scheduled
        return orig_set_timeout(future, None)

    monkeypatch.setattr(queues_mod, "_set_timeout", spy)

    fut = q.put("second")
    try:
        assert calls == [(fut, None)]
        assert not fut.done()
        assert len(q._putters) == 1
        item, pending = q._putters[0]
        assert item == "second"
        assert pending is fut
        assert q.qsize() == 1
    finally:
        fut.cancel()
        q._putters.clear()


def test_put_full_forwards_float_timeout(io_loop, monkeypatch):
    q = Queue(maxsize=1)
    q.put_nowait("first")

    captured = {}
    orig_set_timeout = queues_mod._set_timeout

    def spy(future, timeout):
        captured["future"] = future
        captured["timeout"] = timeout
        return orig_set_timeout(future, None)

    monkeypatch.setattr(queues_mod, "_set_timeout", spy)

    fut = q.put("second", timeout=10.0)
    try:
        assert captured["future"] is fut
        assert captured["timeout"] == 10.0
        assert not fut.done()
        assert len(q._putters) == 1
        assert q._putters[0][1] is fut
    finally:
        fut.cancel()
        q._putters.clear()


def test_put_full_forwards_timedelta_timeout_and_success_ignores_timeout(
    io_loop, monkeypatch
):
    q = Queue(maxsize=1)
    q.put_nowait("first")

    captured = {}
    orig_set_timeout = queues_mod._set_timeout

    def spy(future, timeout):
        captured["timeout"] = timeout
        return orig_set_timeout(future, None)

    monkeypatch.setattr(queues_mod, "_set_timeout", spy)

    td = datetime.timedelta(seconds=5)
    fut = q.put("second", timeout=td)
    try:
        assert captured["timeout"] == td
        assert not fut.done()
        assert q._putters[0][0] == "second"
    finally:
        fut.cancel()
        q._putters.clear()

    # success path ignores timeout and resolves immediately
    q2 = Queue(maxsize=1)
    fut2 = q2.put("x", timeout=td)
    try:
        assert fut2.done()
        assert fut2.result() is None
        assert len(q2._putters) == 0
        assert q2.qsize() == 1
    finally:
        q2._putters.clear()
