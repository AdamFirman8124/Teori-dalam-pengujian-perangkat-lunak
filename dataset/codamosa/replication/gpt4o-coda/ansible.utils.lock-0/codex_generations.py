

# Generated at 2024-06-01 13:15:22.059903
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:15:25.463802
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:15:28.474307
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:15:31.132945
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:15:35.282021
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:15:38.935093
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:15:41.755904
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:15:46.294010
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:15:48.583922
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:15:52.500293
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:15:58.584623
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:01.143678
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:05.055784
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:07.530274
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:10.048373
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:12.551969
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:15.196530
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:17.708000
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass:
        def __init__(self):
            self._lock = threading.Lock()
            self.counter = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            self.counter += 1

    # Test with instance attribute lock
    obj = TestClass()
    obj.increment()
    assert obj.counter == 1, "Counter should be incremented to 1"

    # Test with explicit lock
    explicit_lock = threading.Lock()

    @lock_decorator(lock=explicit_lock)
    def increment_counter(counter):
        counter[0] += 1

    counter = [0]
    increment_counter(counter)
    assert counter[0] == 1, "Counter should be incremented to 1"

    print("All tests passed.")

test_lock_decorator()

# Generated at 2024-06-01 13:16:20.240450
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:22.792635
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:33.225857
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:36.337550
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:40.281180
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:42.666509
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:45.156204
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:48.918488
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:52.610274
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:56.049301
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:16:59.288913
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:17:04.123673
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:17:21.828239
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:17:24.494260
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:17:26.891461
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:17:29.870182
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:17:33.811023
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:17:36.657747
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:17:39.679888
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:17:42.889565
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:17:45.481885
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:17:51.457472
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:18:18.902363
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:18:21.900354
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:18:25.033769
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:18:27.633910
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:18:31.137809
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:18:35.358113
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:18:39.835485
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:18:42.248043
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:18:45.876776
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:18:49.544482
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:19:47.655044
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:19:50.918167
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:19:53.961658
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:19:56.703706
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:19:59.484208
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:20:02.626120
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:20:05.542005
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:20:08.773757
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:20:12.134856
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:20:14.909155
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:22:05.343076
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:22:08.386114
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:22:10.742981
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:22:13.844508
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:22:19.014848
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:22:22.213144
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:22:24.775311
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:22:27.135943
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:22:29.772717
# Unit test for function lock_decorator
def test_lock_decorator():    import threading


# Generated at 2024-06-01 13:22:32.193189
# Unit test for function lock_decorator
def test_lock_decorator():    import threading
