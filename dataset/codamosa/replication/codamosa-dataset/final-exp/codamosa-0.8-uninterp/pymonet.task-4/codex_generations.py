

# Generated at 2022-06-14 03:57:52.542415
# Unit test for method map of class Task
def test_Task_map():
    def concat(a, b):
        return a + b
    task = Task.of(1).map(lambda x: x * 2).map(lambda x: concat("_", str(x)))
    assert task.fork("reject", "resolve") == 'resolve_2'


# Generated at 2022-06-14 03:57:57.439556
# Unit test for method map of class Task
def test_Task_map():
    task_mapped = Task.of(10).map(lambda x: x + 10)
    task_mapped.fork(
        lambda arg: print("reject with {}".format(arg)),
        lambda arg: print("resolve with {}".format(arg))
    )


# Generated at 2022-06-14 03:58:07.849586
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test of bind method of class Task

    Expect to return Task with map attribute
    """
    def f1(arg):
        """
        Simple function which we ca use as mapper

        :param arg: argument which will be return
        :type arg: A
        :return: arg
        :rtype: A
        """
        return arg

    def f2(arg):
        """
        Simple function which we ca use as mapper

        :param arg: argument which will be return
        :type arg: A
        :return: Task with argument
        :rtype: Task[A]
        """
        return Task.of(arg)

    def run_test(task, result, fn):
        actual = task.bind(fn)
        # use assert_equal because assert_true not work with Task instances

# Generated at 2022-06-14 03:58:11.407112
# Unit test for method map of class Task
def test_Task_map():
    def result(value):
        return value + ' world'

    task = Task(lambda _, resolve: resolve('hello')).map(result)
    assert task.fork(lambda _: 'bad', lambda value: value) == 'hello world'



# Generated at 2022-06-14 03:58:18.695033
# Unit test for method map of class Task
def test_Task_map():
    def fn(value):
        return value * 2
    task = Task.of(1)
    task = task.map(fn)
    assert task.fork(lambda arg: arg, lambda arg: arg) == 2


# Generated at 2022-06-14 03:58:25.378942
# Unit test for method bind of class Task
def test_Task_bind():
    def map(value): return Task.of(value + 1)


# Generated at 2022-06-14 03:58:32.059059
# Unit test for method map of class Task
def test_Task_map():
    def inc(x):
        return x + 1
    t = Task.of(1).map(inc)
    assert t.fork(lambda value: value, lambda value: value) == 2



# Generated at 2022-06-14 03:58:38.961457
# Unit test for method map of class Task
def test_Task_map():
    """
    Testing map method of Task.
    To test it we used method Task.of which returns resolved Task with stored value.
    """
    assert Task.of("INPUT") \
        .map(lambda x: x + " MAP") \
        .fork(lambda a: None, lambda a: a) == "INPUT MAP"


# Generated at 2022-06-14 03:58:41.706158
# Unit test for method map of class Task
def test_Task_map():
    result = Task.of(1)
    assert result.map(lambda x: x * 2) == Task.of(2)


# Generated at 2022-06-14 03:58:44.789917
# Unit test for method map of class Task
def test_Task_map():
    def fn_Task_map(arg):
        return Task.of(arg + 1)

    assert Task.of(1).map(fn_Task_map).fork(lambda arg: arg, lambda arg: arg) == 2


# Generated at 2022-06-14 03:58:50.899983
# Unit test for method map of class Task
def test_Task_map():
    task = Task(lambda reject, resolve: resolve(1))

    assert task.map(lambda arg: arg + 1).fork(lambda arg: arg, lambda arg: arg) == 2


# Generated at 2022-06-14 03:58:57.224790
# Unit test for method map of class Task
def test_Task_map():
    """
    >>> test_Task_map()
    [1, 2]
    """
    print(list(Task.of([1, 2]).map(lambda x: list(map(lambda x: x + 1, x))).fork()))
    # print(list(Task.reject([1, 2]).map(lambda x: list(map(lambda x: x + 1, x))).fork()))


# Generated at 2022-06-14 03:59:01.282220
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task
    """
    sum = lambda x: lambda y: x + y
    assert Task(sum(1)(1)).bind(sum(1)).fork(
        lambda arg: arg,
        lambda arg: arg
    ) == 3

