

# Generated at 2022-06-14 03:57:52.542415
# Unit test for method map of class Task
def test_Task_map():
    A = 1
    B = 2

    def mapper(arg):
        assert arg == A
        return B

    task = Task.of(A)

    def assert_fork(resolve, reject):
        assert task.fork(resolve, reject) == B

    task.map(mapper).fork(assert_fork, assert_fork)

    assert task.fork(assert_fork, assert_fork) == A


# Generated at 2022-06-14 03:57:58.378877
# Unit test for method map of class Task
def test_Task_map():
    def echo(x):
        return x
    def echo_twice(x):
        return x * 2

    assert Task.of(1).map(echo) == Task.of(1)
    assert Task.of(1).map(echo_twice) == Task.of(2)


# Generated at 2022-06-14 03:58:00.718906
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(1).map(lambda x: x + 1).fork(None, lambda x: x == 2)


# Generated at 2022-06-14 03:58:07.499890
# Unit test for method map of class Task
def test_Task_map():
    # Set test value of type int
    TEST_VALUE = 5

    # Create test Task with mapped value of type str
    def task(reject, resolve):
        resolve(TEST_VALUE)

    # Create mapper test function
    def mapper(value):
        return str(value)

    # Call method map
    mapped = Task(task).map(mapper)

    # Call fork function of mapped Task and assert that result is str value
    assert mapped.fork(lambda _: None, lambda value: type(value)) == str


# Generated at 2022-06-14 03:58:11.315709
# Unit test for method map of class Task
def test_Task_map():
    def mapper(x):
        return x + 5

    def fork(reject, resolve):
        resolve(5)

    assert Task(fork).map(mapper).fork(None, lambda x: x) == 10



# Generated at 2022-06-14 03:58:16.245144
# Unit test for method map of class Task
def test_Task_map():
    # Create simple function
    def f(_): return _

    # Create Task of simple function
    T = Task.of(f)

    # Create Task of function A -> B
    T1 = T.map(lambda g: lambda x: g(x * 2))

    assert T1.fork(Exception, lambda g: g(3)) == 6
    assert T1.fork(Exception, lambda g: g(2)) == 4


# Generated at 2022-06-14 03:58:26.618667
# Unit test for method bind of class Task
def test_Task_bind():
    """
    function for testing bind of class Task
    """
    def test_reject(reason):
        """
        function for testing reject
        :param reason: reason of rejected Task
        :type reason: int
        :returns: null
        :rtype: None
        """

# Generated at 2022-06-14 03:58:39.258148
# Unit test for method bind of class Task

# Generated at 2022-06-14 03:58:44.372623
# Unit test for method bind of class Task
def test_Task_bind():
    def plus2(value):
        return value + 2

    def minus3(value):
        return Task.of(value - 3)

    def plus5(value):
        return value + 5

    assert Task.of(10).bind(plus2).bind(minus3).bind(plus5).fork(lambda a: a, lambda a: a) == 16


# Generated at 2022-06-14 03:58:46.810237
# Unit test for method map of class Task
def test_Task_map():
    result = Task.of(123).map(lambda arg: arg + 1)


# Generated at 2022-06-14 03:59:00.917887
# Unit test for method bind of class Task
def test_Task_bind():
    def add(value):
        return Task.of(value + 10)

    def err(value):
        return Task.reject(value + 10)

    def add_error(value):
        if value > 100:
            return Task.of(value + 10)
        return Task.reject(value + 10)

    assert Task.of(10).bind(add).bind(add).bind(add_error).fork(identity, identity) == 30
    assert Task.of(10).bind(add).bind(add).bind(add_error).bind(add).fork(identity, identity) == 40
    assert Task.of(10).bind(add).bind(add).bind(add_error).bind(add).bind(add_error).fork(identity, identity) == 50
    assert Task.of(10).bind(add).bind

