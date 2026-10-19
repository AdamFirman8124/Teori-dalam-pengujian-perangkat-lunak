

# Generated at 2022-06-14 03:57:53.596444
# Unit test for method bind of class Task
def test_Task_bind():
    def test(a):
        return Task.of(a+1)

    assert Task.of(1).bind(test).fork(lambda _: None, lambda a: a) == 2


# Generated at 2022-06-14 03:57:57.438577
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(0)
    result = task.map(lambda x: x + 1).fork(lambda arg: arg, lambda arg: arg)
    assert result == 1


# Generated at 2022-06-14 03:58:04.647171
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map of class Task
    """
    def inc(x):
        "Increment by 1"
        return x + 1

    def double(x):
        "Multiply by 2"
        return x * 2

    assert Task.of(2).map(double).fork(None, lambda x: x) == 4
    assert Task.of(2).map(inc).map(double).fork(None, lambda x: x) == 6


# Generated at 2022-06-14 03:58:10.199187
# Unit test for method map of class Task
def test_Task_map():
    def test_func(reject, resolve, fn, value, result):
        def fork(reject, resolve):
            resolve(value)

        assert Task(fork).map(fn).fork(reject, resolve) == result

    return test_func



# Generated at 2022-06-14 03:58:18.001174
# Unit test for method bind of class Task
def test_Task_bind():
    t1 = Task.of(2).bind(lambda x: Task.of(x+7)).bind(lambda x: Task.of(x/2))
    assert t1.fork(None, lambda v: v) == 4.5

    t2 = Task.of(2).bind(lambda x: Task.of('a' + str(x)))
    assert t2.fork(None, lambda v: v) == 'a2'

    t3 = Task.of(2).bind(lambda x: Task.of(x + 7)).bind(lambda x: Task.reject(x / 0))
    assert t3.fork(lambda v: v, None) == ZeroDivisionError

    t3 = Task.of(2).bind(lambda x: Task.of(x + 7)).bind(lambda x: Task.reject(x))

# Generated at 2022-06-14 03:58:25.002701
# Unit test for method map of class Task
def test_Task_map():
    # given
    def fork(reject, resolve):
        resolve(2)

    def fn(val):
        return val * 2

    task = Task(fork)

    # when
    task = task.map(fn)
    value = task.fork(None, lambda arg: arg)

    # then
    assert value == 4


# Generated at 2022-06-14 03:58:34.734932
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task
    """
    def resolve(data):
        print(data)
        return data

    def reject(data):
        print(reject)
        return data

    Task.reject(6).bind(
        lambda data: Task.of(data * 2)
    ).fork(reject, resolve)



# Generated at 2022-06-14 03:58:43.404121
# Unit test for method bind of class Task
def test_Task_bind():
    def solve_test(test_case):
        fn_var_for_test, is_error, expected_result = test_case

        if is_error:
            task = Task.reject(fn_var_for_test)
        else:
            task = Task.of(fn_var_for_test)
        result = task.bind(f)
        return result.fork(
            reject=lambda value: value == "Error" if is_error else value == expected_result,
            resolve=lambda value: value == expected_result
        )

    def f(a_or_error):
        return Task.of("Error") if isinstance(a_or_error, Exception) else Task.of(a_or_error + 1)


# Generated at 2022-06-14 03:58:49.931451
# Unit test for method bind of class Task
def test_Task_bind():
    x = 10
    y = 2
    task_x = Task.of(x)
    task_y = Task.of(y)

    def fn(value):
        return Task.of(value / 2)

    result = task_x.bind(fn)
    assert result == Task.of(x / 2)
    assert result.fork(lambda error: error, lambda value: value) == x / 2

    def fn(value):
        return Task.of(value + 2)

    assert task_x.bind(fn) == Task.of(x + 2)

    def fn(value):
        return Task.of(value)

    assert task_x.bind(fn) == Task.of(x)

# Generated at 2022-06-14 03:58:53.626177
# Unit test for method map of class Task
def test_Task_map():
    value = 'string'
    result = Task.of(value).map(lambda arg: arg)
    assert result.fork(lambda arg: arg, lambda arg: arg) == value