# Generated at 2022-06-14 03:59:09.180650
# Unit test for method bind of class Task
def test_Task_bind():
    def test_fn(value):
        return (Task.reject(value) if value == 1 else Task.of(value))

    task = Task.of(1)
    assert task.bind(test_fn).fork(lambda x: x, lambda x: 0) == 1

    task = Task.of(2)
    assert task.bind(test_fn).fork(lambda x: 0, lambda x: x) == 2

    task = Task.reject(3)
    assert task.bind(test_fn).fork(lambda x: x, lambda x: 0) == 3



# Generated at 2022-06-14 03:59:16.730278
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        resolve(10)

    task = Task(fork).map(lambda x: x + 10)
    assert task.fork(None, lambda x: x) == 20

    task = Task(fork).map(lambda x: [x + 10])
    assert task.fork(None, lambda x: x) == [20]

    task = Task(fork).map(lambda x: {'test': x + 10})
    assert task.fork(None, lambda x: x) == {'test': 20}


# Generated at 2022-06-14 03:59:27.588988
# Unit test for method bind of class Task
def test_Task_bind():
    def double(number):
        return number * 2

    def square(number):
        return number ** 2

    def send_number_to_network(number):
        return Task(lambda reject, resolve: resolve(number))

    # test for bind with double function
    task_with_double = Task.of(5).bind(double)
    assert_equal(task_with_double.fork(lambda _: "rejected", lambda value: value), 10)

    # test for bind with square function
    task_with_square = Task.of(5).bind(square)
    assert_equal(task_with_square.fork(lambda _: "rejected", lambda value: value), 25)

    # test for bind with send_number_to_network function