# Generated at 2022-06-14 03:59:09.388753
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve(2)

    task = Task(fork)

    def double(n):
        def fork2(reject, resolve):
            resolve(n * 2)
        return Task(fork2)

    assert task.bind(double).fork(lambda a: a, lambda a: a) == 4

    def fork3(reject, resolve):
        resolve(2)

    task2 = Task(fork3)

    assert task2.bind(lambda n: Task.reject("hello")).fork(lambda a: a, lambda a: a) == "hello"



# Generated at 2022-06-14 03:59:17.670991
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test bind function of Task data-type.
    """
    # Create test Task with value of three
    test_task = Task.of(3)

    # Create function which return Task with value equal to pow of argument
    def pow_task(value):
        return Task.of(value ** 3)

    # Create binded task with value equal to 3 ** 3
    binded_task = test_task.bind(pow_task)

    # Check for value of binded task
    assert binded_task.fork(lambda reject: reject(None), lambda resolve: resolve(None)) == 3 ** 3



# Generated at 2022-06-14 03:59:25.167047
# Unit test for method map of class Task
def test_Task_map():
    value = None
    is_called = False
    def resolve(arg):
        nonlocal value
        nonlocal is_called
        is_called = True
        value = arg

    def reject(_):
        pass

    task = Task(lambda reject, resolve: resolve(0)) \
            .map(lambda value: value + 1) \
            .map(lambda value: value ** 2)

    task.fork(reject, resolve)
    assert(value == 1)
    assert(is_called)


# Generated at 2022-06-14 03:59:33.321255
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task
    """

    def dead_task(value):
        """
        Return new Task without resolve and reject attributes
        """
        return Task(lambda _, __: value)

    task = Task.of(1)
    task = task.bind(lambda _: Task.of(2))
    task = task.bind(lambda _: Task.of(3))
    result = task.fork(Task.reject, Task.of)
    assert result == Task.of(3)

    task = Task.of(1)
    result = task.bind(lambda _: dead_task(2))
    assert result == Task.of(2)

    task = Task.reject(1)
    result = task.bind(lambda _: dead_task(2))

# Generated at 2022-06-14 03:59:39.582332
# Unit test for method map of class Task
def test_Task_map():
    # Call Task.of(2).map(lambda x: x * 2)
    # We should get Task with resolve argument equals 4
    task_map_of = Task.of(2).map(lambda x: x * 2)
    task_map_of.fork(
        reject=lambda x: None,
        resolve=lambda x: x == 4
    )



# Generated at 2022-06-14 03:59:42.652763
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1)
    task_map = Task.of(1).map(lambda x: x + 1)

    assert task.fork(lambda x: x, lambda x: x) == 1
    assert task_map.fork(lambda x: x, lambda x: x) == 2


# Generated at 2022-06-14 03:59:46.593114
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve(1)

    task = Task(fork)

# Generated at 2022-06-14 03:59:56.167827
# Unit test for method map of class Task
def test_Task_map():
    def add_1(value):
        return value + 1

    def multiply_2(value):
        return value * 2

    def divide_2(value):
        return value / 2

    def minus_1(value):
        if value != 0:
            return value - 1

    assert Task.of(1).map(add_1).fork(lambda _: None, lambda x: x) == 2
    assert Task.of(2).map(multiply_2).fork(lambda _: None, lambda x: x) == 4
    assert Task.of(4).map(divide_2).fork(lambda _: None, lambda x: x) == 2
    assert Task.of(2).map(minus_1).fork(lambda _: None, lambda x: x) == 1

# Generated at 2022-06-14 04:00:04.925603
# Unit test for method map of class Task
def test_Task_map():
    # Example of usage for Task.of class method
    of_1 = Task.of(1)

    # Test reject error
    assert of_1.fork(lambda arg: arg, lambda _: None) is None
    assert of_1.fork(lambda _: None, lambda arg: arg) == 1

    # Test map function
    of_2 = of_1.map(lambda arg: arg * 2)
    assert of_2.fork(lambda _: None, lambda arg: arg) == 2