# Generated at 2022-06-14 03:59:00.887318
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task
    """
    task = Task.of(2).bind(lambda x: Task.of(x + 2))
    assert(task.fork(lambda x: -1, lambda x: x) == 4)


# Generated at 2022-06-14 03:59:08.905711
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method map of class Task
    """
    for value in [1, 2, 3, 4, 5]:
        task = Task.of(value)
        task_map = task.map(lambda arg: arg + 1)
        print(task_map.fork(lambda arg: "No", lambda arg: arg))

    task = Task.of(None)
    task_map = task.map(lambda arg: arg + 1)
    print(task_map.fork(lambda arg: "No", lambda arg: arg))

#Unit test for method bind of class Task

# Generated at 2022-06-14 03:59:14.580939
# Unit test for method bind of class Task
def test_Task_bind():
    def get_value():
        def fork(reject, resolve):
            resolve(42)

        return Task(fork)

    def after_get_value(value):
        def fork(reject, resolve):
            resolve(value + 1)

        return Task(fork)

    result = get_value().bind(after_get_value).fork(None, None)
    assert result == 43

# Generated at 2022-06-14 03:59:24.326746
# Unit test for method bind of class Task
def test_Task_bind():
    def fn_reject(response):
        return Task.reject(response * 3)

    def fn_resolve(response):
        return Task.of(response * 2)

    task = Task.of(1)
    task = task.bind(fn_resolve)
    task = task.bind(fn_resolve)
    task = task.bind(fn_resolve)
    task = task.bind(fn_reject)
    task = task.bind(fn_resolve)

# Generated at 2022-06-14 03:59:32.970941
# Unit test for method bind of class Task
def test_Task_bind():
    def test_bind_fn(value):
        def fake_task_fork(reject, resolve):
            resolve(value * 2)

        return Task(fake_task_fork)

    fake_task_fork_result = None
    fake_task_fork_arg = None
    def fake_task_fork(reject, resolve):
        nonlocal fake_task_fork_arg
        nonlocal fake_task_fork_result

        fake_task_fork_arg = (reject, resolve)
        return fake_task_fork_result

    fake_fork_arg = None
    def fake_fork(reject, resolve):
        nonlocal fake_fork_arg
        fake_fork_arg = (reject, resolve)

    fake_task = Task(fake_task_fork)

# Generated at 2022-06-14 03:59:40.467431
# Unit test for method bind of class Task
def test_Task_bind():
    res = Task(lambda _, resolve: resolve(10)).bind(lambda value: Task.of(value * 2))
    assert res.fork(None, lambda value: value) == 20

    res = Task(lambda _, resolve: resolve(10)).bind(
        lambda value: Task.of(value * 2)
    ).bind(
        lambda value: Task.of(value + 1)
    )

    assert res.fork(None, lambda value: value) == 21


# Generated at 2022-06-14 03:59:51.048744
# Unit test for method bind of class Task
def test_Task_bind():
    def fork_reject_reject(reject, _):
        reject(0)

    def fork_reject_resolve(reject, resolve):
        reject(0)

    def fork_resolve_reject(reject, resolve):
        resolve(0)

    def fork_resolve_resolve(reject, resolve):
        resolve(0)

    assert (
        Task(fork_resolve_reject).bind(
            lambda arg: Task(fork_reject_reject)
        ).fork(identity, identity) ==
        0
    )

    assert (
        Task(fork_resolve_reject).bind(
            lambda arg: Task(fork_reject_resolve)
        ).fork(identity, identity) ==
        0
    )


# Generated at 2022-06-14 03:59:55.825508
# Unit test for method map of class Task
def test_Task_map():
    """
    Test for method Task.map()
    """
    task = Task.of('value')
    task = task.map(lambda arg: arg + '_')
    assert task.fork('reject', 'resolve') == 'value_'

# Generated at 2022-06-14 03:59:59.603719
# Unit test for method map of class Task
def test_Task_map():
    task = Task(lambda reject, resolve: resolve(1))
    mapped_task = task.map(lambda value: value + 1)
    assert mapped_task.fork(lambda _: None, lambda val: val) == 2


