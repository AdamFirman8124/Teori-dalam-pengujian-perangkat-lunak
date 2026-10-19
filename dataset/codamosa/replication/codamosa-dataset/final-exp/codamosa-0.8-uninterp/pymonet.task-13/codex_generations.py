

# Generated at 2022-06-14 03:58:02.275888
# Unit test for method map of class Task
def test_Task_map():
    """
    Simple unit test for method ".map" of class Task.
    """
    def assert_map(mapper, value):
        """
        Return True if value is equal result of calling mapper with value of Task.

        :param mapper: mapper function
        :type mapper: Function(A) -> B
        :param value: another value
        :type value: B
        :returns: result of equality
        :rtype: bool
        """
        return Task.of(value).map(mapper).fork(lambda x: x, lambda x: x) == mapper(value)

    assert assert_map(lambda x: x, 10) == 10
    assert assert_map(lambda x: x, -2) == -2
    assert assert_map(lambda x: x, 0) == 0


# Generated at 2022-06-14 03:58:10.516800
# Unit test for method bind of class Task
def test_Task_bind():
    def add3_then_mul_3(resolve, reject):
        resolve(3)

    def add3(resolve, reject):
        resolve(3)
    def mul_3(resolve, reject):
        resolve(3)

    assert Task(add3_then_mul_3).bind(lambda _:
        Task.reject('Error')).fork(lambda error: 'Error', lambda result: 'Result') == 'Error'
    assert Task(add3_then_mul_3).bind(lambda _:
        Task.of(1)).fork(lambda error: 'Error', lambda result: result) == 1

# Generated at 2022-06-14 03:58:13.501145
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(0)

    mapped = task.map(lambda value: value + 1)

    assert mapped.fork(
        lambda value: value,
        lambda value: value
    ) == 1


# Generated at 2022-06-14 03:58:23.890123
# Unit test for method bind of class Task
def test_Task_bind():
    # Case of resolve
    def mapper(value):
        return Task.of(value)

    task = Task.of(1)

# Generated at 2022-06-14 03:58:29.715332
# Unit test for method map of class Task
def test_Task_map():
    def add_one(n):
        return n + 1

    def fail(n):
        return False

    assert Task(lambda r, s: s(1)).map(add_one).fork(fail, lambda x: x) == 2


# Generated at 2022-06-14 03:58:33.680167
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for Task.map method
    """
    assert Task.of(1).map(lambda x: x + 1).fork(lambda _: False, lambda x: x == 2)


# Generated at 2022-06-14 03:58:39.452854
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task.
    """
    assert Task.of(42).map(lambda value: value - 42).fork(lambda value: value + 1, lambda value: value - 1) == 0
    assert Task.of(42).bind(lambda value: Task.of(value - 42)).fork(lambda value: value + 1, lambda value: value - 1) == 0



# Generated at 2022-06-14 03:58:47.197315
# Unit test for method bind of class Task
def test_Task_bind():
    @Task.of
    def add5(value):
        return value + 5

    @Task.of
    def square(value):
        return value * value

    @Task.of
    def wait(value):
        import time
        time.sleep(1)
        return value

    @Task.of
    def wait_and_square(value):
        import time
        time.sleep(1)
        return value * value

    def reject(_):
        return Task.reject(100)

    def reject_and_wait(value):
        import time
        time.sleep(1)
        return Task.reject(value)

    assert 55 == add5(50).fork(None, lambda value: value)
    assert 2500 == add5(50).bind(square).fork(None, lambda value: value)
    assert 25 == add

# Generated at 2022-06-14 03:58:54.989628
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(arg):
        return arg + 1

    def test(arg, exp):
        def is_equal(is_equal, _):
            is_equal(exp == arg)

        return Task.of(arg).bind(fn).fork(is_equal, fail)

    test(5, 6)
    test(-5, -4)
    test(0, 1)
    test(21, 22)
    test(22, 23)
    test(23, 24)


# Generated at 2022-06-14 03:58:57.952191
# Unit test for method map of class Task
def test_Task_map():
    def plus_one(arg):
        return arg + 1

    task = Task(
        lambda _, resolve: resolve(1)
    )
    mapped_task = task.map(plus_one)
    assert mapped_task.fork(
        lambda reject: reject * 3,
        lambda resolve: resolve * 3
    ) == 6