# Generated at 2022-06-14 04:00:17.998174
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve_ok(value):
        assert value == "value_ok"
        return Task.of("OK")

    def reject_ok(value):
        assert value == "value_ok"
        return Task.reject("Reject")

    value_ok = Task.of("value_ok")
    value_ok.bind(resolve_ok)

    value_ok = Task.of("value_ok")
    value_ok.bind(reject_ok)

    def reject_bad(value):
        assert value == "value_bad"
        return Task.of("OK")

    def resolve_bad(value):
        assert value == "value_bad"
        return Task.reject("Reject")

    value_bad = Task.reject("value_bad")
    value_bad.bind(resolve_bad)

   

# Generated at 2022-06-14 04:00:23.125057
# Unit test for method bind of class Task
def test_Task_bind():
    # Create Task with resolve value
    result = Task.of(3) \
        .bind(lambda x: Task.of(x + 2)) \
        .bind(lambda x: Task.of(x / 2)) \
        .bind(lambda x: Task.of(x - 1))

    # Execute and compare returned value
    assert result.fork(lambda x: None, lambda x: x) == 2


# Generated at 2022-06-14 04:00:27.246676
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of(5).map(lambda val: val + 1).fork(
        lambda err: False,
        lambda val: val == 6,
    ) is True



# Generated at 2022-06-14 04:00:30.447551
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of('test').map(lambda v: v.upper()).fork(
        lambda _: None,
        lambda a: a == 'TEST'
    )


# Generated at 2022-06-14 04:00:34.263791
# Unit test for method map of class Task
def test_Task_map():
    def fn(n):
        return n + 2

    assert Task(lambda _, resolve: resolve(2)).map(fn).fork(
        lambda reject: None,
        lambda resolve: resolve
    ) == 4


# Generated at 2022-06-14 04:00:42.398367
# Unit test for method map of class Task
def test_Task_map():
    def test_resolve_reject(reject, resolve):
        def test_resolve(value):
            assert value == 'qwerty'

        def test_reject(value):
            assert value == '1234567'
        reject('1234567')

    task_foo = Task(test_resolve_reject)
    task_foo_map = task_foo.map(lambda x: 'qwerty')
    task_foo_map.fork(
        lambda x: print(x),
        lambda x: print(x)
    )


# Generated at 2022-06-14 04:00:44.227598
# Unit test for method map of class Task
def test_Task_map():
    assert Task(lambda _, resolve: resolve(2)).map(lambda x: x*2).fork(None, lambda x: x) == 4


# Generated at 2022-06-14 04:00:47.171120
# Unit test for method map of class Task
def test_Task_map():
    def square(value):
        return value * value

    assert Task.of(2).map(square).fork(None, lambda x: x) == 4

    assert Task.reject(2).map(square).fork(lambda x: x, None) == 2


# Generated at 2022-06-14 04:00:50.625209
# Unit test for method map of class Task
def test_Task_map():
    data = [1, 2]
    mapped_data = Task.of(data).map(lambda value: map(lambda x: x ** 2, value))
    fork_result = mapped_data.fork(lambda arg: arg, lambda arg: arg)
    assert fork_result == [1, 4], 'test_Task_map'



# Generated at 2022-06-14 04:01:00.078064
# Unit test for method map of class Task
def test_Task_map():
    """
    Function sorts list of tuples by second item.
    """
    def mapper(value):
        return sorted(value, key=lambda x: x[1])

    task = Task.of([
        (3, 'ccc'),
        (5, 'aaa'),
        (4, 'bbb'),
    ])

    new_task = task.map(mapper)
    value = new_task.fork(lambda x: print(x), lambda x: x)
    assert value == [(5, 'aaa'), (4, 'bbb'), (3, 'ccc')]


# Generated at 2022-06-14 04:01:12.520533
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task

    :returns: None
    """
    def resolve(value):
        return Task.of(value + 1)

    def reject(value):
        return Task.reject(value + 1)

    def fork(reject, resolve):
        resolve(1)

    def main():
        """
        Test case

        :returns: None
        """
        task = Task(fork)
        task = task.bind(resolve)
        task = task.bind(resolve)
        task = task.bind(reject)
        task.fork(
            lambda value: print("rejected value:", value) if value == 2 else None,
            lambda value: print("resolved value:", value) if value == 3 else None
        )

    main()

# Generated at 2022-06-14 04:01:21.023211
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Check that for function bind of class Task validate the following property:
         bind(f).bind(g) = bind(x -> f(x).bind(g))
    """
    def f(x):
        return Task.of(x * 2)

    def g(x):
        return Task.of(x * 3)

    t1 = Task.of(2)
    t2 = t1.bind(f).bind(g)
    t3 = t1.bind(lambda x: f(x).bind(g))
    assert(t2.fork(lambda _: None, lambda v: v) == t3.fork(lambda _: None, lambda v: v))