# Generated at 2022-06-14 04:00:03.002225
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for Task.bind method.
    """
    task = Task.of("test")

    def mapper(value):
        return Task.of("mapped " + value)

    assert task.bind(mapper).fork(lambda _: False, lambda value: value == "mapped test")


# Generated at 2022-06-14 04:00:11.323404
# Unit test for method bind of class Task
def test_Task_bind():
    def inc_task(val):
        return Task.of(val + 1)

    task = Task.of(1).bind(inc_task)

    assert task.fork(
        lambda _: None,
        lambda arg: arg
    ) == 2



# Generated at 2022-06-14 04:00:16.262518
# Unit test for method map of class Task
def test_Task_map():
    def add_2(value):
        return value + 2

    def mul_2(value):
        return value * 2

    case = Task.of(4).map(add_2).map(mul_2)

    assert case.fork(lambda _: None, lambda resolve: resolve) == 10


# Generated at 2022-06-14 04:00:19.763318
# Unit test for method bind of class Task
def test_Task_bind():
    t1 = Task.of(42)
    t2 = Task.of(84)


# Generated at 2022-06-14 04:00:25.664452
# Unit test for method map of class Task
def test_Task_map():
    def assert_equal(expect, result):
        assert expect == result, "expected {}, got {}".format(expect, result)

    def fork_mock(reject, resolve):
        return reject(0)

    def fn(value):
        return value + 1

    def map_mock(reject, resolve):
        return resolve(fn(0))

    # Task.of(0).map(lambda x: x + 1).fork(lambda e: e, lambda r: r)   # -> 1
    task = Task(fork_mock).map(fn)
    assert task.fork(lambda e: e, lambda r: r) == map_mock(lambda e: e, lambda r: r)

    # Task.reject(0).map(lambda x: x + 1).fork(lambda e: e, lambda r: r

# Generated at 2022-06-14 04:00:30.732850
# Unit test for method bind of class Task
def test_Task_bind():
    def sample(value):
        return Task.of(value ** 2)

    def test_resolve(resolve, reject):
        Task.of(5).bind(sample).fork(reject, resolve)

    assert test_resolve(lambda value: value == 25)


# Generated at 2022-06-14 04:00:40.997536
# Unit test for method bind of class Task
def test_Task_bind():
    def inc(value):
        return value + 1

    def times(value):
        return Task.reject(value * 2)

    assert Task.of(1).bind(inc).fork(lambda arg: arg, lambda arg: arg) == 2
    assert Task.reject(1).bind(inc).fork(lambda arg: arg, lambda arg: arg) == 1
    assert Task.of(1).bind(lambda arg: Task.of(arg)).fork(lambda arg: arg, lambda arg: arg) == 1
    assert Task.reject(1).bind(lambda arg: Task.of(arg)).fork(lambda arg: arg, lambda arg: arg) == 1
    assert Task.reject(1).bind(times).fork(lambda arg: arg, lambda arg: arg) == 2


# Generated at 2022-06-14 04:00:44.734132
# Unit test for method bind of class Task
def test_Task_bind():
    def error_fn(value):
        return Task.reject(value)
    result = Task.of(1).bind(error_fn)

    assert(result.fork(
        lambda _: True,
        lambda _: False
    ))


# Generated at 2022-06-14 04:00:49.621725
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(1)
    task = task.bind(lambda arg: Task.of(arg + 2))
    task = task.bind(lambda arg: Task.of(arg * 2))
    assert task.fork(
        lambda arg: 'error',
        lambda arg: arg
    ) == 6


# Generated at 2022-06-14 04:00:53.747007
# Unit test for method map of class Task
def test_Task_map():

    assert Task.of(3).map(lambda x: x * x).fork(None, lambda x: x) == 9

# Generated at 2022-06-14 04:01:01.458870
# Unit test for method map of class Task
def test_Task_map():
    def add_one(x):
        return x + 1

    def add_two(x):
        return x + 2

    assert Task.of(1).map(add_one).fork(None, lambda x: x == 2)
    assert Task.of(1).map(add_one).map(add_two).fork(None, lambda x: x == 3)
    assert Task.of(1).map(add_two).map(add_one).fork(None, lambda x: x == 3)

    def raise_error(x):
        raise ValueError()

    assert Task.of(1).map(raise_error).fork(lambda _: True, None)


# Generated at 2022-06-14 04:01:14.902670
# Unit test for method bind of class Task
def test_Task_bind():
    add2 = Task.of(2).bind(lambda a: Task.of(a + 2))
    multiply_by_3 = Task.of(3).bind(lambda a: Task.of(a * 3))
    assert add2.fork(lambda _: None, lambda n: n) == 4
    assert multiply_by_3.fork(lambda _: None, lambda n: n) == 9

# Generated at 2022-06-14 04:01:18.399481
# Unit test for method bind of class Task
def test_Task_bind():
    def bind_func(arg):
        return Task.of(arg + 2)

    task = Task.of(1)

# Generated at 2022-06-14 04:01:23.771847
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(2).bind(lambda value: Task.of(value + 2))
    assert task.fork(None, lambda value: value) == 4
    task = Task.of(2).bind(lambda value: Task.reject(value + 2))
    assert task.fork(
        lambda value: value,
        None
    ) == 4


# Generated at 2022-06-14 04:01:27.952450
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        return resolve(1)

    def fn(a):
        def fork(reject, resolve):
            return resolve(a + 1)

        return Task(fork)

    assert Task(fork).bind(fn).fork(None, lambda a: a) == 2


# Generated at 2022-06-14 04:01:34.675176
# Unit test for method bind of class Task
def test_Task_bind():
    def function_for_task(arg):
        return Task.of(arg + 1)

    def run():
        initial_value = 0
        task = Task.of(initial_value)
        mapped_task = task.map(lambda __: initial_value)
        binded_task = task.bind(function_for_task)

        assert initial_value + 1 == binded_task.fork(_, lambda x: x)
        assert initial_value == mapped_task.fork(_, lambda x: x)
        assert initial_value == initial_value

    run()


# Generated at 2022-06-14 04:01:38.483797
# Unit test for method bind of class Task
def test_Task_bind():
    task_of_2 = Task.of(2)
    task_of_6 = task_of_2.bind(
        lambda x: Task.of(x * 3)
    )

    assert isinstance(task_of_6, Task)
    assert task_of_6.fork(id, id) == 6


# Generated at 2022-06-14 04:01:42.455520
# Unit test for method map of class Task
def test_Task_map():
    def assert_result(value, expected):
        def fn(value):
            return value * 2

        def fork(reject, resolve):
            resolve(value)

        task = Task(fork)
        result = task.map(fn).fork(
            lambda arg: None,
            lambda arg: arg
        )
        assert result == expected

    assert_result(0, 0)
    assert_result(1, 2)
    assert_result(2, 4)



# Generated at 2022-06-14 04:01:51.630921
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test functionality of Task.bind classmethod.
    """
    v1 = {'a': 'a'}
    v2 = {'a': 'b'}
    v3 = {'a': 'c'}

    def mapper(value):
        """
        Example of mapper function.
        """
        return Task(lambda _, resolve: resolve(value))

    t1 = Task.of(v1)
    t2 = t1.bind(mapper)
    assert t2.fork(lambda arg: arg, lambda arg: arg) == v1

    t3 = t2.map(lambda arg: {**arg, 'a': 'b'})
    t4 = t3.bind(mapper)
    assert t4.fork(lambda arg: arg, lambda arg: arg) == v2

    t5