# Generated at 2022-06-14 03:59:33.320798
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test check work of bind method of Task class.
    """
    def double(number):
        return Task.of(number * 2)

    def reject(message):
        return Task.reject(message)

    def resolve(arg):
        return 'resolved'

    def reject_work(arg):
        return 'rejected'

    assert Task.of(2).bind(double).fork(reject_work, resolve) == 'resolved'
    assert Task.of(2).bind(reject).fork(reject_work, resolve) == 'rejected'

    print('SUCCESS')


# Generated at 2022-06-14 03:59:39.581891
# Unit test for method bind of class Task
def test_Task_bind():
    # Task.of(1).bind(lambda _: Task.of(2)).fork(print, print)
    # Task.of(1).bind(lambda _: Task.reject("error")).fork(print, print)
    Task.reject("error").bind(lambda _: Task.of(1)).fork(print, print)
    pass


# Generated at 2022-06-14 03:59:46.778024
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    task = task.map(lambda value: 1 if value == 1 else 0)
    assert task.fork(lambda _: 'rejected', lambda arg: arg) == 1

    def check_rejected():
        task = Task.reject(1)
        task = task.map(lambda value: 1)
        assert task.fork(lambda arg: arg, lambda _: 'resolved') == 1

    check_rejected()
    return True
print(test_Task_map())


# Generated at 2022-06-14 03:59:55.444027
# Unit test for method bind of class Task
def test_Task_bind():
    """
    When bind is called on Task[reject, resolve] it should return new Task[reject,
    mapped_value].

    Calling fork on this Task should call fork on original Task and then call fork on
    result of stored mapper function.
    """
    def test_reject(reject, resolve):
        reject('rejected')

    def test_resolve(reject, resolve):
        resolve('resolved')

    def mapper(arg):
        return Task(test_resolve)

    original = Task(test_reject)
    t = original.bind(mapper)
    assert t.fork(lambda arg: arg, lambda arg: arg) == 'resolved'


# Generated at 2022-06-14 04:00:07.425351
# Unit test for method bind of class Task
def test_Task_bind():
    a = Task.reject(1).bind(lambda x: Task.of(1)).fork(
        reject=lambda x: print('should not be reject: {0}'.format(x)),
        resolve=lambda x: print('should be 1: {0}'.format(x))
    )
    print('-'*50)
    b = Task.of(1).bind(lambda x: Task.reject(x)).fork(
        reject=lambda x: print('should be 1: {0}'.format(x)),
        resolve=lambda x: print('should not be resolve: {0}'.format(x))
    )
    print('-'*50)

# Generated at 2022-06-14 04:00:15.716070
# Unit test for method bind of class Task
def test_Task_bind():
    value = 'value'

    def reject(arg):
        return arg

    def resolve(arg):
        return arg

    def bind(arg):
        return arg + arg

    def bind_with_error(arg):
        raise ValueError()

    Task.of(value).bind(bind).fork(reject, resolve) == value + value
    Task.of(value).bind(bind_with_error).fork(reject, resolve) == value

    Task.reject(value).bind(bind).fork(resolve, reject) == value
    Task.reject(value).bind(bind_with_error).fork(resolve, reject) == value


# Generated at 2022-06-14 04:00:19.102996
# Unit test for method bind of class Task
def test_Task_bind():
    """Assert that Task.bind is FunctionCompose composition
    """

    def f(arg):
        return Task.of(arg + 1)

    def g(arg):
        return Task.of(arg ** 2)

    def f_g(arg):
        return Task.of(g(f(arg)))

    assert Task.of(1).bind(f).bind(g) == f_g(1)


# Generated at 2022-06-14 04:00:25.487025
# Unit test for method map of class Task
def test_Task_map():

    # Helper function for perform test of method map
    def to_be_equal(resolve, value, expected):
        resolved = 0

        def checker(arg):
            nonlocal resolved

            if resolved == 1:
                return

            assert arg == expected
            resolved += 1

        def reject(_):
            assert False

        task = Task.of(value)
        resolve(task.map(checker))
        task.fork(reject, checker)

    return Task((lambda resolve, _: resolve(to_be_equal)))



# Generated at 2022-06-14 04:00:38.098448
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Create Task with fork function and bind with another fork function.
    During bind method call store result of this call in left_fork and map_fork.
    Check that left_fork and map_fork not called.
    Check that fork_resolve_called and fork_resolve_value must be equal True and values.
    Check that fork_reject_called and fork_reject_value must be equal False and None.
    """
    values = ['some value']
    fork_resolve_called = None
    fork_resolve_value = None
    fork_reject_called = None
    fork_reject_value = None
    left_fork = None
    map_fork = None

    def resolve(arg):
        nonlocal fork_resolve_called, fork_resolve_value
        fork_resolve_called = True
       

# Generated at 2022-06-14 04:00:47.587366
# Unit test for method bind of class Task
def test_Task_bind():
    def addOne(n): return Task.of(n + 1)

    def rejectFn(n):
        if n == 3:
            return Task.reject('foo')
        else:
            return Task.of(n + 1)

    result = Task.of(3) \
        .map(addOne) \
        .bind(addOne) \
        .bind(addOne) \
        .bind(addOne) \
        .bind(rejectFn) \
        .map(addOne) \
        .bind(addOne) \
        .fork(lambda a: a, lambda a: a)

    assert result == 'foo'

# Generated at 2022-06-14 04:00:52.700825
# Unit test for method bind of class Task
def test_Task_bind():
    def add(a):
        return Task.of(a + 1)

    a = Task.of(1).bind(add)
    assert a.fork(None, lambda a: a) == 2

    b = Task.of(10).bind(lambda x: Task.reject(x + 1))
    assert b.fork(lambda a: a, None) == 11


# Generated at 2022-06-14 04:00:59.570703
# Unit test for method bind of class Task
def test_Task_bind():
    def _task_test(test_data):
        def _test_data_test(test_data):
            def _test_data_test_test(test_data):
                return Task.of(test_data + 1)

            return Task.of(test_data).bind(_test_data_test_test)

        return Task.of(test_data).bind(_test_data_test)

    assert Task.bind(_task_test(10)) == 11



# Generated at 2022-06-14 04:01:04.119197
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        return resolve(1)

    assert Task(fork).bind(lambda x: Task.of(x + 1)).fork(
        lambda arg: False,
        lambda arg: True if arg == 2 else False
    )