# Generated at 2022-06-14 04:01:24.981439
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Call Task.bind function with function and return Task.

    :returns: resolved Task
    :rtype: Task
    """
    return Task(resolve=lambda _, resolve: resolve(42))


# Generated at 2022-06-14 04:01:29.669100
# Unit test for method map of class Task
def test_Task_map():
    def foo(value):
        return value ** 2

    task = Task.of(2)
    assert(task.map(foo).fork(lambda err: err, lambda res: res)() == 4)

    task = Task.of(77)
    assert(task.map(foo).fork(lambda err: err, lambda res: res)() == 5929)



# Generated at 2022-06-14 04:01:37.734163
# Unit test for method map of class Task
def test_Task_map():
    """
    Test of Task.map functionality.
    """
    def test(value: int):
        def fn(resolve):
            """
            Resolve Task with value.
            """
            return Task.of(value).map(lambda x: x + 2).fork(
                lambda error: None,
                lambda resolved: resolve(resolved)
            )

        return Task(fn)

    assert test(5).fork(lambda err: None, lambda res: res) == 7


# Generated at 2022-06-14 04:01:43.012766
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve_test(reject, resolve):
        resolve(42)

    def reject_test(reject, resolve):
        reject(42)

    def bind_test(reject, resolve):
        resolve(Task(resolve_test))

    assert Task(bind_test).fork(lambda value: False, lambda value: value.fork(lambda _: False, lambda _: True)) == True

    def bind_test(reject, resolve):
        resolve(Task(reject_test))

    assert Task(bind_test).fork(lambda value: True, lambda value: value.fork(lambda _: True, lambda _: False)) == True


# Generated at 2022-06-14 04:01:55.816841
# Unit test for method bind of class Task
def test_Task_bind():
    def f1(value):
        if value > 10:
            return Task.reject(value)
        else:
            return Task.of(value)

    def f2(value):
        return Task.of(value)

    assert Task.reject(2).bind(f1).fork(
        lambda reject_value: reject_value,
        lambda _: None
    ) == 2

    assert Task.reject(20).bind(f1).fork(
        lambda reject_value: reject_value,
        lambda _: None
    ) == 20

    assert Task.of(2).bind(f2).bind(f1).fork(
        lambda reject_value: reject_value,
        lambda resolve_value: resolve_value
    ) == 2


# Generated at 2022-06-14 04:02:02.185330
# Unit test for method map of class Task
def test_Task_map():
    """
    Map method should take function and store it for future call.
    """
    def fn(x):
        return x + 1

    task = Task.of(3)
    task = task.map(fn)

    result = False
    def resolve(value):
        nonlocal result
        result = value

    task.fork(lambda x: None, resolve)

    assert result == fn(3)



# Generated at 2022-06-14 04:02:12.028027
# Unit test for method map of class Task
def test_Task_map():

    def task_mapper(value):
        return value + 3

    initial_task = Task.of(2)
    transformed_task = initial_task.map(task_mapper)

    # Check transform function
    assert isinstance(transformed_task, Task)

    # Check value of transformed task
    result = []
    def handle_reject(arg):
        result.append(arg)
        return arg

    def handle_resolve(arg):
        result.append(arg)
        return arg

    transformed_task.fork(handle_reject, handle_resolve)

    expected = [5]
    assert result == expected


# Generated at 2022-06-14 04:02:15.022220
# Unit test for method map of class Task
def test_Task_map():
    @Task.of
    def source():
        return "test"

    assert source.map(lambda arg: arg + '1').fork(lambda arg: arg, lambda arg: arg) == 'test1'



# Generated at 2022-06-14 04:02:24.309434
# Unit test for method bind of class Task
def test_Task_bind():
    assert (
        Task(lambda reject, resolve: resolve(1))
        .bind(lambda x: Task.of(x + 2))
        .fork(lambda _: False, lambda x: x)
        == 3
    )

    assert (
        Task(lambda reject, resolve: resolve(1))
        .bind(lambda x: Task.reject(x + 2))
        .fork(lambda x: x, lambda _: False)
        == 3
    )

    assert (
        Task(lambda reject, resolve: reject(1))
        .bind(lambda x: Task.of(x + 2))
        .fork(lambda x: x, lambda _: False)
        == 1
    )


# Generated at 2022-06-14 04:02:28.636132
# Unit test for method bind of class Task
def test_Task_bind():
    task = Task.reject(0) \
        .map(lambda arg: arg + 1)
    assert task.fork.__name__ == 'result' \
        and task.fork(lambda arg: arg, None).__name__ == 'reject'

# Generated at 2022-06-14 04:02:39.353083
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(value):
        assert not value
        return Task.of(value)

    def reject(value):
        assert value
        return Task.reject(value)

    @Task.of("a")
    def a(value):
        assert value == "a"
        return value

    @a.map(lambda value: value + "a")
    def aa(value):
        assert value == "aa"
        return value

    @Task.of("q")
    def q(value):
        assert value == "q"
        return value

    @aa.bind(lambda value: value + "a")
    def aaa(value):
        assert value == "aaa"
        return value

    @aaa.map(reject)
    def reject_aaa(value):
        pass


# Generated at 2022-06-14 04:02:48.013694
# Unit test for method map of class Task
def test_Task_map():
    def execute(resolve, reject):
        resolve(7)

    def test_fn(value):
        return value + 1

    def execute_mapper(resolve, reject):
        reject("Fail")

    def test_fn_fail(value):
        return value + 1

    assert Task(execute).map(test_fn).fork(lambda x: None, lambda x: x) == 8
    assert Task(execute_mapper).map(test_fn_fail).fork(
        lambda x: x,
        lambda x: x
    ) == "Fail"

    assert Task.of(7).map(test_fn).fork(lambda x: None, lambda x: x) == 8
    assert Task.reject(7).map(test_fn).fork(lambda x: x, lambda x: x) == 7


# Generated at 2022-06-14 04:02:53.973492
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(5).map(lambda x: x + 2)
    assert isinstance(task, Task)
    assert task.fork(lambda x: x, lambda x: x) == 7

    task = Task.reject('error').map(lambda x: 'test is not broken')
    assert isinstance(task, Task)
    assert task.fork(lambda x: x, lambda x: x) == 'error'


# Generated at 2022-06-14 04:02:57.267451
# Unit test for method map of class Task
def test_Task_map():
    def get_number():
        return Task.of(1)

    def add_one(number):
        return number + 1

    assert get_number().map(add_one).fork(lambda x: x, lambda x: x) == 2



# Generated at 2022-06-14 04:02:59.701412
# Unit test for method bind of class Task
def test_Task_bind():
    """

    """
    return Task.of(4).bind(lambda x: Task.of(x + 2))



# Generated at 2022-06-14 04:03:04.895285
# Unit test for method map of class Task
def test_Task_map():
    def mapper(val):
        return val + ' mapped'

    assert_equal(Task.of(1).map(lambda val: val + 2).fork(None, None), 3)
    assert_equal(Task.of('raw').map(mapper).fork(None, None), 'raw mapped')


# Generated at 2022-06-14 04:03:10.177626
# Unit test for method map of class Task
def test_Task_map():
    def fn_for_task(reject, resolve):
        return resolve(1)

    def map_fn(arg):
        return arg + 1

    expected = 2

    task = Task(fn_for_task).map(map_fn)
    current = task.fork(lambda _: 'error', lambda v: v)

    assert expected == current


# Generated at 2022-06-14 04:03:11.838339
# Unit test for method bind of class Task
def test_Task_bind():
    def mapper(value):
        return Task.reject(value + 1)

    assert Task.of(5).bind(mapper).fork(lambda x: x, lambda x: x) == 6

# Generated at 2022-06-14 04:03:32.518348
# Unit test for method bind of class Task
def test_Task_bind():
    # Scenario, when reject wasn't called
    def resolve_called(resolve, reject, should_resolve):
        if should_resolve:
            return resolve(True)
    # Scenario, when reject was called
    def reject_called(resolve, reject, should_reject):
        if should_reject:
            return reject(True)

    def should_called(mapper, should_resolve, should_reject):
        return mapper(
            lambda arg: arg,
            lambda arg: not arg
        )(lambda _: should_resolve, lambda _: should_reject)

    assert should_called(resolve_called, True, False) == True
    assert should_called(reject_called, False, True) == True


# Generated at 2022-06-14 04:03:35.792683
# Unit test for method map of class Task
def test_Task_map():

    def bind(arg):
        return arg + 1

    assert Task(lambda _, resolve: resolve(2)).map(bind).fork(lambda _: None, lambda arg: arg) == 3


# Generated at 2022-06-14 04:03:40.636385
# Unit test for method map of class Task
def test_Task_map():
    assert Task.of("foo").map(lambda x: x + "bar").fork(lambda _: None, lambda v: v) == "foobar"
    assert Task.of(1).map(lambda x: x + 1).fork(lambda _: None, lambda v: v) == 2


# Generated at 2022-06-14 04:03:50.742826
# Unit test for method bind of class Task
def test_Task_bind():
    """
    test_Task_bind() -> None

    In case of success -> print "Scenario #1 success"
    In case of fail -> print fail message
    """
    def test1():
        """
        Function for testing.
        :returns: Task of value 5
        :rtype: Task[Function(_, resolve) -> Int]
        """
        return Task.of(5)

    def test2():
        """
        Function for testing.
        :returns: Task of value 10
        :rtype: Task[Function(_, resolve) -> Int]
        """
        return Task.of(10)

    def test3():
        """
        Function for testing.
        :returns: Task of value 15
        :rtype: Task[Function(_, resolve) -> Int]
        """
        return Task.of(15)

# Generated at 2022-06-14 04:03:56.041956
# Unit test for method bind of class Task
def test_Task_bind():
    def fork1(reject, resolve):
        resolve(10)

    def fork2(reject, resolve):
        resolve(20)

    task1 = Task(fork1)

    task2 = Task(fork2)

    assert task1.bind(lambda a: task2).fork(lambda a: None, lambda b: b) == 20



# Generated at 2022-06-14 04:04:01.528760
# Unit test for method bind of class Task
def test_Task_bind():
    assert Task.reject("error").bind(lambda v: v + " is error").fork(
        lambda err: err == "error is error",
        lambda v: False
    )
    assert Task.of("ok").bind(lambda v: Task.reject(v + " is error")).fork(
        lambda err: err == "ok is error",
        lambda v: False
    )
    assert Task.of("ok").bind(lambda v: Task.of(v + " is ok")).fork(
        lambda err: False,
        lambda v: v == "ok is ok"
    )


# Generated at 2022-06-14 04:04:11.468691
# Unit test for method map of class Task
def test_Task_map():
    def _resolve(a, b):
        return a + b

    def _reject(a, b):
        return a + b

    def _mod(a, _):
        return a + 1

    def _mod2(a, _):
        return a + 2

    def _mod3(a, _):
        return a + 3

    def _mod4(a, _):
        return a + 4

    def _mod5(a, _):
        return a + 5

    # try to map not Task

# Generated at 2022-06-14 04:04:16.504354
# Unit test for method map of class Task
def test_Task_map():
    """ Test of method map of class Task """
    def double(value):
        """ Double value """
        return value * 2

    task = Task.of(1)
    double_task = task.map(double)
    assert double_task.fork(lambda _, __: 1, lambda _: _) == 2



# Generated at 2022-06-14 04:04:21.278708
# Unit test for method map of class Task
def test_Task_map():
    def add_zero(value):
        return value + 0

    rejected_task = Task.reject(42)
    resolved_task = Task.of(42)

    assert rejected_task.map(add_zero).fork(lambda value: value, lambda _: None) == 42
    assert resolved_task.map(add_zero).fork(lambda _: None, lambda value: value) == 42


# Generated at 2022-06-14 04:04:28.287791
# Unit test for method map of class Task
def test_Task_map():
    def task_fork(reject, resolve):
        reject(1)

    def mapper(value):
        return value + 1

    task_test = Task(task_fork)
    task_test.map(mapper)


# Generated at 2022-06-14 04:04:59.867697
# Unit test for method bind of class Task
def test_Task_bind():
    def f(x):
        return Task.of(x * 2)

    t = Task.of(10)
    assert t.bind(f).fork(
        lambda x: x * 2,
        lambda x: x * 2
    ) == 20

    assert Task.of(10).bind(f).bind(f).fork(
        lambda x: x * 2,
        lambda x: x * 2
    ) == 40

    g = lambda x: Task.reject(x * 2)

    assert Task.of(10).bind(g).bind(f).fork(
        lambda x: x * 2,
        lambda x: x * 2
    ) == 20


# Generated at 2022-06-14 04:05:05.021772
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        def raiser():
            raise Exception('Something wrong')

        def value():
            return 'Some value'

        return reject(raiser())

    t = Task(fork) \
            .bind(
                lambda value: Task.of(value)
            ) \
            .bind(
                lambda value: Task.of(value)
            )

    assert t.fork(lambda err: err(), lambda value: 'Some value') == 'Some value'


# Generated at 2022-06-14 04:05:14.762908
# Unit test for method bind of class Task

# Generated at 2022-06-14 04:05:21.554662
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test check work of method bind of class Task.
    """
    def add(x):
        """Example function that add 1 to argument."""
        return x + 1

    task = Task.of(1)
    task_result = task.bind(lambda value: Task.of(add(value)))
    assert task_result.fork(None, lambda x: x) == 2