# Generated at 2022-06-14 04:01:56.066979
# Unit test for method map of class Task
def test_Task_map():
    # Call Task.map with function
    # Task[Function(_, resolve) -> A]
    task = Task.of(1).map(lambda x: x + 1)

    # Task[Function(resolve, reject) -> A | B]
    assert type(task) is Task

    # 2
    assert task.fork(
        lambda reject: reject,
        lambda resolve: resolve
    ) == 2


# Generated at 2022-06-14 04:02:02.046151
# Unit test for method map of class Task
def test_Task_map():
    def test(a):
        return Task.of(a) \
            .map(lambda x: x * 2) \
            .map(lambda x: x * 2) \
            .fork(
                lambda x: False,
                lambda x: x == 4 * 2 * 2
            )

    assert test(1)
    assert not test(2)


# Generated at 2022-06-14 04:02:24.723963
# Unit test for method bind of class Task
def test_Task_bind():
    def fn(value):
        return Task.of(value * 2)

    def reject(value):
        raise ValueError('This is test reject')

    def resolve(value):
        assert value == 4

    task = Task.of(2).bind(fn)
    task.fork(reject, resolve)

# Generated at 2022-06-14 04:02:30.058632
# Unit test for method map of class Task

# Generated at 2022-06-14 04:02:37.479949
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Make sure that bind method of Task works as expected.
    """
    # No value set
    no_value = Task(lambda _, resolve: resolve(None))
    assert no_value.bind(lambda _: Task.of('salam')).fork(lambda _: None, lambda A: A) == 'salam'

    # Value set
    value = Task(lambda _, resolve: resolve('salam'))
    assert value.bind(lambda _: Task.of('hello')).fork(lambda _: None, lambda A: A) == 'hello'


# Generated at 2022-06-14 04:02:45.234332
# Unit test for method map of class Task
def test_Task_map():
    """

    """
    # Work with Task.reject
    assert Task.reject(1).map(lambda x: x * 2) == Task.reject(1)

    # Work with Task.of
    #
    # Test mapping Task.of(1) => Task.of(2)
    assert Task.of(1).map(lambda x: x * 2) == Task.of(2)
    #
    # Test mapping Task.of(1) => Task.reject(2)
    assert Task.of(1).map(lambda x: Task.reject(2)) == Task.reject(2)


# Generated at 2022-06-14 04:02:50.499631
# Unit test for method bind of class Task
def test_Task_bind():
    result = Task.of(5) \
        .bind(lambda x: Task.reject(x)) \
        .bind(lambda x: Task.of(x)) \
        .fork(
            lambda x: print('error', x),
            lambda x: x
        )
    assert result == 5

# TODO: extend Task class with all combinators to Task, Result and Task

# Generated at 2022-06-14 04:02:56.580466
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(value):
        return Task.of(value + 2)

    def add1(value):
        return Task.of(value + 1)

    assert Task.of(1).bind(mapper).fork(lambda e: e, lambda s: s) == 3
    assert Task.of(1).bind(mapper).bind(add1).fork(lambda e: e, lambda s: s) == 4



# Generated at 2022-06-14 04:03:05.307305
# Unit test for method bind of class Task
def test_Task_bind():
    def foo(arg):
        return Task.of(arg + 1)

    def foo_chain(arg):
        return Task(
            lambda _, resolve: resolve(arg + 1)
        )

    task = Task.of(1)
    task_bind_result = task.bind(foo)
    task_chain_result = task.map(lambda arg: arg + 1)

    assert task_bind_result.fork(lambda err: err, lambda arg: arg) == 2
    assert task_chain_result.fork(lambda err: err, lambda arg: arg) == 2


# Generated at 2022-06-14 04:03:09.178869
# Unit test for method map of class Task
def test_Task_map():
    def plus_one(val):
        return val + 1

    assert Task.of(1).map(plus_one).fork(
        lambda arg: arg,
        lambda arg: arg
    ) == 2

    assert Task.of(1).map(plus_one).map(plus_one).fork(
        lambda arg: arg,
        lambda arg: arg
    ) == 3


# Generated at 2022-06-14 04:03:15.556946
# Unit test for method bind of class Task
def test_Task_bind():
    mock_fork = mocker.Mock()
    mock_reject = mocker.Mock()
    mock_resolve = mocker.Mock()
    mock_reject.return_value = 1
    mock_resolve.return_value = 2

    task = Task(mock_fork)
    task.bind(lambda _: mock_reject).fork(reject=mock_reject, resolve=mock_resolve)
    mock_fork.assert_called_once_with(
        reject=mock_reject,
        resolve=mock_reject
    )

    task = Task(mock_fork)
    task.bind(lambda _: mock_resolve).fork(reject=mock_reject, resolve=mock_resolve)

# Generated at 2022-06-14 04:03:20.243825
# Unit test for method map of class Task
def test_Task_map():
    def fn(value):
        return value ** 2

    assert Task(lambda rejects, resolve: resolve(3)) \
                   .map(fn) \
                   .fork(lambda x: None, lambda x: x) == 9

    assert Task(lambda rejects, resolve: rejects(False)) \
                   .map(fn) \
                   .fork(lambda x: None, lambda x: False) == None



# Generated at 2022-06-14 04:04:09.542998
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test method bind of class Task.
    """
    def fn(value):
        return Task.of(value+1)

    def fn_neg(value):
        return Task.reject(value+1)

    def test_callable(fn, test_value):
        """
        Test Task.fork with different success and fail cases.

        :param fn: function to test
        :type fn: Function(value) -> Task[reject, mapped_value]
        """
        # Success case
        assert fn(test_value).fork(
            lambda _: False,
            lambda value: value == test_value + 1
        )

        # Fail case
        assert fn_neg(test_value).fork(
            lambda value: value == test_value + 1,
            lambda _: False
        )

    test_callable