# Generated at 2022-06-14 04:01:08.571724
# Unit test for method bind of class Task
def test_Task_bind():
    def test_function(fun_to_call):
        return fun_to_call(arg)

    arg = 10
    task = Task.of(10)
    mapped = task.bind(test_function)
    assert arg == mapped.fork(lambda x: x, lambda x: x)


# Generated at 2022-06-14 04:01:26.567713
# Unit test for method map of class Task
def test_Task_map():
    """
    Create Task with stored function, call fork with resolve and reject function and
    check if mapper function is called with value during resolving.
    """
    # input value
    VALUE = 'value'
    # mapper function
    FN = lambda _: 'mapped'

    def fork(reject, resolve):
        # set value and call resolve function
        resolve(VALUE)

    # create task with fork function
    task = Task(fork)

    # map task with mapper function
    result = task.map(FN)

    # call fork function with resolve and reject functions
    result.fork(lambda _: None, lambda value: value)



# Generated at 2022-06-14 04:01:31.116185
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(1).map(lambda x: x + 1).fork(print, lambda x: x) == 2
    assert Task.of([1, 2, 3]).map(lambda x: [x[0] + 1]).fork(print, lambda x: x) == [2]
    assert Task.reject(1).map(lambda x: x + 1).fork(print, lambda x: x) == 1



# Generated at 2022-06-14 04:01:34.872889
# Unit test for method map of class Task
def test_Task_map():
    def f(arg):
        return arg + 1

    def test_case(value):
        return Task.of(value).map(f).fork(
            lambda arg: arg + 1,
            lambda arg: arg + 2
        )

    assert test_case(1) == 4


# Generated at 2022-06-14 04:01:38.945529
# Unit test for method bind of class Task
def test_Task_bind():
    def double(n):
        return Task.of(n * 2)

    def inc(n):
        return n + 1

    def double_inc(n):
        return Task.of(n) \
                   .map(inc) \
                   .bind(double)

    assert double_inc(1).fork(lambda _: None, lambda arg: arg) == 4


# Generated at 2022-06-14 04:01:44.697180
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Run test for method bind of class Task

    :returns: output of test method
    :rtype: str
    """
    def fork(reject, resolve):
        return resolve('begin')

    def bind1(value):
        def fork(reject, resolve):
            return resolve('middle1')

        return Task(fork)

    def bind2(value):
        def fork(reject, resolve):
            return resolve('middle2')

        return Task(fork)

    task = Task(fork)
    task = task.bind(bind1)
    task = task.bind(bind2)
    return task.fork(lambda _: 'error', lambda x: x)

print('test_Task_bind: {}'.format(test_Task_bind()))


# Generated at 2022-06-14 04:01:53.957385
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task(lambda _, resolve: resolve(1)).bind(lambda x: Task.of(x + 1)) == Task.of(2)
    assert Task(lambda _, resolve: resolve(1)).bind(lambda x: Task.of(x + 2)) == Task.of(3)
    assert Task(lambda _, resolve: resolve(1)).bind(lambda x: Task.of(x + 3)) == Task.of(4)
    assert Task(lambda _, resolve: resolve(1)).bind(lambda x: Task.of(x + 4)) == Task.of(5)
    assert Task(lambda _, resolve: resolve(1)).bind(lambda x: Task.of(x + 5)) == Task.of(6)

# Generated at 2022-06-14 04:02:01.013807
# Unit test for method bind of class Task
def test_Task_bind():
    def f(x):
        return Task.of(x + 1)

    def g(x):
        return Task.of(x * 2)

    def h(x):
        return Task.of(x - 1)

    t1 = Task.of(2)
    result = t1.map(f).bind(g).bind(h)

    assert result.fork(lambda _: "Error", lambda value: value) == 5


# Generated at 2022-06-14 04:02:13.411833
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test cases for Task().bind(fn) method
    """
    @given(st.integers(), st.integers())
    def test_Task_of_bind_resolved_Task_of(x, y):
        assert Task.of(x).bind(lambda arg: Task.of(arg + y)) == Task.of(x + y)

    @given(st.integers())
    def test_Task_of_bind_rejected_Task_of(x):
        assert Task.of(x).bind(lambda arg: Task.reject(arg)) == Task.reject(x)