# Generated at 2022-06-14 03:59:11.845538
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve_one(resolve):
        resolve(1)

    def reject_error(reject):
        reject(RuntimeError('Danger! Danger!'))

    resolve_one_task = Task(resolve_one)
    reject_error_task = Task(reject_error)

    def add_one(value):
        return Task.of(value + 1)

    # resolve case
    result_resolve = resolve_one_task.bind(add_one)
    assert result_resolve.fork(
        lambda arg: None,
        lambda arg: arg
    ) == 2

    # reject case
    result_reject = reject_error_task.bind(add_one)

# Generated at 2022-06-14 03:59:14.322603
# Unit test for method bind of class Task
def test_Task_bind():
    assert (
        Task.of(2).bind(lambda val: Task.of(val * 2)).fork(lambda arg: arg, lambda arg: arg) == 4
    )


# Generated at 2022-06-14 03:59:22.424550
# Unit test for method bind of class Task
def test_Task_bind():
    called = 0
    def increment(arg):
        nonlocal called
        called += 1
        return Task.of(arg + 1)

    def fork(reject, resolve):
        resolve(0)

    Task(fork).bind(increment).bind(increment).fork(
        lambda arg: print(arg),
        lambda arg: print(arg)
    )

    assert called == 2

    # Unit test for method map of class Task

# Generated at 2022-06-14 03:59:27.287636
# Unit test for method map of class Task
def test_Task_map():
    """
    Task.map should return new Task with mapped resolve attribute.
    """
    def test_mapper(value):
        return value ** 2

    def test_fork(reject, resolve):
        return resolve(2)

    result = Task(test_fork).map(test_mapper)
    assert result.fork(None, lambda value: value) == 4


# Generated at 2022-06-14 03:59:33.818202
# Unit test for method bind of class Task
def test_Task_bind():
    def reject(value): return Task.reject(value)
    def resolve(value): return Task.of(value)

    assert Task(
        lambda _, resolve: resolve('a')
    ).bind(lambda arg: resolve(arg + 'b')
    ).fork(reject, resolve).fork(
        lambda arg: arg,
        lambda arg: arg
    ) == 'ab'


# Generated at 2022-06-14 03:59:40.517107
# Unit test for method map of class Task
def test_Task_map():
    def double(x):
        return x * 2

    task = Task.of(3)
    task = task.map(double).map(str)

    fork = task.fork

    def on_reject(x):
        assert False

    def on_resolve(x):
        assert x == '6'
        print('Get it!')

    fork(on_reject, on_resolve)


# Generated at 2022-06-14 03:59:42.934572
# Unit test for method bind of class Task

# Generated at 2022-06-14 03:59:50.958742
# Unit test for method bind of class Task
def test_Task_bind():
    """Same function can use like <value>.bind(mapper) or Task.bind(mapper, <value>)"""
    def assert_bind(task, bind_value):
        assert task.bind(lambda arg: arg) == bind_value

    assert_bind(Task.of(1), Task.of(1))
    assert_bind(Task.of(1).bind(lambda x: Task.of(x + 1)), Task.of(1).bind(lambda x: Task.of(x + 1)))

# Generated at 2022-06-14 03:59:56.212105
# Unit test for method map of class Task
def test_Task_map():
    fn = lambda x: x + 1
    reject = lambda _: None
    resolve = lambda _: None

    start = Task(lambda reject, resolve: resolve(1))
    end = start.map(fn)
    assert end.fork(reject, resolve) == 2



# Generated at 2022-06-14 03:59:59.305940
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    task = task.map(lambda x: x + 1)

    assert task.fork(None, lambda x: x) == 2


# Generated at 2022-06-14 04:00:06.396466
# Unit test for method bind of class Task
def test_Task_bind():
    task_a = Task.of('A')
    task_b = task_a.bind(lambda value: Task.of(value.swapcase()))
    task_c = task_a.bind(lambda value: Task.reject(value.swapcase()))

    result = task_b.fork(None, print) # print A -> a
    assert result is None
    result = task_c.fork(print, None) # print A -> a
    assert result is None

# Generated at 2022-06-14 04:00:11.731656
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(1).map(lambda b: b * 2).fork(
        lambda value: False,
        lambda value: value == 2
    )

    assert Task.of(1).map(
        lambda b: b * 2
    ).fork(lambda value: True, lambda value: False) == False