# Generated at 2022-06-14 04:04:14.335498
# Unit test for method map of class Task
def test_Task_map():
    # create task
    task = Task(lambda _, resolve: resolve(5))

    # map task
    mapped = task.map(lambda x: x * x)

    # assert
    assert mapped.fork(lambda _: None, lambda x: x) == 25



# Generated at 2022-06-14 04:04:23.365175
# Unit test for method bind of class Task
def test_Task_bind():
    def for_task_of():
        def mapper(value):
            assert value == 'foo'
            return Task.of('baz')

        task = Task.of('foo').bind(mapper)

# Generated at 2022-06-14 04:04:37.140592
# Unit test for method bind of class Task
def test_Task_bind():
    called = [0, 0, 0, 0]

    def mock_reject(value):
        pass

    def mock_resolve(value):
        pass

    def a_fork_fn(_, resolve):
        called[0] += 1
        resolve('a')

    def b_fork_fn(_, resolve):
        called[1] += 1
        resolve('b')

    def c_fork_fn(_, resolve):
        called[2] += 1
        resolve('c')

    def a_fn(x):
        assert x == 'a'
        called[3] += 1

    a = Task(a_fork_fn)
    b = Task(b_fork_fn)
    c = Task(c_fork_fn)

# Generated at 2022-06-14 04:04:40.319083
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(1).bind(lambda v: Task.of(v * 2)).fork(None, lambda v: v) == 2