# Generated at 2022-06-14 04:02:17.669895
# Unit test for method map of class Task
def test_Task_map():
    def to_upper(str):
        return str.upper()

    task = Task.of('Hello').map(to_upper)
    assert task.fork(None, lambda arg: arg) == 'HELLO'


# Generated at 2022-06-14 04:02:22.304463
# Unit test for method map of class Task
def test_Task_map():
    def fork(reject, resolve):
        resolve(5)

    def mapper(x):
        return x * 2

    task = Task(fork)
    result = task.map(mapper)

    assert result.fork(lambda x: x, lambda x: x) == 10, \
        "Error in Task.map"


# Generated at 2022-06-14 04:02:48.462707
# Unit test for method map of class Task
def test_Task_map():
    def square_number(a):
        return a * a

    def take_number_plus_two(a):
        return a

    my_task = Task.of(2)

    assert my_task.fork(take_number_plus_two, square_number) == 4
    assert my_task.map(square_number).fork(take_number_plus_two, square_number) == 4
    assert isinstance(my_task.map(square_number), Task)
    assert my_task.map(square_number).fork(take_number_plus_two, square_number) == 4


# Generated at 2022-06-14 04:02:53.589155
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(2)
    bind_task = task.bind(lambda x: Task.of(x * 2))

    def mock_resolve(value):
        assert value == 4

    def mock_reject(value):
        raise AssertionError(value)

    bind_task.fork(mock_reject, mock_resolve)


# Generated at 2022-06-14 04:02:59.591840
# Unit test for method bind of class Task
def test_Task_bind():
    counter = 0
    def fork_fn(reject, resolve):
        nonlocal counter
        counter += 1
        return resolve(counter)

    def assert_fn(task):
        assert task.fork(lambda _: None, lambda _: None) == 2

    Task(fork_fn).bind(lambda _: Task.of(2)).map(assert_fn)

    # check side effects
    assert counter == 1



# Generated at 2022-06-14 04:03:05.614209
# Unit test for method map of class Task
def test_Task_map():
    mock_fn = Mock()
    task = Task.of('value')

    @mock_fn.add_mock
    def mock(resolve, reject):
        resolve('value')

    task.map(mock_fn).fork(lambda arg: arg, lambda arg: arg)

    mock_fn.assert_called_once_with('value')



# Generated at 2022-06-14 04:03:16.446878
# Unit test for method map of class Task
def test_Task_map():
    def add_one(x):
        return x + 1

    def add_two(x):
        return x + 2

    def forker(reject, resolve):
        resolve(1)

    def forker2(reject, resolve):
        resolve(2)

    task = Task(forker)
    task2 = Task(forker2)

    task_piped = task.map(add_one)
    task_piped2 = task.map(add_two)

    assert task_piped.fork(raise_error, identity) == 2
    assert task_piped2.fork(raise_error, identity) == 3
    assert task_piped.bind(lambda x: task2).fork(raise_error, identity) == 3



# Generated at 2022-06-14 04:03:19.989023
# Unit test for method map of class Task
def test_Task_map():
    def square(value):
        return value ** 2

    task = Task.of(10)
    assert task.map(square).fork(None, lambda value: value) == 100


# Generated at 2022-06-14 04:03:32.090444
# Unit test for method map of class Task
def test_Task_map():
    def resolve(x):
        assert isinstance(x, int)
        return x + 10

    def reject(x):
        assert isinstance(x, int)
        return x - 1

    def test_function(resolve, reject):
        return resolve(100)

    task = Task(test_function)
    
    result = task.map(resolve)
    assert result.fork(reject, resolve) == 110

    result = task.map(reject)
    assert result.fork(reject, resolve) == 99

    result = task.map(resolve).map(reject)
    assert result.fork(reject, resolve) == 89

    result = task.map(reject).map(reject)
    assert result.fork(reject, resolve) == 98