# Generated at 2022-06-14 04:00:15.757053
# Unit test for method map of class Task
def test_Task_map():
    def test_add_1(resolve, reject):
        return resolve(10)

    def add_1(value):
        return value + 1

    assert Task(test_add_1).map(add_1).fork(lambda _: None, lambda v: v) == 11


# Generated at 2022-06-14 04:00:23.142163
# Unit test for method map of class Task
def test_Task_map():
    """
    Wrap Task.of into Task.reject with bind method and check that result is rejected.
    Wrap Task.of into Task.of with map method and check that result is mapped.
    """
    def tester(fork):
        return fork(lambda a: a, lambda a: a)

    assert tester(Task.reject(42).bind(lambda x: Task.of(x + 5)).fork) == 42
    assert tester(Task.of(5).map(lambda x: x + 5).fork) == 10


# Generated at 2022-06-14 04:00:24.963998
# Unit test for method map of class Task

# Generated at 2022-06-14 04:00:37.716338
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Create Task with function, which return value and resolve it.
    Call fork function on created Task and get resolved value of this Task.

    :returns: None
    :rtype: None
    """

    def add(x):
        return Task.of(x + 1)

    def multiply(x):
        return Task.of(x * 2)

    def fn(x):
        return x * x

    def result(resolve, reject):
        return add(x).bind(multiply).bind(lambda x: add(x)).fork(
            reject, lambda x: resolve(fn(x))
        )

    t = Task(result)
    value = t.fork(lambda x: x, lambda x: x)
    assert value == (x + 1) * 2 * (x + 1) * 2 * x * x


# Generated at 2022-06-14 04:00:49.827802
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map.
    """
    def test_map_resolve(task, value, expect):
        """
        Check resolve path of mapped function.

        :param value: value to use in mapper function
        :type value: B
        :param expect: expected value
        :type expect: B
        """
        mock_resolve = Mock()
        mock_reject = Mock()
        task.fork(mock_reject, mock_resolve)
        mock_resolve.assert_called_once_with(expect)

    def test_map_reject(task, value, expect):
        """
        Check reject path of mapped function.

        :param value: value to use in mapper function
        :type value: B
        :param expect: expected value
        :type expect: B
        """
       

# Generated at 2022-06-14 04:00:56.467946
# Unit test for method map of class Task
def test_Task_map():
    def add_two(value):
        return value + 2

    task = Task(lambda _, resolve: resolve(8))
    result = task.map(add_two).fork(lambda reject: reject, lambda resolve: resolve)
    assert result == 10