# Generated at 2022-06-14 04:05:29.273311
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind
    """
    def test_fn(value):
        return Task.of(value + 10)


# Generated at 2022-06-14 04:05:37.432006
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test Task.bind method
    """
    def foo(x):
        return Task.of(x)

    def bar(x):
        return Task.reject("error")

    # Test Task.bind with Task.of as argument
    t = Task.of("hello").bind(foo)
    assert t.fork("error", "result") == "hello"

    # Test Task.bind with Task.reject as argument
    t = Task.of("hello").bind(bar)
    assert t.fork("error", "result") == "error"

# Generated at 2022-06-14 04:05:39.620854
# Unit test for method map of class Task
def test_Task_map():
    some_value = 'some_value'
    some_fn = lambda arg: arg

    assert Task.of(some_value).map(some_fn).fork(None, lambda result: result) == some_value

# Generated at 2022-06-14 04:05:42.474192
# Unit test for method map of class Task
def test_Task_map():
    value = Task.of(1).map(lambda x: x + 1).fork(lambda result: -1,
        lambda result: result)
    assert value == 2

    fail = Task.reject(0).map(lambda x: x + 1).fork(lambda result: -1,
        lambda result: result)
    assert fail == -1



# Generated at 2022-06-14 04:05:55.139746
# Unit test for method bind of class Task
def test_Task_bind():
    def plus(x, y):
        return x + y

    def sqrt(x):
        return x ** 0.5

    def div(x, y):
        return x / y

    fn = Task.of(36)
    g = fn.bind(lambda x: Task.of((x,)))
    assert g.fork(None, plus) == 36

    fg = fn.bind(lambda x: Task.of((x,))).bind(lambda x, y: Task.of(x + y))
    assert fg.fork(None, None) == 72