# Generated at 2022-06-14 04:03:43.346274
# Unit test for method map of class Task
def test_Task_map():
    """
    Tests for Task.map method
    """
    def func(value):
        return value + 1

    task = Task.of(1)

    result = task.map(func)
    assert result.fork(
        lambda _: 'error',
        lambda value: value
    ) == 2

    result = task \
        .map(lambda value: value + 1) \
        .map(lambda value: value + 1)

    assert result.fork(
        lambda _: 'error',
        lambda value: value
    ) == 3

    # Test for non A -> B function
    def func2(value):
        return str(value)

    result = task.map(func2)
    assert result.fork(
        lambda _: 'error',
        lambda value: value
    ) == '1'


# Generated at 2022-06-14 04:03:50.067808
# Unit test for method bind of class Task
def test_Task_bind():
    def assert_raise(fn):
        class CustomException(Exception):
            pass

        @fn
        def test(value):
            assert value == 2
            raise CustomException()

        test()

    # test of bind for case on error
    assert_raise(Task.of(2).bind)

    # test of bind for case on success

# Generated at 2022-06-14 04:03:56.709021
# Unit test for method map of class Task
def test_Task_map():
    # simple map
    assert Task.of(4).map(
        lambda a: a + 2
    ).fork(lambda a: a, lambda a: a) == 6

    # throw error at mapped function
    assert Task.of(4).map(
        lambda a: an_error()
    ).fork(
        lambda a: True,
        lambda a: False
    )

    # throw error before map at original Task
    assert Task.reject(an_error()).map(
        lambda a: True
    ).fork(
        lambda a: type(a) == RuntimeError,
        lambda a: False
    )