# Generated at 2022-06-14 04:04:48.812751
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(value):
        return Task.of(value + 1)

    def reject(value):
        return Task.reject(value + 1)

    assert 1 == Task.of(0).bind(resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, lambda value: value)
    assert 5 == Task.of(3).bind(reject).fork(reject, resolve).fork(reject, resolve).fork(lambda value: value, reject).fork(lambda value: value, reject)


# Generated at 2022-06-14 04:04:57.068683
# Unit test for method map of class Task
def test_Task_map():
    """
    Resolved Task should return new Task with mapped resolve value.

    :returns: None
    :rtype: None
    """
    def fork(reject, resolve):
        return resolve(5)

    task = Task(fork)
    expected_value = 10
    actual_value = task.map(lambda arg: arg * 2).fork(None, lambda arg: arg)

    assert actual_value == expected_value, str(
        actual_value
    ) + " != " + str(expected_value)


# Generated at 2022-06-14 04:05:08.607775
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for Task.bind(Function) method.

    This test use assert method from pytest, for checking that method bind return expected result of Task.
    """
    first_task = Task.of('test')
    second_task = Task.of('second task')

    def bind_fn(arg):
        if arg == 'test':
            return second_task
        else:
            return Task.reject('reject')

    task_with_mapper_fn = first_task.bind(bind_fn)
    def test_successful_resolution(reject, resolve):
        resolve('success')

    def test_successful_rejection(reject, resolve):
        reject('reject')

    assert task_with_mapper_fn.fork(test_successful_rejection, test_successful_resolution) == 'success'

#

# Generated at 2022-06-14 04:05:12.765415
# Unit test for method map of class Task
def test_Task_map():
    def function(arg):
        return "result " + arg

    task = Task(function)
    final = task.map(function).fork(
        lambda value: "fail",
        lambda value: value
    )
    assert final == "result result value"


# Generated at 2022-06-14 04:05:18.192422
# Unit test for method bind of class Task
def test_Task_bind():
    def some_function(value):
        """Map function for unit test of Task.bind method."""
        return Task.of(int(value))

    value = 0

    # Check if Task.bind return Task with mapped value
    def test_return_value_M():
        nonlocal value
        value += 1

        def some_function_mock(val):
            """Mock for function"""
            assert val == 123
            return Task.of(value)

        task = Task(lambda _, resolve: resolve(123))
        result = task.bind(some_function_mock)
        assert isinstance(result, Task)
        assert result.fork(lambda _: False, lambda val: val == value) is True

    # Check if Task.bind return resolved Task if Task returned by mapper function
    # is resolved

# Generated at 2022-06-14 04:06:59.147864
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(value):
        return Task.of("Task(" + value + ")")

    def reject(value):
        return Task.reject("Task(" + value + ")")

    assert Task.of("hello").bind(resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork(reject, resolve).fork

# Generated at 2022-06-14 04:07:06.143018
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test method bind of class Task.
    """

    def ok(a):
        return Task.of(a)

    def fail(a):
        return Task.reject(a)

    def called(a):
        return Task.of(a).map(lambda a: a + 2)

    assert Task.of(1).bind(ok).fork(lambda a: a, lambda a: a) == 3
    assert Task.of(1).bind(fail).fork(lambda a: a, lambda a: a) == 2
    assert Task.reject(1).bind(ok).fork(lambda a: a, lambda a: a) == 1
    assert Task.reject(1).bind(fail).fork(lambda a: a, lambda a: a) == 1