# Generated at 2022-06-14 04:05:59.411336
# Unit test for method map of class Task
def test_Task_map():
    def add(x):
        return x + 1

    task = Task.of(1).map(add)
    assert task.fork(None, None) == 2, 'method map of class Task is failed!'


# Generated at 2022-06-14 04:06:57.205070
# Unit test for method bind of class Task
def test_Task_bind():
    def fork(reject, resolve):
        resolve(5)

    def mapper(value):
        return Task.of(value * value)

    task1 = Task(fork)
    task2 = task1.bind(mapper)
    assert task2.fork(lambda arg: arg, lambda arg: arg) == 25

# Generated at 2022-06-14 04:07:05.738737
# Unit test for method bind of class Task
def test_Task_bind():
    def fetch(id):
        print('fetch')
        Task.reject(1)
        return Task.of(id)

    def validate(user):
        print('validate')
        Task.reject(2)
        return Task.of(user)

    def do_smth(user):
        print('do_smth')
        Task.reject(3)
        return Task.of(user)

    def save(user):
        print('save')
        Task.reject(4)
        return Task.of(user)

    def handle_error(error):
        print('error')
        return error

    task = (
        Task.of(1)
        .bind(fetch)
        .bind(validate)
        .bind(do_smth)
        .bind(save)
    )

