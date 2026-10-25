# file: project/tornado/queues.py:336-346
# asked: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}
# gained: {"lines": [337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}

from tornado.queues import Queue


def test_queue_format_when_empty():
    queue = Queue()

    assert queue._format() == "maxsize=0"


def test_queue_format_with_queue_waiters_and_unfinished_tasks():
    queue = Queue(maxsize=3)
    queue.put_nowait("item")
    queue._getters.append(object())
    queue._putters.append(object())

    try:
        assert queue._format() == (
            "maxsize=3 queue=deque(['item']) getters[1] putters[1] tasks=1"
        )
    finally:
        queue._getters.clear()
        queue._putters.clear()
        if not queue.empty():
            queue.get_nowait()
            queue.task_done()