# Generated at 2022-06-14 04:07:15.534047
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(1) \
        .bind(lambda value: Task.of(value + 1)) \
        .fork(lambda failure: failure, lambda success: success) == 2
    assert Task.of(1) \
        .bind(lambda value: Task.reject(value + 1)) \
        .fork(lambda failure: failure, lambda success: success) == 2
    assert Task.of(1) \
        .bind(lambda value: Task.reject(value + 1)) \
        .bind(lambda failure: Task.of(failure)) \
        .fork(lambda failure: failure, lambda success: success) == 2
    assert Task.reject(1) \
        .bind(lambda value: Task.of(value + 1)) \
        .fork(lambda failure: failure, lambda success: success) == 1

# Unit test

# Generated at 2022-06-14 04:07:22.134858
# Unit test for method bind of class Task
def test_Task_bind():
    def check_reject_attribute(reject, _):
        reject(24)

    def check_resolve_attribute(_, resolve):
        resolve(42)

    assert Task(check_reject_attribute).bind(lambda _: None).fork(lambda arg: arg, lambda _: None) == 24
    assert Task(check_resolve_attribute).bind(lambda arg: arg).fork(lambda _: None, lambda arg: arg) == 42



# Generated at 2022-06-14 04:07:26.727946
# Unit test for method bind of class Task
def test_Task_bind():
    f = lambda x: Task.reject(x)
    g = lambda x: Task.reject(x + 1)
    r = f(1).bind(g)
    assert r.fork(lambda x: x == 2, lambda x: False)


# Generated at 2022-06-14 04:07:33.645048
# Unit test for method map of class Task
def test_Task_map():
    # Success test

    expected = Task(lambda _, resolve: resolve(None))
    actual = Task.of(None)
    assert actual.map(lambda _: _).fork == expected.fork

    expected = Task(lambda _, resolve: resolve(1))
    actual = Task.of(1)
    assert actual.map(lambda _: _).fork == expected.fork

    expected = Task(lambda _, resolve: resolve("one"))
    actual = Task.of("one")
    assert actual.map(lambda _: _).fork == expected.fork

    expected = Task(lambda _, resolve: resolve("one"))
    actual = Task.of("one")
    assert actual.map(lambda _: _).map(lambda _: _).fork == expected.fork

    expected = Task(lambda _, resolve: resolve("one"))
    actual = Task

# Generated at 2022-06-14 04:07:44.241450
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test task with resolved value
    """
    first_task_value = 20
    second_task_value = 1000
    third_task_value = first_task_value + second_task_value

    def fork(reject, resolve):
        resolve(first_task_value)

    def make_another_task(task_value):
        def another_fork(reject, resolve):
            resolve(task_value)
        return Task(another_fork)

    def check_value(task_value):
        assert task_value == third_task_value

    first_task = Task(fork)
    first_task.bind(make_another_task).fork(lambda: 0, check_value)


# Generated at 2022-06-14 04:07:49.823490
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test Task bind method.
    """
    y = Task.of(1).bind(lambda x: Task.of(x + 1))
    assert y.fork(None, lambda x: x) == 2

    y = Task.reject(1).bind(lambda x: Task.of(x + 1))
    assert y.fork(_id, None) == 1