# Generated at 2022-06-14 04:04:41.906282
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test bind method of Task
    """
    def func(value):
        """
        Example of mapper function

        :param value: input of mapper function
        :type value: Any
        :returns: value
        :rtype: Any
        """
        return value

    # Create resolved Task with value 1
    task = Task.of(1)
    # Create new Task with mapped resolve
    mapped_task = task.map(func)

    assert mapped_task.fork(lambda _: False, lambda value: value == 1)


# Generated at 2022-06-14 04:04:46.551071
# Unit test for method map of class Task
def test_Task_map():
    """
    Test method map of class Task
    """
    # Make sure map function returns function with expected result

# Generated at 2022-06-14 04:04:51.452358
# Unit test for method map of class Task
def test_Task_map():
    def test(x, y):
        return Task(lambda _, resolve: resolve(x + y))

    assert test(1, 2).map(lambda v: v * 2).fork(lambda _: False, lambda v: v == 6)


# Generated at 2022-06-14 04:04:57.161516
# Unit test for method bind of class Task
def test_Task_bind():
    def raw(reject, resolve):
        resolve(1)

    def task(reject, resolve):
        resolve(2)

    def task_reject(reject, resolve):
        def result_reject(value):
            resolve(value + 2)

        return Task(
            lambda reject, resolve: reject(1)
        ).map(result_reject)

    assert Task(raw).bind(task).fork(lambda x: False, lambda x: x == 2)
    assert Task(raw).bind(task_reject).fork(lambda x: x == 3, lambda x: False)

# Generated at 2022-06-14 04:05:01.873701
# Unit test for method map of class Task
def test_Task_map():
    """
    Assert that Task.map method call mapper function on resolve value.
    """
    def mapper(value):
        return value + 1

    task = Task.of(1)
    task = task.map(mapper)
    assert task.fork(
        lambda value: None,
        lambda value: value
    ) == 2


# Generated at 2022-06-14 04:05:08.608269
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(2).map(lambda x: x + 2).fork(None, lambda x: x) == 4
    assert Task.of(2).map(lambda x: x / 2).fork(None, lambda x: x) == 1
    assert Task.of(3).map(lambda x: x * 5).fork(None, lambda x: x) == 15


# Generated at 2022-06-14 04:05:16.705190
# Unit test for method map of class Task
def test_Task_map():
    """
    Result of calling map is equal to transformed value.
    """
    def sigma(n):
        return 1 if n == 0 else n + sigma(n - 1)

    def t_map(n):
        return Task(lambda _, resolve: resolve(n))

    def fn(n):
        return sigma(n)
    assert Task.of(0).map(fn).fork(None, Call) == 0
    assert Task.of(1).map(fn).fork(None, Call) == 1
    assert Task.of(2).map(fn).fork(None, Call) == 3
    assert Task.of(3).map(fn).fork(None, Call) == 6
    assert Task.of(4).map(fn).fork(None, Call) == 10

# Generated at 2022-06-14 04:05:28.362597
# Unit test for method bind of class Task
def test_Task_bind():
    import unittest

    class TaskTest(unittest.TestCase):
        def setUp(self):
            self.add_value_1 = 5
            self.add_value_2 = 3

            self.addTask = Task.of(self.add_value_1)
            self.addTask.bind(lambda a: Task.of(a+self.add_value_2))

        def test_addTask(self):
            self.assertEqual(self.addTask.value, self.add_value_1)

        def test_addTask_fork_resolve(self):
            test_value = self.add_value_1 + self.add_value_2

# Generated at 2022-06-14 04:05:37.611300
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(value):
        return Task.of(value + 1)

    task = Task.of(1).bind(mapper)
    test.it("Must equal 2")
    test.assert_equals(task.fork(None, lambda x: x), 2)

    def reject_mapper(value):
        return Task.reject(value + 1)

    task = Task.of(1).bind(reject_mapper)
    test.it("Must equal 2")
    test.assert_equals(task.fork(lambda x: x, None), 2)


# Generated at 2022-06-14 04:05:40.602131
# Unit test for method map of class Task
def test_Task_map():
    def mock_fork(reject, resolve):
        resolve(10)

    mock = Task(mock_fork)

    result = mock.map(lambda val: val * 2)

    assert result.fork(lambda reject: reject(0), lambda resolve: resolve(1)) == 20



# Generated at 2022-06-14 04:07:21.021094
# Unit test for method map of class Task

# Generated at 2022-06-14 04:07:24.214935
# Unit test for method bind of class Task
def test_Task_bind():
    def func(reject, resolve):
        return reject(1)

    task = Task(func)
    assert task.fork(lambda a: a, lambda b: b) == 1


# Generated at 2022-06-14 04:07:27.418675
# Unit test for method map of class Task
def test_Task_map():
    def test():
        assert Task.of(1).map(lambda a: a + 1).fork(identity, identity) == 2

    test()


# Generated at 2022-06-14 04:07:32.415299
# Unit test for method bind of class Task
def test_Task_bind():

    def test_bind(task, value):
        def fn(x):
            assert x == value
            return Task.of(x + 1)

        res = task.bind(fn).fork(
            lambda x: None,
            lambda x: x
        )

        assert res == value + 1

    test_bind(Task.of(1), 1)
    test_bind(Task.reject(1), 1)

    print("====================")
    print("Task.bind(): OK")
    print("====================")



# Generated at 2022-06-14 04:07:36.678515
# Unit test for method map of class Task
def test_Task_map():
    def fork(_, resolve):
        return resolve(2)

    def fn(value):
        return value + 1

    assert Task(fork).map(fn).fork(None, identity) == 3


# Generated at 2022-06-14 04:07:40.282997
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.of(1).bind(lambda x: Task.of(2 * x))
    assert task.fork(lambda arg: arg, lambda arg: arg) == 2


if __name__ == "__main__":
    test_Task_bind()

# Generated at 2022-06-14 04:07:41.425425
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.of(1).bind(
        lambda x: Task.of(x + 1)
    ).fork(lambda x: x, lambda x: x) == 2



# Generated at 2022-06-14 04:07:49.402689
# Unit test for method bind of class Task
def test_Task_bind():
    def fail():
        raise ValueError("fail")

    def fail_with_result():
        return Task.of(10).bind(fail)

    def fail_with_value():
        return Task.of(10).map(fail)

    @pytest.mark.parametrize("f_fail", [fail_with_result, fail_with_value])
    def test_bind_Task_reject_with_error_on_error(f_fail, mock_reject):
        f_fail().fork(mock_reject, lambda _: None)

        assert mock_reject.called, "reject function was not called"
        assert isinstance(mock_reject.call_args[0][0], ValueError)
