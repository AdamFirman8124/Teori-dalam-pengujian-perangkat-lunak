# file: project/tornado/queues.py:336-346
# asked: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}
# gained: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}

from tornado.queues import Queue


def test_queue_format_when_empty():
    queue = Queue(maxsize=0)

    assert queue._format() == "maxsize=0"


def test_queue_format_includes_all_nonempty_state(monkeypatch):
    queue = Queue(maxsize=3)

    monkeypatch.setattr(queue, "_queue", ["item"])
    monkeypatch.setattr(queue, "_getters", [object(), object()])
    monkeypatch.setattr(queue, "_putters", [object()])
    monkeypatch.setattr(queue, "_unfinished_tasks", 4)

    assert (
        queue._format()
        == "maxsize=3 queue=['item'] getters[2] putters[1] tasks=4"
    )