# Generated at 2022-06-14 04:01:08.658615
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for bind method of class Task.
    """
    mockTaskResolved = Mock(spec=Task)
    mockTaskRejected = Mock(spec=Task)
    mockTaskResolved.fork.return_value = 'resolved'
    mockTaskRejected.fork.return_value = 'rejected'

    def mapperResolved(value):
        return mockTaskResolved

    def mapperRejected(value):
        return mockTaskRejected

    mockFork = Mock()

    task = Task(mockFork)

    # fork is not called
    assert task.bind(mapperResolved).fork(
        lambda a: 'a', lambda a: 'b') == 'resolved'
    assert mockTaskResolved.fork.call_count == 1
    assert mockTaskRejected.fork.call_count == 0


# Generated at 2022-06-14 04:01:21.861975
# Unit test for method map of class Task
def test_Task_map():
    def add(x, y):
        return x + y

    def add_two(x):
        return add(x, 2)

    def add_three(x):
        return add(x, 3)


    # printf('\n', 'Task.of(2).map(add_two).map(add_three).fork(identity, identity)')
    # printf('Result of evaluating Task.of(2).map(add_two).map(add_three).fork(identity, identity):', '\n')
    # printf(Task.of(2).map(add_two).map(add_three).fork(identity, identity))
    # printf('\n')

    assert(Task.of(2).map(add_two).map(add_three).fork(identity, identity) == 7)

# Unit test

# Generated at 2022-06-14 04:01:29.149907
# Unit test for method bind of class Task
def test_Task_bind():
    def add_one(value):
        return value + 1

    def pow_two(value):
        return Task.of(value ** 2)

    t = Task.of(1)
    t1 = t.map(add_one).map(add_one).bind(pow_two)

    assert t1.fork(print, print) == 16



# Generated at 2022-06-14 04:01:32.702738
# Unit test for method map of class Task
def test_Task_map():
    """
    Test to check Task.map method.
    """
    double = Task.of(2)
    two_task = Task.of(2).map(lambda x: x * 2)

    assert two_task.fork(lambda x: x, lambda x: x) == double.fork(lambda x: x, lambda x: x)


# Generated at 2022-06-14 04:01:40.361421
# Unit test for method map of class Task
def test_Task_map():
    """
    1. Create Task object with function that return
    5 + 4, and map it with function lambda x: x * x.
    2. Create Task object with function that return
    'bad input', and map it with function lambda x: x * x.
    3. Check if every previous Task object have right
    resolve and reject value.

    :returns: None
    """
    task = Task(lambda _, resolve: resolve(5 + 4)).map(lambda x: x * x)
    assert task.fork(lambda e: e, lambda v: (v == 81))

    task = Task(lambda _, resolve: resolve('bad input')).map(lambda x: x * x)
    assert task.fork(lambda e: e == 'bad input', lambda _: False)


# Generated at 2022-06-14 04:01:45.901109
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task.of(value + 1)

    # Resolved task
    task = Task.of(1)
    assert task.bind(fn).fork(None, lambda value: value) == 2

    # Rejected task
    task = Task.reject(1)
    assert task.bind(fn).fork(lambda value: value, None) == 1


# Generated at 2022-06-14 04:01:54.062268
# Unit test for method bind of class Task
def test_Task_bind():
    def task_resolver(value):
        def resolver(_, resolve):
            return resolve(value)
        return Task(resolver)

    def task_rejecter(value):
        def rejecter(reject, _):
            return reject(value)
        return Task(rejecter)

    @profile
    def test():

        assert Task.of(42).bind(lambda x: task_resolver(x + 1)) == Task.of(43)
        assert Task.of(42).bind(lambda x: task_rejecter(x + 1)) == Task.reject(43)


###############################################################################

if __name__ == '__main__':
    test_Task_map()
    test_Task_bind()

# Generated at 2022-06-14 04:02:05.536752
# Unit test for method bind of class Task
def test_Task_bind():
    def call_reject(arg):
        reject_called[0] = True

    def call_resolve(arg):
        resolve_called[0] = True

    # test for rejected Task
    reject_called = [False]
    resolved_called = [False]
    t = Task(lambda reject, _: reject(None))
    t = t.bind(lambda arg: Task.of(arg))
    t.fork(call_reject, call_resolve)
    assert reject_called[0] and not resolved_called[0]

    # test for resolved Task
    reject_called = [False]
    resolved_called = [False]
    t = Task(lambda _, resolve: resolve(None))
    t = t.bind(lambda arg: Task.of(arg))

# Generated at 2022-06-14 04:02:13.124573
# Unit test for method bind of class Task
def test_Task_bind():
    def bind_func(value):
        return Task.of(value+1)

    task_value = Task.of(1).bind(bind_func)

    def resolve(value):
        assert value == 2
        return value

    def reject(value):
        assert False

    task_value.fork(reject, resolve)


# Generated at 2022-06-14 04:02:17.058019
# Unit test for method map of class Task
def test_Task_map():
    """
    >>> f = lambda x: x + 1
    >>> task = Task.of(1)
    >>> task.map(f)
    Task(lambda _, resolve: resolve(f(1)))
    >>> task.map(f).fork(lambda err: None, lambda val: val)
    2
    """



# Generated at 2022-06-14 04:02:20.955010
# Unit test for method map of class Task
def test_Task_map():
    def my_function(arg):
        return arg + '!'

    assert Task(lambda _, resolve: resolve(1)).map(my_function) == 1
    assert Task(lambda _, resolve: resolve('Hello')).map(my_function) == 'Hello!'


# Generated at 2022-06-14 04:02:25.720349
# Unit test for method map of class Task
def test_Task_map():
    def add_one(x):
        return x + 1

    def add_two(x):
        return x + 2

    def resolve(x):
        assert x == 3
        print("Test 1 passed")

    def reject(x):
        assert False

    def resolve_resolve(x):
        assert x == 4
        print("Test 2 passed")

    def reject_resolve(x):
        assert False

    Task.of(2).map(add_one).fork(reject, resolve)
    Task.of(2).map(add_one).map(add_two).fork(reject, resolve_resolve)


# Generated at 2022-06-14 04:02:34.985459
# Unit test for method map of class Task
def test_Task_map():
    def identity(value):
        return value

    def plus_one(value):
        return value + 1

    plus_one_task = Task.of(1).map(plus_one)

    assert plus_one_task.fork(identity, identity) == 2

    plus_one_identity_task = Task.of(1).map(plus_one).map(identity)

    assert plus_one_identity_task.fork(identity, identity) == 2


# Generated at 2022-06-14 04:02:45.358387
# Unit test for method map of class Task
def test_Task_map():
    """
    Function to run unit test for method map of class Task.
    """

    # Case: when task is resolved and mapped value not empty
    resolved_not_empty = Task(lambda _, resolve: resolve(100)).map(lambda value: value * 3)

    assert resolved_not_empty.fork(lambda arg: arg, lambda arg: arg) == 300

    # Case: when task is resolved and mapped value is empty
    resolved_empty = Task(lambda _, resolve: resolve(100)).map(lambda _: None)

    assert resolved_empty.fork(lambda arg: arg, lambda arg: arg) is None

    # Case: when task is rejected and mapped value not empty
    rejected_not_empty = Task(lambda reject, _: reject(100)).map(lambda value: value * 3)


# Generated at 2022-06-14 04:02:48.661700
# Unit test for method bind of class Task

# Generated at 2022-06-14 04:02:55.295320
# Unit test for method map of class Task
def test_Task_map():
    """
    Test map method of class Task.

    :returns: status of test
    :rtype: bool
    """
    def mocked(message):
        def tmp(reject, resolve):
            resolve(message)
        return Task(tmp)

    result = mocked('hello').map(lambda arg: arg + ' world').fork(
        lambda _: 'fail',
        lambda arg: arg
    )

    return result == 'hello world'


# Generated at 2022-06-14 04:02:59.734684
# Unit test for method map of class Task
def test_Task_map():
    def mock_fn(arg):
        return 'MOCK_FUNC: ' + arg

    task = Task.of('MOCK_ARG')

    assert task.map(mock_fn).fork(lambda arg: 'REJECTED', lambda arg: arg) == 'MOCK_FUNC: MOCK_ARG'


# Generated at 2022-06-14 04:03:09.610022
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve_x(x):
        return Task.of(x + 1)

    def resolve_y(y):
        return Task.of(y + 2)

    def reject(e):
        return Task.reject(e)

    def fork(reject, resolve):
        return reject(4 / 0)

    task = Task(fork)

    result = (
        task
        .bind(lambda _: task.bind(lambda _: resolve_x(1)))
        .bind(lambda _: resolve_y(3))
        .bind(lambda _: Task.of(5))
    )

    assert result.fork(reject, lambda y: y) == 6


# Generated at 2022-06-14 04:03:12.164138
# Unit test for method map of class Task
def test_Task_map():
    """
    Test case for method Task.map

    :returns: bool
    :rtype: bool
    """
    value = Task.of(2).map(lambda n: n + 2).fork(
        lambda error: False,
        lambda res: res == 4
    )

    return value


# Generated at 2022-06-14 04:03:15.580831
# Unit test for method bind of class Task
def test_Task_bind():
    def increment(value):
        return Task.of(value + 1)

    task = Task.of(1)

    assert task.bind(increment).bind(increment).bind(increment).fork(None, None) == 4


# Generated at 2022-06-14 04:03:21.975617
# Unit test for method map of class Task
def test_Task_map():
    value = 'value'
    rejected = False
    resolved = False

    def mapper(arg):
        nonlocal value
        nonlocal resolved

        assert arg == value
        resolved = True
        return arg

    def reject(arg):
        nonlocal value
        nonlocal rejected

        assert arg == value
        rejected = True

    def resolve(arg):
        nonlocal value
        nonlocal resolved

        assert arg == value
        resolved = True

    task = Task.of(value).map(mapper)
    task.fork(reject, resolve)
    assert resolved and not rejected


# Generated at 2022-06-14 04:03:28.908549
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of('test')
    task = task.bind(lambda arg: Task.reject(arg))
    assert task.fork('reject', 'resolve') == 'reject'

    task = Task.of('test')
    task = task.bind(lambda arg: Task.of(arg))
    assert task.fork('reject', 'resolve') == 'resolve'


# Generated at 2022-06-14 04:03:41.027114
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Task.bind is like >>> operator in Haskell.
    """
    def add(value):
        return Task.of(value + 3)

    def sub(value):
        return Task.of(value - 2)

    result = Task.of(0) \
                .bind(add) \
                .bind(sub)