# Generated at 2022-06-14 04:07:09.266781
# Unit test for method map of class Task
def test_Task_map():
    task = Task.of(1).map(lambda x: x * x)
    assert task.fork(lambda x: x, lambda x: x) == 1


# Generated at 2022-06-14 04:07:16.199662
# Unit test for method bind of class Task
def test_Task_bind():

    def my_reject(arg):
        assert arg == 0

    def my_resolve(arg):
        assert arg == 1

    def my_resolve_1(arg):
        assert arg == 1

    def my_resolve_2(arg):
        assert arg == 2

    def my_resolve_3(arg):
        assert arg == 3

    Task.of(4) \
        .bind(lambda x: Task.of(x / 2)) \
        .bind(lambda x: Task.of(x + 1)) \
        .bind(lambda x: Task.of(x / 2)) \
        .fork(my_reject, my_resolve)


# Generated at 2022-06-14 04:07:23.851798
# Unit test for method bind of class Task
def test_Task_bind():
    """
    Test for method bind of class Task.
    Return True if method works.
    """
    task = Task.of(2)

    def mapper(value):
        return Task.of(value * 2)

    def mapper_with_error(value):
        return Task.reject(value * 2)

    def test_success():
        """
        Test for method with successful result.
        """
        def success(value):
            assert value == 4
            return True

        return task.bind(mapper).fork(lambda _: False, success)

    def test_error():
        """
        Test for method with error.
        """
        def err(value):
            assert value == 4
            return True

        return task.bind(mapper_with_error).fork(err, lambda _: False)

    return test