# Generated at 2022-06-14 04:03:44.268940
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task.
    """
    assert Task.of(10).bind(lambda value: Task.of(value / 2)) == Task(lambda _, resolve: resolve(5))



# Generated at 2022-06-14 04:03:53.669749
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Tests bind method of class Task
    """
    def get_sum(arg):
        def result(reject, resolve):
            value = arg + 1
            return resolve(value)

        return Task(result)

    def mapped(value):
        return value + 2

    def test(value):
        def result(reject, resolve):
            if value == 3:
                return resolve(True)

            return reject(False)

        return Task(result)

    assert Task.of(1).bind(get_sum).bind(lambda v: test(v)).fork(print, print) is True
    assert Task.of(1).bind(get_sum).bind(lambda v: test(v)).fork(print, print) is True

# Generated at 2022-06-14 04:03:55.771044
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(1).map(lambda x: x + 10).fork(identity, identity) == 11


# Generated at 2022-06-14 04:03:59.636945
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve(1)

    Task(fork).bind(lambda x: Task.of(x + 1)).fork(
        lambda x: assertEqual(x, 2),
        lambda x: assertEqual(x, 1)
    )


# Generated at 2022-06-14 04:04:09.138409
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map of class Task.
    """
    def fn(value):
        return value + 10

    def mapper(value):
        return value * 2

    def assert_Task(arg, expected_value):
        task = Task(arg)
        expected = Task.of(expected_value)

        assert task.map(mapper).fork(
            lambda value: value,
            lambda value: value
        ) == expected.fork(
            lambda value: value,
            lambda value: value
        )

    assert_Task(Task.of(10).fork, 10)
    assert_Task(Task.reject(20).fork, 20)



# Generated at 2022-06-14 04:04:19.838103
# Unit test for method map of class Task
def test_Task_map():
    """
    Test map method of Task class.
    """
    # Create test data
    value = lambda x: x + 1
    mock_reject = Mock(return_value=None)
    mock_resolve = Mock(return_value=None)
    mock_fork = Mock(return_value=None)
    task = Task(mock_fork)
    expected_result = Task(lambda reject, resolve: task.map(value).fork(reject, resolve))

    # Call test method
    result = task.map(value)

    # Check result
    mock_fork.assert_called_once_with(mock_reject, mock_resolve)
    assert result == expected_result
    assert task.fork.__name__ == mock_fork.__name__


# Generated at 2022-06-14 04:04:23.730673
# Unit test for method bind of class Task
def test_Task_bind():
    failed_task = Task.reject(42)
    return failed_task.bind(lambda value: Task.of(value + 1)).fork(
        lambda error: print(error),
        lambda value: print(value)
    )


# Generated at 2022-06-14 04:04:28.096692
# Unit test for method map of class Task
def test_Task_map():
    def increment(value):
        return value + 1

    task = Task.of(1).map(increment)

    equal(
        2,
        task.fork(lambda v: None, lambda v: v)
    )


# Generated at 2022-06-14 04:04:37.423576
# Unit test for method map of class Task
def test_Task_map():

    def slow_add(x, y):
        time.sleep(0.5)
        return x + y

    task = Task.of(1)
    result = task.map(lambda x: slow_add(x, 2)).map(lambda x: slow_add(x, 3))

    def get_result(reject, resolve):
        def result(error, value):
            if error: reject(error)
            resolve(value)

        result.fork(reject, resolve)

    assert equals(result.fork(get_result), 6)

# Generated at 2022-06-14 04:05:00.531360
# Unit test for method map of class Task
def test_Task_map():
    """
    Execute unit tests for map method of Task
    """
    # test for map
    assert Task.of(lambda x: x + 1).map(lambda x: x(1)).fork(lambda x: False, lambda x: True) == True
    assert Task.reject(lambda x: x + 1).map(lambda x: x(1)).fork(lambda x: True, lambda x: False) == True

    # test for of
    def add(x, y):
        return x + y

    assert Task.of(1).fork(lambda x: False, lambda x: True) == True
    assert Task.of(add(1, 1)).fork(lambda x: False, lambda x: True) == True

    # test for reject
    assert Task.reject(0).fork(lambda x: True, lambda x: False) == True



# Generated at 2022-06-14 04:05:12.652841
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Task[Any] -> Function(Any) -> Task[Any]
    """

    def testFnThatReturnTask(arg):
        """
        Function(Any) -> Task[Any]

        :param arg:
        :type arg: Any
        :returns: Task[Any]
        :rtype: Task[Any]
        """
        return Task.of(arg)

    def notCalledFunction(arg):
        """
        Function(Any) -> Any

        :param arg:
        :type arg: Any
        :returns: Any
        :rtype: Any
        """
        raise Exception("Task.bind bind function that don't return task")


# Generated at 2022-06-14 04:05:16.436313
# Unit test for method bind of class Task
def test_Task_bind():
    def f(x):
        return x / 0
    def g(x):
        return Task.of(x * 2)

    # Test bind of map
    assert Task.of(2).bind(f).map(g).fork(lambda arg: arg, lambda arg: arg) == 2

    # Test reject
    assert Task.of(3).bind(f).fork(lambda arg: arg, lambda arg: arg) == 3


# Generated at 2022-06-14 04:05:28.220473
# Unit test for method bind of class Task
def test_Task_bind():
    def test_map(value):
        return Task.of(value + 1)

    task = Task.of(1)
    assert task.bind(test_map).fork(None, lambda value: value) == 2

    def test_reject(value):
        return Task.reject(value + 1)

    task = Task.of(1)
    assert task.bind(test_reject).fork(lambda value: value, None) == 2

    def test_map_with_fork(value):
        def fork(_, resolve):
            return resolve(value + 1)

        return Task(fork)

    task = Task.of(1)
    assert task.bind(test_map_with_fork).fork(None, lambda value: value) == 2


# Generated at 2022-06-14 04:05:35.275294
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Assertion test cases for function bind of class Task
    """

    def bind_case(value):
        """
        Create Task.reject(value)

        :param value: value for reject Task
        :type value: A
        :returns: rejected Task with value
        :rtype: Task[Function(reject, _) -> A]
        """
        return Task.reject(value)

    task = Task.of('foo')
    assert task.bind(bind_case).fork(lambda x: x, lambda y: y) == 'foo'



# Generated at 2022-06-14 04:05:42.295263
# Unit test for method bind of class Task
def test_Task_bind():

    def fn(x):
        return Task.of(x + 10)

    task = Task.of(100)
    assert task.fork(lambda arg: arg, lambda arg: arg) == 100

    task = task.map(fn)
    assert task.fork(lambda arg: arg, lambda arg: arg) == 200

    task = Task.of(None).bind(lambda _: Task.of(100))
    assert task.fork(lambda _: None, lambda arg: arg) == 100

    def fn(x):
        return task.bind(lambda a: Task.reject(a + x))

    task = Task.of(100).bind(fn)
    assert task.fork(lambda arg: arg, lambda _: None) == 200


# Generated at 2022-06-14 04:05:52.888462
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(value):
        return value

    task = Task.of(5).bind(lambda arg: Task.reject(arg * 2))
    assert task.fork(resolve, resolve) == 10

    task = Task.of(5).bind(lambda arg: Task.reject(arg * 2)).bind(lambda arg: Task.of(arg + 1))
    assert task.fork(resolve, resolve) == 11

    task = Task.of(5).bind(lambda arg: Task.of(arg * 2)).bind(lambda arg: Task.reject(arg + 1))
    assert task.fork(resolve, resolve) == 11


# Generated at 2022-06-14 04:05:56.616891
# Unit test for method map of class Task
def test_Task_map():
    def function(x):
        return x * x * x
    def fork(reject, resolve):
        return resolve(2)

    task = Task(fork)


# Generated at 2022-06-14 04:06:04.797043
# Unit test for method bind of class Task
def test_Task_bind():
    """
        Check correct binding on task

        :returns: nothing if test passed
        :raises: AssertionError if test doesn't passed
        """
    task1 = Task.of(1)
    task2 = Task.of(2)
    task3 = Task.of(3)
    task4 = Task.of(4)

    def bind_task(value):
        return Task.of(value).bind(
            lambda value: task1.bind(
                lambda value: task2.bind(
                    lambda value: task3.bind(
                        lambda value: task4
                    )
                )
            )
        )

    assert bind_task(5).fork(None, lambda value: None) == 4



# Generated at 2022-06-14 04:06:07.393854
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task.of(value + 1)

    assert Task.of(1).bind(fn).fork(None, None) == 2


# Generated at 2022-06-14 04:06:41.174767
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(value):
        return Task.of(value + 1)

    task = Task.of(10).bind(mapper)
    task.fork(lambda _: print('Task is rejected'),
            lambda value: print('Task is resolved and has value:', value))


test_Task_bind()


# Generated at 2022-06-14 04:06:51.037123
# Unit test for method bind of class Task
def test_Task_bind():
    # Function that return Promise of Task
    def get_task():
        def fork(_, resolve):
            resolve(Task.of('bar'))
        return Promise.of(Task(fork))

    def task_map(task):
        def fork(_, resolve):
            resolve(task.map(lambda x: '<' + x + '>'))
        return Promise.of(Task(fork))

    # Function that receive Promise of Task and return Promise of Task
    def promise_of_task(promise):
        def fork(_, resolve):
            promise.fork(
                lambda arg: reject(arg),
                lambda arg: resolve(arg)
            )
        return Promise.of(Task(fork))

    # Function that return Promise of Task with mapped value

# Generated at 2022-06-14 04:06:54.940373
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of('hello')
    task = task.map(lambda arg: arg + ' world')

    assert task.fork('', lambda arg: arg) == 'hello world'


# Generated at 2022-06-14 04:07:00.845875
# Unit test for method map of class Task
def test_Task_map():
    """Test for method Task.map."""
    called = False

    def mapper(value):
        """Dummy mapper function."""
        nonlocal called
        called = True
        return value

    Task.of(None).map(mapper)
    assert called is True



# Generated at 2022-06-14 04:07:14.717327
# Unit test for method bind of class Task
def test_Task_bind():
    def func1(x):
        if x < 0:
            return Task.reject("argument is negative")
        else:
            return Task.of(x + 1)

    def func2(x):
        if x == 0:
            return Task.reject("argument is zero")
        else:
            return Task.of(x * 2)

    def func3(x):
        if x > 10:
            return Task.reject("argument is more than 10")
        else:
            return Task.of(x)

    assert Task.of(2).bind(func1).bind(func2).bind(func3).fork(lambda e: e, lambda x: x) == 4
    assert Task.of(-2).bind(func1).bind(func2).bind(func3).fork(lambda e: e, lambda x: x)

# Generated at 2022-06-14 04:07:18.354140
# Unit test for method map of class Task
def test_Task_map():
    def mapper(value):
        return value + 1

    def fork(reject, resolve):
        resolve(1000)

    task = Task(fork)

    assert task.map(mapper).fork(lambda _: None, lambda result: result) == 1001

# Generated at 2022-06-14 04:07:26.046585
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task.
    """
    def mapper(arg):
        return Task.of(arg + 'a')

    def task_reject(arg):
        assert arg == 'b'
        print('reject b')

    def task_resolve(arg):
        assert arg == 'ba'
        print('resolve ba')

    Task.of('b').bind(mapper).fork(task_reject, task_resolve)


# Generated at 2022-06-14 04:07:32.403198
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Create Task with callable function
    Create another Task in this function and return it.
    Call method bind with this function and check
    that fork function of new Task call fork function of old Task.
    """
    inner = Task.of("test")
    outer = Task.of("test2")

    def fn(arg):
        assert arg == "test2"  # check that outer task value is "test2"
        return inner

    result = outer.bind(fn)
    result.fork(
        lambda arg: print("Error: ", arg),
        lambda arg: print("Result: ", arg)
    )


# Generated at 2022-06-14 04:07:40.089621
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Check result of two Task bind execution.
    """
    def reject(code):
        print(code)
        return None

    def resolve(value):
        print(value)
        return value

    task = Task.of(1)
    task = task.bind(lambda value: Task.of(value + 1))
    task = task.bind(lambda value: task if value < 3 else Task.reject(2))
    task.fork(reject, resolve)

# Generated at 2022-06-14 04:07:43.223598
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(value):
        return Task.of(value + 1)

    def reject_mapper(value):
        return Task.reject(value + 1)

    result = Task.of(1).bind(mapper)
    assert_result(result, 2)

    result = Task.reject(1).bind(reject_mapper)
    assert_result(result, 2, True)