# Generated at 2022-06-14 04:07:31.003149
# Unit test for method map of class Task
def test_Task_map():
    @Task.of(2)
    def return_2():
        pass

    @Task.reject(3)
    def return_3():
        pass

    @Task.of(2).map(lambda arg: arg * 2)
    def return_4():
        pass

    @return_3.map(lambda arg: arg * 2)
    def return_3_rejected():
        pass

    assert return_2() == 2
    assert return_3() == 3
    assert return_4() == 4
    assert return_3_rejected() == 3


# Generated at 2022-06-14 04:07:34.291290
# Unit test for method map of class Task
def test_Task_map():
    fn = lambda x: x
    task = Task.of(42).map(fn)
    assert task.fork(None, lambda x: x) == 42


# Generated at 2022-06-14 04:07:37.969931
# Unit test for method map of class Task
def test_Task_map():
    def testFn(value): return value * 2
    assert Task.of(12).map(testFn).fork(None, lambda arg: arg) == 24


# Generated at 2022-06-14 04:07:44.241108
# Unit test for method bind of class Task
def test_Task_bind():
    def resolve(arg):
        return arg

    def reject(arg):
        return arg

    assert Task(resolve).bind(lambda arg: Task(resolve)).fork(reject, resolve) == resolve
    assert Task(resolve).bind(lambda arg: Task(reject)).fork(resolve, reject) == reject
    assert Task(reject).bind(lambda arg: Task(resolve)).fork(reject, resolve) == reject
